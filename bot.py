from dataclasses import dataclass, field
from pathlib import Path
from telegram import Update
from telegram.ext import (
    Application,
    ContextTypes,
    MessageHandler,
    filters,
)
from google import genai
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI = genai.Client(api_key=GEMINI_API_KEY)
PROMPT = """
## Istruzioni

1. **Trascrivi l'audio in italiano:** Trascrivi accuratamente il contenuto del file audio allegato, in italiano.

2. **Analizza, correggi e migliora:** Analizza il contesto dell'audio, correggi eventuali errori di sintassi, semantica o grammatica e migliora il flusso del discorso.

3. **Post-processing:** Elimina ripetizioni, esitazioni o informazioni irrilevanti.

4. **Restituisci solo il testo:** Restituisci *esclusivamente* il testo post-processato in italiano, senza ulteriori commenti o spiegazioni.
"""

@dataclass
class WhitelistLoader:
    whitelist: list[int] = field(default_factory=list)
    file_path: str = "whitelist.txt"

    @property
    def load_from_file(self) -> list[int]:
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if line.isdigit():
                        self.whitelist.append(int(line))
            return self.whitelist
        except FileNotFoundError:
            print(f"Errore: Il file '{self.file_path}' non esiste.")
            return self.whitelist
        except ValueError as e:
            print(f"Errore nel parsing del file: {e}")
            return self.whitelist


WHITELIST = WhitelistLoader()


async def transcribe_audio(audio_file_path: Path) -> str | None:
    try:
        myfile = GEMINI.files.upload(file=audio_file_path)

        response = GEMINI.models.generate_content(
            model="gemini-2.0-flash", contents=[PROMPT, myfile]
        )

        return response.text
    except Exception as e:
        return f"Errore: {str(e)}"


async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user
    if not user_id:
        return
    user_id = user_id.id
    if user_id in WHITELIST.load_from_file:
        audio_file = await context.bot.getFile(update.message.voice.file_id)  # type: ignore
        audio_file_path = await audio_file.download_to_drive()
        transcription = await transcribe_audio(audio_file_path)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,  # type: ignore
            text=f"Trascrizione: {transcription}",
        )
        os.remove(audio_file_path)
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,  # type: ignore
            text="Non sei autorizzato a utilizzare questo bot.",
        )


def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(MessageHandler(filters.VOICE, handle_audio))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

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
WHITELIST = [23616716, 20540653]
PROMPT = """
## Istruzioni

1. **Trascrivi l'audio in italiano:** Trascrivi accuratamente il contenuto del file audio allegato, in italiano.

2. **Analizza, correggi e migliora:** Analizza il contesto dell'audio, correggi eventuali errori di sintassi, semantica o grammatica e migliora il flusso del discorso.

3. **Post-processing:** Elimina ripetizioni, esitazioni o informazioni irrilevanti.

4. **Restituisci solo il testo:** Restituisci *esclusivamente* il testo post-processato in italiano, senza ulteriori commenti o spiegazioni.
"""

client = genai.Client(api_key=GEMINI_API_KEY)


async def transcribe_audio(audio_file_path):
    try:
        myfile = client.files.upload(file=audio_file_path)

        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=[PROMPT, myfile]
        )

        return response.text
    except Exception as e:  # Qualsiasi altro errore generico
        return f"Errore: {str(e)}"


async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user
    if not user_id:
        return
    user_id = user_id.id
    print(user_id)
    if user_id in WHITELIST:
        audio_file = await context.bot.getFile(update.message.voice.file_id)
        audio_file_path = await audio_file.download_to_drive()
        transcription = await transcribe_audio(audio_file_path)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Trascrizione: {transcription}",
        )
        os.remove(audio_file_path)
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Non sei autorizzato a utilizzare questo bot.",
        )


def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(MessageHandler(filters.VOICE, handle_audio))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

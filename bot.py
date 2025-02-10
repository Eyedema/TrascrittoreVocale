import cfg
import os

from google import genai
from pathlib import Path
from telegram import Update
from telegram.ext import (
    Application,
    ContextTypes,
    MessageHandler,
    filters,
)


client = genai.Client(api_key=cfg.GEMINI_API_KEY)


def load_users(file_path: str) -> list:
    try:
        with open(file_path, "r") as f:
            users = [line.strip() for line in f]
        return users
    except FileNotFoundError:
        print(f"file non trovato: {file_path}")
        return []
    except Exception as e:
        print(f"errore: {e}")
        return []


async def transcribe_audio(audio_file_path: Path) -> str | None:
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                cfg.PROMPT.format(audio_file_path=audio_file_path),
                client.files.upload(file=audio_file_path),
            ]
        )
        return response.text
    except Exception as e:
        return f"Errore: {str(e)}"


async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user
    if not user_id:
        return
    user_id = user_id.id
    print(f'nuovo messaggio da {user_id}')
    if str(user_id) in load_users("whitelist.txt"):
        audio_file = await context.bot.getFile(update.message.voice.file_id)
        audio_file_path = await audio_file.download_to_drive()
        transcription = await transcribe_audio(audio_file_path)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=transcription,
        )
        os.remove(audio_file_path)
    else:
        print(f'utente {user_id} non in whitelist')
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="🚫 Privilegi insufficienti.",
        )


def main():
    application = Application.builder().token(cfg.TELEGRAM_BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.VOICE, handle_audio))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

# Token del bot Telegram.
# Questo token è necessario per autenticare il bot e permettergli di interagire con l'API di Telegram.
# Puoi ottenere il token creando un bot tramite BotFather su Telegram.
TELEGRAM_BOT_TOKEN = ''

# Chiave API di Gemini.
# Questa chiave è necessaria per accedere ai servizi di Gemini, come la trascrizione audio.
# Puoi ottenere la chiave registrandoti sulla piattaforma Gemini e creando un progetto.
GEMINI_API_KEY = ''

# Prompt per la trascrizione audio.
# Questo prompt viene inviato a Gemini insieme al file audio per guidare il processo di trascrizione.
# Contiene istruzioni specifiche sul tipo di output desiderato, come la lingua, il formato e il post-processing.
# La variabile {audio_file_path} verrà sostituita con il percorso effettivo del file audio prima dell'invio a Gemini.
PROMPT = '''
## Istruzioni

1. **Trascrivi l'audio in italiano:** Trascrivi accuratamente il contenuto del file audio allegato, in italiano.

2. **Analizza, correggi e migliora:** Analizza il contesto dell'audio, correggi eventuali errori di sintassi, semantica o grammatica e migliora il flusso del discorso.

3. **Post-processing:** Elimina ripetizioni, esitazioni o informazioni irrilevanti.

4. **Restituisci solo il testo:** Restituisci *esclusivamente* il testo post-processato in italiano, senza ulteriori commenti o spiegazioni.

## File audio

{audio_file_path}

## Note aggiuntive

* Se possibile, fornisci ulteriori informazioni sul contesto dell'audio (ad esempio, chi parla, dove è stato registrato, di cosa si parla) per aiutare l'IA a comprendere meglio il significato del discorso.
* Se hai esigenze specifiche riguardo alla formattazione del testo (ad esempio, utilizzo di grassetto, corsivo, ecc.), indicale nel prompt.

'''
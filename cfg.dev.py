
TELEGRAM_BOT_TOKEN = ''

GEMINI_API_KEY = ''

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

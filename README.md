
# Bot di Trascrizione Audio con Gemini

Questo bot Telegram utilizza l'API di Gemini per trascrivere messaggi audio in italiano.  È stato progettato per semplificare la trascrizione di memo vocali, interviste o qualsiasi altro contenuto audio direttamente all'interno di Telegram.

## Funzionalità

* Trascrizione accurata di audio in italiano.
* Elaborazione del testo per migliorare chiarezza e leggibilità.
* Gestione di una whitelist di utenti autorizzati.
* Integrazione con Telegram tramite python-telegram-bot.

## Installazione

1. **Clona il repository:**

```bash
git clone https://github.com/Eyedema/TrascrittoreVocale.git
cd TrascrittoreVocale

```

2.  **Crea un ambiente virtuale (consigliato):**

```
python3 -m venv .venv
source .venv/bin/activate  # Su Linux/macOS
.venv\Scripts\activate  # Su Windows

```

3.  **Installa le dipendenze:**

```
pip install -r requirements.txt

```


4.  **Configura il bot:**

-   **Crea un file `cfg.py`:** Copia il contenuto di `cfg.dev.py` in un nuovo file chiamato `cfg.py`. Questo file conterrà le informazioni di configurazione.

-   **Compila il file `cfg.py`**

-   **Crea un file `whitelist.txt`:** Inserisci un ID utente di Telegram per riga. Solo gli utenti presenti in questa lista potranno utilizzare il bot.

5.  **Esegui il bot:**



```
python main.py

```

## Utilizzo

1.  Avvia il bot su Telegram.
2.  Invia un messaggio vocale al bot.
3.  Se il tuo ID utente è presente nella `whitelist.txt`, il bot trascriverà l'audio e ti invierà il testo.

## Note

-   Assicurati di aver installato correttamente le librerie necessarie.
-   Il bot utilizza l'API di Gemini, quindi è necessario avere una chiave API valida.
-   La `whitelist.txt` permette di controllare l'accesso al bot.

## Contribuisci

Se desideri contribuire al progetto, sentiti libero di aprire una issue o una pull request.
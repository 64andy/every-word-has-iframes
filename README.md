# Every Word has I-Frames
### ***Archival*** - *An inside joke Twitter bot*

* Originally hosted on [replit](https://replit.com/@64andy2000/every-word-has-iframes)
* [Bot account](https://twitter.com/wordhaveiframes)

---

This bot was created for a DMC1 inside joke.<br>
Posts tweets in the format "Every {word} has iframes".<br>
Sometimes, using NLP, it posts "{adjective} {word} {has/had/have} iframes"

This bot was discontinued in December 2019

### Setup:
0. **Note:** Recommend putting into its own venv
1. The required packages are in `requirements.txt`, to install run `pip install -r requirements.txt`
2. Change the settings in `settings.py`, to your liking, all 2 of em
3. Add your bot account's 4 API keys to a `.env` file (see the provided file)
4. Optional: Add/remove your favourite words from `cleaned_words.txt` (I added it so it wouldn't say slurs. Still swears tho)
5. Run `main.py`

---

This bot used a repl.it hack with Flask to keep it constantly running.
Flask hack from [@GarethDwyer1](https://replit.com/@GarethDwyer1/discord-bot)

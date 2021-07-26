'''
An every word Twitter bot for the format "neutral {word} has iframes"
Uses the Natural Language Toolkit (NLTK) to modify this sentence slightly
i.e. Past tense words cause the output "neutral {word} had iframes"
Plurals, pronouns, etc cause the output "neutral {word} have iframes"
If it's an adjective, it grabs 2 words and replaces "neutral" with "adjective" 
Created by @64andy2000
24/7 bot trick by https://repl.it/@GarethDwyer1
Created on 26/06/2019'''

print("Importing modules...")
import os
import time
import random
from datetime import datetime
import twitter
from nltk.tag import pos_tag
import settings
from server import run_server, errors
from dotenv import load_dotenv
load_dotenv()
print("Done")


HAD_TAGS = {"VBN", "VBD"}
HAVE_TAGS = {"MD", "NNS", "NPSS", "PDT", "PRP", "PRP$"}

api = twitter.Api(
            consumer_key        = os.environ["CONSUMER_PUBLIC_KEY"],
            consumer_secret     = os.environ["CONSUMER_SECRET_KEY"],
            access_token_key    = os.environ["ACCESS_PUBLIC"      ],
            access_token_secret = os.environ["ACCESS_SECRET"      ],
            tweet_mode          = 'extended'
        )

try:
    pos_tag(["testing"])
except LookupError:
    print("Downloading tagger...")
    import nltk
    nltk.download("averaged_perceptron_tagger")
    print("Done")


def is_adjective(tag: str) -> bool:
    return tag.startswith("J")


def generate_tweet(word_a: str, 
                    word_b: str,
                    default_adjective: str = settings.default_adjective
                    ) -> str:
    word_a = word_a.strip()
    word_b = word_b.strip()
    tag_a = pos_tag([word_a])[0][1]
    tag_b = pos_tag([word_b])[0][1]
    log_message = f"{word_a}, {tag_a} | {word_b}, {tag_b}"
    print(log_message)

    if is_adjective(tag_a):
        adjective = word_a
        word_a = word_b
        tag_a = tag_b
    else:
        adjective = default_adjective
    print("Adjective:", adjective)
    if tag_a in HAD_TAGS:
        join_word = "had"
    elif tag_a in HAVE_TAGS:
        join_word = "have"
    else:
        join_word = "has"
    
    tweet = f"{adjective} {word_a} {join_word} iframes"
    with open("tweet_logger.txt", "a") as w:
        w.write(f"{tweet} -> {log_message}, adjective={adjective}\n")
    return tweet

def send_tweet(text: str):
    print(datetime.now(), text)
    api.PostUpdate(text)


def main():
    while True:
        try:
            # If o'clock is a few seconds away
            if (settings.TWEET_EVERY-1) < (time.time() % settings.TWEET_EVERY):
                with open("cleaned_words.txt") as r:
                    word_a, word_b = random.choices(r.readlines(), k=2)
                text = generate_tweet(word_a, word_b)
                send_tweet(text)
                time.sleep(max(settings.TWEET_EVERY-3, 1)) # Go to sleeeep
            time.sleep(1)
        except KeyboardInterrupt:
            # Kill server
            print("Killing server...")
            global t
            t.terminate()
            t.join()
            quit()
        except Exception as e:
            print(repr(e))
            errors.append(e)



if __name__ == "__main__":
    print("Starting up at", datetime.now())
    global t
    t = run_server()
    main()

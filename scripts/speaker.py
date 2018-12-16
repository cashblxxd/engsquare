import urllib.request
import os

FORMAT = "mp3"
KEY = "9b4c9789-7c82-4d99-81df-f06b19b96535"
SPEAKER = "ermil"
SPEED = "1.1"
EMOTION = "neutral"

def download_word(word):
    name = "./" + word + ".mp3"
    word = urllib.request.quote(word.encode('utf-8'))
    url = ('https://tts.voicetech.yandex.net/generate?text=' + word +
           '&format=' + FORMAT + '&lang=en-US' +
           '&speaker=' + SPEAKER + '&emotion=' + EMOTION + '&key=' + KEY)
    urllib.request.urlretrieve(url, name)
    os.system("curl \"https://tts.voicetech.yandex.net/generate?text=abstruse&format=mp3&lang=en-US&speaker=zahar&emotion=good&key=9705b14c-14a9-4ab2-93ba-75d50318cc8d\" -G --data-urlencode \"text=This text is ready\" > speech.mp3")


if __name__ == "__main__":
    with open('sources/word_to_tell.txt', 'r') as f:
        try:
            download_word(f.read().strip())
        except Exception: pass

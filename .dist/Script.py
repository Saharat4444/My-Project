#pip install googletrans==4.0.0-rc1
from googletrans import Translator

translator = Translator()

try:
    with open('./.dist./asset./text.txt', mode='r', encoding='utf-8') as my_file:
        text = my_file.read()
        # Translate the content of the file to Japanese
        Jp_translation = translator.translate(text, dest="ja")
        Rus_translation = translator.translate(text, dest="ru")
        Th_translation = translator.translate(text, dest="th")

        print("Translated text:")
        print(Jp_translation.text)
        print(Rus_translation.text)
        print(Th_translation.text)

except FileNotFoundError:
    print("Check your path, silly!")
except Exception as e:
    print(f"An error occurred: {e}")

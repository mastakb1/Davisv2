import translators as ts
import pyttsx3
import time

engine = pyttsx3.init()



text = "This company was founded in 2010 by the infamous movie star, \
          Graeme Alexander. Currently, the company worths USD 1 billion \
          according to Forbes report in 2023. What an achievement in just \
          13 years."
engine.say(text)
engine.runAndWait()
time.sleep(2)
engine.say("terjemahannya dalam bahasa Indonesia sebagai berikut")
engine.runAndWait()
time.sleep(2)
hasil = ts.translate_text(text, to_language="id", translator='google')
print(hasil)
time.sleep(1)
engine.say(hasil)
engine.runAndWait()
engine.stop()

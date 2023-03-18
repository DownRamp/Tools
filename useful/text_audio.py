# pip install playsound
from playsound import playsound
# pip install gtts
from gtts import gTTS

audio_file = "speech.mp3"
wishes = ["I would like to be good at something.",
"I would like to be better at coding.",
"I would like to be a better boyfriend.",
"I would like to be a better lover.",
"I would like to be more focused.",
"I would like to finish what I start.",
"I would like to handle pressure better.",
"I would like to be less stressed.",
"I would like to make more things.",
"I would like to make my own company.",
"I would like to sleep 8 to 10 hours a night.",
"I would like to feel strong.",
"I would like to be more confident.",
"I would like to be more organized.",
"I would like to not be afraid of conversations",
"I would like to be more patient."]

text_to_convert=""
for i in wishes:
    for j in range(3):
        text_to_convert += i+" "
language = "en"
print(text_to_convert)
speech = gTTS(text=text_to_convert, lang=language, slow=False)

speech.save(audio_file)
playsound(audio_file)

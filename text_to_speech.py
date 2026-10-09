from gtts import gTTS

text = input("Enter text to speech: ")

tts = gTTS(text=text, lang="en")
tts.save("voice.mp3")

print("audio saved successfully")
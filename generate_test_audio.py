from gtts import gTTS

text = "This is a test for voice-to-text conversion."
speech = gTTS(text)
speech.save("test_audio.mp3")

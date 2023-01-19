from gtts import gTTS

text = "Olá! Bem vindo ao @codeemumminuto"
tts = gTTS(text=text, lang='pt-BR')
tts.save("audio.mp3")
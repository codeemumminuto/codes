from pydub import AudioSegment

# Arquivo de vídeo
video = AudioSegment.from_file("meuvideo.mp4", format="mp4")

# Converter o arquivo de vídeo para áudio
audio = video.set_channels(1)

# Salvar o arquivo como .mp3
audio.export("meuaudio.mp3", format="mp3")
from pydub import AudioSegment
from pydub.playback import play

# Load the .m4a file
audio = AudioSegment.from_file("recordings/Hello_Eran.m4a", format="m4a")

# Play the audio
play(audio)

import subprocess
import glob
from shlex import join

for i in glob.glob("*.wav"):
    command = ["ffmpeg","-i","cover.png","-i",i,"-vf","loop=loop=-1:size=1","-shortest","-map","0:v:0","-map","1:a:0","-y",i + ".mp4"]
    print(join(command))
    subprocess.call(command)
    print('Done ' + i)
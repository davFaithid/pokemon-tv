import ytdl
import sys, os, time
from configparser import ConfigParser
configur = ConfigParser()

if sys.argv[1] == '-h':
    print("""
    main.py <seasonnumber> <episodenumber>
    ie:
        main.py 1 1
    would be episode one of season 1.
          """)

season = sys.argv[1]
episode = sys.argv[2]

# Merge in user-specific configuration 
configur.read(os.path.expanduser('episodes.ini')) 

pkmnurl = configur.get(season, episode)
ydl = ytdl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

with ydl:
    result = ydl.extract_info(
        pkmnurl,
        download=False # We just want to extract the info
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

video_url = video['url']


import subprocess
cmds = ['ffplay', '-i', video_url]
player = subprocess.Popen(cmds, stdout=subprocess.PIPE, shell=True)

try:
    outs, errs = player.communicate()
except TimeoutExpired:
    player.kill()
    outs, errs = player.communicate()

print("\n\nExiting...")
time.sleep(5)
sys.exit()



"""
    Watch (currently only the first season) of Pokemon in python3
    Copyright (C) 2019  davFaithid

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys, os, time
from configparser import ConfigParser
configur = ConfigParser()

if sys.argv[1] == '-h':
    print("""
    pokemon-tv <seasonnumber> <episodenumber>
    ie:
        pokemon-tv 1 1
    would be episode one of season 1.
          """)
    sys.exit()

season = sys.argv[1]
episode = sys.argv[2]

# Merge in user-specific configuration 
configur.read(os.path.expanduser('episodes.ini')) 

pkmnurl = configur.get(season, episode)

print("Loading video at %s" %(pkmnurl))

import mpv

player = mpv.MPV(ytdl=True, input_default_bindings=True, input_vo_keyboard=True)
player.play(pkmnurl)
player.wait_for_playback()

del player

print("\nExiting...")
time.sleep(3)
sys.exit()





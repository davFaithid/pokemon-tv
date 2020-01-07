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
from urllib.request import urlopen
import re
import sys
from bs4 import BeautifulSoup

def getLinks(url):
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, features="html.parser")
    links = []
    if int(sys.argv[1]) < 10:
        season_number = "0" + str(sys.argv[1])
    else:
        season_number = str(sys.argv[1])
    if int(sys.argv[2]) < 10:
        episode_number = "0" + str(sys.argv[2])
    else:
        episode_number = str(sys.argv[2])
    for link in soup.findAll('a', attrs={'href': re.compile("/"+season_number+"_"+episode_number+"-")}):
        links.append(link.get('href'))

    return links

if sys.argv[1] == '-h':
    print("""
    main.py <seasonnumber> <episodenumber>
    ie:
        main.py 1 1
    would be episode one of season 1.
          """)
    sys.exit()

"""
season = sys.argv[1]
episode = sys.argv[2]
"""

# Merge in user-specific configuration 

baseseason = "https://www.pokemon.com/us/pokemon-episodes/pokemon-tv-seasons/season-"+sys.argv[1]
link1 = str(getLinks(str(baseseason))).strip('[]')
link2 = link1.replace("'/us/", "https://www.pokemon.com/us/")
pkmnurl = str(link2).strip("''")

if pkmnurl.endswith("?play=true") == True:
    print("Loading video at %s" %(pkmnurl))
    import mpv

    player = mpv.MPV(ytdl=True, input_default_bindings=True, input_vo_keyboard=True)
    player.play(pkmnurl)
    player.wait_for_playback()

    del player

    print("\nExiting...")
    time.sleep(3)
    sys.exit()
else:
    print("Video is not available for playback.")
    sys.exit()
   
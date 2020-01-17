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
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mpv

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
    pokemon-tv <seasonnumber> <episodenumber>
    ie:
        pokemon-tv 1 1
    would be episode one of season 1.
          """)
    sys.exit()

baseseason = "https://www.pokemon.com/us/pokemon-episodes/pokemon-tv-seasons/season-"+sys.argv[1]+"/"
link1 = str(getLinks(str(baseseason))).strip('[]')
link2 = link1.replace("'/us/", "https://www.pokemon.com/us/")
pkmnurl = str(link2).strip("''")

def play(url):
    class MainWin(QMainWindow):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.container = QWidget(self)
            self.setCentralWidget(self.container)
            self.container.setAttribute(Qt.WA_DontCreateNativeAncestors)
            self.container.setAttribute(Qt.WA_NativeWindow)
            self.setWindowTitle("Pokemon TV")
            self.setWindowIcon(QIcon('icon.png'))
            self.resize(1000, 563)

            player = mpv.MPV(wid=str(int(self.container.winId())), ytdl=True, input_default_bindings=True, input_vo_keyboard=True)
            @player.on_key_press('esc')
            def my_key_binding():
                print('')
                sys.exit(app.exec_())
            player.play(url)
        #   player.wait_for_playback()
            del player
    app = QApplication(sys.argv)
    import locale
    locale.setlocale(locale.LC_NUMERIC, 'C')
    win = MainWin()
    win.show()
    sys.exit(app.exec_())

if pkmnurl.endswith("?play=true") == True:
    print("Loading video at %s" %(pkmnurl))
    play(pkmnurl)
else:
    print("Video is not available for playback.")
    sys.exit()
<<<<<<< HEAD
=======
   
>>>>>>> 1be230f1900cf738250534e4ff8f0a6ffdd1cbe8

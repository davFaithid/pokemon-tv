# How to setup

Setup is pretty simple, though there are quirks along the way which are super annoying.

First make sure you have [python 3](https://www.python.org/downloads/) installed on path (important! path is our friend)

Next make sure you have [git](https://git-scm.com/downloads) installed and is usuable on command prompt. (Just in case, it's better to download from the [release](https://github.com/davFaithid/pokemon-tv/releases) tab and downloading `Source code (zip)`)

Unzip the zip file from `Source code (zip)` to a folder (preferrably somewhere on your Desktop or Documents folder) and then open command prompt and cd to the folder (ie `cd C:\Users\user\Documents\pokemon-tv`)

Now type `pip3 install -r requirements.txt` and wait for all packages to install. 

Then (if you haven't already) download the `mpv-1.dll` from the README and place it in a folder that is on path (preferably your python3 folder; ie `%localappdata%/Programs/Python/Python38-32`). 

Now, with the command cd'd to your folder type `cd pokemon-tv` and then type `py -3 __init__.py -h` or `python3 __init__.py -h`

Most of these steps will be obsolete, and thus replaced or removed as nessecary in the future. As such, your command prompt should display the following,
```
    pokemon-tv <seasonnumber> <episodenumber>
    ie:
        pokemon-tv 1 1
    would be episode one of season 1.
```
This is my grand scheme of trying to future proof. Until we have a proper pypi package that compiles, please follow the above steps and following the help screen just shown, type `py -3 __init__.py 1 1` or `python3 __init__.py 1 1` and it should play the first episode of the first season.

# For those unfortunate few who used my pypi package.

Sadly, the package doesn't create any executable file to run. Not sure why. In the meantime, create a batch file (`pokemon-tv.bat`) and place it in `%localappdata%/Programs/Python/Python38-32/Scripts`

```
cd %localappdata%/Programs/Python/Python38-32/Lib/site-packages/pokemon-tv
python3 __init__.py "%~1" "%~2"
```

Now, please just use the steps I provided earlier please. It's less hassle somehow, and is less frustrating.
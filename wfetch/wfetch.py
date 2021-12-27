#!/usr/bin/python3

# MODULES

# Weather
from pyowm import OWM # Main weather
from pyowm.commons import exceptions # Weather exceptions

# Other
import requests # For geolocation
from fire import Fire # For CLI argument control
from datetime import datetime # For date+time
import os # For system-related stuff

# FUNCTIONS

# Main function
def main(help:bool=False, ascii:str='', place:str=None, hpa:bool=False):
    # If "help" argument, call help function
    if help: man()

    # Get geolocation
    try: GEO = requests.get('https://ipinfo.io/').json() # IP
    except requests.exceptions.ConnectionError: # Except if no internet
        print("\u001b[1m\u001b[31mLOW INTERNET CONNECTION.\u001b[0m")
        exit(1)

    # Set city to geolocation
    if not place: CITY = f"{GEO['city']}, {GEO['country']}"
    else: # Set city to "place" argument (if given)
        if isinstance(place, tuple): CITY = ', '.join(place) # Join if recognized as tuple 
        else: CITY = place # Do nothing if recognized as str/int

    # Get API key envirement variable and set CLIENT
    try: CLIENT = OWM(os.environ['WEATHER_CLI_API'])
    except KeyError: # Except if API key variable not found
        print("\u001b[1m\u001b[31mAPI KEY NOT FOUND. TRY ADDING THIS TO YOUR BASH/ZSH PROFILES: export WEATHER_CLI_API=(your OWM api key)")
        exit(1)

    # Get weather from api
    WM = CLIENT.weather_manager()

    # Get data from weather
    try:
        if isinstance(CITY, int): WEATHER = WM.weather_at_id(CITY).weather # If CITY is a number, get weather at id
        else: WEATHER = WM.weather_at_place(CITY).weather # If CITY is a string, get weather at place
    except exceptions.NotFoundError: # Except if city not found
        print("\u001b[1m\u001b[31mPLACE NOT FOUND.\u001b[0m")
        exit(1)
    except exceptions.UnauthorizedError:  # Except if API key is invalid
        print("\u001b[1m\u001b[31mINVALID API KEY. IF YOU JUST ADDED YOUR KEY, CHECK IT AND WAIT A FEW MINUTES.\u001b[0m")
        exit(1)
    except exceptions.TimeoutError: # Except if no internet
        print("\u001b[1m\u001b[31mLOW INTERNET CONNECTION.\u001b[0m")
        exit(1)

    # Get the ascii art name
    if not ascii: STATUS = WEATHER.detailed_status.replace(" ", "_") # Get from weather data
    else: STATUS = ascii.replace('_day', '').replace('_night', '') # Get the ascii art name from "ascii" argument (if given)

    if GEO['country'] == 'US': METRICS = ('fahrenheit', 'miles_hour', 'mph', datetime.today().strftime(r'%m-%d-%y'), 'inHg', 33.864) # US measurements
    else: METRICS = ('celsius', 'meters_sec', 'm/s', datetime.today().strftime(r'%d.%m.%y'), 'mmHg', 1.333) # EU measurements
    
    if hpa: # HPa support
        METRICS = list(METRICS) # Convert METRICS to list
        METRICS[4] = 'HPa' # Change mmHg/inHg to HPa
        METRICS[5] = 1 # Change the number
    
    # Get day or night
    if datetime.fromtimestamp(WEATHER.sunrise_time()) > datetime.today() or datetime.fromtimestamp(WEATHER.sunset_time()) < datetime.today(): ASCIITYPE = DAYNIGHT = 'night'
    else: ASCIITYPE = DAYNIGHT = 'day'
    
    # Get day or night from "ascii" argument (if given)
    if ascii.endswith('_day'): ASCIITYPE = 'day' 
    elif ascii.endswith('_night'): ASCIITYPE = 'night'

    # Get ascii icon
    if "XDG_CONFIG_HOME" in os.environ: # XDG_CONFIG_HOME support (thanks zsadroh)
        HOME=os.environ["XDG_CONFIG_HOME"]
        CONFIG_FOLDER = "wfetch"
    else:
        HOME=os.path.expanduser("~")
        CONFIG_FOLDER = ".wfetch"

    ICONPATH = os.path.join(HOME, CONFIG_FOLDER) # Get the path to icon folder
    try: ICON = open(os.path.join(ICONPATH, 'neutral', f'{STATUS}.txt')).read().splitlines() # Get neutral icon from /icons/neutral directory
    except FileNotFoundError: # Except if file not found in /icons/neutral directory
        try: ICON = open(os.path.join(ICONPATH, ASCIITYPE, f'{STATUS}.txt')).read().splitlines() # Get icon from /icons/(day|night) directory
        except FileNotFoundError: ICON = open(os.path.join(ICONPATH, 'unknown.txt')).read().splitlines() # If not found, display "?"
    COLOR = ICON.pop(0) # Get color as first line

    # Info string (self-explanatory)
    INFO = f'''    \u001b[1m\u001b[{COLOR}m{WEATHER.detailed_status.title().replace(" ", "")}\u001b[37m@{CITY.split(', ')[0]}\u001b[0m
    \u001b[1m\u001b[{COLOR}m{METRICS[3]}\u001b[37m:{DAYNIGHT.title()}\u001b[0m

    \u001b[{COLOR}mTemperature\u001b[0m\u001b[37m:    {round(WEATHER.temperature(METRICS[0])['temp'])}°{METRICS[0][0].upper()}
    \u001b[{COLOR}mHumidity\u001b[0m\u001b[37m:       {WEATHER.humidity}%
    \u001b[{COLOR}mPressure\u001b[0m\u001b[37m:       {round(WEATHER.pressure['press']/METRICS[5])}{METRICS[4]}
    \u001b[{COLOR}mWind\u001b[0m\u001b[37m:           {round(WEATHER.wind(METRICS[1])['speed'])}{METRICS[2]}@{WEATHER.wind()['deg']}°
    \u001b[{COLOR}mSunrise-sunset\u001b[0m\u001b[37m: {datetime.fromtimestamp(WEATHER.sunrise_time()).strftime('%-H:%M')}-{datetime.fromtimestamp(WEATHER.sunset_time()).strftime('%-H:%M')}
    \u001b[0m'''.splitlines()

    # Print the info
    print('\n', end='') # Newline
    for line in enumerate(ICON): # Go through icon lines
        try: print(f'\u001b[{COLOR}m' + line[1] + '\u001b[0m' + INFO[line[0]]) # Print icon line + info line
        except IndexError: print(line[1]) # If icon is bigger than info, print only icon
    print('\n', end='') # Newline

# Help function
def man():
    # Print the help string (self-explanatory)
    print('''   
    \u001b[1mArguments\u001b[1m:
    \u001b[1m--help\u001b[0m:                               Shows this message
    \u001b[1m--ascii="icon_name"\u001b[0m:                  Changes the icon to whatever you choose (ex. "light_rain")
                                            \u001b[1mNote\u001b[0m: Some icons have day and night variants, just add "_day" or "_night" to see them (ex. "clear_sky_night")
    \u001b[1m--place="City, Country(2 Letters)"\u001b[0m:   Shows the weather at that place (ex. "London, UK")

    \u001b[1mAuthors & Contributors\u001b[0m:
    \u001b[1mG_cat\u001b[0m:                                Author (https://github.com/Gcat101)
    \u001b[1mPure Cheekbones\u001b[0m:                      Install + .gitignore cleanup (https://github.com/pure-cheekbones)
    \u001b[1mZsadroh\u001b[0m:                              Install cleanup (https://github.com/zsadroh)
    \u001b[1mMatt Camp\u001b[0m:                            XDG_CONFIG_HOME support (https://github.com/usmcamp0811)
    ''')
    exit(0) # Exit so main function does not get called

# CLI
if __name__ == '__main__': # Check if not imported
    Fire(main) # Launch main function with arguments

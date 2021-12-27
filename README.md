# Wfetch

**Neofetch/pfetch, but for weather**

![Logo](https://github.com/Gcat101/Wfetch/blob/master/Logo.png)

[![oxygen](https://forthebadge.com/images/badges/powered-by-oxygen.svg)](https://forthebadge.com)

[![contributions](https://img.shields.io/badge/contributions-welcome-green)](https://img.shields.io/badge/contributions-welcome-green)

## Features

- Information about the weather outside:
    1. Weather condition
    2. Temperature
    3. Humidity
    4. Pressure
    5. Wind
    6. Sunrise-sunset time

- Cool logo for each weather condition

- Ability to choose logos

- See weather at different places

## Requirements

Python3

## Installation

### ~~Pip~~

**WIP**

### Git

```shell
git clone "https://github.com/Gcat101/Wfetch.git"; cd ./Wfetch; sudo bash "install.sh"
```

### Curl

```shell
sudo curl -s https://raw.githubusercontent.com/Gcat101/Wfetch/master/install.sh | sudo bash -s
```

## Getting the api key (IMPORTANT)

1. Go to [OWM](https://openweathermap.org/) and click "api"
2. Sign up
3. Click "api keys"
4. Create an api key
5. Add `export WEATHER_CLI_API=(your api key)` to your ~/.bashrc
6. You're ready to go!

## Usage

Get the weather at your current location:

```shell
wfetch
```

Specify the ascii logo:

```shell
wfetch --ascii="mist"
```

Get the weather from a different location:

```shell
wfetch --place="London, UK"
```

Get pressure in HPa units:

```shell
wfetch --hpa
```

Get the manual:

```shell
wfetch --help
```

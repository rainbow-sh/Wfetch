# Wfetch

**Neofetch/pfetch, but for weather.**

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

- Abilty to choose logos

- See weather at different places

## Requirements

Python3

## Installation

### ~~Install through pip~~

**WIP**

### Or from github

```shell
git clone https://github.com/Gcat101/wfetch
cd wfetch
sh ./install.sh
cd ../
```

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

Get the manual:

```shell
wfetch --help
```

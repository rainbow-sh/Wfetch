# Wfetch

**Neofetch/pfetch, but for weather.**

---

![Logo](https://github.com/Gcat101/Wfetch/blob/master/Logo.png)

---

## Features

- Information about the weather outside
    1. Weather condition
    2. Temperature
    3. Humidity
    4. Pressure
    5. Wind
    6. Sunrise-sunset time

- Cool logo for each weather condition

- Abilty to choose logos

- See weather at different places

---

## Requirements

Python3

---

## Installation

Install through pip:

```shell
/usr/bin/python3 -m pip install wfetch
```

Or from source:

```shell
git clone https://github.com/Gcat101/wfetch
cd wfetch
/usr/bin/python3 -m pip -r ./requirements.txt
cp -a ./src/wfetch/. /usr/local/bin
```

---

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

---

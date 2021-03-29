# Gilfoyle Bitcoin Alert

[![forthebadge](https://forthebadge.com/images/badges/powered-by-black-magic.svg)](https://forthebadge.com)

Made for devotion to the TV series Silicon Valley, **Gilfoyle Bitcoin Alert** is a Python3 script which alerts the user with the Napalm Death sound (as the one used by Gilfoyle in Season 5 Episode 3) when the Bitcoin price changes rapidly above or below a given threshold.

The price is fetched from the [_CoinMarketCap API_](https://coinmarketcap.com/api/) every 5 minutes and the default currency is USD.

## How to install and run code
### Installation

```console
# clone the repo
$ git clone https://github.com/BITPoliTO/bitcoin-alert.git

# change the working directory to bitcoin-alert
$ cd bitcoin-alert

# install general requirements
$ pip install -r requirements.txt

# Run this line only on MacOS
$ pip install pyobjc
```
On **Linux** make sure `python3-gst-1.0` is installed by running `sudo apt install python3-gst-1.0`

### Run
```console
$ python alert.py
```

<br>
<img src="https://raw.githubusercontent.com/alessandroguggino/GilfoyleBTCAlert/master/gif_gilfoyle.gif" width="350" title="Silicon Valley GIF" />
<br>


#### Made to scare the BIT PoliTO office 👻 by  
  
<a href="https://github.com/BITPoliTO/bitcoin-alert/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=bitpolito/bitcoin-alert" />
</a>

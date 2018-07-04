# bawiBot
bawi Crawling bot for Python3

## Python Package Requirements
 * pip3 install selenium
 * pip3 install bs4
 * pip3 install Slacker

## For Ubuntu
 * Download Chrome Driver from below
   https://sites.google.com/a/chromium.org/chromedriver/downloads


## For Raspberry Pi 3
 * sudo apt-get update
 * sudo apt-get install iceweasel
 * sudo apt-get install xvfb
 * sudo pip3 install selenium==2.53.6
 * sudo pip3 install PyVirtualDisplay
 * sudo pip3 install xvfbwrapper

 * (in case of geckodriver Error) selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
   * wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-arm7hf.tar.gz
   * tar -xvf gecko~.tar.gz
   * chmod +x geckodriver
   * sudo cp geckodriver /usr/local/bin/

## Usage
 * python3 main.py [uid] [passwd] [slackbotToken]

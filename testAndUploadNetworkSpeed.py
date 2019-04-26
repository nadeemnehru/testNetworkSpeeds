mport subprocess
import time
import glob
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from TwitterAPI import TwitterAPI


# Function to connect to networks one by one, test their speed and save the result
def getSpeeds():
        networks = {SSID1: PASSWORD , SSID2: PASSWORD,...}
        for key,value in networks.items():
                print("Connecting to " + key)
                conn = subprocess.Popen(['nmcli', 'dev', 'wifi', 'connect', key, 'password', value], stdout = subprocess.PIPE)
                chrome_options = Options()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                driver = webdriver.Chrome(chrome_options=chrome_options)
                print("Beginning speed test of " + key)
                driver.get('https://fast.com/')
                print("Waiting for speed test result of " + key)
                time.sleep(120)
                driver.save_screenshot(PATH_TO_SAVE_SCREENSHOT + key + '.png')
                print("Saved speed test result of " + key + PATH_WHERE_SCREENSHOT_IS_SAVED)
        uploadResults()


# Function to upload saved speed test results to twitter
def uploadResults():
        paths = glob.glob(PATH_WHERE_SCREENSHOTS_ARE_SAVED/*)
        CONSUMER_KEY = YOUR_CONSUMER_KEY 
        CONSUMER_SECRET = YOUR_CONSUMER_SCRET
        ACCESS_TOKEN_KEY = YOUR_ACCESS_TOKEN_KEY
        ACCESS_TOKEN_SECRET = YOUR_ACCESS_TOKEN_SECRET
        api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

        p = re.compile(r'[a-zA-Z]+.png')
        print("Uploading speed test results")
        for file in paths:
                network = p.findall(file)[0]
                with open(file, 'rb') as f:
                        data = f.read()
                        r = api.request('statuses/update_with_media', {'status':network}, {'media[]':data})
                        print('Upload status for ' + network, r.status_code)


if __name__ == '__main__':
        getSpeeds()

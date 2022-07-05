import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO


class League:
    options = Options()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options, executable_path=os.environ.get("CHROMEDRIVER_PATH"))

    def get_rune(self, champion, role):
        # All the recommended runes are from u.gg
        self.driver.get(f'https://u.gg/lol/champions/{champion}/build?role={role}')
        self.driver.execute_script("window.scrollTo(0, 200)")

        image = self.driver.find_element(By.CLASS_NAME, 'recommended-build_runes').screenshot_as_png
        im = Image.open(BytesIO(image))
        im.save(f'{champion}.png')
        self.driver.back()
        return f'{champion}.png'


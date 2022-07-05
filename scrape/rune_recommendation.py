import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO


class League:
    options = Options()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument('--allow-insecure-localhost')
    prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                        'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                        'notifications': 2, 'auto_select_certificate': 2,
                                                        'fullscreen': 2,
                                                        'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                        'media_stream_mic': 2, 'media_stream_camera': 2,
                                                        'protocol_handlers': 2,
                                                        'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                        'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                        'metro_switch_to_desktop': 2,
                                                        'protected_media_identifier': 2, 'app_banner': 2,
                                                        'site_engagement': 2,
                                                        'durable_storage': 2}}
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('prefs', prefs)
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-javascript")
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


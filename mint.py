from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc

def run_session():
    chrome_options = uc.ChromeOptions()
    chrome_options.headless = True 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    chrome_options.add_argument(f'--disable-gpu')
    
    chrome_options.add_argument(f'--disable-dev-shm-usage')
    driver = uc.Chrome(options=chrome_options)
    try:
        driver.get("https://mrscan.onrender.com")
        print(f" connected to page")
        i = 0
        while True:
          i= 1+1
          print(i)
        
   
    except Exception as err:
       pass
    
while True:    
    run_session()

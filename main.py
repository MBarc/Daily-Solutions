import time
from discord_webhook import DiscordWebhook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

productLink = 'https://www.amazon.com/gp/offer-listing/B07VGRJDFY/ref=as_li_ss_tl?ie=UTF8&m=ATVPDKIKX0DER&mv_color_name=1&mv_style_name=0&linkCode=ll2&tag=siusa-mp-20&linkId=d2441ad1601b8676b5d2916d328bdea1&language=en_US'

driver = webdriver.Chrome('C:\\Users\\micha\\AppData\\Local\\Programs\\Python\\chromedriver.exe')
driver.get(f'{productLink}')
webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/722527059003572285/ryOWs7ZUNHofcmA-V5FnktmFz48LL_ZEiDaftvXsh2e_fYLjj5mxHcnrKelgqHEo3H70', content=f'<{productLink}>')


while True:

    try:
        preOrderButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "submit.addToCart"))
        )
    except:
        preOrderButton = False

    if preOrderButton:
        response = webhook.execute()
        time.sleep(5)
    else:
        print('preOrder button not located.')

    driver.refresh()

driver.close()

'''
Purpose: To notify user when the Nintendo Switch was in stock on Amazon.com.

Problem Description: My girlfriend really wanted a Nintedo Switch and had been trying to buy one for the 3 months prior to this script's creation.
She was using StockInformer <https://www.stockinformer.co.uk/blog-discord-stock-notification-alerts>. After trying StockInformer myself, I found that the notifications
they send out were ~10 minutes late. So I decided to create this script that would send the notifications almost instantly (1 second delay). After deploying this script, my girlfriend
was able to buy a Nintendo Switch the first time she got the notification that it was in stock.

import time
from discord_webhook import DiscordWebhook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

productLink = 'https://www.amazon.com/gp/offer-listing/B07VGRJDFY/ref=as_li_ss_tl?ie=UTF8&m=ATVPDKIKX0DER&mv_color_name=1&mv_style_name=0&linkCode=ll2&tag=siusa-mp-20&linkId=d2441ad1601b8676b5d2916d328bdea1&language=en_US'

driver = webdriver.Chrome('C:\\Absolute\\Path\\To\\chromedriver.exe')
driver.get(f'{productLink}')
webhook = DiscordWebhook(url='my-custom-webhook-url', content=f'<{productLink}>')


while True:

    # See if the 'Add To Cart' Button exists and set to False if it doesn't.
    try:
        preOrderButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "submit.addToCart"))
        )
    except:
        preOrderButton = False

    # If the 'Add To Cart' button exists, send the notification via webhook.
    if preOrderButton:
        response = webhook.execute()
        time.sleep(5)
    else:
        print('preOrder button not located.')

    #Refresh the page to see if conditions have changed.
    driver.refresh()

driver.close()

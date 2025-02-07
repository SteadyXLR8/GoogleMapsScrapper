from selenium.webdriver.support.wait import WebDriverWait

from tentVendor.scrapper import Booking
import pandas as pd
import time

# context managers
with Booking(teardown=False) as bot:
    bot.land_first_page()
    # bot.enter_search_text("Bangalore tent and Pandal Service")
    # bot.enter_search_text("Tent and Pandal Services in Bengaluru")
    bot.enter_search_text("tent house providers in Bengaluru")
    bot.collect_data()


    # Creating csv file from the list
    pd.DataFrame(bot.getData()).to_csv("tent_pandal_vendors.csv", index=True)
    print(
        f"Successfully created a file named tent_pandal_vendors.csv in the current directory."
    )
    WebDriverWait(bot, 10)
    time.sleep(10)
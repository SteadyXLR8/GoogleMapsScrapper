from selenium.webdriver.support.wait import WebDriverWait

from tentVendor.scrapper import Booking
import pandas as pd
import time

# context managers
with Booking(teardown=False) as bot:
    bot.land_first_page()
    # bot.enter_search_text("Tent Services in Bengaluru")
    bot.enter_search_text("Event management companies in Bengaluru")
    bot.collect_data()


    # Creating csv file from the list
    # file_name = "tent_vendor.csv"
    file_name = "event_management_vendor.csv"

    pd.DataFrame(bot.getData()).to_csv(file_name, index=True)
    print(
        f"Successfully created a file name {file_name} in the current directory."
    )
    WebDriverWait(bot, 10)
    time.sleep(10)
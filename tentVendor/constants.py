# BASE_URL = "https://www.justdial.com/"
BASE_URL = "https://www.google.com/maps/"

# selector for search box
SEARCH_BOX_ID = "searchboxinput"

# selector for result feed
RESULT_FEED_SELECTOR = "div[role='feed']"

# class for items in the feed
RESULT_ITEM_CLASS = "Nv2PK"

# # class for links in each item
RESULT_LINK_CLASS = "hfpxzc"

# class for name of each item
RESULT_NAME_CLASS = "qBF1Pd"

# selector for address of each item
RESULT_ADDRESS_SELECTOR = "[data-item-id='address']"

# selector for phone of each item
RESULT_PHONE_SELECTOR = "[data-item-id*='phone:']"

# selector for closing the item info window
CLOSE_ITEM_INFO_WINDOW_SELECTOR = "[data-disable-idom='true']"

# error message during data fetching
ERROR_MESSAGE = "Sorry, we are unable to fetch the data at the moment due to "

# selector for share button
SHARE_BUTTON_SELECTOR = "[data-value='Share']"

# selector for input element for the link
LINK_INPUT_SELECTOR = "vrsrZe"

# selector for close button for the modal
CLOSE_BUTTON_SELECTOR = '[aria-label="Close"]'

# script for bringing the list items into focus
BRING_IN_FOCUS_SCRIPT = "arguments[0].scrollIntoView();"

# const to keep track of how many times to scroll the feed container
# More data -> increase the counter
SCROLL_FEED_COUNTER = 750
# less data -> decrease the counter
# SCROLL_FEED_COUNTER = 300

# timeout after each scroll
SCROLL_TIMEOUT = 1

# timeout after searching
SEARCH_TIMEOUT = 10

# timeout in seconds -> waiting x seconds before doing any activity
IMPLICIT_WAIT_TIME = 15

# timeout after executing bring in focus script
TIMEOUT_AFTER_SCRIPT_EXE = 2

# timeout after clicking each result item
TIMEOUT_AFTER_CLICK = 2

# Not available string when info is missing
NOT_AVAILABLE = "N/A"
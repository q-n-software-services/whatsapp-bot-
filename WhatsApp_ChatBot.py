import datetime

import pyautogui as pt
from time import sleep
import pyperclip
import random
import turtle

sleep(3)
x = 122
y = 122
pt.moveTo(x, y, duration=1)
# Gets Message


def get_message():
    global x, y

    position = pt.locateOnScreen("smily_paperclip.jpg", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x+85, y-45, duration=.5)

    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, -122)
    pt.click()

    whatsapp_message = pyperclip.paste()

    print("message recieved:\t\t" + whatsapp_message)

    return whatsapp_message

# posts


def post_response(message):
    global x, y
    position = pt.locateOnScreen("smily_paperclip.jpg", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200, y+20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)

# processes response

def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any Questions"
    else:
        if random_no == 0:
            return "Thats cool"
        elif random_no == 1:
            return "Please call if its urgent, I won't reply on WhatsApp"
        else:
            return "I want to eat something"


# check for new messages

def check_for_new_messages():

    while True:
        # continuously checks for green dot and new messages

        position = pt.locateOnScreen("green_circle.jpg", confidence=.92)
        if position is not None:
            pt.moveTo(position)
            pt.moveRel(-100, 0)
            pt.click()


        else:
            print("No new messages found", datetime.datetime.now())
            continue

        #if pt.pixelMatchesColor(int(x+50), int(y-70), (255, 255, 255), tolerance=10):
         #   print("is white")
        processed_message = process_response(get_message())

        post_response(processed_message)

        position = pt.locateOnScreen('options_tab.jpg', confidence=.92)
        if position is not None:
            pt.moveTo(position)
            pt.moveRel(14, 0)
            pt.click()

            pt.moveRel(-24, 138)
            pt.click()

        # else:
        #    print("No new messages yet...")


check_for_new_messages()







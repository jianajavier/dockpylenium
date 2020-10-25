from helpers.web_helper_methods import *
from datetime import datetime
import argparse
import pdb

TODAYS_DATE = datetime.today().strftime('%Y-%m-%d')
SCREENSHOT_NAME = "screenshot_%s.png" % TODAYS_DATE

class Dockpylenium(object):
    def __init__(self, driver):
        self.driver = driver

    def interact_with_browser(self):
        f = open("links.txt", "r")
        for link in f:
            self.driver.get(link)
            self.send_results_to_email(link)
            print("Success. Check your email!")

    def send_results_to_email(self, link):
        save_screenshot(self.driver, SCREENSHOT_NAME)
        send_email(self.prepare_email(link))

    def prepare_email(self, link):
        email_params = {}
        email_params['subject'] = "Your Subject"
        email_params['screenshot_name'] = SCREENSHOT_NAME
        email_params['body'] = """\
                                <p>%s</p>
                                <p>Screenshot<br/>
                                    <img src="cid:image1">
                                </p>
                                """ % link
        return email_params

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--debug", help="Debug mode", type=int, default=0)
    argus = parser.parse_args()
    return argus

def main(debug):
    Dockpylenium(initialize_driver(debug)).interact_with_browser()

if __name__ == '__main__':
    argus = parse_arguments()
    main(argus.debug)




import datetime
import pdb
import os

# Selenium libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Email libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

TO_EMAIL = 'youremail@mail.com' # Change this to your email
FROM_EMAIL = 'jianascripts@gmail.com' # Change this if you create an email
APP_PASSWORD = 'woczgwgmwjsmnuhe' # Change this to your created email app password

def initialize_driver(debug_mode = 0):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    if debug_mode != 1:
        chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def save_screenshot(driver, screenshot_name, error = ''):
    os.makedirs("screenshots", exist_ok=True)
    screenshot_name = "screenshots/%s%s" % (error, screenshot_name)
    driver.save_screenshot(os.path.abspath(screenshot_name))

def send_email(params):
    from_email = FROM_EMAIL
    to_email = TO_EMAIL

    msg = MIMEMultipart('related')
    msg['Subject'] = params['subject']
    msg['From'] = from_email
    msg['To'] = to_email

    # Create the body of the message.
    html = params['body']

    screenshot_name = "screenshots/%s" % params['screenshot_name']
    img_file = open(os.path.abspath(screenshot_name), 'rb')
    img = img_file.read()
    msgImg = MIMEImage(img, 'png')
    msgImg.add_header('Content-ID', '<image1>')
    msgImg.add_header('Content-Disposition', 'inline', filename=screenshot_name)

    # Record the MIME types.
    msgHtml = MIMEText(html, 'html')
    msg.attach(msgHtml)
    msg.attach(msgImg)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(from_email, APP_PASSWORD)
    server.sendmail(from_email, to_email, msg.as_string())

    server.quit()


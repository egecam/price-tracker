from bs4 import BeautifulSoup
import requests
import checktime
import smtplib
import time
import config

getNow = checktime.timeCheck()


def check_price():
    html_text = requests.get(
        'https://www.pt.com.tr/macbook-air-13-3-inc-m1-8c-8gb-ram-256gb-ssd-uzay-grisi-mgn63tu-a').text
    soup = BeautifulSoup(html_text, 'lxml')
    price = soup.find('div', class_='col-md-12 price pricePTpro').text
    converted_price = float(price[0:5])

    if (converted_price < 8.999):
        print('₺', converted_price, getNow)
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('egeege95@gmail.com', config.password)

    subject = 'Price fell down!'
    body = "Check the product link: https://www.pt.com.tr/macbook-air-13-3-inc-m1-8c-8gb-ram-256gb-ssd-uzay-grisi-mgn63tu-a"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('egeege95@gmail.com', 'egecam000@gmail.com', msg)
    print('Email has been sent!')

    server.quit()


check_price()

while(True):
    check_price()
    time.sleep(86400)

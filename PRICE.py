import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Apple-Watch-GPS-Cellular-44mm-Aluminium/dp/B07J9MV4BV/ref=sr_1_2_sspa?crid=2SRCSVTSZQ1AO&keywords=apple+watch+series+4&qid=1563874206&s=gateway&sprefix=apple+%2Caps%2C1089&sr=8-2-spons&psc=1'
headers = {"user-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
def check_price():


	page = requests.get(URL , headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')	
	price = soup.find(id="priceblock_ourprice").get_test()
	converted_price = float(price[0:6])
	if(converted_price < 40000):
		send_mail()

def send_mail():
# Enable the 2 step varification in google and generate a new password for main and then use that password here 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('your_gmail_id','your_generated_password')
	subject = 'PRICE FALL !!'
	body = ' check it out... https://www.amazon.in/Apple-Watch-GPS-Cellular-44mm-Aluminium/dp/B07J9MV4BV/ref=sr_1_2_sspa?crid=2SRCSVTSZQ1AO&keywords=apple+watch+series+4&qid=1563874206&s=gateway&sprefix=apple+%2Caps%2C1089&sr=8-2-spons&psc=1'
	
	msg = f"Subject : {subject}\n\n{body}"

	server.sendmail(
	'your_email_id',
	'your_email_id'
	msg
	)
	print("MAIL SENT !!")
	server.quit()
while(True):
	check_price()
	time.sleep(60*60*12)	

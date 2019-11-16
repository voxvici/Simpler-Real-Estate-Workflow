from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import csv
import sys
import time
import pyperclip

class SREWF:

	def __init__(self):
		self.address = []
		self.a = 1
		self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
		self.url = 'https://www.phila.gov/revenue/realestatetax/'
		self.Start()

	def Start(self):
		print('Working on it, Boss..')

		with open('redata.csv', 'r') as file:
			reader = csv.reader(file)

			for column in reader:
				self.address.append(column[1])

		addressvalue = len(self.address)

		balanceduetxt = open('balancedue.txt', 'a')
		saledatetxt = open('saledate.txt', 'a')
		salepricetxt = open('saleprice.txt', 'a')
		ownertxt = open('owner.txt', 'a')

		try:
			while self.a < addressvalue:

				self.address[self.a]
				self.driver.get(self.url)
				time.sleep(3)
				self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/div/form/input').send_keys(self.address[self.a])
				self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/div/button').click()
				time.sleep(6)

				balancedue = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/h2/b')
				pyperclip.copy(balancedue.text)
				balanceduetxt.write(pyperclip.paste() + '\n')

				saledate = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/div[1]/div/div/div[2]/table/tbody/tr[5]/td')
				pyperclip.copy(saledate.text)
				saledatetxt.write(pyperclip.paste() + '\n')

				saleprice = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/div[1]/div/div/div[2]/table/tbody/tr[6]/td')
				pyperclip.copy(saleprice.text)
				salepricetxt.write(pyperclip.paste() + '\n')

				owner = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/div[1]/div/div/div[2]/table/tbody/tr[3]/td')
				pyperclip.copy(owner.text)
				ownertxt.write(pyperclip.paste() + '\n')
				self.a += 1
				time.sleep(1)

		except Exception:
			print('Please try again..')

if __name__ == '__main__':
	SREWF()

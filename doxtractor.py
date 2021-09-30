
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

import requests, sys, os, time, re, json

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options,executable_path="geckodriver")

def checkfile():
	print('[+] checking file result_single.txt....')
	print('[+] checking file result_mass.txt....')
	try:
		file=open('result_single.txt')
		file=open('result_mass.txt')
		file=open('result_subdomain.txt')
		print('[+] result_single.txt found 🚀')
		print('[+] result_mass.txt found 🚀')
	except IOError:
		print('[+] Creating file result_single.txt')
		print('[+] Creating file result_mass.txt')
		print('[+] Starting tool...')
		open('result_single.txt', 'a').write("")
		open('result_mass.txt', 'a').write("")
		open('result_subdomain.txt', 'a').write("")

		#grabber()


def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def login():
	url = "https://securitytrails.com/app/auth/login"
	driver.get(url)
	driver.find_element_by_xpath('//*[@id="email"]').send_keys('keviril762@ergowiki.com')
	driver.find_element_by_xpath('//*[@id="password"]').send_keys('Doxtractor123')
	driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/main/div/div/form/div[4]/button').click()
	print('[+] Trying login to account')
	print('[+] Login success')
	time.sleep(1)



def mass_key(target):
	page = 1
	while(True):
		print('[+] Scraping page : {} | Keyword : {}' .format(page, target))	
		url2 = "https://securitytrails.com/list/keyword/{}?page={}" .format(target,page)
		driver.get(url2)
		if '/domain/' in driver.page_source:
			find = re.findall('href="/domain/(.*?)/dns">', driver.page_source)
			a = open('result_mass.txt', mode='r').read()
			for result in find:
				if result in a:
					print('{} -> Duplicate | SKIPPED' .format(result))
				else:
					print(result)
					asik = ''+result
					open('result_mass.txt', 'a', encoding='utf-8').write(asik+'\n')

		else:
			break

		page+=1

def mass_ip(target):
	page = 1
	while(True):
		print('[+] Scraping page : {} | Keyword : {}' .format(page, target))	
		url2 = "https://securitytrails.com/list/ip/{}?page={}" .format(target,page)
		driver.get(url2)
		if '/domain/' in driver.page_source:
			find = re.findall('href="/domain/(.*?)/dns">', driver.page_source)
			a = open('result_mass.txt', mode='r').read()
			for result in find:
				if result in a:
					print('{} -> Duplicate | SKIPPED' .format(result))
				else:
					print(result)
					asik = ''+result
					open('result_mass.txt', 'a', encoding='utf-8').write(asik+'\n')

		else:
			break

		page+=1

def keyword():	
	keyword = input('Keyword : ')
	page = 1
	while(True):
		print('[+] Scraping page : {}' .format(page))
		url2 = "https://securitytrails.com/list/keyword/{}?page={}" .format(keyword,page)
		driver.get(url2)
		if '/domain/' in driver.page_source:
			find = re.findall('href="/domain/(.*?)/dns">', driver.page_source)
			a = open('result_single.txt', mode='r').read()
			for result in find:
				if result in a:
					print('{} -> Duplicate | SKIPPED' .format(result))
				else:
					print(result)
					asik = ''+result
					open('result_single.txt', 'a', encoding='utf-8').write(asik+'\n')
		else:
			print("[+] Done in page : {}" .format(page))
			break

		page +=1

def domain():
	try:
		dom = input('domain : ')
		t = 0
		url = "https://securitytrails.com/_next/data/0e25d3b6/list/apex_domain/"
		form = ".json?page=1&domain="+dom
		driver.get(url + dom + form)
		if '"records"' in driver.page_source:
			find = re.findall('],"hostname":"(.*?)"', driver.page_source)
			a = open('result_subdomain.txt', mode='r').read()
			for result in find:
				if result in a:
					print('{} -> Duplicate | SKIPPED' .format(result))
				else:
					print(result)
					asik = ''+result
					open('result_subdomain.txt', 'a', encoding='utf-8').write(asik+'\n')
		else:
			print("[+] Done in page : {}" .format(page))
			
		t +=1
	except IndexError:
		print('done')


def ip():
	keyword = input('IP : ')
	page = 1
	while(True):
		print('[+] Scraping page : {}' .format(page))
		url3 = "https://securitytrails.com/list/ip/{}?page={}" .format(keyword,page)
		driver.get(url3)
		if '/domain/' in driver.page_source:
			find = re.findall('href="/domain/(.*?)/dns">', driver.page_source)
			a = open('result_single.txt', mode='r').read()
			for result in find:
				if result in a:
					print('{} -> Duplicate | SKIPPED' .format(result))
				else:
					print(result)
					asik = ''+result
					open('result_single.txt', 'a', encoding='utf-8').write(asik+'\n')
		else:
			print("[+] Done in page : {}" .format(page))
			break

		page +=1

def option():
	nanya = input('Your list : ')
	lis = open(nanya, 'r', encoding='utf-8').read().splitlines()
	for site in lis:
		target = site.strip()
		mass_key(target)

def option1():
	nanya = input('Your list : ')
	lis = open(nanya, 'r', encoding='utf-8').read().splitlines()
	for site in lis:
		target = site.strip()
		mass_ip(target)

def interupt():
	clear()
	print("\n")
	print(" User Interruption Detected..!")
	time.sleep(1)

def banner2():
	print("""

░█▀▀▄ ░█▀▀▀█ ▀▄░▄▀ ▀▀█▀▀ ░█▀▀█ ─█▀▀█ ░█▀▀█ ▀▀█▀▀ ░█▀▀▀█ ░█▀▀█ 
░█─░█ ░█──░█ ─░█── ─░█── ░█▄▄▀ ░█▄▄█ ░█─── ─░█── ░█──░█ ░█▄▄▀ 
░█▄▄▀ ░█▄▄▄█ ▄▀░▀▄ ─░█── ░█─░█ ░█─░█ ░█▄▄█ ─░█── ░█▄▄▄█ ░█─░█ v1.0.beta

                   coded by riotsun_ X Nxq_
    """)


def banner():
	print("""
	        OPTIONS :
		[1] single keyword
		[2] Mass keyword 
		[3] single IP
		[4] Mass IP
		[5] Subdomain Lookup
		[0] exit
		""")

if __name__ == "__main__":
	ins = '1'
	checkfile()
	login()
	clear()
	while ins != ("0"):
		
		
		banner2()
		banner()
		ins = input('Choose : ')
		if ins == '1':
			keyword()
			
		elif ins == '2':
			option()

		elif ins == '3':
			ip()
			
		elif ins == '0':
			sys.exit()

		elif ins == '4':
			option1()

		elif ins == '5':
			domain()

		else:
			print('Wrong choice !')
	

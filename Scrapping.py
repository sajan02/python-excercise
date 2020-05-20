import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import urllib2
from bs4 import BeautifulSoup



# Using this to check if its the first time of the day or not
# Default initiated with True.
#f = open("status_storage.txt", "r")
#status = f.read()

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() + "/chromedriver_linux64" + "/chromedriver"
print(chrome_driver)

def get_scrap(url):
    #quote_page = 'https://retail.onlinesbi.com/retail/login.htm'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    #name_box = soup.find('a', attrs={'class': 'login_button'})
    print(soup)

def find_all_indexes(input_str, substring):
    l2 = []
    length = len(input_str)
    index = 0
    while index < length:
        i = input_str.find(substring, index)
        if i == -1:
            return l2
        l2.append(i)
        index = i + 1
    return l2

def bank_scrapping():
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    #browser.maximize_window()

    browser.get("https://netbanking.netpnb.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&__FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=024")
    
    username = browser.find_element_by_xpath("//input[@name='AuthenticationFG.USER_PRINCIPAL']")
    username.send_keys('randomusername')    #username here
    time.sleep(1)
    
    continueBtn = browser.find_element_by_xpath("//input[@name='Action.STU_VALIDATE_CREDENTIALS']")
    continueBtn.click()
    time.sleep(1)

    password = browser.find_element_by_xpath("//input[@name='AuthenticationFG.ACCESS_CODE']")
    password.send_keys('ranndompassword') #password here
    time.sleep(1)

    loginBtn = browser.find_element_by_xpath("//input[@name='Action.VALIDATE_STU_CREDENTIALS']")
    loginBtn.click()

    time.sleep(1)
    
    ACbtn = browser.find_element_by_xpath("//a[@id='My-ShortCuts_Account-Statement']")
    ACbtn.click()
    time.sleep(1)

    SearchBtn = browser.find_element_by_xpath("//input[@name='Action.SEARCH']")
    SearchBtn.click()

    date_from = browser.find_element_by_xpath("//input[@name='TransactionHistoryFG.FROM_TXN_DATE']")
    date_to = browser.find_element_by_xpath("//input[@id='TransactionHistoryFG.TO_TXN_DATE']")
    date_from.clear()
    date_to.clear()
    date_from.send_keys("19/11/2018")
    date_to.send_keys("19/02/2019")
    # print(date_from)
    
    search_btn = browser.find_element_by_xpath("//input[@id='SEARCH']")
    search_btn.click()
    
    # time.sleep(1)    
    # tableData = browser.find_element_by_id("txnHistoryList")
   
    # print(browser.page_source)
    pageinationTxt = browser.find_element_by_xpath("//span[@class='paginationtxt1']")
    pageCount = int(pageinationTxt.text.split(' ')[-1])
    next_page = browser.find_element_by_xpath("//input[@id='Action.OpTransactionListing.GOTO_NEXT__']")
    table_data = browser.find_elements_by_xpath("//tbody")
    table_row = browser.find_elements_by_xpath("//tr")
    print(len(table_row))
    # while pageCount!=0:
    #     next_page = browser.find_element_by_xpath("//input[@id='Action.OpTransactionListing.GOTO_NEXT__']")
    #     table_data = browser.find_elements_by_xpath("//tbody")
    #     table_row = table_data.find_elements_by_xpath("//tr")
        # for t in table_data:
        #     print(t.text)
        #     print(".....")
        # pageCount-=1
        # next_page.click()
        # print(page_source)
    # tbodyIndex = find_all_indexes(browser.page_source,'tbody')
    # tBodyData = browser.page_source[tbodyIndex[0]-1 : tbodyIndex[1]+6]   
    # soup = BeautifulSoup(tBodyData, 'html.parser')
    # print(soup.prettify())
    # AuthenticationFG.USER_PRINCIPAL
    # Action.STU_VALIDATE_CREDENTIALS
    # continue_button = browser.find_element_by_xpath("//a[@class='login_button']")
    

    # #search_field.send_keys("Selenium WebDriver Interview questions")
    # continue_button.click()

    # username = browser.find_element_by_xpath("//input[@name='userName']")
    # password = browser.find_element_by_xpath("//input[@name='password']")
    # login = browser.find_element_by_xpath("//input[@id='Button2']")
    # username.send_keys("")
    # time.sleep(2)
    # password.send_keys("")
    # time.sleep(2)
    # login.click()
    # time.sleep(1)
    # account_statement = browser.find_element_by_link_text('Account Statement')
    # account_statement.click()
    # date_picker1 = browser.find_element_by_xpath("//input[@id='datepicker1']")
    # date_picker2 = browser.find_element_by_xpath("//input[@id='datepicker2']")
    # date_picker1.send_keys("01/01/2019")
    # date_picker2.send_keys("10/02/2019")
    # time.sleep(1)
    # submit_button = browser.find_element_by_xpath("//input[@id='Submit3']")
    # submit_button.click()

    # #list_arr = browser.find_elements_by_xpath("//tr[td]")
    # list_arr = browser.find_element_by_tag_name("tr")

    # #for t in list_arr:
    #  #   print(t.get_attribute("td"))
    # #time.sleep(2)
    # #get_scrap(browser.page_source)
    # print(list_arr.text)
    time.sleep(2)
    
bank_scrapping()

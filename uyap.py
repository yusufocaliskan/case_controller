from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

class Uyap:

    driver_path = '/opt/homebrew/bin/chromedriver'
    browser = ''
    
    #Use the T.C Id number
    username = ''

    #Password
    password = ''

    #How many count you have?
    case_count = '1'

    #-Should I bring all the case to you?
    #-Set it True if it is yes..
    bring_all = False

    def __init__(self):
        
        #Set browser
        self.browser = webdriver.Chrome(Uyap.driver_path)

        
    def signIn(self):
        self.browser.get('https://vatandas.uyap.gov.tr/main/vatandas/giris.jsp')
        time.sleep(2)
        element = self.browser.find_element_by_class_name('red-flamingo')
        element.click()


        time.sleep(3)

        #fill the form
        id_no = self.browser.find_element_by_name('tridField')
        password = self.browser.find_element_by_name('egpField') 
        id_no.send_keys(self.username)
        password.send_keys(self.password)
        
        password.send_keys(Keys.ENTER)

        time.sleep(4)
        self.browser.get('https://vatandas.uyap.gov.tr/main/jsp/vatandas/index.jsp?menuId=12573');

        time.sleep(2)

        query_button = self.browser.find_element_by_id('btnQueryDoc')
        query_button.click();

        time.sleep(7)

        #tbody = self.browser.find_element_by_xpath('//tbody/tr[1]/td[6]').text
        #table_row = self.browser.find_elements_by_tag_name("tr")
        i = 0
        message_body = []
        while i < self.case_count:
            i +=1
            table_data = self.browser.find_element_by_xpath("//tbody/tr["+str(i)+"]/td[6]").text
            case_status = table_data.split('(')
            
            #Bring only the available ones
            if(case_status[0] != 'Kapalı ' and self.bring_all != True):
                message_body.append(str(i)+" - "+table_data)
            
            #is it set it true?
            if(self.bring_all == True):
                message_body.append(str(i)+" - "+table_data)

        
        message_content = "\n".join(message_body)

        time.sleep(1)
        self.sent_an_email(message_content)
        time.sleep(1)
        self.browser.close()


    def sent_an_email(self, text):
        return requests.post(
            "https://api.mailgun.net/v3/sandboxc229ce117fa54977a27d09fb0bb4d6a6.mailgun.org/messages",
            auth=("api", "7780264ca6ad1717e52700321d970fca-5e7fba0f-f9e46322"),
            data={"from": "<rawaax90@gmail.com>",
                "to": "Yusuf Caliskan <yusufocaliskan@gmail.com>",
                "subject": "Rewşa Doza te:",
                "text": "Ev mail otomatîk tê ji ter. Rewşa doza te : \n"+text})




    def __del__(self):
        time.sleep(5)
        #self.browser.close()

app = Uyap()

app.username= 28844464482
app.password = 'Ma5ik33ysi45'
app.case_count = 4

app.signIn()

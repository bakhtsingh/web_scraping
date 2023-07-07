import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback
import time
import csv
from csv import writer

delay = 5
url = "https://www.henleyglobal.com/passport-index"

def country_codes(country_name):
    countries = {"American Samoa **":"ASM","Australia **":"AUS","Cook Islands":"COK","Fiji":"FJI","French Polynesia":"PYF","Guam":"GUM","Kiribati":"KIR"
    ,"Marshall Islands":"MHL","Micronesia":"FSM","New Caledonia":"NCL","New Zealand **":"NZL","Niue":"NIU",
    "Northern Mariana Islands":"MNP","Palau Islands *":"PLW","Papua New Guinea *":"PNG","Samoa *":"WSM","Solomon Islands *":"SLB","Tonga *":"TON","Tuvalu *":"TUV","Vanuatu":"VUT",
    "Armenia":"ARM","Bahrain *":"BHR","Iraq":"IRQ","Israel":"ISR","Jordan *":"JOR","Kuwait *":"KWT","Lebanon *":"LBN","Oman":"OMN","Palestinian Territory":"PSE","Qatar":"QAT","Saudi Arabia *":"SAU","United Arab Emirates *":"ARE","Albania":"ALB",
    "Andorra":"AND","Austria":"AUT","Belgium":"BEL","Bosnia and Herzegovina":"BIH","Bulgaria":"BGR","Croatia":"HRV","Cyprus":"CYP",
    "Czech Republic":"CZE","Denmark":"DNK","Estonia":"EST","Faroe Islands":"FRO","Finland":"FIN","France":"FRA","Georgia":"GEO","Germany":"DEU","Gibraltar":"GIB","Greece":"GRC","Greenland":"GRL","Hungary":"HUN","Iceland":"ISL","Ireland":"IRL",
    "Italy":"ITA","Kosovo":"KOS","Latvia":"LVA","Liechtenstein":"LIE","Lithuania":"LTU","Luxembourg":"LUX","Malta":"MLT","Moldova":"MDA","Monaco":"MCO","Montenegro":"MNE","Netherlands":"NLD","North Macedonia":"MKD","Norway":"NOR","Poland":"POL",
    "Portugal":"PRT","Romania":"ROU","San Marino":"SMR","Serbia":"SRB","Slovakia":"SVK","Slovenia":"SVN","Spain":"ESP","Sweden":"SWE","Switzerland":"CHE","Ukraine":"UKR","United Kingdom":"GBR","Vatican City":"VAT","Anguilla":"AIA","Antigua and Barbuda":"ATG",
    "Aruba":"ABW","Bahamas":"BHS","Barbados":"BRB","Bonaire; St. Eustatius and Saba":"BES","British Virgin Islands":"VGB","Cayman Islands":"CYM","Curacao":"CUW","Dominica":"DMA","Dominican Republic":"DOM","Grenada":"GRD","Haiti":"HTI","Jamaica":"JAM","Montserrat":"MSR",
    "Puerto Rico":"PRI","St. Kitts and Nevis":"KNA","St. Lucia":"LCA","St. Maarten":"MAF","St. Vincent and the Grenadines":"VCT","Trinidad and Tobago":"TTO","Turks and Caicos Islands":"TCA","US Virgin Islands":"VIR","Bangladesh *":"BGD","Brunei":"BRN","Cambodia *":"KHM","Hong Kong (SAR China)":"HKG","Indonesia":"IDN","Kazakhstan":"KAZ",
    "Kyrgyzstan":"KGZ","Laos *":"LAO","Macao (SAR China)":"MAC","Malaysia":"MYS","Maldives *":"MDV","Mongolia":"MNG","Nepal *":"NPL","Pakistan **":"PAK","Philippines":"PHL",
    "Singapore":"SGP","South Korea":"KOR","Sri Lanka **":"LKA","Taiwan (Chinese Taipei)":"TWN","Tajikistan *":"TJK","Thailand":"THA","Timor-Leste *":"TLS","Uzbekistan":"UZB","Argentina":"ARG","Belize":"BLE","Bermuda":"BMU","Bolivia *":"BOL",
    "Brazil":"BRA","Canada":"CAN","Chile":"CHL","Colombia":"COL","Costa Rica":"CRI","Ecuador":"ECU","El Salvador":"SLV","Falkland Islands":"FLK","French Guiana":"GUF","Guatemala":"GTM","Guyana":"GUY","Honduras":"HND","Mexico":"MEX","Nicaragua":"NIC",
    "Panama":"PAN","Paraguay *":"PRY","Peru":"PER","Uruguay":"URY","Botswana":"BWA","Burkina Faso *":"BFA","Burundi *":"BDI","Cape Verde Islands *":"CPV","Central African Republic":"CAF","Comoro Islands *":"COM","Egypt *":"EGY","Equatorial Guinea":"GNQ","eSwatini":"SWZ","Ethiopia *":"ETH","Gabon *":"GAB","Guinea-Bissau *":"GNB","Lesotho":"LSO",
    "Madagascar *":"MDG","Malawi *":"MWI","Mauritania *":"MRT","Mauritius":"MUS","Mayotte":"MYT","Morocco":"MAR","Mozambique *":"MOZ","Namibia":"NAM","Reunion":"REW","Rwanda *":"RWA","Sao Tome and Principe":"STP","Senegal":"SEN","Seychelles *":"SYC","Sierra Leone *":"SLE","Somalia *":"SOM","South Africa":"ZAF","St. Helena *":"SHN","Tanzania *":"TZA",
    "The Gambia *":"GMB","Togo *":"TGO","Tunisia":"TUN","Uganda *":"UGA","Zambia *":"ZMB","Zimbabwe *":"ZWE","Nauru":"NRU","Iran":"IRN","Syria":"SYR","Yemen":"YEM","Azerbaijan":"AZE","Belarus":"BLR","Russian Federation":"RUS","Türkiye":"TUR","Cuba":"CUB","Afghanistan":"AFG","Bhutan":"BTN","China":"CHN","India":"IND",
    "Japan":"JPN","Myanmar":"MMR","North Korea":"PRK","Turkmenistan":"TKM","Vietnam":"VNM","Suriname":"SUR","Venezuela":"VEN","Algeria":"DZA","Angola":"AGO","Benin":"BEN","Cameroon":"CMR","Chad":"TCD","Congo (Dem. Rep.)":"COD","Congo (Rep.)":"COG","Cote d'Ivoire":"CIV","Djibouti":"DJI","Eritrea":"ERI",
    "Ghana":"GHA","Guinea":"GIN","Kenya":"KEN","Liberia":"LBR","Libya":"LBY","Mali":"MLI","Niger":"NER","Nigeria":"NGA","South Sudan":"SSD","Sudan":"SDN","United States":"USA"}
    return countries[country_name]

def initialize_driver():
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    chrome_options = Options()
    options = [
        #"--headless",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver

def french_west_indies(driver,select_country,country_from_menu):
    other_isos_list = ["GLP","MTQ","BLM","MAF"]
    time.sleep(delay)
    webdriver.ActionChains(driver).move_to_element(select_country).click(select_country).perform()
    time.sleep(delay)
    for item in other_isos_list:
        visa_not_required_countries = driver.find_elements(By.CLASS_NAME,"country-container")
        with open('/Users/xxxxxxxxx/xxxxxxxx/Repos/passport_requirements/'+item+'_passport_requirements.csv', 'w', encoding='utf8', newline='') as f:
            thewriter = writer(f)
            header = ['Source/From', 'To/Destination Country', 'Visa Required']
            thewriter.writerow(header)
            for countries in visa_not_required_countries:
                source = item
                visa_required = "Visa on Arrival"
                country = countries.text
                country = country_codes(country)
                #print(country)
                info = [source, country, visa_required]
                thewriter.writerow(info)

            change_to_visa_required = driver.find_element(By.CSS_SELECTOR,'[for="passport-visa-required1"]')
            time.sleep(delay)
            webdriver.ActionChains(driver).move_to_element(change_to_visa_required).click(change_to_visa_required).perform()
            visa_required_countries = driver.find_elements(By.CLASS_NAME,"country-container")
            for countries in visa_required_countries:
                source = item
                visa_required = "Visa Required"
                country = countries.text
                country = country_codes(country)
                info = [source, country, visa_required]
                thewriter.writerow(info)

def scrap_data():
    driver = initialize_driver()
    driver.get(url)
    time.sleep(delay)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Accept all"]'))).click()
    counter = 1
    while counter < 200:
        #dropdown_menu = driver.find_element(By.XPATH,'//div[@class="form-group contained-content filled"]/span[2]')
        dropdown_menu = driver.find_elements(By.XPATH,'//span[(contains(@id,"CountryDropDown"))]')
        time.sleep(delay)
        print(len(dropdown_menu))
        dropdown_menu = dropdown_menu[0]
        time.sleep(delay)
        driver.execute_script("arguments[0].scrollIntoView();",dropdown_menu)
        time.sleep(delay)
        driver.execute_script("arguments[0].click();",dropdown_menu)
        time.sleep(delay)
        #select_country = driver.find_elements(By.XPATH,'//li[@class="ui-menu-item"]/div')
        #select_country = driver.find_element(By.XPATH,'//div[text()="United States"]')
        #country_from_menu = select_country[counter].text
        country_from_menu = "Afghanistan"
        print(country_from_menu)
        #select_country = driver.find_element(By.XPATH,'//div[text()="'+country_from_menu+'"]')
        """
        time.sleep(delay)
        driver.execute_script("arguments[0].scrollIntoView();",select_country[counter])
        #driver.execute_script("arguments[0].click();",select_country)
        webdriver.ActionChains(driver).move_to_element(select_country[counter]).click(select_country[counter]).perform()
        time.sleep(delay)"""
        if country_from_menu == "French West Indies":
            pass
            #french_west_indies(driver,select_country[counter],country_from_menu)
        else:
            choose_country = driver.find_element(By.XPATH,'//div[text()="'+country_from_menu+'"]')
            #time.sleep(delay)
            #driver.execute_script("arguments[0].scrollIntoView();",choose_country)
            driver.execute_script("arguments[0].click();",choose_country)
            #webdriver.ActionChains(driver).move_to_element(choose_country).click(choose_country).perform()
            time.sleep(delay)
            visa_not_required_countries = driver.find_elements(By.CLASS_NAME,"country-container")
            with open('/Users/xxxxxxxxxx/xxxxxxxx/xxxxx/passport_requirements/'+country_codes(country_from_menu)+'_passport_requirements.csv', 'w', encoding='utf8', newline='') as f:
                thewriter = writer(f)
                header = ['Source/From', 'To/Destination Country', 'Visa Required']
                thewriter.writerow(header)
                for countries in visa_not_required_countries:
                    if countries == "French West Indies":
                        other_isos_list = ["GLP","MTQ","BLM","MAF"]
                        for list in other_isos_list:
                            source = country_from_menu
                            source = country_codes(source)
                            visa_required = "Visa on Arrival"
                            country = list
                            info = [source, country, visa_required]
                            thewriter.writerow(info)
                    else:
                        source = country_from_menu
                        source = country_codes(source)
                        visa_required = "Visa on Arrival"
                        country = countries.text
                        country = country_codes(country)
                        print(country)
                        info = [source, country, visa_required]
                        thewriter.writerow(info)
                
                input('enter')
                time.sleep(delay)
                change_to_visa_required = driver.find_element(By.CSS_SELECTOR,'[for="passport-visa-required1"]')
                time.sleep(delay)
                webdriver.ActionChains(driver).move_to_element(change_to_visa_required).click(change_to_visa_required).perform()
                visa_required_countries = driver.find_elements(By.CLASS_NAME,"country-container")
                for countries in visa_required_countries:
                    if countries == "French West Indies":
                        other_isos_list = ["GLP","MTQ","BLM","MAF"]
                        for list in other_isos_list:
                            source = country_from_menu
                            source = country_codes(source)
                            visa_required = "Visa on Arrival"
                            country = list
                            info = [source, country, visa_required]
                            thewriter.writerow(info)
                    else:
                        source = country_from_menu
                        source = country_codes(source)
                        visa_required = "Visa Required"
                        country = countries.text
                        country = country_codes(country)
                        print(country)
                        info = [source, country, visa_required]
                        thewriter.writerow(info)
        counter += 1
    
scrap_data()

#Guadeloupe - GLP
#Martinique - MTQ
#Saint Barthélemy - BLM
#Saint Martin - MAF



import json
from selenium import webdriver

bot = webdriver.Chrome(executable_path="D:\\SinauPy\\Scrapper\\chromedriver.exe")
bot.get('https://www.worldometers.info/coronavirus/')
tr = bot.find_elements_by_tag_name('tr')
data_covid = list()
for i in range(int(len(tr) / 2 )):
    country = bot.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr['+str(i+1)+']/td[1]').text
    total_cases = bot.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr['+str(i+1)+']/td[2]').text.replace(',', '')
    new_cases = bot.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr['+str(i+1)+']/td[3]').text.replace(',', '')
    total_deaths = bot.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr['+str(i+1)+']/td[4]').text.replace(',', '')
    new_deaths = bot.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr['+str(i+1)+']/td[5]').text.replace(',', '')
    total_recovered = bot.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr['+str(i+1)+']/td[6]').text.replace(',', '')
    active_cases = bot.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr['+str(i+1)+']/td[7]').text.replace(',', '')
    serious_or_crtical = bot.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr['+str(i+1)+']/td[8]').text.replace(',', '')
    
    data = {
            "id" : "ID00" + str(i),
            "country" : country,
            "total_cases" : total_cases,
            "new_cases" : new_cases,
            "total_deaths" : total_deaths,
            "new_deaths" : new_deaths,
            "total_recovered" : total_recovered,
            "active_cases" : active_cases,
            "serious_or_crtical" : serious_or_crtical,
    }
    data_covid.append(data)

    filename = 'covid.json'
    f = open(filename, 'w')
    f.write(json.dumps(data_covid))
        
    
print('saved!')
bot.close()
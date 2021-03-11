import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fox_path = r'/mnt/c/Users/tjdql/Desktop/geckodriver-v0.29.0-win64/geckodriver.exe'

user_list = ['jwm1992', 'pwr01000']


driver = webdriver.Firefox(executable_path=fox_path)

user_id = user_list[0]
page_no = 1

def crawling_json_selling(driver,user_id, page_no):
    selling_url = r'http://www.encar.com/dc/dc_carsearchlist.do?method=sellcar' + '&userId=' + user_id + '&pageNo=' + str(page_no)
    driver.get(selling_url)
    while True:
        html = driver.page_source
        soup=BeautifulSoup(html, 'html.parser')
        car_cnt_str = soup.find('strong', id='txtTotalCnt').text
        if len(car_cnt_str)>0:
            break
        time.sleep(0.02)
    car_cnt = int(car_cnt_str)
    # print(car_cnt) #TODO: all count check
    img_list = []
    [img_list.append(img['src']) for img in soup.find('tbody', id='listCar').findAll('img')]
    kind1_list = []
    [kind1_list.append(kind1.text) for kind1 in soup.findAll('span', class_='cls')]
    kind2_list = []
    [kind2_list.append(kind2.text) for kind2 in soup.findAll('span', class_='dtl')]
    auto_list = []
    [auto_list.append(auto.text) for auto in soup.findAll('span', class_='trs')]
    fuel_list = []
    [fuel_list.append(fuel.text) for fuel in soup.findAll('span', class_='fue')]
    year_list=[]
    [year_list.append(year.text) for year in soup.findAll('td', class_='yer')]
    distance_list=[]
    [distance_list.append(distance.text) for distance in soup.findAll('td', class_='km')]
    price_list=[]
    [price_list.append(price.text) for price in soup.findAll('td', class_='prc')]
    day_list=[]
    [day_list.append(day.text[0:12].strip()) for day in soup.findAll('td', class_='fdt')]
    sub_url_list=[]
    [sub_url_list.append('http://www.encar.com/'+sub_url['href']) for sub_url in soup.find('tbody', id='listCar').findAll('a')]
    data = []
    for i in range(1, car_cnt):
        item = {}
        item['img'] = img_list[i]
        item['kind1'] = kind1_list[i]
        item['kind2'] = kind2_list[i]
        item['auto'] = auto_list[i]
        item['fuel'] = fuel_list[i]
        item['year'] = year_list[i]
        item['distance'] = distance_list[i]
        item['price'] = price_list[i]
        item['day'] = day_list[i]
        item['sub_url'] = sub_url_list[i]
        data.append(item)

    return driver, data

def crawling_json_selled(driver,user_id, page_no):
    selled_url = r'http://www.encar.com/dc/dc_carsearchlist.do?method=sellerSummary' + '&userId=' + user_id + '&pageNo=' + str(page_no)
    driver.get(selled_url)
    while True:
        html = driver.page_source
        soup=BeautifulSoup(html, 'html.parser')
        car_cnt_str = soup.find('h4', class_='summary').find('strong', class_='red').text
        if len(car_cnt_str)>0:
            break
        time.sleep(0.02)
    car_cnt = int(car_cnt_str)
    print(car_cnt) #TODO: all count check
    img_list = []
    [img_list.append(img['src']) for img in soup.find('table', class_='car_list').findAll('img')]
    kind1_list = []
    [kind1_list.append(kind1.text) for kind1 in soup.findAll('span', class_='cls')]
    kind2_list = []
    [kind2_list.append(kind2.text) for kind2 in soup.findAll('span', class_='dtl')]
    auto_list = []
    [auto_list.append(auto.text) for auto in soup.findAll('span', class_='trs')]
    fuel_list = []
    [fuel_list.append(fuel.text) for fuel in soup.findAll('span', class_='fue')]
    year_list=[]
    [year_list.append(year.text) for year in soup.findAll('td', class_='yer')]
    distance_list=[]
    [distance_list.append(distance.text) for distance in soup.findAll('td', class_='km')]
    day_list=[]
    [day_list.append(day.text[0:12].strip()) for day in soup.findAll('td', class_='fdt')]
    data = []
    for i in range(1, car_cnt):
        item = {}
        item['img'] = img_list[i]
        item['kind1'] = kind1_list[i]
        item['kind2'] = kind2_list[i]
        item['auto'] = auto_list[i]
        item['fuel'] = fuel_list[i]
        item['year'] = year_list[i]
        item['distance'] = distance_list[i]
        item['day'] = day_list[i]
        data.append(item)

    return driver, data
'''
'''
# crawling_json_selling(driver, user_id, page_no)
driver, data = crawling_json_selled(driver, user_id, page_no)
print(data)

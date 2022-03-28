import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Screenshot import Screenshot_Clipping
import os, shutil

surah = '78'
page = 583
ayah_num_list = [1, 31] # ayah numbers that starts a new page

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=user_data_dir6")
# options.add_argument("--start-maximized");
options.add_argument('--headless')
options.add_argument("--window-size=2560x1600") # ANYTHING MORE THAN 3200 width my pycharm cant cope (Rendering error)

driver = webdriver.Chrome(executable_path=r'./chromedriver', options=options)
quran_folder_name = f'Quran_Tajweed/{surah}'
if os.path.isdir(quran_folder_name):
    shutil.rmtree(quran_folder_name)
os.mkdir(quran_folder_name)
# for i in (1, 6, 17, 25, 30, 38, 49, 58, 62, 70, 77, 84, 89, 94, 102):
# for i in (106,113,120,127,135,142,146,154,164,170,177,182,187,191,197,203,211,216,220,225,231,234,238,246,249,253,257,260,265,270,275,282,283):
for i in (1,31):  # ayah numbers that starts a new page
    driver.get('http://www.recitequran.com/{}:{}'.format(surah, str(i)))
    time.sleep(5)
    driver.find_element_by_id('MainContent').screenshot(f'{quran_folder_name}/{page}.png')
    page += 1
driver.close()
driver.quit()

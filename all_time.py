from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from bs4 import BeautifulSoup as BS

class AllTimeScraper:
    data_2 = []
    data_info = []

    def __init__(self) -> None:

        self.options = webdriver.ChromeOptions()

        self.options.add_argument("--start-maximized")
        self.path = ChromeDriverManager().install()
        self.driver = webdriver.Chrome(self.path, chrome_options=self.options)
        self.url = 'https://opensea.io/rankings?sortBy=total_volume'
        self.driver.get(self.url)
        self.df1 = None
        self.df2 = None
        self.num = 0
        self.num_1 = 0

    def scroll(self):

        """ Get urls from Opensea.io """

        scroll_pause_time = 1  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
        screen_height = self.driver.execute_script("return window.screen.height;")  # get the screen height of the web
        wait = WebDriverWait(self.driver, 10)
        i = 1
        time.sleep(2)
        while self.num != 6:
            # scroll one screen height each time
            self.driver.execute_script(
                "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
            i += 1
            time.sleep(scroll_pause_time)
            main_url = 'https://opensea.io'
            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            scroll_height = self.driver.execute_script("return document.body.scrollHeight;")
            soup = BS(self.driver.page_source, 'html.parser')

            divs = soup.find_all('a', class_='sc-1pie21o-0 elyzfO sc-1xf18x6-0 sc-1twd32i-0 sc-1idymv7-0 sc-12irlp3-0 gBJwSz kKpYwv iLNufV bODGfa fresnel-greaterThanOrEqual-xl')
            for items in divs:
    #     for item in items:
                name = items.find('div', class_='sc-7qr9y8-0 iUvoJs Ranking--collection-name-overflow').text.strip()
                runk = items.find('span').text.strip()
                link = main_url + items['href'] 

                volume = items.find('span', class_='sc-1xf18x6-0 sc-1w94ul3-0 sc-12irlp3-3 jIFPFr hrcjVi').text.strip()
                one_day = items.find('div', class_= 'sc-1xf18x6-0 sc-1twd32i-0 cTvSkV kKpYwv').text.strip()
                weekly = items.find('div', class_='sc-1xf18x6-0 sc-1twd32i-0 haVRLx kKpYwv').text.strip()
                d = {
                    'name' : name,
                    'url' : link,
                    'runk' : runk,
                    'volume' : volume,
                    'one_day' : one_day,
                    'weekly' : weekly
                }
                print('Done!')
                AllTimeScraper.data_info.append(d)


                if (screen_height) * i > scroll_height:
                    el = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/button[2]').click()
                    time.sleep(7)
                    self.num = self.num + 1
                    self.scroll()
                    if self.num == 6:
                        # driver.close()
                        break

    def main(self):

        screen_height = self.driver.execute_script("return window.screen.height;")  # get the screen height of the web
        self.df1 = pd.DataFrame(AllTimeScraper.data_info).drop_duplicates()
        i = 1
        for urls in self.df1['url'].values:
            self.driver.get(urls)
            time.sleep(2)

            self.driver.execute_script(
                "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
            time.sleep(1)
            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            owners = None
            floor_price = None
            items = None
            blockchain =None
            contractaddress = None
            pic2 = None
            pic3 = None
            pic4 = None
            pic5 = None

            try:
                owners = self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div/div[5]/div/div[1]/div/div[3]/div/div[4]/a/div/span[1]/div').text
                floor_price = self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div/div[5]/div/div[1]/div/div[3]/div/div[6]/a/div/span[1]/div').text
                items = self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div/div[5]/div/div[1]/div/div[3]/div/div[2]/a/div/span[1]/div').text
            except:
                owners = 'None'
                floor_price = 'None'
                items = 'None'
            try:
                el = self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/a[1]').get_attribute(
                    'href')
            
                contractaddress = el
            except:
                contractaddress = 'None'
            try:
                img1 = self.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div/div[1]/div/button/div/img')
                pic1 = img1.get_attribute('src')
            except:
                pic1  = 'None'
            try:
                img2 = self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div/div[5]/div/div[3]/div[3]/div[3]/div[3]/div[2]/div/div/div[1]/div/article/a/div[1]/div/div/div/div/img')
                pic2 = img2.get_attribute('src')
                img3 = self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div/div[5]/div/div[3]/div[3]/div[3]/div[3]/div[2]/div/div/div[2]/div/article/a/div[1]/div/div/div/div/img')
                pic3 = img3.get_attribute('src')
                img4 = self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div/div[5]/div/div[3]/div[3]/div[3]/div[3]/div[2]/div/div/div[3]/div/article/a/div[1]/div/div/div/div/img')
                pic4 = img4.get_attribute('src')
                img5 = self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div/div[5]/div/div[3]/div[3]/div[3]/div[3]/div[2]/div/div/div[4]/div/article/a/div[1]/div/div/div/div/img')
                pic5 = img5.get_attribute('src')
            except:
                pic2 = 'None'
                pic3 = 'None'
                pic4 = 'None'
                pic5 = 'None'
            try:
                if 'https://static.opensea.io/solana-just-s-symbol-colored.svg' in self.driver.find_element_by_xpath(
                        f'//*[@id="main"]/div/div/div[5]/div/div[1]/div/div[3]/div/div[6]/a/div/span[1]/div/div/button/div/img').get_attribute(
                        'src'):

                    blockchain = 'Soloana blockchain'
                else:
                    blockchain = 'Etherium blockchain'
            except:
                blockchain = 'None'
            main_d = {
                'owners' : owners,
                'floor_price' : floor_price,
                'blockchain' : blockchain,
                'items' : items,
                'contractaddress': contractaddress,
                'pic1': pic1,
                'pic2': pic2,
                'pic3': pic3,
                'pic4': pic4,
                'pic5': pic5
            }
            print('Done!!')
            AllTimeScraper.data_2.append(main_d)
            
            if self.num_1 == len(self.df1['url'].values):
                break

    def run_all(self):

        
        self.df1 = pd.DataFrame(AllTimeScraper.data_info).drop_duplicates()

        self.scroll()
        print(len(self.df1))
        self.main()
        self.df2 = pd.DataFrame(AllTimeScraper.data_2).drop_duplicates()
        new_file = self.df1.merge(self.df2, left_index=True, right_index=True)
        with open('all_time.json', 'w') as f:
            f.write(new_file)
        print('All time data is ready!')


if __name__ == '__main__':
    mydaily = AllTimeScraper()
    mydaily.run_all()



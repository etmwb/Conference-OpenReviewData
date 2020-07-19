import argparse 

from time import sleep 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options 

class Args():
    def __init__(self):
        parser = argparse.ArgumentParser(description='Conference \
            Papers')
        parser.add_argument('--conf-name', type=str, default='ICLR2020',
                            help='conference name (default: ICLR2020)')
        # the parser
        self.parser = parser

    def parse(self):
        args = self.parser.parse_args()
        urls = {
            'iclr2020': 'https://openreview.net/group?id=ICLR.cc/2020/Conference#all-submissions', 
        }
        args.url = urls[args.conf_name.lower()] 
        print(args)
        return args

def get_data_ids(browser): 
    data_ids, done, page = [], False, 1
    while not done:
        print('Page: {}'.format(page))
        for item in browser.find_elements_by_class_name("note"):
            data_id = item.get_attribute('data-id') 
            data_ids.append(data_id)

        right_arrow = browser.find_elements_by_class_name("right-arrow")
        if len(right_arrow) > 0:        
            browser.execute_script("arguments[0].click();", right_arrow[0])
            sleep(5)
            page += 1
        else:
            done = True
    return data_ids

if __name__ == '__main__': 
    args = Args()

    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    browser.get(args.url)

    data_ids = list(set(get_data_ids(browser)))
    print('Number of submission: {}'.format(len(data_id_list)))
    with open('generated/urls.txt', 'w') as urls_txt:
        for data_id in data_ids:
            urls_txt.write('https://openreview.net/forum?id={}\n'.format(data_id))

    
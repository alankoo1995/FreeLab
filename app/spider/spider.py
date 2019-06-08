from lxml import etree

class Spider:
    URL = "https://status.cse.unsw.edu.au/labstatus/"
    FILEPATH = "app/spider/weekly_db/week{}day{}.json"
    FIRST_WEEK = [2019, 6, 3]
    TIME = "/html/body/table/tr[position()>1]/th"
    LABS = "/html/body/table/tr[1]/th[position()>1]"
    LABS_INFO = "/html/body/table/tr[@class='top']/th[position()>1]/div[@class='details']/text()[preceding-sibling::br]"
    ALLOCATIONS = "/html/body/table/tr[position()>1]/td[{}]"

    def __init__(self):
        self.nth_week = self.get_nth_week()
        self.weekday = self.get_weekday()
        self.data = None

        if self.isRequiredUpdate():
            res = self.get_web_data(Spider.URL)
            self.data = self.parse_data(res)
            self.persistence(self.data)
        else:
            res = self.get_local_data(Spider.FILEPATH)
            self.data = self.load_json_file(Spider.FILEPATH)
            
    def get_data(self):
        return self.data
    
    def isRequiredUpdate(self):
        '''
        check whether the server should grab the info from external website
        :return: boolean value
        '''
        from os.path import exists
        return not exists(Spider.FILEPATH.format(self.nth_week, self.weekday))

    def get_web_data(self, url):
        '''
        :param: url the url that gonna to request
        :return: Object consisting of webpage data
        '''
        import urllib.request
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
        }

        request = urllib.request.Request(url, headers=headers)

        response = urllib.request.urlopen(request)
        return response.read()

    def get_local_data(self, filepath):
        '''
        :param: filepath the path of the file 
        :return: the content of of the file
        '''
        from io import StringIO
        raw_data = StringIO()
        with open(filepath.format(self.nth_week, self.weekday)) as file:
            raw_data.write(file.read())
        return raw_data.getvalue()

    def load_json_file(self, filepath):
        from json import load
        return load(open(filepath.format(self.nth_week, self.weekday)))

    def parse_data(self, raw_data):
        '''
        :param: string of the web page
        :return: parse data in json format 
        '''
        html = etree.HTML(raw_data, parser=etree.HTMLParser(encoding='UTF-8'))
        labs_name = html.xpath(Spider.LABS)
        labs_name_arr = [e.text for e in labs_name]
        labs_info = html.xpath(Spider.LABS_INFO)
        labs_info_arr = [e for e in labs_info] #already get the text object
        data = []
        for i in range(1, len(labs_name)):
            allocation = html.xpath(Spider.ALLOCATIONS.format(i))
            allocation_arr = ['' if e.text is None or e.text.endswith('free') else e.text for e in allocation]
            # status_pair = {'status': allocation_arr}
            # labs_info_pair = {'info': labs_info_arr[i-1]}
            pair = {
                labs_name_arr[i-1] : {
                    "info" : labs_info_arr[i-1],
                    "status" : allocation_arr,
                }
            }
            data.append(pair)
        
        return data
    
    def persistence(self, data):
        '''
        store the dataset into the database in json format
        :param: the dataset
        :return: VOID
        '''
        from json import dumps
        import logging
        # with open (Spider.FILEPATH.format(self.nth_week, self.weekday), 'w') as file:
            # dump(data, file)

        # Due to the consideration of thread-safe problem, use logging rather than open
        logging.basicConfig(filename=Spider.FILEPATH.format(self.nth_week, self.weekday), filemode='w', \
            format='%(message)s', level=logging.INFO)
        logging.info(dumps(data))

    def get_nth_week(self):
        '''
        calculate the nth week
        :return: nth week
        '''
        from datetime import date
        first_week = int(date(*Spider.FIRST_WEEK).strftime("%W"))
        current_week = int(date.today().strftime("%W"))
        nth_week = (current_week - first_week) + 1
        return nth_week
    
    def get_weekday(self):
        from datetime import date
        return date.today().weekday()

if __name__ == '__main__':
    print(Spider().get_data())
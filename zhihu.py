# -*- coding:utf-8 -*-
import re, json
from spider import ZhihuHtml
from bs4 import BeautifulSoup


class ZhihuImgCollector(ZhihuHtml):
    store_path = 'E:/爬虫测试/'

    def start_collect(self):
        self.LoginUrl()
        content = self.OpenUrl(self.url)
        soup = BeautifulSoup(content.text, "html.parser")
        answers = soup.find_all('div', class_='zm-item-answer zm-item-expanded')
        title = re.findall(r'<span.*?class="zm-editable-content">(.*?)</span>', content.text, re.S)
        self.store_path = self.store_path + title[0] + '/'
        self.process_answer(answers)
        self.get_more()

    def get_more(self):
        offset = 20
        Flag = True
        while Flag:
            params = json.dumps({"url_token": 41801510, "pagesize": 10, "offset": offset})
            datas = {
                "method": "next",
                "params": params,
                "_xsrf": self._xsrf
            }
            offset += 10
            res = self.PostData('https://www.zhihu.com/node/QuestionAnswerListV2', datas, self.header)
            if res.json()["r"] == 1:
               Flag = False
            else:
                ans = ' '.join(res.json()["msg"])
                soup = BeautifulSoup(ans, "html.parser")
                answers = soup.find_all('div', class_='zm-item-answer zm-item-expanded')
                self.process_answer(answers)

    def process_answer(self, answers):
        for answer in answers:
            imgs = re.findall(r'<img.*?src="(.*?)".*?>', answer.__str__(), re.S)
            name = re.findall(r'data-author-name="(.*?)"', answer.__str__(), re.S)
            imgs = list(set(imgs))
            if len(imgs):
                i = 1
                for img in imgs:
                    if 'http' not in img:
                        continue
                    store_name = self.store_path + ''.join(name) + str(i) + '.jpg'
                    self.SaveImg(img, store_name)
                    i += 1

if __name__ == '__main__':
    spider = ZhihuImgCollector()
    spider.start_collect()
    

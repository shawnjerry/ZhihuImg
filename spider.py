# -*- coding:utf-8 -*-

import requests, os, re, time
from subprocess import Popen


class ZhihuHtml(object):
    header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) '
                            'AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20'}
    base_url = 'https://www.zhihu.com'
    login_url = 'https://www.zhihu.com/login/phone_num'
    url = 'https://www.zhihu.com/question/41801510'

    def __init__(self):
        self.__session = requests.session()
        self._xsrf = ''

    def LoginUrl(self):
        res = self.OpenUrl(self.base_url)
        xsrf = re.findall(r'name="_xsrf".*?value="(.*?)"', res.text, re.S)
        self._xsrf = xsrf[0]
        login_img = 'http://www.zhihu.com/captcha.gif?r=' + str(int(time.time() * 1000)) + "&type=login"
        r = self.OpenUrl(login_img)
        with open('code.gif', 'wb') as f:
            f.write(r.content)
        Popen('code.gif', shell=True)
        captcha = input('请输入验证码：')
        lo_info = {
            '_xsrf': xsrf[0],
            'phone_num': '15622371802',
            'password': 'hellozhihu123',
            'captcha': captcha
        }
        res = self.PostData(self.login_url, lo_info, self.header)
        if res.json()["r"] == 0:
            print('Login Successfully!')
        else:
            print('Login Failed!')

    def OpenUrl(self, url):
        return self.__session.get(url, headers=self.header)

    def PostData(self, url, data, header):
        return self.__session.post(url, data=data, headers=header)

    def SaveImg(self, img, filename):
        self.CheckDir(filename)
        res = requests.get(img)
        with open(filename, 'wb') as fd:
            data = res.content
            fd.write(data)
        fd.close()

    def CheckDir(self, filename):
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

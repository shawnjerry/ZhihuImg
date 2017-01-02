# ZhihuImg
This is a crawler to download pictures under a topic on ZhiHu

'''<br />
author:shawnjerrry<br />
Date:2017-01-02<br />
'''

简介：<br />
爬虫小程序抓取知乎下某个话题的图片，并以回答人的昵称命名图片<br />

使用方法：<br />
将spider.py下的lo_info{}加入账户密码，另外需要手动输入验证码<br />
将ZhihuHtml的url字段改为对应话题的链接即可<br />
另外如果使用邮箱账户登陆需将ZhihuHtml的post_url字段改为：login_url = 'https://www.zhihu.com/login/email'<br />

存在问题：<br />
1、运行的耗时太久，未用多线程、多进程，主要是自己还没学到<br />
2、偶尔出现SSL错误，估计是Python底层socket实现的一些Bug<br />
requests.exceptions.SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure<br />
3、代码结构不清晰，还需要整理

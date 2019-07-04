#!/user/bin/env python
#coding=utf-8

# @project : rearend
# @author  : kalifun
# @file   : spiderone.py
# @ide    : PyCharm
# @time   : 2019/7/3 11:45

import time
import requests
from bs4 import BeautifulSoup


class OneSpider():
    def __init__(self):
        self.url = "http://www.wufazhuce.com/"

    def Gethtml(self):
        req = requests.get(self.url)
        try:
            if req.status_code == 200:
                data = req.text
                return data
            else:
                time.sleep(2000)
                self.Gethtml()
        except Exception as e:
            print(e)

    # def DownloadPic(self,url):
    #     try:
    #         r = requests.get(url)
    #         with open("demo3.zip", "wb") as code:
    #             code.write(r.content)
    #     except Exception as e:
    #         print(e)

    def Processfile(self):
        webfile = self.Gethtml()
        soup = BeautifulSoup(webfile, 'html.parser')
        try:
            daylog = soup.find('div', attrs={'class': 'item active'})
            pics = daylog.find(attrs={'class': 'fp-one-imagen'})
            src = pics.get('src')

            VOL = daylog.find(attrs={'class': 'titulo'}).getText()

            cita = daylog.find(attrs={'class': 'fp-one-cita'}).getText()

            return src, VOL, cita
        except Exception as e:
            print(e)

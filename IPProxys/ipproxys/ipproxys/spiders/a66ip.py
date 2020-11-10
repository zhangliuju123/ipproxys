# -*- coding: utf-8 -*-
import os

import scrapy
from scrapy import Request


class A66ipSpider(scrapy.Spider):
    name = '66ip'
    allowed_domains = ['http://www.66ip.cn/']
    start_urls = ['http://www.66ip.cn//']

    def parse(self, response):
        for k in range(1,100):
            next_url = f'http://www.66ip.cn/{k}.html'
            print(next_url)
            yield Request(url=next_url, callback=self.parse_ip, dont_filter=True)

    def parse_ip(self,response):
        try:
            for i in range(2, 9):
                p = response.xpath(f"//*[@id='main']/div/div[1]/table/tr[{i}]/td[1]").extract_first()
                if p:
                    Ip = p.strip('<td></td>')
                    print(Ip)
                    with open(os.path.join(os.getcwd(), 'Ipproxys.txt'), 'a+', encoding='utf-8') as f:
                        f.write(Ip + '\n')
                else:
                    p = response.xpath(f"//*[@id='main']/div/div[1]/table/tr[2]/td[1]").extract_first()
                    Ip = p.strip('<td></td>')
                    print(Ip)
                    with open(os.path.join(os.getcwd(), 'Ipproxys.txt'), 'a+', encoding='utf-8') as f:
                        f.write(Ip + '\n')
        except Exception as e:
            print(e)
# -*- coding: utf-8 -*-
__auto__ = 'zhangliujun'
__date__ = '2020/11/4 14:48'

import os, sys
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

SPIDER_NAME = '66ip'

execute(['scrapy', 'crawl', SPIDER_NAME])

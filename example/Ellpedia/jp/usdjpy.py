# coding: utf-8
from bs4 import BeautifulSoup
import urllib.request as req
import json
import collections as cl
from math import modf
from datetime import datetime
import codecs

ys = cl.OrderedDict()
content = cl.OrderedDict()
# HTMLを取得
try:
  url = "http://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"
  res = req.urlopen(url, timeout=10)

  # HTMLを解析
  soup = BeautifulSoup(res, "html.parser")

  # 任意のデータを抽出 --- (※1)
  price = soup.select_one(".stoksPrice").string
  n = float('%.3f' % float(price))
  decimal, integer = modf(n)
  content["integer"] = int(integer)
  dec = '%.3f' % decimal
  content["decimal"] = dec.lstrip('0')
  ys["USDJPY"] = content
  ys["time"] = datetime.now().strftime("%m/%d %H:%M")
  fw = codecs.open('/path/to/stocks.json', 'w')
  json.dump(ys, fw, indent = 4, ensure_ascii=False)
except:
	pass

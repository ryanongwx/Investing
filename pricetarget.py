import requests
from bs4 import BeautifulSoup
import csv

csv_file = open('pricetarget.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Ticker', 'Price', 'Price Target', 'Potential Gain'])

class ptfinder:
    def __init__(self, pturl, findpricetargettag, findpricetargetclass, priceurl, findpricetag, findpriceclass, nameurl, findnametag, findnameclass, peurl, findpetag, findpeclass):
        self.pturl = pturl
        self.priceurl = priceurl
        self.findpricetag = findpricetag
        self.findpriceclass = findpriceclass
        self.nameurl = nameurl
        self.findnametag = findnametag
        self.findnameclass = findnameclass
        self.findpricetargettag = findpricetargettag
        self.findpricetargetclass = findpricetargetclass
        self.peurl = peurl
        self.findpetag = findpetag
        self.findpeclass = findpeclass


    def name(self):
        self.source = requests.get(self.nameurl).text
        self.soup = BeautifulSoup(self.source, 'lxml')
        try:
            self.name1 = self.soup.find(self.findnametag, class_=self.findnameclass).text
            return self.name1
        except:
            return "Stock Not Found"

    def price(self):
        self.source = requests.get(self.priceurl).text
        self.soup1 = BeautifulSoup(self.source, 'lxml')
        try:
            self.price1 = self.soup1.find(self.findpricetag, class_=self.findpriceclass).text
            return float(self.price1)
        except:
            return 0

    def pricetarget(self):
        self.source = requests.get(self.pturl).text
        self.soup2 = BeautifulSoup(self.source, 'lxml')
        try:
            self.pricetarget1 = self.soup.find(self.findpricetargettag, attrs=self.findpricetargetclass)
            return float(self.pricetarget1.text)
        except:
            return 0

    def findpe(self):
        self.source = requests.get(self.peurl).text
        self.soup3 = BeautifulSoup(self.source, 'lxml')
        try:
            pe1 = list(self.soup3.find(self.findpetag, class_=self.findpeclass).text.split())
            x = pe1[11]
            return float(x)
        except:
            return 0

    def findpg(self):
        if self.price() > 0 and self.findpe() > 0:
            pricetargeted = self.pricetarget() * self.findpe()
            pg = str(((pricetargeted - self.price())/self.price())*100) + '%'
            return pg
        else:
            return 0


stocksymbols = []
stockname = []
pt = []
textfile = open("/Users/ryanong/PycharmProjects/investing/stockksymbols.txt", 'r')
for line in textfile:
    shares = list(line.split(','))
    stocksymbols.append(shares[0])
    stockname.append(shares[1])

for i in range(20):
    checkstock = str(stocksymbols[i])
    nameurl = 'https://finance.yahoo.com/quote/' + checkstock + '/analysis?p=' + checkstock
    priceurl = 'https://finance.yahoo.com/quote/' + checkstock + '/analysis?p=' + checkstock
    pturl = 'https://finance.yahoo.com/quote/' + checkstock + '/analysis?p=' + checkstock
    peurl = 'https://ycharts.com/companies/' + checkstock + '/pe_ratio'
    s = ptfinder(
        pturl, 'span', {'data-reactid': '52'},
        priceurl, 'span', 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)',
        nameurl, 'h1', 'D(ib) Fz(18px)',
        peurl, 'table', 'rangeModTable')
    pt.append(s)


for j in pt:
    csv_writer.writerow([j.name(), j.price(), (j.pricetarget()*j.findpe()), j.findpg()])

csv_file.close()
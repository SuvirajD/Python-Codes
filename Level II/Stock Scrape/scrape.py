import requests
from bs4 import BeautifulSoup
import time
import csv
import mail
from datetime import date    			# The Stocks below can be taken from any website granting permission to scrape
urls = ['https://finance.yahoo.com/quote/FCONSUMER.NS?p=FCONSUMER.NS&.tsrc=fin-srch','https://finance.yahoo.com/quote/BHARATFORG.NS?p=BHARATFORG.NS&.tsrc=fin-srch','https://finance.yahoo.com/quote/LEMONTREE.NS?p=LEMONTREE.NS&.tsrc=fin-srch',
'https://finance.yahoo.com/quote/SUNDRMFAST.NS?p=SUNDRMFAST.NS&.tsrc=fin-srch','https://finance.yahoo.com/quote/CUMMINSIND-EQ.NS?p=CUMMINSIND-EQ.NS&.tsrc=fin-srch','https://finance.yahoo.com/quote/HINDUNILVR.NS?p=HINDUNILVR.NS&.tsrc=fin-srch',
'https://finance.yahoo.com/quote/BAJFINANCE.NS?p=BAJFINANCE.NS&.tsrc=fin-srch','https://finance.yahoo.com/quote/MAHSCOOTER.NS?p=MAHSCOOTER.NS&.tsrc=fin-srch','https://finance.yahoo.com/quote/BANKBARODA.NS?p=BANKBARODA.NS&.tsrc=fin-srch', 
'https://finance.yahoo.com/quote/CUB.NS?p=CUB.NS&.tsrc=fin-srch', 'https://finance.yahoo.com/quote/CUB.NS?p=CUB.NS&.tsrc=fin-srch', 'https://finance.yahoo.com/quote/KOTAKBANK.NS?p=KOTAKBANK.NS&.tsrc=fin-srch', 'https://finance.yahoo.com/quote/TECHM.NS?p=TECHM.NS&.tsrc=fin-srch',
'https://finance.yahoo.com/quote/RAYMOND.NS?p=RAYMOND.NS&.tsrc=fin-srch', 'https://finance.yahoo.com/quote/ONGC.NS?p=ONGC.NS&.tsrc=fin-srch']
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

today = str(date.today()) + '.csv'
csv_file = open(today,'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name','Current Price','Previous Close','Open','Bid','Ask',"Day's Range",'52 Week Range','Volume','Avg. Volume'])

for url in urls:
	stock = []
	requested_page = requests.get(url, headers = headers)
	soup = BeautifulSoup(requested_page.content, 'lxml')
	page_header = soup.find_all('div', id = 'quote-header-info')[0]

	stock_title = page_header.find('h1').get_text()
	current_price = page_header.find('div', class_ = 'My(6px) Pos(r) smartphone_Mt(6px)').find('span').get_text()
	stock.append(stock_title)
	stock.append(current_price)

	table_info = soup.find_all('div', class_ = 'Bxz(bb) D(ib) Va(t) Mih(250px)--lgv2 W(100%) Mt(-6px) Mt(0px)--mobp Mt(0px)--mobl W(50%)--lgv2 Mend(20px)--lgv2 Pend(10px)--lgv2 BdEnd--lgv2 Bdendc($seperatorColor)--lgv2')[0].find_all('tr')
	for i in range(0,8):
		value = table_info[i].find_all('td')[1].get_text()
		stock.append(value)
	csv_writer.writerow(stock)
	time.sleep(2)

csv_file.close()
mail.send(filename = today)


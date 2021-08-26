import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok="

# 0 = 코스피
# 1 = 코스닥
kosp = "0"
filename="시가총액(코스피).csv"
if kosp ==0:
    filename = "시가총액(코스피).csv"
else:
    filename = "시가총액(코스닥).csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

#엑셀 타이틀
title = "No.	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for page in range(1,33):
    res = requests.get(url+str(kosp)+"&page="+str(page))
    res.raise_for_status
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")
        #의미없는 TD라인 스킵
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns ]
        writer.writerow(data)

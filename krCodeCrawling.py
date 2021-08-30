import pandas as pd
import mariadb

# 코스닥
# https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&marketType=kosdaqMkt
# 유가증권
# https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&marketType=stockMkt

url = 'https://kind.krx.co.kr/corpgeneral/corpList.do' # 1

kosdaq = pd.read_html(url+"?method=download&marketType=kosdaqMkt")[0] #2
kospi = pd.read_html(url+"?method=download&marketType=stockMkt")[0] #3

#전체 종목 수
print(f'kosdaq length: {len(kosdaq)}, kospi length {len(kospi)}')

#코드명 6자리로 채우기
kosdaq.종목코드 = kosdaq.종목코드.astype(str).apply(lambda x:x.zfill(6))
kospi.종목코드 = kospi.종목코드.astype(str).apply(lambda x:x.zfill(6))

#마켓구분 추가
kosdaq['marketname'] = 'KQ'
kospi['marketname'] = 'KS'

stocks = kospi.append(kosdaq)

#코드명 변경
stocks = stocks.rename(columns={'회사명':'companyname','종목코드':'companycode'})
stocks = stocks[['companycode','companyname','marketname']]

stocks.to_csv('companycode.txt', sep = '\t', index=None, header=None)


## DB연결

mariaUser = 'quant'
mariaPassword = 'dkagh=12'
mariaDatabase = ''
mariaHost = 'localhost'

conn = mariadb.connect(user='mariaUser', password='mariaPassword', database='mariaDatabase', host='mariaHost')

cursor = conn.cursor()

INSERT_TABLE_COMPANYCODE = """
INSERT INTO company_code
(
    companycode
   ,companyname
   ,marketname
)
VALUE
(
    ?
   ,?
   ,?
)
"""
data = list(stocks.interpolate(index=False, name=None))
cursor.execute(INSERT_TABLE_COMPANYCODE,data)
conn.commit()


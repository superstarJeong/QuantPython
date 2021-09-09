from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
from bs4 import BeautifulSoup


# 기업코드 수집 URL
url = 'https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=1fe9aaff0c557a4699b3e7351f222ac8b35775e1'

resp = urlopen(url)

with ZipFile(BytesIO(resp.read())) as zf:
  file_list = zf.namelist()
  while len(file_list) > 0:
    file_name = file_list.pop()
    corpCode = zf.open(file_name).read().decode()
    break

# XML 데이터 파싱
soup = BeautifulSoup(corpCode, 'html.parser')

print(soup.prettify())
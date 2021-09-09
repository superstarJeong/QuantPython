from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO

def bind_params(params : dict):
  url_params = []
  for key in params:
    url_params.append(key + '=' + params[key])
  return url_params

url = 'https://opendart.fss.or.kr/api/company.json?'
params = {
  'crtfc_key':'1fe9aaff0c557a4699b3e7351f222ac8b35775e1', # API 인증키
  'corp_code':'00578325' # 기업 고유번호 8자리
}

url = url + '&'.join(bind_params(params))

resp = urlopen(url)

if resp.code == 200:
    resp_json_str = resp.read().decode()

print(resp_json_str)

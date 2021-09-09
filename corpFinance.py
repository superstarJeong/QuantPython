import requests
import json

URL = 'https://opendart.fss.or.kr/api/fnlttSinglAcnt.json'
PARAMS = {
  'crtfc_key': '1fe9aaff0c557a4699b3e7351f222ac8b35775e1', # API 인증키
  'corp_code': '00299321', # 쿠쿠홈시스 고유번호
  'bsns_year': '2021', # 사업연도(4자리)
  'reprt_code': '11013', # 사업보고서
}

resp = requests.get(url = URL, params = PARAMS)

# http 정상응답시 처리
if resp.status_code == 200:
  data_json = resp.json()
  
  # 콘솔 output
  data_str = json.dumps(data_json, indent=4, ensure_ascii=False)
  print(data_str)
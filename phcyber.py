import time
import urllib
import sys
import os
try:
    import requests
except ImportError:
       print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    print('%s Requests has been installed.')
    os.system('clear')
    import requests
header = {"Host": "panel.phcyber.com",
          "accept":"application/json, text/javascript, */*; q=0.01",
          "x-requested-with":"XMLHttpRequest",
          "save-data":"on",
          "uer-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Safari/537.36",
          "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
          "orgins":"https://panel.phcyber.com",
          "sec-fetch-site":"same-orgin",
          "sec-fetch-mode":"cors",
          "sec-fetch-dest":"empty",
          "referer":"https://panel.phcyber.com/vpn-panel",
          "accept-encoding":"gzip, deflate, br",
          "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}

cookies = {"userFromEEA":"false",
           "_ga":"GA1.2.1244296561.1604122830",
           "PHPSESSID":"fa0c3ef0bae16fdfead90bd486599352",
           "__cfduid":"d316baf965e5ea8804e44876fa95f20a11606728889",
           "_gid":"GA1.2.44312568.1606895801",
           "__gads":"ID=eb76ad1a90c5e03b:T=1606895875:S=ALNI_MZgGTv5IuZtgdg9X_QBo15dsshgSA"}

r2 = requests.post("https://panel.phcyber.com/ads/video_rewarded", headers=header,cookies=cookies)
r2 = x
print(x)


           

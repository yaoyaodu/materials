import requests
import json # 用于解析
import pandas as pd  
source = input('请输入你要翻译的内容：')
website = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
uaagent = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}
obtain_info = requests.post(url=website,headers=uaagent).text
data = {}
data['i'] = source
data['doctype'] = 'json'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['client'] = 'fanyideskweb'
obtain_info = requests.post(url=website,headers=uaagent,data=data).text
dict1 = json.loads(obtain_info)  #json解析
result = dict1['translateResult'][0][0]['tgt']
results = pd.DataFrame({'a':[source], 'b':[result]})
results.to_csv('c:/翻译结果.csv',index=False,header=0,mode='a',encoding="ANSI")



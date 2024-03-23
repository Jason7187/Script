##每天60s新闻阅读

import requests  
import notify  
from datetime import datetime  

cron:1 10 * * * DailyNews.py

url = 'https://60s.viki.moe/?encoding=text'  
resp = requests.get(url)  
  
# 获取当前日期，并格式化为字符串  
current_date = datetime.now().strftime('%Y-%m-%d')  
  
# 不再分片处理，直接发送整个响应内容  
content = resp.text  
  
# 在通知内容前添加日期  
notification_content = f"{current_date}\n\n{content}"  
  
# 发送完整内容推送，包括日期  
notify.send("每天60s读懂世界", notification_content)

import requests, json 
import os
import logging
import notify

# 控制是否启用通知的变量
enable_notification = 1

# 只有在需要发送通知时才尝试导入notify模块
if enable_notification == 1:
    try:
        from notify import send
    except ModuleNotFoundError:
        print("警告：未找到notify.py模块。它不是一个依赖项，请勿错误安装。程序将退出。")
        sys.exit(1)
        
# 设置变量 xk_username 和 xk_password

xk_username= os.getenv("xk_username").split('&')
xk_password = os.getenv("xk_password").split('&')


logging.captureWarnings(True)
for i in range(len(xk_username)):
    print(f'开始第{i + 1}个帐号签到')
    url = 'https://www.xkdaili.com/tools/submit_ajax.ashx?action=user_login&site_id=1'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Length': '50',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.xkdaili.com',
        'Origin': 'https://www.xkdaili.com',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'https://www.xkdaili.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {
        'username': f'{xk_username[i]}',
        'password': f'{xk_password[i]}',
        'remember': 1
    }
    response = requests.post(url=url, headers=headers, data=data,verify=False)
    cookie=str(requests.utils.dict_from_cookiejar(response.cookies)).replace(',',';').replace(':','=').replace('\'','').replace('{','').replace('}','').replace(' ','')
    r = json.loads(response.text)['msg']
    print(r)

    url_sign = 'https://www.xkdaili.com/tools/submit_ajax.ashx?action=user_receive_point'
    headers_sign = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Length': '10',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Host': 'www.xkdaili.com',
        'Origin': 'https://www.xkdaili.com',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'https://www.xkdaili.com/main/usercenter.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data_sign = {
        'type': 'login'
    }
    html_sign = requests.post(url=url_sign, headers=headers_sign, data=data_sign, verify=False)
    result = json.loads(html_sign.text)['msg']
    print(result)

        # 如果需要发送通知
    if enable_notification == 1:
        send("星空代理-通知",result)
  
    

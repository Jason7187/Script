import requests
import json
from datetime import datetime
import ast

isvtoken = ""#可能一天换一次   点赞浏览可能有问题，多执行几次总会成功
encryptionkey = ""#可能一天换一次
unionId = ""
wxOpenId = ""
mobile = ""  #手机号
openId = ""#可能一天换一次,不报错不需要管
mntoken = ""  #蒙牛抽奖页面搜这个url里面请求体的token
headers = {
    "Host": "mp-isv.youzanyun.com",
    "encryptionkey": encryptionkey,
    "accept": "application/json",
    "isv-token":isvtoken ,
    "xweb_xhr": "1",
    "isv": "mengniu.isv.youzan.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9079",
    "content-type": "application/json",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx4332719bca2e4089/107/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
url = "https://mp-isv.youzanyun.com/client/article/read"


url0 = "https://mp-isv.youzanyun.com/point/getNutrition"
data0 = {
    "userInfo": {
        "wxOpenId": wxOpenId
    },
    "unionId": unionId
}
data0 = json.dumps(data0, separators=(',', ':'))
response0 = requests.post(url0, headers=headers, data=data0)
# 解析 JSON 数据
parsed_data = json.loads(response0.text)

# 获取 pointsBalanceValue 的值
points_balance_value = parsed_data["data"]["pointsBalanceValue"]
print("当前营养值为:", points_balance_value)
#for _ in range(3):  #三次浏览文章,每次10营养值
    

#print("浏览完毕")



url4 = "https://mp-isv.youzanyun.com/user/center/protein/task/list"
params = {
    "mobile": mobile,
    "levelTemplateId": "1",
    "unionId": unionId
}
response4 = requests.get(url4, headers=headers, params=params)

parsed_data = json.loads(response4.text)

# 遍历任务列表，查找taskId为4的任务
for task in parsed_data["data"]:
    if task["taskId"] == 4:
        # 找到taskId为4的任务后，判断taskLightStatus是否为0
        if task["taskLightStatus"] == 0:
            print("开始进行点赞任务")

            for _ in range(3):#点赞文章
                url2 = "https://mp-isv.youzanyun.com/client/article/selectArticleByCategoryAndTopicTagV1102" #查询未点赞文章
                data2 = {
                    "pageNo": 1,
                    "pageSize": 100,
                    "wxOpenId": wxOpenId,
                    "categoryId": 106754,
                    "topicTagId": 0,
                    "unionId": unionId
                }
                
                data2 = json.dumps(data2, separators=(',', ':'))
                wzlb = requests.post(url2, headers=headers, data=data2)
                
                # 将文本数据转换为字典
                wz = json.loads(wzlb.text)
                #print(wz)
                # 查询memberIsLike为false的id
                for item in wz["data"]["data"]:
                    
                    if not item["memberIsLike"]:
                        
                        print("未点赞文章的id为:", item["id"])
                        id_str = str(item["id"])
                        url3 = "https://mp-isv.youzanyun.com/client/article/like"
                        data3 = {
                        "articleId": id_str,  
                        "wxOpenId": wxOpenId,
                        "like": 1,
                        "unionId": unionId
                        }
                        data = {
                        "wxOpenId":wxOpenId ,
                        "articleId": id_str,
                        "read": 1,
                        "unionId": unionId
                        }
                        data = json.dumps(data, separators=(',', ':'))
                        data3 = json.dumps(data3, separators=(',', ':'))
                        response3 = requests.post(url3, headers=headers, data=data3)
                        print(response3.text)
                        print("点赞完成,本次点赞的文章id为:"+id_str)
                        print("进行浏览此文章")
                        response = requests.post(url, headers=headers, data=data)
                        print(response.text)
                        break  # 
                    else:
                        print("你已经把所有文章都点赞了")  
                        break  


        else:
            print("点赞任务已完成")
            #print(task["taskLightStatus"])
        break
    else:
        print("开始找点赞任务")
        #print(task["taskId"])

# 生成当前时间的时间戳
current_timestamp = datetime.now().timestamp()

# 将时间戳转换为指定格式的时间字符串
current_time = datetime.fromtimestamp(current_timestamp).strftime("%Y-%m-%d %H:%M:%S")

headers5 = {
    "Host": "mp-isv.youzanyun.com",
    "encryptionkey": encryptionkey,
    "accept": "application/json",
    "isv-token": isvtoken,
    "xweb_xhr": "1",
    "isv": "mengniu.isv.youzan.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9079",
    "content-type": "application/json",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx4332719bca2e4089/107/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
url5 = "https://mp-isv.youzanyun.com/sign"
data5 = {
    "yzOpenId": openId,
    "signDate": current_time,
    "brandName": "真果粒",
    "activityName": "签到有礼，果真是你",
    "unionId": unionId
}
data5 = json.dumps(data5, separators=(',', ':'))

headers6 = {
    "Host": "mp-isv.youzanyun.com",
    "encryptionkey": encryptionkey,
    "accept": "application/json",
    "isv-token": isvtoken,
    "xweb_xhr": "1",
    "isv": "mengniu.isv.youzan.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9079",
    "content-type": "application/json",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx4332719bca2e4089/108/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
url6 = "https://mp-isv.youzanyun.com/activity/add_sign_in_customer"
data6 = {
    "mobile": mobile,
    "storeId": 130177909,
    "actionName": "3月精选牧场签到",
    "time": current_time,  # 替换为当前时间字符串
    "proteinNumber": 5,
    "openId": openId,
    "totalId": 581,
    "brand": "JING_XUAN_MU_CHANG"
}
data6 = json.dumps(data6)


headers7 = {
    "Host": "mp-isv.youzanyun.com",
    "encryptionkey": encryptionkey,
    "accept": "application/json",
    "isv-token": isvtoken,
    "xweb_xhr": "1",
    "isv": "choujiang.isv.youzan.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9079",
    "content-type": "application/x-www-form-urlencoded",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx4332719bca2e4089/108/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
url7 = "https://mp-isv.youzanyun.com/proxy"
data7 = {
    "action": "/mini/choujiang/taskSignIn",
    "token": mntoken,
    "activityID": "9031ee49560643eaa1d31a6d70b3186c"
}
response7 = requests.post(url7, headers=headers7, data=data7)#蒙牛抽奖签到
data7 = json.loads(response7.text)
message = data7["message"]
# 使用ast模块进行Unicode解码
decoded_message2 = ast.literal_eval(f'"{message}"')
print("蒙牛抽奖签到")
print(decoded_message2)

headers11 = {
    "Host": "mp-isv.youzanyun.com",
    "encryptionkey": encryptionkey,
    "accept": "application/json",
    "isv-token": isvtoken,
    "xweb_xhr": "1",
    "isv": "mengniu.isv.youzan.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9079",
    "content-type": "application/json",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx4332719bca2e4089/108/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
data11 = {
    "mobile": mobile,
    "storeId": 130177909,
    "actionName": "品牌签到_白奶",
    "time": current_time,
    "proteinNumber": 5,
    "openId": openId,
    "totalId": 24,
    "brand": "MENG_NIU"
}
data11 = json.dumps(data11, separators=(',', ':'))

data8 = {
    "action": "/mini/choujiang/winPrize",
    "token": mntoken,
    "number": "1",
    "activityID": "9031ee49560643eaa1d31a6d70b3186c"
}
for _ in range(2):
    response8 = requests.post(url7, headers=headers7, data=data8)#蒙牛抽奖
    #print(response8.text)
    # 解析JSON字符串
    data = json.loads(response8.text)
    
    message = data["message"]
    # 使用ast模块进行Unicode解码
    decoded_message = ast.literal_eval(f'"{message}"')
    print(decoded_message)
print("抽奖完毕")   

data9 = {
    "action": "/mini/choujiang/queryRewards",
    "token": mntoken,
    "activityID": "9031ee49560643eaa1d31a6d70b3186c"
}

response9 = requests.post(url7, headers=headers7, data=data9)
# 将JSON数据解析为Python字典
data_dict = json.loads(response9.text)


# 查找状态为2的奖励信息中的编号
for key, value in data_dict["data"]["rewards"].items():
    if value["gift"]["state"] == 2:
        print("编号:", key)
        data10 = {
            "action": "/mini/choujiang/requestRewards",
            "token": mntoken,
            "rewardID": key,
            "activityID": "9031ee49560643eaa1d31a6d70b3186c"
        }
        if str(key) in data_dict["data"]["rewards"]:
            product_title = data_dict["data"]["rewards"][str(key)]["reward"]["score"]["product_title"]
            print(f"可以领取奖励的key为:{key}: {product_title}")
        else:
            print(f"领取异常")
        response10 = requests.post(url7, headers=headers7, data=data10)  # 领取奖励      
    else:
        print("遍历可以领取的奖励信息,遍历不到既没有可以领取的奖励")   

headers12 = {
    "Host": "mp-isv.youzanyun.com",
    "encryptionkey": encryptionkey,
    "accept": "application/json",
    "isv-token": isvtoken,
    "xweb_xhr": "1",
    "isv": "mengniu.isv.youzan.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9079",
    "content-type": "application/json",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx4332719bca2e4089/108/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
data12 = {
    "mobile": mobile,
    "storeId": 130177909,
    "actionName": "酸酸乳签到",
    "time": current_time,
    "proteinNumber": 5,
    "openId": openId,
    "totalId": 528,
    "brand": "SUAN_SUAN_RU"
}

headers13 = {
    "Host": "mp-isv.youzanyun.com",
    "encryptionkey": encryptionkey,
    "accept": "application/json",
    "isv-token": isvtoken,
    "xweb_xhr": "1",
    "isv": "mengniu.isv.youzan.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9079",
    "content-type": "application/json",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx4332719bca2e4089/108/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
data13 = {
    "mobile": mobile,
    "storeId": 130177909,
    "actionName": "奶特签到",
    "time": current_time,
    "proteinNumber": 5,
    "openId": openId,
    "totalId": 183,
    "brand": "NAI_TE"
}

headers14 = {
    "Host": "mp-isv.youzanyun.com",
    "encryptionkey": encryptionkey,
    "accept": "application/json",
    "isv-token": isvtoken,
    "xweb_xhr": "1",
    "isv": "mengniu.isv.youzan.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9079",
    "content-type": "application/json",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx4332719bca2e4089/108/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
data14 = {
    "mobile": mobile,
    "storeId": 130177909,
    "actionName": "未来星签到",
    "time": current_time,
    "proteinNumber": 5,
    "openId": openId,
    "totalId": 547,
    "brand": "WEI_LAI_XING"
}
response5 = requests.post(url5, headers=headers5, data=data5)#真果粒签到
print(response5.text)
print("真果粒签到完成")

response11 = requests.post(url6, headers=headers11, data=data11)
print(response11.text)#蒙牛签到
print("蒙牛签到完成")

response14 = requests.post(url6, headers=headers14, json=data14)
print(response14.text)
print("未来星签到完成")

response6 = requests.post(url6, headers=headers6, data=data6)#牧场签到
print(response6.text)
print("牧场签到完成")

response12 = requests.post(url6, headers=headers12, json=data12)
print(response12.text)
print("酸酸乳签到完成")

response13 = requests.post(url6, headers=headers13, json=data13)
print(response13.text)
print("奶特签到完成")

response00 = requests.post(url0, headers=headers, data=data0)
# 解析 JSON 数据
parsed_data = json.loads(response00.text)

# 获取 pointsBalanceValue 的值
points_balance_value2 = parsed_data["data"]["pointsBalanceValue"]
print("当前营养值为:", points_balance_value2)
sum=points_balance_value2-points_balance_value
print("本次增加的营养值为:"+str(sum))

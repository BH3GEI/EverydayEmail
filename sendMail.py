import smtplib
from email.mime.text import MIMEText
import string
import datetime
import requests
import json
import re
from bs4 import BeautifulSoup


sender_name = 'xxx'
receiver_name = 'xxx'

kenenbi = '1949-10-01'  # 纪念日
name = 'xxx'  # 发件人名称
mail_title = 'xxx'  # 邮件名称



mailto_list = ["xxx@xxx.com"]  # 收件人
mail_host = "smtp.qq.com"  # 发件服务器
mail_user = "xxxx"  # 用户名
mail_pass = "xxx"  # 密码


def get_deltaDay():
    """
    计算日期差
    """
    d1 = datetime.datetime.strptime(kenenbi, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
    delta = d2 - d1
    return delta.days


def get_date():
    """
    获取今天的日期
    """
    i = datetime.datetime.now()
    date = "%s/%s/%s" % (i.year, i.month, i.day)
    return date


def get_weathertips():
    """
    从墨迹天气获取天气提示
    """
    url = "https://tianqi.moji.com/weather/china/jilin/nanguan-district"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html5lib", from_encoding="utf-8")
    all_tertiaryconsumers = soup.find_all(class_='wea_tips clearfix')
    for tertiaryconsumer in all_tertiaryconsumers:
        return re.search('<em>(.+?)</em>', str(tertiaryconsumer)).group(1)


def get_tuwei():
    """
    获取一段土味情话
    """
    url = "https://api.shadiao.app/chp"
    resp = requests.get(url)
    txt = json.loads(resp.text)
    txt = txt['data']['text']
    return txt


def get_weather_zz():
    """
    获取天气a
    """
    url = "https://tianqi.moji.com/weather/china/henan/xinzheng"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html5lib", from_encoding="utf-8")
    all_tertiaryconsumers = soup.find_all(class_='days clearfix')
    html = ''
    for tertiaryconsumer in all_tertiaryconsumers:
        day = tertiaryconsumer.find(name='a').text
        url = re.search('src="(.+?)"', str(tertiaryconsumer)).group(1)
        weather = re.search('<img alt="(.+?)"', str(tertiaryconsumer)).group(1)
        temperature = re.search('(\w+° \/ \w+°)', str(tertiaryconsumer)).group(1)
        if 'level_1' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_1').text.strip()
            color = '#8fc31f'
        if 'level_2' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_2').text.strip()
            color = '#d7af0e'
        if 'level_3' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_3').text.strip()
            color = '#f39800'
        if 'level_4' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_4').text.strip()
            color = '#e2361a'
        if 'level_5' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_5').text.strip()
            color = '#5f52a0'
        if 'level_6' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_6').text.strip()
            color = '#631541'
        html += """<div style="display: flex;margin-top:5px;height: 30px;line-height: 30px;justify-content: space-around;align-items: center;">
        <span style="width:15%%; text-align:center;">%s</span>
        <div style="width:10%%; text-align:center;">
            <img style="height:26px;vertical-align:middle;" src='%s' alt="">
        </div>
        <span style="width:25%%; text-align:center;">%s</span>
        <div style="width:35%%; ">
            <span style="display:inline-block;padding:0 8px;line-height:25px;color:%s; border-radius:15px; text-align:center;">%s</span>
        </div>
        </div>
        """ % (day, url, temperature, color, WindLevel)
    return html




def get_weather_cc():
    """
    获取天气b
    """
    url = "https://tianqi.moji.com/weather/china/henan/xinzheng"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html5lib", from_encoding="utf-8")
    all_tertiaryconsumers = soup.find_all(class_='days clearfix')
    html = ''
    for tertiaryconsumer in all_tertiaryconsumers:
        day = tertiaryconsumer.find(name='a').text
        url = re.search('src="(.+?)"', str(tertiaryconsumer)).group(1)
        weather = re.search('<img alt="(.+?)"', str(tertiaryconsumer)).group(1)
        temperature = re.search('(\w+° \/ \w+°)', str(tertiaryconsumer)).group(1)
        if 'level_1' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_1').text.strip()
            color = '#8fc31f'
        if 'level_2' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_2').text.strip()
            color = '#d7af0e'
        if 'level_3' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_3').text.strip()
            color = '#f39800'
        if 'level_4' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_4').text.strip()
            color = '#e2361a'
        if 'level_5' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_5').text.strip()
            color = '#5f52a0'
        if 'level_6' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_6').text.strip()
            color = '#631541'
        html += """<div style="display: flex;margin-top:5px;height: 30px;line-height: 30px;justify-content: space-around;align-items: center;">
        <span style="width:15%%; text-align:center;">%s</span>
        <div style="width:10%%; text-align:center;">
            <img style="height:26px;vertical-align:middle;" src='%s' alt="">
        </div>
        <span style="width:25%%; text-align:center;">%s</span>
        <div style="width:35%%; ">
            <span style="display:inline-block;padding:0 8px;line-height:25px;color:%s; border-radius:15px; text-align:center;">%s</span>
        </div>
        </div>
        """ % (day, url, temperature, color, WindLevel)
    return html


def get_weather_hohhot():
    """
    获取天气c
    """
    url = "https://tianqi.moji.com/weather/china/henan/xinzheng"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html5lib", from_encoding="utf-8")
    all_tertiaryconsumers = soup.find_all(class_='days clearfix')
    html = ''
    for tertiaryconsumer in all_tertiaryconsumers:
        day = tertiaryconsumer.find(name='a').text
        url = re.search('src="(.+?)"', str(tertiaryconsumer)).group(1)
        weather = re.search('<img alt="(.+?)"', str(tertiaryconsumer)).group(1)
        temperature = re.search('(\w+° \/ \w+°)', str(tertiaryconsumer)).group(1)
        if 'level_1' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_1').text.strip()
            color = '#8fc31f'
        if 'level_2' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_2').text.strip()
            color = '#d7af0e'
        if 'level_3' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_3').text.strip()
            color = '#f39800'
        if 'level_4' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_4').text.strip()
            color = '#e2361a'
        if 'level_5' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_5').text.strip()
            color = '#5f52a0'
        if 'level_6' in str(tertiaryconsumer):
            WindLevel = tertiaryconsumer.find(class_='level_6').text.strip()
            color = '#631541'
        html += """<div style="display: flex;margin-top:5px;height: 30px;line-height: 30px;justify-content: space-around;align-items: center;">
        <span style="width:15%%; text-align:center;">%s</span>
        <div style="width:10%%; text-align:center;">
            <img style="height:26px;vertical-align:middle;" src='%s' alt="">
        </div>
        <span style="width:25%%; text-align:center;">%s</span>
        <div style="width:35%%; ">
            <span style="display:inline-block;padding:0 8px;line-height:25px;color:%s; border-radius:15px; text-align:center;">%s</span>
        </div>
        </div>
        """ % (day, url, temperature, color, WindLevel)
    return html


def get_image():
    """
    获取一张鸡汤图片
    """

    url = "http://wufazhuce.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html5lib", from_encoding="utf-8")
    return re.search('src="(.+?)"', str(soup.find(class_='fp-one-imagen'))).group(1)


mail_content = """<!DOCTYPE html>
<html><head>
    <title>
    </title>
    <meta name="viewport" content="width=device-width,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no">
    <link rel="stylesheet" href="/stylesheets/style.css">
</head>
<body style="margin:0;padding:0;" class="vsc-initialized">
    <div style="width:100%; margin: 40px auto;font-size:20px; color:#5f5e5e;text-align:center">
        <span>正计时</span>
        <span style="font-size:24px;color:rgb(221, 73, 73)">{0}</span>
      
    </div>
    <div style="width:60%; margin: 40px auto;color:#5f5e5e;text-align:center">
    <span style="display:block;color:#676767;font-size:20px">{1}</span>
    <img src="{2}" style="width:100%;margin-top:10px;" alt="">
    </div>
    <div style="width:100%; margin: 40px auto;color:#5f5e5e;text-align:center">        
        <span style="display:block;margin-top:15px;color:#676767;font-size:15px">🧡a的天气💛</span> {3}
        <span style="display:block;margin-top:15px;color:#676767;font-size:15px">🧡b的天气💛</span> {4}
        <span style="display:block;margin-top:15px;color:#676767;font-size:15px">🧡c的天气💛</span> {5}
    </div>
    <div style="width:100%; margin: 40px auto;color:#5f5e5e;text-align:center">
        <span style="display:block;color:#676767;font-size:20px">{6}</span>
        <span style="display:block;margin-top:55px;color:#676767;font-size:15px">{7} ❤️ {8}</span>
        <span style="display:block;margin-top:25px;font-size:22px; color:#9d9d9d; ">{9}</span>
    </div>
</body></html>""".format(str(get_deltaDay()), get_weathertips(), get_image(), get_weather_zz(), get_weather_hohhot(), get_weather_cc(), get_tuwei(), sender_name, receiver_name, get_date(), get_image())


def send_mail(to_list, sub, content):
    """
    发送邮件
    """
    me = name + "<" + mail_user + ">"
    msg = MIMEText(content, _subtype='html', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ",".join(mailto_list)
    try:
        server = smtplib.SMTP_SSL(mail_host, )
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False

#print(get_deltaDay())
#print(get_date())
#print(get_weathertips())
#print(get_tuwei())
#print(get_weather_cc())
#print(get_weather_hohhot())
#print(get_image())

if __name__ == '__main__':
    if send_mail(mailto_list, mail_title, mail_content):
        print("success!")
    else:
        print("failure!")






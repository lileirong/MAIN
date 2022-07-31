# -*- coding: utf-8 -*-
import requests
import ddddocr
import time
import re

session_1 = requests
shi = time.time() * 1000
shi = str(int(shi))
session = requests.Session()

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
           'Host': 'xgxlsg.cqbvc.edu.cn:17535',
           'Referer': 'http://xgxlsg.cqbvc.edu.cn:17535/SPCP/Web/Account/ChooseType',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',

           }

tu_url = 'http://xgxlsg.cqbvc.edu.cn:17535/SPCP/Web/Account/GetLoginVCode?dt=' + shi
panDuan = "<Response [200]>"
while panDuan == "<Response [200]>":
    c = requests.get(tu_url, headers, verify=False)
    c_1 = c.content
    with open("daka.png", "wb") as fb:
        fb.write(c_1)
        # print(c)
    ocr = ddddocr.DdddOcr()
    with open('daka.png', 'rb') as f:
        img_bytes = f.read()
        res = ocr.classification(img_bytes)
        print(len(res))
        print(res)
    print(c.cookies.get_dict())
    cookie = c.cookies.get_dict()
    data = {
        'ReSubmiteFlag': '60675386-535d-4861-9839-476d33934469',
        'StuLoginMode': '3',
        'txtUid': '202104322',
        'txtPwd': '252724',
        'code': res
    }
    print(res)
    url = 'http://xgxlsg.cqbvc.edu.cn:17535/SPCP/Web/'
    session_1 = session.post(url, data, cookies=cookie, allow_redirects=False, verify=False)  # 登录
    panDuan = str(session_1)

print(panDuan)
session_2 = session_1.content.decode('utf8')
print(session_2)
data_1 = {
    'StudentId': '202104322',
    'Name': '任思蓉',
    'Sex': '女',
    'SpeType': 'Z',
    'CollegeNo': '02',
    'SpeGrade': '2021',
    'SpecialtyName': '数字图文信息处理技术',
    'ClassName': '2021级数字图文信息处理技术1班',
    'MoveTel': '15123046563',
    'Province': '500000',
    'City': '500100',
    'County': '500115',
    'ComeWhere': '长寿区寿城水岸二期公租房',
    'FaProvince': '500000',
    'FaCity': '500100',
    'FaCounty': '500115',
    'FaComeWhere': '风城街道寿城水岸二期公租房',
    'text_1': '15123046563',
    'radio_1': '03c4143d-01ce-4a94-af3d-de3bffbff573',
    'text_2': '大学城中路1号重庆商务职业学院D1503',
    'radio_2': 'c8421877-04e4-43c3-bf6e-dc0fc67a0a8a',
    'radio_3': '0024e4f7-2e9b-4a9d-836b-68565da4dbaf',
    'radio_4': 'e862dac5-a3c4-4a48-a6d2-456678f43ae5',
    'radio_5': '67345d29-d462-4976-88ce-1c6f063e3269',
    'text_3': '36.7',
    'text_4': '36.9',
    'radio_6': 'afd7222b-978d-4d04-b222-6fa55f94f442',
    'radio_7': '43d7a8e1-9f7a-40c1-921c-60d5c20fea97',
    'radio_8': '4ef91fb0-45a9-4c31-a4ad-d07a6fa45c03',
    'radio_9': 'df74af3b-3faf-4ca6-86a7-3cd68bcaacc0',
    'radio_10': '0ee450e4-8002-44ff-b4f4-c87c120e4170',
    'checkbox_1': 'c6aa5baa-5b8a-43f6-ae5c-e88818599544',
    'Other': '',
    'GetAreaUrl': '/SPCP/Web/Report/GetArea',
    'IdCard': '500221200203252724',
    'ProvinceName': '重庆市',
    'CityName': '重庆市市辖区',
    'CountyName': '长寿区',
    'FaProvinceName': '重庆市',
    'FaCityName': '重庆市市辖区',
    'FaCountyName': '长寿区',
    'radioCount': '10',
    'checkboxCount': '1',
    'blackCount': '4',
    'PZData': '[{"OptionName":"是","SelectId":"03c4143d-01ce-4a94-af3d-de3bffbff573","TitleId":"6dccbd83-af36-430d-aaeb-bda049b26ce0","OptionType":"0"},{"OptionName":"绿码","SelectId":"c8421877-04e4-43c3-bf6e-dc0fc67a0a8a","TitleId":"51e5356e-d9b8-4bb4-af10-6cfb0f1dca3b","OptionType":"0"},{"OptionName":"无","SelectId":"0024e4f7-2e9b-4a9d-836b-68565da4dbaf","TitleId":"2baec89e-027a-4886-8141-8aad37bf5d65","OptionType":"0"},{"OptionName":"无","SelectId":"e862dac5-a3c4-4a48-a6d2-456678f43ae5","TitleId":"f0d809ad-55aa-422d-976e-febc6b2cce92","OptionType":"0"},{"OptionName":"无认定","SelectId":"67345d29-d462-4976-88ce-1c6f063e3269","TitleId":"a1fbc63e-7aff-434b-b37e-83c67a138ffb","OptionType":"0"},{"OptionName":"已检测，结果阴性","SelectId":"afd7222b-978d-4d04-b222-6fa55f94f442","TitleId":"ebc9b343-b197-4528-8e09-41b2cb7024a3","OptionType":"0"},{"OptionName":"是","SelectId":"43d7a8e1-9f7a-40c1-921c-60d5c20fea97","TitleId":"82a11bd9-aba7-41e4-ab2e-7b192a81d819","OptionType":"0"},{"OptionName":"已打加强针（两针剂）","SelectId":"4ef91fb0-45a9-4c31-a4ad-d07a6fa45c03","TitleId":"a34a586c-ad13-4ad1-b051-b4170b0f7165","OptionType":"0"},{"OptionName":"否","SelectId":"df74af3b-3faf-4ca6-86a7-3cd68bcaacc0","TitleId":"909c86e3-a47d-44dc-8dfa-8359fe1f654d","OptionType":"0"},{"OptionName":"未隔离","SelectId":"0ee450e4-8002-44ff-b4f4-c87c120e4170","TitleId":"b1597017-37bd-4838-806b-416f164cf74b","OptionType":"0"},{"TitleId":"d8b2e68b-a002-4b41-97c9-f2a09319c6d1","OptionName":"绿码","SelectId":"c6aa5baa-5b8a-43f6-ae5c-e88818599544","OptionType":"1"},{"OptionName":"15123046563","SelectId":"","TitleId":"c2daa526-a21b-4197-b831-89611dc8822f","OptionType":"2"},{"OptionName":"大学城中路1号重庆商务职业学院D1503","SelectId":"","TitleId":"d3be8ad0-181f-4f34-be01-3429e7cb66e4","OptionType":"2"},{"OptionName":"36.7","SelectId":"","TitleId":"7c8fbfab-9a1a-4712-929e-92cadb725896","OptionType":"2"},{"OptionName":"36.9","SelectId":"","TitleId":"0fd3066f-f108-4c50-8389-3d7336d7f1a2","OptionType":"2"}]',
    'ReSubmiteFlag': 'd49b031d-7a7b-4c05-84db-50ba1fd2b9e9'
}
url_1 = 'http://xgxlsg.cqbvc.edu.cn:17535/SPCP/Web/Report/Index'
session_3 = session.post(data=data_1, url=url_1, headers=headers, verify=False)
session_4 = session_3.content.decode("utf-8")
print(session_4)


def qqemail(subject: object, email: object, text: object):
    # 无需安装第三方库
    key = 'xwmnbxfzvxjndfcj'  # 换成你的QQ邮箱SMTP的授权码(QQ邮箱设置里)  设置-> 账户-> SMTP服务
    email_address = '2822552903@qq.com'  # 换成你的邮箱地址
    email_password = key

    import smtplib
    smtp = smtplib.SMTP('smtp.qq.com', 25)
    smtp.ehlo("smtp.qq.com")
    smtp.quit()

    import ssl
    context = ssl.create_default_context()
    sender = email_address  # 发件邮箱
    receiver = email  # "*********@qq.com"#EMAIL_ADDRESS
    # 收件邮箱
    from email.message import EmailMessage
    subject = subject
    body = text
    msg = EmailMessage()
    msg['subject'] = subject  # 邮件主题
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(body)  # 邮件内容

    with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)


session_5 = str(session_4)
result = ''.join(re.findall(r'[\u4e00-\u9fa5]', session_5))
print(result)
result = result[13:-2]
email_1 = "1422143766@qq.com"
email_2 = "2033353019@qq.com"
#qqemail(subject="打卡", email=email_1, text=result)
qqemail(subject="打卡", email=email_2, text=result)

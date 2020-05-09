import requests
from bs4 import BeautifulSoup
import schedule
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender = ''
my_pass = ''
my_user1 = ''
my_user2 =''
my_user3 =''



headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
         'Cookie':'ddscreen=2; dest_area=country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0; __permanent_id=20200504164418279554810514077662078; __visit_id=20200504164418280158636886854317737; __out_refer=; __trace_id=20200504170019176192158175862280961; __rpm=...1588581943719%7C...1588582819184'
        }

list_all=[]
def getdata():
    for i in range(1,4):
        res=requests.get(headers=headers,url='http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-{}'.format(str(i)))
        #print(res.status_code)
        soup = BeautifulSoup(res.text, 'html.parser')
        items = soup.find('ul',class_='bang_list_mode')
        list = items.find_all('li')
        for shudan in list:
            shuming=shudan.find('div',class_='name').find('a')
            title=shuming['title']
            zuozhe = shudan.find('div',class_='publisher_info').find('a')
            author=zuozhe['title']
            jiage = shudan.find('div', class_='price').find('span',class_='price_n').text
            list100=title+'-----' + author +'-----'+ jiage+'-----'
            list_all.append(list100)
            mess100=str(list_all)
    return mess100



def mail(mess100):
    ret = True
    try:
        msg = MIMEText(mess100,'plain', 'utf-8')
        msg['From'] = formataddr(["大哥", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["小弟", my_user1])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "每天问候"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user1,my_user2,my_user3,], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret

    ret = mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")

mess100 = getdata()
mail(mess100)


























#scrapy框架里面的spider代码
# import scrapy,bs4
# from ..items import DangdangItem
# class Dangdangspider(scrapy.Spider):
#     name='dangdang'
#     allowed_domians=['bang.dangdang.com']
#     start_urls=[]
#     for x in range(1,4):
#         url='http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-'+str(x)
#         start_urls.append(url)
#     def parse(self,response):
#         bs=bs4.BeautifulSoup(response.text,'html.parser')
#         items1 = bs.find('ul',class_='bang_list_mode')
#         list = items1.find_all('li')
#         for shudan in list:
#             item = DangdangItem()
#             shuming=shudan.find('div',class_='name').find('a')
#             item['title']=shuming['title']
#             zuozhe = shudan.find('div',class_='publisher_info').find('a')
#             item['author']=zuozhe['title']
#             item['jiage']= shudan.find('div', class_='price').find('span',class_='price_n').text
#             print(item['title'])
#             yield item
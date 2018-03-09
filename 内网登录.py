import os
import re
import requests
import time
import subprocess
import socket
import queue
import urllib3
urllib3.disable_warnings()


def GetIP():
    '''name = socket.getfqdn(socket.gethostname())
    IP = socket.gethostbyname(name)
    return IP'''
    url = "https://portal2.cjlu.edu.cn:801/eportal/?c=ACSetting&a=Login&wlanuserip="
    data = requests.get(url)
    IP = re.findall('wlanuserip=(.*?)&', data.url)[0]
    return IP


def Login(IP,  username,  password):
    url = 'https://portal2.cjlu.edu.cn:801/eportal/?c=ACSetting&a=Login&wlanuserip='+ \
          IP + '&wlanacip=null&wlanacname=&port=&iTermType=1&mac=000000000000&ip=' + \
          IP + '&redirect=null'
    data = {}
    data['DDDDD'] = username
    data['upass'] = password
    data['R1'] = '0'
    data['R2'] = '' 
    data['R6'] = '0'
    data['para'] = '00'
    data['0MKKey'] = '123456'
    LoginData = requests.post(url, data = data, verify = False)
    LoginData.encoding = 'gb2312'
    if(re.search('用户登录成功',LoginData.text)==None):
        #CheckError()
        return False
    else:
        return True


def Logout():
    url = 'https://portal2.cjlu.edu.cn:801/eportal/?c=ACSetting&a=Logout' \
          '&wlanuserip=null&wlanacip=null&wlanacname=&port=&iTermType=1'
    url_data = requests.get(url, verify=False)
    return url_data


def CheckError():
    url = 'https://portal2.cjlu.edu.cn/errcode'
    url_data = requests.get(url, verify = False)
    error = re.findall('ret=\'(.*)\'',url_data.text)[0]
    if "auth error5" in error:
        print("本账号已停机")
    elif "auth error80" in error:
        print("本时段禁止上网")
    elif "auth error" in error:
        print("密码错误，请输入正确的密码")
    elif "In use" in error:
        print("登录超过人数限制")
    elif "no errcode" in error:
        print("本IP已经在线")
    elif "Authentication Fail ErrCode=04" in error:
        print("上网时长/流量已到上限")
    else:
        print("错误代码:"+error)


def CheckInternet():
    status_1 = subprocess.run("ping -n 2 -w 40 www.baidu.com", shell=True)
    if status_1.returncode == 0:
        return 1
    status_2 = subprocess.run("ping -n 2 -w 40 www.cjlu.edu.cn", shell=True)
    if status_2.returncode ==0:
        return 2
    status_3 = subprocess.run('ping -n 2 -w 40 portal2.cjlu.edu.cn', shell=True)
    if status_3.returncode ==0:
        return 3
    return 0

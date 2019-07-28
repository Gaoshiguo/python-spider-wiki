import requests
from urllib import request
from urllib import parse
import time

def douban():
        url = "https://accounts.douban.com/j/mobile/login/request_phone_code"
        data = {
                'ck': '',
                'area_code': '+86',
                'number': '15638518680',
        }
        return url,data
def zhonggongjiaoyu():#需要进行url解密
        url = "http://www.kaoyan365.cn/index.php?m=formguide&c=forms&a=send_sms&formid=64&siteid=1&callback=jQuery183044249785972974953_1564280557736&phone=15729392171&_=1564280583517"
        data = {
                'm': 'formguide',
                'c': 'forms',
                'a': 'send_sms',
                'formid': '64',
                'siteid': '1',
                'callback': 'jQuery183044249785972974953_1564280557736',
                'phone': '15638518680',
                '_': '1564280583517',
        }
        return url, data
def ITjuzi():
        url = "https://www.itjuzi.com/api/verificationCodes"
        data = {
                'account': "15638518680"
        }
        return url, data
def dangdanghe():
        url = "http://www.dangdanghe.com/sms.php?step=getverifycode1&r=0.12788030295664465"
        data = {
                'mobile': '15638518580'
        }
        return url, data

def zhonghuayingcai():
        url = "https://passport.baidu.com/viewlog?ak=1e3f2dd1c81f2075171a547893391274&as=4b1f5626&fs=Iolr5IfSVvZ4X1g6pSGL8KBcRlbVP4NyAu9XZYdglwPW87J7DAU3kTdn7Nb7HTPl5dECDOdekZlsHn0TEXUoHyP1ZK8zFSTZmy2hkQEdEjl%2BEbFK63%2FSgqt%2BwbcG560EsKUyuUHt0dDtlWdzE%2F9Fj6lBOcGkhS%2BV7Oxbg6PLWnpwyWcMZ2XQEYjQQ%2FINjplfBn8%2BSUC4MFwA2UR%2B65Aj0zpMRdiD9Hhvgp1VT5mR4a2FC2bWHwuZUr82l3Qgdfik19OXfMEMRL4Cejl%2FSFAisz3f2mMre%2Fo2bO09oCuJQ52hQToEh6XgH2HghD%2Bo66WGo6cpllfpNXPJA5E8vGuP%2B6D1TjA3hg9fTOfOTQ7ORcPLVur2ZHU7t7XnVjGWoWc6xEp%2BUIbM0fNcpIDeGxOmJ2VqKxiw57dKmkPv2uTAzcJB8nkildoSfYkFtws0YZK3yfIKa%2BE3Dy45TzcAGZCMNTEs1UXSlt3VpqxclLrw4Eu4pDn59AFCw%2Fu4vrbDVrNMJl0MsR269DdxRrYDMNx4O4gjcrnVotmHFJv5R74HlcvKSs3L0o%2FzdozkPnBh5N3viALlsKY%2FngiqDRvxvdWq1bhaHfiZ8SyAyMfPnjrj2LpnfPonbbxVDG%2FJmPO4Oz%2BeUduvQa79XRrU0k6BarbbBjxiRl7uNqf9FU43KXBsHvGDxxKPyopxwiP2FRIXEpt2q3fC1gGB87vM%2B7kAP6okTwJy7psfZ%2B3te2ISBCbPwDOslz8Y9ND%2BX1ogRdHNXdsFD707kP%2FUhaPbC2urv5PD7lvWH2X6uEJTbgW1fi79n2cypoi5XBLJgLt002rlGrncoS0hQWISif6hXX2%2Bgm4N5%2ByqynF87Xv6gad3q3IliP6V%2FbFNsJPjK6gNJhsMmv%2BCeoMgsC57DR2SKJpHNsNFjxBITm94ujOEbl5i730pCs5%2Fynb6KG9JwlrqTqejxkExtBAwPB4cPs0X%2BhRNG77qmlYAW7yNpVbN%2Fla9nHFJjY54Qgv06%2FCimEKYTun5mNa3PO09u3htlV53WAxHBulD2foT073Nq%2FxqdY%2BwA8PetVoaCll1sU%2BsRLpDz5XijcYOqF4VsMY5VgeSPAlI%2B%2FwBsoSxcnDWrLHn%2B%2BMj7dStiHIko3Tq%2FS8uQxVCfLu7iGfMzrrBwXHUegO3jcRUH840WNQ66gUT68KS5oLKC%2BJVketgG4o11kj33AyTKXw1sHCqZYCEjDfmkIJ80bidxBmTM4Mf67tSwBhdHib1qTYTg1ceN%2BFZYCfvPbCTat2dsHRA%2FgD8ThgDGUE25xnIYrykFX0MBB0Wemr2H49YXOikWgDm9jZrptxMGcr%2BU8v4IcIL%2F8RXE8c8Th5HrzpiNAgWD2KIFgxfROrLKaM534MnqvhPjgZLN8FCRFkgv5J0myNZ&callback=jsonpCallbackb8099&v=5095"
        data = {
                'getphonestatus': '',
                'token': 'eadbf7bcc457eb042d3818cc8d650797',
                'tpl': 'bceplat',
                'apiver': 'v3',
                'tt': '1564302193486',
                'gid': 'D69FA3D-6077-40BB-8F39-178DA73878FC',
                'phone': '15729392171',
                'loginversion': 'v4',
                'countrycode': '',
                'traceid': '',
                'callback': 'bd__cbs__3xcvfl'
        }
        return url,data
def send_message():
        url,data=zhonggongjiaoyu()
        url_data = parse.urlencode(data)
        print(url_data)
        response = requests.post(url=url + url_data, data=data)
        if response.status_code==200:
                print("中公教育发送成功!")
        else:
                print("中公教育发送失败！")

        url, data = douban()
        url_data = parse.urlencode(data)
        print(url_data)
        response = requests.post(url=url, data=data)
        if response.status_code == 200:
                print("豆瓣发送成功!")
        else:
                print("豆瓣发送失败！")

        # url, data = ITjuzi()
        # url_data = parse.urlencode(data)
        # print(url_data)
        # response = requests.post(url=url, data=data)
        # if response.status_code == 200:
        #         print("发送成功!")
        # else:
        #         print("发送失败！")

        url, data = dangdanghe()
        url_data = parse.urlencode(data)
        print(url_data)
        response = requests.post(url=url, data=data)
        if response.status_code == 200:
                print("当当何发送成功!")
        else:
                print("当当何发送失败！")

        url, data = zhonghuayingcai()
        url_data = parse.urlencode(data)
        print(url_data)
        response = requests.post(url=url + url_data, data=data)
        if response.status_code == 200:
                print("中华英才发送成功!")
        else:
                print("中华英才发送失败！")

def sleeptime(hour,min,sec):
	return hour*3600 + min*60 + sec;
second = sleeptime(0,0,60);
while 1==1:
        send_message()
        time.sleep(second);

#这是隔执行一次


'''
相比1.3.1
修改时间顺序问题
'''

import requests
import json
import pytesseract
import re
import time
import random
import time
import traceback
import json
from bs4 import BeautifulSoup

from urllib.parse import urlencode
from lxml import etree
from PIL import Image

airport_dict={
'安庆': 'aqg',
'安顺': 'ava',
'阿克苏': 'aku',
'阿勒泰': 'aat',
'鞍山': 'aog',
'阿里': 'ngq',
'阿尔山': 'yie',
'阿拉善左旗': 'axf',
'阿拉善右旗': 'rht',
'北京': 'bjs',
'北京南苑': 'nay',
'北京首都': 'pek',
'北海': 'bhy',
'包头': 'bav',
'博乐': 'bpl',
'保山': 'bsd',
'百色': 'aeb',
'巴彦淖尔': 'rlk',
'毕节': 'bfj',
'白城': 'dbc',
'承德': 'cde',
'长沙': 'csx',
'常德': 'cgd',
'长春': 'cgq',
'常州': 'czx',
'朝阳': 'chg',
'赤峰': 'cif',
'长治': 'cih',
'成都': 'ctu',
'重庆': 'ckg',
'池州': 'juh',
'敦煌': 'dnh',
'大连': 'dlc',
'丹东': 'ddg',
'东营': 'doy',
'大同': 'dat',
'达州': 'dax',
'迪庆': 'dig',
'大庆': 'dqa',
'稻城': 'dcy',
'德令哈': 'hxd',
'恩施': 'enh',
'二连浩特': 'erl',
'额济纳旗': 'ejn',
'阜阳': 'fug',
'福州': 'foc',
'富蕴': 'fyn',
'佛山': 'fuo',
'抚远': 'fyj',
'广州': 'can',
'桂林': 'kwl',
'贵阳': 'kwe',
'赣州': 'kow',
'广元': 'gys',
'固原': 'gyu',
'格尔木': 'goq',
'合肥': 'hfe',
'黄山': 'txn',
'海口': 'hak',
'哈尔滨': 'hrb',
'黑河': 'hek',
'海拉尔': 'hld',
'呼和浩特': 'het',
'杭州': 'hgh',
'邯郸': 'hdg',
'淮安': 'hia',
'怀化': 'hjj',
'红原': 'ahj',
'汉中': 'hzg',
'河池': 'hcj',
'衡阳': 'hny',
'惠州': 'huz',
'嘉峪关': 'jgn',
'佳木斯': 'jmu',
'井冈山': 'jgs',
'景德镇': 'jdz',
'锦州': 'jnz',
'济南': 'tna',
'济宁': 'jng',
'鸡西': 'jxa',
'金昌': 'jic',
'揭阳': 'swa',
'加格达奇': 'jgd',
'库车': 'kca',
'库尔勒': 'krl',
'昆明': 'kmg',
'康定': 'kgt',
'克拉玛依': 'kry',
'凯里': 'kjh',
'兰州': 'lhw',
'柳州': 'lzh',
'黎平': 'hzh',
'洛阳': 'lya',
'连云港': 'lyg',
'临沂': 'lyi',
'泸州': 'lzo',
'拉萨': 'lxa',
'丽江': 'ljg',
'荔波': 'llb',
'龙岩': 'lcx',
'吕梁': 'llv',
'六盘水': 'lpf',
'临汾': 'lfq',
'临沧': 'lnj',
'牡丹江': 'mdg',
'满洲里': 'nzh',
'绵阳': 'mig',
'芒市': 'lum',
'漠河': 'ohe',
'梅州': 'mxz',
'南宁': 'nng',
'南阳': 'nny',
'南京': 'nkg',
'南通': 'ntg',
'南昌': 'khn',
'南充': 'nao',
'宁波': 'ngb',
'林芝': 'lzy',
'宁蒗': 'nlh',
'鄂尔多斯': 'dsn',
'攀枝花': 'pzi',
'普洱': 'sym',
'庆阳': 'iqn',
'秦皇岛': 'bpe',
'齐齐哈尔': 'ndg',
'青岛': 'tao',
'昌都': 'bpx',
'且末': 'iqm',
'衢州': 'juz',
'泉州': 'jjn',
'黔江': 'jiq',
'日喀则': 'rkz',
'深圳': 'szx',
'三亚': 'syx',
'石家庄': 'sjw',
'沈阳': 'she',
'上海': 'shh',
'上海虹桥': 'sha',
'上海浦东': 'pvg',
'神农架': 'hpg',
'三明': 'sqj',
'上饶': 'sqd',
'铜仁': 'ten',
'通辽': 'tgo',
'太原': 'tyn',
'天津': 'tsn',
'塔城': 'tcg',
'台州': 'hyn',
'天水': 'thq',
'腾冲': 'tcz',
'吐鲁番': 'tlq',
'通化': 'tnh',
'乌兰浩特': 'hlh',
'乌鲁木齐': 'urc',
'乌兰察布': 'ucb',
'武夷山': 'wus',
'梧州': 'wuz',
'武汉': 'wuh',
'无锡': 'wux',
'乌海': 'wua',
'威海': 'weh',
'万州': 'wxn',
'温州': 'wnz',
'厦门': 'xmn',
'兴义': 'acx',
'襄阳': 'xfn',
'徐州': 'xuz',
'锡林浩特': 'xil',
'西宁': 'xnn',
'西安': 'xiy',
'西昌': 'xic',
'西双版纳': 'jhg',
'夏河': 'gxh',
'忻州': 'wut',
'宜昌': 'yih',
'延吉': 'ynj',
'盐城': 'ynz',
'银川': 'inc',
'烟台': 'ynt',
'运城': 'ycu',
'延安': 'eny',
'榆林': 'uyn',
'宜宾': 'ybp',
'义乌': 'yiw',
'伊春': 'lds',
'扬州': 'yty',
'宜春': 'yic',
'营口': 'ykh',
'湛江': 'zha',
'珠海': 'zuh',
'郑州': 'cgo',
'张家界': 'dyg',
'昭通': 'zat',
'舟山': 'hsn',
'中卫': 'zhy',
'张掖': 'yzy',
'遵义': 'zyi',
'张家口': 'zqz',
'扎兰屯': 'nzl',
'和田市': 'htn',
'喀什市': 'khg',
'图木舒克': 'twc',
'伊宁市': 'yin',
'大理': 'dlu',
'哈密市': 'hmi',
'建三江': 'jsj',
'陇南': 'lnl',
'日照': 'riz',
'十堰': 'wds',
'松原': 'ysq',
'邵阳': 'wgn',
'信阳': 'xai',
'玉树县': 'yus',
'岳阳': 'yya',
'白山': 'nbs',
'巴中': 'bzx',
'沧源': 'cwj',
'文山市': 'wnh',
'澜沧': 'jmj',
'花土沟': 'htt',
'江门': 'jbd',
'遵义': 'wmt',
'五大连池': 'dtu',
'霍林郭勒': 'huo',
'新源': 'nlt',
'若羌': 'rqa',
'莎车': 'qsz',
'果洛': 'gmq',
'祁连': 'hbq',
'石河子': 'shf',
}

company_dict={
'HU': '海南航空',
'FU': '福州航空',
'MU': '东方航空',
'QW': '青岛航空',
'CZ': '南方航空',
'8L': '祥鹏航空',
'GS': '天津航空',
'KN': '中国联航',
'GJ': '长龙航空',
'CA': '中国国航',
'SC': '山东航空',
'G5': '华夏航空',
'ZH': '深圳航空',
'MF': '厦门航空',
'PN': '西部航空',
'3U': '四川航空',
'JR': '幸福航空',
'EU': '成都航空',
'HO': '吉祥航空',
'FM': '上海航空',
'TV': '西藏航空',
'NH': '全日空',
'KL': '荷兰皇家航空公司',
'AA': '美国航空',
'KY': '昆明航空',
'NZ': '新西兰航空公司',
'NS': '河北航空',
'AC': '加拿大航空',
'OQ': '重庆航空',
'HX': '香港航空',
'JD': '首都航空',
'CN': '大新华航空',
'QF': '澳航',
'GX': '北部湾航空',
'RY': '江西航空',
'DZ': '东海航空',
'Y8': '金鹏航空',
'UQ': '乌鲁木齐航空',
'DL': '达美航空公司',
'DR': '瑞丽航空',
'GY': '多彩航空',
'GT': '桂林航空',
'9H': '长安航空',
'A6': '红土航空',
'BK': '奥凯航空',
'9C': '春秋航空',
'JL': '日本航空',
'BA': '英国航空',
'EY': '阿联酋阿提哈德航空公司',
'AQ': '九元航空',
'SQ': '新加坡航空公司',
'LT': '龙江航空',
}



class variflight(object):

    def __init__(self):
        self.base_url = 'http://www.variflight.com' # 飞常准官网

        self.ip_pool = []                           # ip池
        file = open('pool.txt','r')
        for line in file:
            line = line.split()
            self.ip_pool.append(line[0])

        self.key =['ccc3b9d25a0f1271a5c828d0836c0a03',]


    # 结果检查
    def check(self,obj):
        if(len(obj)==0):
            return '--'
        else:
            return obj[0]

    # 时间检查
    def time_check(self,obj):
        if obj[0:2].isdigit() and obj[3:5].isdigit():
            return obj
        return '--'

    def check_time(self,obj):
        if len(obj) != 5:
            return '--'
        if obj[0].isdigit() and obj[1].isdigit() and obj[3].isdigit() and obj[4].isdigit():
            return obj
        return '--'

    # 通过url获取信息列表(航段或航班号)
    def get_mesbyurl(self, url, dt):

        result=[]
        r = requests.Session()
        while(1):
            r.proxies = {"http": "http://"+random.choice(self.ip_pool)}
            try:
                resp = r.get(url,timeout = 2)
                if(resp.status_code != 200):
                    continue
            except:
                continue
            selector = etree.HTML(resp.text)
            test = selector.xpath('//div[@class="oy_hd_shortcut"]')
            if test:
                continue
            break

        mylist = selector.xpath('//*[@id="list"]/li')
        if mylist:

            # 实际起降时间顺序
            try:
                l = re.search("b\(\d,\d\);",str(resp.text),flags=0).group()
            except:
                l=[]

            for selector in mylist:
                airline = selector.xpath('div[@class="li_com"]/span[1]/b/a/text()')     # 航班信息

                plan_up = selector.xpath('div[@class="li_com"]/span[2]/@dplan')         # 计划起飞
                depart = selector.xpath('div[@class="li_com"]/span[4]/text()')          # 出发地
                real_up = selector.xpath('div[@class="li_com"]/span[3]/img/@src')       # 实际起飞

                if real_up:
                    try:
                        url = self.base_url + real_up[0]
                        resp = r.get(url)
                        filename = './real_up.png'
                        with open(filename, 'wb') as f:
                            f.write(resp.content)
                        real_up = pytesseract.image_to_string(Image.open(filename))

                        if len(real_up) < 5:
                            real_up = real_up[:2] + ':' + real_up[2:]
                        if len(real_up) == 5:
                            real_up = real_up[:2] + ':' + real_up[3:]
                        real_up = self.time_check(real_up)
                    except:
                        traceback.print_exc(file = open('error.txt','a'))
                        real_up = '--'
                else:
                    real_up = '--'

                plan_down = selector.xpath('div[@class="li_com"]/span[5]/@aplan')       # 计划到达
                arrive = selector.xpath('div[@class="li_com"]/span[7]/text()')          # 到达地
                real_down = selector.xpath('div[@class="li_com"]/span[6]/img/@src')     # 实际到达

                if real_down:
                    try:
                        url = self.base_url + real_down[0]
                        resp = r.get(url)
                        filename = './real_down.png'
                        with open(filename, 'wb') as f:
                            f.write(resp.content)
                        real_down = pytesseract.image_to_string(Image.open(filename))

                        if len(real_down) < 5:
                            real_down = real_down[:2] + ':' + real_down[2:]
                        if len(real_down) == 5:
                            real_down = real_down[:2] + ':' + real_down[3:]
                        real_down = self.time_check(real_down)
                    except:
                        traceback.print_exc(file = open('error.txt','a'))
                        real_down = '--'
                else:
                    real_down = '--'

                state = selector.xpath('div[@class="li_com"]/span[9]/text()')           # 状态


                # 实际起降时间修正
                if(l[2] == '2'):
                    temp = real_up
                    real_up = real_down
                    real_down = temp

                real_up = self.check_time(real_up)
                real_down = self.check_time(real_down)

                if state[0] == '到达':
                    if real_up == '--':
                        real_up = plan_up[0]
                    if real_down == '--':
                        real_down = plan_down[0]
                if state[0] == '起飞':
                    if real_up == '--':
                        real_up = plan_up[0]



                ac = selector.xpath('div[@class="li_com"]/span[8]/img/@src')            # 准点率
                if ac:
                    try:
                        ac = self.base_url + ac[0]
                        filename = './ac.png'
                        q = r.get(ac)
                        with open(filename, 'wb') as t:
                            t.write(q.content)
                        ac = pytesseract.image_to_string(Image.open(filename))
                    except:
                        traceback.print_exc(file = open('error.txt','a'))
                        ac = '--'
                else:
                    ac = '--'

                detail_url = self.base_url + selector.xpath('a/@href')[0]

                mydict = {
                    # 基本信息
                    'flight_id':airline[1],                     # 航班号
                    'company':airline[0],                       # 航空公司
                    'real_flight_id':'--',                      # 实际承运航班号

                    'plan_departure_time':plan_up[0],           # 计划起飞时间 只有时间
                    'plan_arrival_time':plan_down[0],           # 计划到达时间 只有时间

                    "actual_departure_time": real_up,           # 实际起飞时间 只有时间
                    "actual_arrival_time": real_down,           # 实际到达时间 只有时间

                    'flight_status':state[0],                   # 航班状态

                    'departure':depart[0],                      # 出发地
                    'arrival':arrive[0],                        # 目的地

                    'punctuality_rate':ac,                      # 准点率

                    'check_in':'--',                            # 值机柜台
                    'boarding_port':'--',                       # 登机口
                    'arriving_port':'--',                       # 到达口
                    'Baggage_num':'--',                         # 行李转盘


                    # 航程信息
                    'length':'--',                              # 航线距离
                    'time':'--',                                # 飞行时间
                    'proc':'--',                                # 飞行进度（百分比）

                    # 飞机信息
                    'plane':'--',                               # 飞机型号
                    'age':'--',                                 # 飞机机龄
                    'forecast':'--',                            # 预计是否延误
                    'old_state':'--',                           # 前序航班状态

                    # 出发地机场信息
                    'd_weather':'--',                           # 天气
                    'd_pm':'--',                                # pm2.5
                    'd_state':'--',                             # 机场拥堵情况

                    # 目的地机场信息
                    'a_weather':'--',                           # 天气
                    'a_pm':'--',                                # pm2.5
                    'a_state':'--',                             # 机场拥堵情况

                    'datetime':dt,
                    "detail_url":detail_url,                    # 获取详细信息url
                }
                result.append(mydict)
        else:
            print("航班不存在信息")
        return result


    # 通过url获取详细信息(具体航班)
    def get_detail_mes(self,url,dt):

        result = []
        r = requests.Session()
        while(1):
            r.proxies = {"http": "http://"+random.choice(self.ip_pool)}
            try:
                resp = r.get(url,timeout = 2)
                if(resp.status_code != 200):
                    continue
            except:
                continue
            selector = etree.HTML(resp.text)
            test = selector.xpath('//div[@class="oy_hd_shortcut"]')
            if test:
                continue
            break

        BS = BeautifulSoup(resp.text,'html.parser')
        selector = etree.HTML(resp.text)
        mylist = selector.xpath('//div[@class="detail_main"]')
        if mylist:

            #基础信息
            airline = selector.xpath('//div[@class="tit"]/span[1]/b[1]/text()')
            airline_real = selector.xpath('//p[@id="order"]/a[3]/text()')   # 实际承运


            plan_up = selector.xpath('//div[@class="f_title f_title_a"]/span[1]/text()')[0].split()
            plan_down = selector.xpath('//div[@class="f_title f_title_c"]/span[1]/text()')[0].split()
            plan_up = plan_up[1][-5:]
            plan_down = plan_down[1][-5:]


            state = selector.xpath('//div[@class="state"]/div[1]/text()')

            depart = selector.xpath('//div[@class="f_title f_title_a"]/h2[1]/@title')
            arrive = selector.xpath('//div[@class="f_title f_title_c"]/h2[1]/@title')
            ac = selector.xpath('//li[@class="per"]/span[1]/img[1]/@src')

            if ac:
                try:
                    ac = self.base_url + ac[0]
                    q = r.get(ac)
                    filename = './detail_ac' + '.png'
                    with open(filename, 'wb') as t:
                        t.write(q.content)
                    ac = pytesseract.image_to_string(Image.open(filename))
                except:
                    traceback.print_exc(file = open('error.txt','a'))
                    ac = '--'
            else:
                ac = '--'

            #航线信息
            length = selector.xpath('//div[@class="p_ti"]/span[1]/text()')  # 航程距离
            time = selector.xpath('//div[@class="p_ti"]/span[2]/text()')    # 航程所需时间
            proc = selector.xpath('//div[@class="plane"]/@style')           # 航线进度

            proc = self.check(proc)
            if proc != '--':
                proc = re.split(':|%',proc)[1]

            # 飞机信息
            plane = selector.xpath('//li[@class="mileage"]/span[1]/text()') # 机型
            age = selector.xpath('//li[@class="time"]/span[1]/text()')      # 机龄
            forecast = selector.xpath('//li[@class="age"]/span[1]/text()')  # 预计是否准点
            old_state = selector.xpath('//div[@class="old_state"]/text()')  # 前序航班信息

            # 出发地机场信息
            d_weather = selector.xpath('//ul[@class="f_common rand_ul_dep"]/li[1]/p[1]/text()')[0].split()  # 天气
            d_pm = selector.xpath('//ul[@class="f_common rand_ul_dep"]/li[1]/p[2]/text()')                  # pm2.5
            d_state = selector.xpath('//ul[@class="f_common rand_ul_dep"]/li[1]/p[3]/text()')               # 机场拥堵情况
            if(len(d_weather)<3):
                d_weather = d_weather[0]
            else:
                d_weather = d_weather[0] + d_weather[1] + d_weather[2]

            # 目的地机场信息
            a_weather = selector.xpath('//ul[@class="f_common rand_ul_arr"]/li[1]/p[1]/text()')[0].split()  # 天气
            a_pm = selector.xpath('//ul[@class="f_common rand_ul_arr"]/li[1]/p[2]/text()')                  # pm2.5
            a_state = selector.xpath('//ul[@class="f_common rand_ul_arr"]/li[1]/p[3]/text()')               # 机场拥堵情况

            if(len(a_weather)<2):
                a_weather = a_weather[0]
            else:
                a_weather = a_weather[0] + a_weather[1]

            # 获取图片信息列表
            test = BS.find_all('p',class_ = 'com rand_p')
            if(len(test)>6):
                del(test[3:9])
            src_dep = selector.xpath('//ul[@class="f_common rand_ul_dep"]/li/p[2]/img/@src')
            src_arr = selector.xpath('//ul[@class="f_common rand_ul_arr"]/li/p[2]/img/@src')
            src = src_dep + src_arr
            for num in range(6):
                if(len(test[num].text.split())!=0):
                    src.insert(num,'--')

            #获取图片信息顺序
            data = str(selector.xpath('//div[@class="f_content"]/script/text()')[1])
            l1 = re.search("func\('rand_ul_dep', \d,\d,\d",data,flags=0).group().replace(' ','').split(',')
            l2 = re.search("func\('rand_ul_arr', \d,\d,\d",data,flags=0).group().replace(' ','').split(',')
            data = [l1[1],l1[2],l1[3],l2[1],l2[2],l2[3]]

            #解析图片信息
            for num in range(3):
                if(src[num]!='--'):

                    url = self.base_url + src[num]
                    resp = r.get(url)

                    if(data[num]=='1'):
                        try:
                            filename = './depart_t.png'
                            with open(filename, 'wb') as f:
                                f.write(resp.content)
                            depart_t = pytesseract.image_to_string(Image.open(filename))
                            if(len(depart_t) == 0):
                                depart_t = '--'
                        except:
                            traceback.print_exc(file = open('error.txt','a'))
                            depart_t = '--'

                    elif(data[num]=='2'):
                        try:
                            filename = './depart_s.png'
                            with open(filename, 'wb') as f:
                                f.write(resp.content)
                            depart_s = pytesseract.image_to_string(Image.open(filename))
                            if(len(depart_s) == 0):
                                depart_s = '--'
                        except:
                            traceback.print_exc(file = open('error.txt','a'))
                            depart_s = '--'

                    elif(data[num]=='3'):
                        try:
                            filename = './depart_e.png'
                            with open(filename, 'wb') as f:
                                f.write(resp.content)
                            depart_e = pytesseract.image_to_string(Image.open(filename))
                            if(len(depart_e) == 0):
                                depart_e = '--'
                        except:
                            traceback.print_exc(file = open('error.txt','a'))
                            depart_e = '--'

                else:
                    if(data[num] == '1'):
                        depart_t = '--'
                    elif(data[num] == '2'):
                        depart_s = '--'
                    elif(data[num] == '3'):
                        depart_e = '--'

            for num in range(3,6):
                if(src[num]!='--'):

                    url = self.base_url + src[num]
                    resp = r.get(url)

                    if(data[num]=='1'):
                        try:
                            filename = './arrive_t.png'
                            with open(filename, 'wb') as f:
                                f.write(resp.content)
                            arrive_t = pytesseract.image_to_string(Image.open(filename))
                            if(len(arrive_t) == 0):
                                arrive_t = '--'
                        except:
                            traceback.print_exc(file = open('error.txt','a'))
                            arrive_t = '--'

                    elif(data[num]=='2'):
                        try:
                            filename = './arrive_s.png'
                            with open(filename, 'wb') as f:
                                f.write(resp.content)
                            arrive_s = pytesseract.image_to_string(Image.open(filename))
                            if(len(arrive_s) == 0):
                                arrive_s = '--'
                        except:
                            traceback.print_exc(file = open('error.txt','a'))
                            arrive_s = '--'

                    elif(data[num]=='3'):
                        try:
                            filename = './arrive_e.png'
                            with open(filename, 'wb') as f:
                                f.write(resp.content)
                            arrive_e = pytesseract.image_to_string(Image.open(filename))
                            if(len(arrive_e) == 0):
                                arrive_e = '--'
                        except:
                            traceback.print_exc(file = open('error.txt','a'))
                            arrive_e = '--'

                else:
                    if(data[num] == '1'):
                        arrive_t = '--'
                    elif(data[num] == '2'):
                        arrive_s = '--'
                    elif(data[num] == '3'):
                        arrive_e = '--'

            airline = airline[0].split()

            mydict = {
                # 基本信息
                'flight_id':airline[1],                     # 航班号
                'company':airline[0],                       # 航空公司
                'real_flight_id': self.check(airline_real), # 实际承运航班号

                'plan_departure_time':plan_up,              # 计划起飞时间 只有时间
                'plan_arrival_time':plan_down,              # 计划到达时间 只有时间
                "actual_departure_time": depart_t,          # 实际起飞或预计起飞时间 只有时间
                "actual_arrival_time": arrive_t,            # 实际到达或预计到达时间 只有时间

                'flight_status':state[0],                   # 航班状态
                'departure':depart[0],                      # 出发地
                'arrival':arrive[0],                        # 目的地

                'punctuality_rate':ac,                      # 准点率
                'check_in':depart_s,                        # 值机柜台
                'boarding_port':depart_e,                   # 登机口
                'arriving_port':arrive_e,                   # 到达口
                'Baggage_num':arrive_s,                     # 行李转盘


                # 航程信息
                'length':self.check(length),                # 航线距离
                'time':self.check(time),                    # 飞行时间
                'proc':proc,                                # 飞行进度（百分比）

                # 飞机信息
                'plane':self.check(plane),                  # 飞机型号
                'age':self.check(age),                      # 飞机机龄
                'forecast':self.check(forecast),            # 预计是否延误
                'old_state':self.check(old_state),          # 前序航班状态

                # 出发地机场信息
                'd_weather':d_weather,                      # 天气
                'd_pm':self.check(d_pm),                    # pm2.5
                'd_state':self.check(d_state),              # 机场拥堵情况

                # 目的地机场信息
                'a_weather':a_weather,                      # 天气
                'a_pm':self.check(a_pm),                    # pm2.5
                'a_state':self.check(a_state),              # 机场拥堵情况

                'datetime':dt,
                'detail_url':'--',

                }


            result.append(mydict)
        else:
            print("航班不存在信息")
        return result


    def fix(self,obj):
        if(str(obj)=='[]'):
            return ''
        return obj

    # 快速航段信息获取
    def quick_get_mesbyurl(self,depart,arrive,dt):

        result = []

        if(depart == '北京'):
            dep = ['PEK','NAY']
        elif(depart == '上海'):
            dep = ['SHA','PVG']
        else:
            dep = [airport_dict[depart]]

        if(arrive == '北京'):
            arr = ['PEK','NAY']
        elif(arrive == '上海'):
            arr = ['SHA','PVG']
        else:
            arr = [airport_dict[arrive]]

        url = []
        for d in dep:
            for a in arr:
                url.append('http://op.juhe.cn/flight/df/fs?key=' + random.choice(self.key) + '&orgCity=' + d + '&dstCity=' + a + '&flightNo&dtype=json')

        for u in url:

            r = requests.get(u)
            js = json.loads(r.text)

            if(js['error_code'] == 10012):
                print('请求次数超限')

            if(js['reason'] != "Success"):
                continue
            for each in js['result']:

                # 生成detail_url
                detail_url = 'http://www.variflight.com/schedule/'+each['DepCode']+'-'+each['ArrCode']+'-'+each['FlightNo']+'.html?AE71649A58c77='

                if each['Rate'] == '0.00':
                    ac = '--'
                else:
                    ac = each['Rate'] + '%'

                if str(each['DepActual'])[-8:-3] == '00:00':
                    real_up = '--'
                else:
                    real_up = str(each['DepActual'])[-8:-3]

                if str(each['ArrActual'])[-8:-3] == '00:00':
                    real_down = '--'
                else:
                    real_down = str(each['ArrActual'])[-8:-3]


                # 每个航班的信息字典
                mydict = {
                    # 基本信息
                    'flight_id': each['FlightNo'],              # 航班号
                    'company':company_dict[each['FlightNo'][0:2]],
                                                                # 航空公司
                    'real_flight_id': '--',                     # 实际承运航班号

                    'plan_departure_time': str(each['DepScheduled'])[-8:-3],
                                                                # 计划起飞时间 只有时间
                    'plan_arrival_time': str(each['ArrScheduled'])[-8:-3],
                                                                # 计划到达时间 只有时间

                    "actual_departure_time": real_up,           # 实际起飞时间 只有时间
                    "actual_arrival_time": real_down,           # 实际到达时间 只有时间

                    'flight_status': each['FlightState'],       # 航班状态

                    'departure': self.fix(each['DepCity']) + self.fix(each['DepTerminal']),
                                                                # 出发地
                    'arrival': self.fix(each['ArrCity']) + self.fix(each['ArrTerminal']),
                                                                # 目的地

                    'punctuality_rate': ac,                     # 准点率

                    'check_in':'--',                            # 值机柜台
                    'boarding_port':'--',                       # 登机口
                    'arriving_port':'--',                       # 到达口
                    'Baggage_num':'--',                         # 行李转盘


                    # 航程信息
                    'length':'--',                              # 航线距离
                    'time':'--',                                # 飞行时间
                    'proc':'--',                                # 飞行进度（百分比）

                    # 飞机信息
                    'plane':'--',                               # 飞机型号
                    'age':'--',                                 # 飞机机龄
                    'forecast':'--',                            # 预计是否延误
                    'old_state':'--',                           # 前序航班状态

                    # 出发地机场信息
                    'd_weather':'--',                           # 天气
                    'd_pm':'--',                                # pm2.5
                    'd_state':'--',                             # 机场拥堵情况

                    # 目的地机场信息
                    'a_weather':'--',                           # 天气
                    'a_pm':'--',                                # pm2.5
                    'a_state':'--',                             # 机场拥堵情况

                    'datetime':dt,
                    "detail_url":detail_url,                    # 获取详细信息url
                    }
                result.append(mydict)

        return result



    '''
    通过航班号获取航班信息，返回字典列表
    参数num为航班号字符串,参数date为日期字符串,如2019-05-07
    '''
    def search_num(self,num,date):

        dt=date

        #获取今日日期
        localtime  =time.localtime(time.time())

        year = str(localtime.tm_year)
        mon = str(localtime.tm_mon)
        day = str(localtime.tm_mday)
        if(len(mon)==1):
            mon = '0' + mon
        if(len(day)==1):
            day = '0' + day

        today = year + mon + day

        #整理传入日期格式
        date=date.split('-')
        date=date[0]+date[1]+date[2]

        #获取当天信息
        if(int(date)==int(today)):
            url = 'http://www.variflight.com/flight/fnum/' + num + '.html?AE71649A58c77'

        #获取历史信息
        if(int(date)<int(today)):
            url = 'http://www.variflight.com/flight/fnum/' + num + '.html?AE71649A58c77&fdate=' + date

        return self.get_mesbyurl(url,dt)


    '''
    通过其降地获取航班信息，返回字典列表
    参数depart为出发城市字符串,参数arrive为到达城市字符串,参数date为日期字符串,如2019-05-07
    '''
    def search_seg(self,depart,arrive,date):

        dt=date

        #获取今日日期
        localtime  =time.localtime(time.time())

        year = str(localtime.tm_year)
        mon = str(localtime.tm_mon)
        day = str(localtime.tm_mday)
        if(len(mon)==1):
            mon = '0' + mon
        if(len(day)==1):
            day = '0' + day

        today = year + mon + day

        #整理传入日期格式
        date=date.split('-')
        date=date[0]+date[1]+date[2]

        #获取当天信息
        if(int(date)==int(today)):

            # api快速访问
            #return self.quick_get_mesbyurl(depart,arrive,dt)

            url = 'http://www.variflight.com/flight/' + airport_dict[depart] + '-' + airport_dict[arrive] + '.html?AE71649A58c77'

        #获取历史信息
        if(int(date)<int(today)):
            url = 'http://www.variflight.com/flight/' + airport_dict[depart] + '-' + airport_dict[arrive] + '.html?AE71649A58c77&fdate=' + date

        return self.get_mesbyurl(url,dt)



def main():
    # 初始化
    vf = variflight()

    # api快速访问查找
    #l1 = vf.quick_get_mesbyurl('包头','大连','2019-06-03')
    #print(json.dumps(l1,indent=2,ensure_ascii=False))

    # 通过航班号查询，返回字典列表
    l1=vf.search_num('ca1121','2019-06-03')
    print(json.dumps(l1,indent=2,ensure_ascii=False))

    # 通过起降地查询，返回字典列表
    #l2=vf.search_seg('北京首都','上海浦东','2019-05-24')
    #print(json.dumps(l2,indent=2,ensure_ascii=False))

    # 通过detai_url查询详细信息，返回字典列表,列表只有一个元素
    #l3=vf.get_detail_mes('http://www.variflight.com/schedule/BHY-CSX-CZ3147.html?AE71649A58c77=&fdate=20190527','2019-05-20')
    #print(json.dumps(l3,indent=2,ensure_ascii=False))
    
if __name__ == '__main__':
    main()

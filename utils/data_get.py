import requests
import json
import pytesseract
import re
import time
import random
import time
from bs4 import BeautifulSoup

from urllib.parse import urlencode
from lxml import etree
from PIL import Image

airport_dict = {
    '哈尔滨': 'HRB',
    '齐齐哈尔': 'NDG',
    '牡丹江': 'MDG',
    '伊春': 'LDS',
    '佳木斯': 'JMU',
    '鸡西': 'JXA',
    '黑河': 'HEK',
    '漠河': 'OHE',
    '依兰': 'YLN',
    '大庆': 'DQA',
    '长春': 'CGQ',
    '延吉': 'YNJ',
    '吉林': 'JIL',
    '大连': 'DLC',
    '沈阳': 'SHE',
    '锦州': 'JNZ',
    '丹东': 'DDG',
    '朝阳': 'CHG',
    '鞍山': 'IOB',
    '长海': 'CNI',
    '呼和浩特': 'HET',
    '包头': 'BAV',
    '乌兰浩特': 'HLH',
    '海拉尔': 'HLD',
    '锡林浩特': 'XIL',
    '赤峰': 'CIF',
    '通辽': 'TGO',
    '乌海': 'WUA',
    '满洲里': 'NZH',
    '鄂尔多斯': 'DSN',
    '北京首都': 'PEK',
    '北京南苑': 'NAY',
    '天津': 'TSN',
    '石家庄': 'SJW',
    '秦皇岛': 'SHP',
    '邯郸': 'HDG',
    '太原': 'TYN',
    '大同': 'DAT',
    '长治': 'CIH',
    '运城': 'YCU',
    '郑州': 'CGO',
    '洛阳': 'LYA',
    '南阳': 'NNY',
    '安阳': 'AYN',
    '武汉': 'WUH',
    '荆州': 'SHS',
    '襄樊': 'XFN',
    '宜昌': 'YIH',
    '恩施': 'ENH',
    '张家界': 'DYG',
    '长沙': 'CSX',
    '常德': 'CGD',
    '芷江': 'HJJ',
    '衡阳': 'HNY',
    '怀化': 'HJJ',
    '永州': 'LLF',
    '广州': 'CAN',
    '梅县': 'MXZ',
    '珠海': 'ZUH',
    '揭阳': 'SWA',
    '深圳': 'SZX',
    '湛江': 'ZHA',
    '惠州': 'HUZ',
    '佛山': 'ZCP',
    '兴宁': 'XIN',
    '海口': 'HAK',
    '三亚': 'SYX',
    '南宁': 'NNG',
    '桂林': 'KWL',
    '北海': 'BHY',
    '柳州': 'LZH',
    '梧州': 'YUZ',
    '百色': 'AEB',
    '济南': 'TNA',
    '威海': 'WEH',
    '青岛': 'TAO',
    '潍坊': 'WEF',
    '烟台': 'YNT',
    '临沂': 'LYI',
    '泗水': 'SUB',
    '济宁': 'JNG',
    '东营': 'DOY',
    '南昌': 'KHN',
    '九江': 'JIU',
    '景德镇': 'JDZ',
    '赣州': 'KOW',
    '井冈山': 'JGS',
    '黄山': 'TXN',
    '合肥': 'HFE',
    '安庆': 'AQG',
    '阜阳': 'FUG',
    '杭州': 'HGH',
    '温州': 'WNZ',
    '舟山': 'HSN',
    '宁波': 'NGB',
    '义乌': 'YIW',
    '台州': 'HYN',
    '衢州': 'JUZ',
    '南京': 'NKG',
    '徐州': 'XUZ',
    '连云港': 'LYG',
    '盐城': 'YNZ',
    '常州': 'CZX',
    '南通': 'NTG',
    '无锡': 'WUX',
    '上海虹桥': 'SHA',
    '上海浦东': 'PVG',
    '厦门': 'XMN',
    '福州': 'FOC',
    '晋江': 'JJN',
    '武夷山': 'WUS',
    '连城': 'LCX',
    '昆明': 'KMG',
    '丽江': 'LJG',
    '西双版纳': 'JHG',
    '香格里拉': 'DIG',
    '大理': 'DLU',
    '芒市': 'LUM',
    '迪庆': 'DIG',
    '思茅': 'SYM',
    '保山': 'BSD',
    '昭通': 'ZAT',
    '临沧': 'LNJ',
    '元谋': 'YUA',
    '拉萨': 'LXA',
    '昌都': 'BPX',
    '林芝': 'LZY',
    '成都': 'CTU',
    '绵阳': 'MIG',
    '宜宾': 'YBP',
    '泸州': 'LZO',
    '九寨沟': 'JZH',
    '攀枝花': 'PZI',
    '西昌': 'XIC',
    '达州': 'DAX',
    '南充': 'NAO',
    '广汉': 'GHN',
    '广元': 'GYS',
    '康定': 'KGT',
    '重庆': 'CKG',
    '万州': 'WXN',
    '万县': 'LIA',
    '贵阳': 'KWE',
    '铜仁': 'TEN',
    '遵义': 'ZYI',
    '安顺': 'AVA',
    '兴义': 'ACX',
    '西安': 'SIA',
    '汉中': 'HZG',
    '延安': 'ENY',
    '安康': 'AKA',
    '榆林': 'UYN',
    '兰州': 'LHW',
    '天水': 'THQ',
    '敦煌': 'DNH',
    '嘉峪关': 'JGN',
    '庆阳': 'IQN',
    '酒泉': 'CHW',
    '西宁': 'XNN',
    '格尔木': 'GOQ',
    '玉树': 'LDS',
    '银川': 'INC',
    '乌鲁木齐': 'URC',
    '和田': 'HTN',
    '伊宁': 'YIN',
    '克拉玛依': 'KRY',
    '塔城': 'TCG',
    '阿勒泰': 'AAT',
    '阿克苏': 'AKU',
    '库尔勒': 'KRL',
    '库车': 'KCA',
    '喀什': 'KHG',
    '且末': 'IQM',
    '哈密': 'HMI',
    '富蕴': 'FYN',
    '那拉提': 'NLT',

    # 双机场城市
    '北京': 'BJS',
    '上海': 'SHH'
}


class variflight(object):

    def __init__(self):
        self.base_url = 'http://www.variflight.com'  # 飞常准官网
        self.num_list = []  # 航班列表
        self.seg_list = []  # 航段列表

    def check(self, obj):
        if (len(obj) == 0):
            return '--'
        else:
            return obj[0]

            # 通过url获取信息列表(航段或航班号)

    def get_mesbyurl(self, url, dt):
        result = []
        r = requests.Session()
        resp = r.get(url)
        selector = etree.HTML(resp.text)
        mylist = selector.xpath('//*[@id="list"]/li')
        if mylist:
            for selector in mylist:
                airline = selector.xpath('div[@class="li_com"]/span[1]/b/a/text()')  # 航班信息

                plan_up = selector.xpath('div[@class="li_com"]/span[2]/@dplan')  # 计划起飞
                depart = selector.xpath('div[@class="li_com"]/span[4]/text()')  # 出发地
                real_up = selector.xpath('div[@class="li_com"]/span[3]/img/@src')  # 实际起飞

                if real_up:
                    url = self.base_url + real_up[0]
                    resp = r.get(url)
                    filename = './real_up.png'
                    with open(filename, 'wb') as f:
                        f.write(resp.content)
                    real_up = pytesseract.image_to_string(Image.open(filename))

                    if len(real_up) < 5:
                        real_up = real_up[:2] + ':' + real_up[2:]
                else:
                    real_up = '--'

                plan_down = selector.xpath('div[@class="li_com"]/span[5]/@aplan')  # 计划到达
                arrive = selector.xpath('div[@class="li_com"]/span[7]/text()')  # 到达地
                real_down = selector.xpath('div[@class="li_com"]/span[6]/img/@src')  # 实际到达

                if real_down:
                    url = self.base_url + real_down[0]
                    resp = r.get(url)
                    filename = './real_down.png'
                    with open(filename, 'wb') as f:
                        f.write(resp.content)
                    real_down = pytesseract.image_to_string(Image.open(filename))
                    if len(real_down) < 5:
                        real_down = real_down[:2] + ':' + real_down[2:]
                else:
                    real_down = '--'

                state = selector.xpath('div[@class="li_com"]/span[9]/text()')  # 状态
                ac = selector.xpath('div[@class="li_com"]/span[8]/img/@src')  # 准点率

                if ac:
                    ac = self.base_url + ac[0]
                    filename = './ac.png'
                    q = r.get(ac)
                    with open(filename, 'wb') as t:
                        t.write(q.content)
                    ac = pytesseract.image_to_string(Image.open(filename))
                else:
                    ac = '--'

                # 待修复bug
                if state[0] == '起飞' and real_down != '--':
                    real_up = real_down
                    real_down = '--'
                #

                detail_url = self.base_url + selector.xpath('a/@href')[0]

                mydict = {
                    # 基本信息
                    'flight_id': airline[1],  # 航班号
                    'company': airline[0],  # 航空公司
                    'real_flight_id': '--',  # 实际承运航班号

                    'plan_departure_time': plan_up[0],  # 计划起飞时间 只有时间
                    'plan_arrival_time': plan_down[0],  # 计划到达时间 只有时间

                    "actual_departure_time": real_up,  # 实际起飞时间 只有时间
                    "actual_arrival_time": real_down,  # 实际到达时间 只有时间

                    'flight_status': state[0],  # 航班状态

                    'departure': depart[0],  # 出发地
                    'arrival': arrive[0],  # 目的地

                    'punctuality_rate': ac,  # 准点率

                    'check_in': '--',  # 值机柜台
                    'boarding_port': '--',  # 登机口
                    'arriving_port': '--',  # 到达口
                    'Baggage_num': '--',  # 行李转盘

                    # 航程信息
                    'length': '--',  # 航线距离
                    'time': '--',  # 飞行时间
                    'proc': '--',  # 飞行进度（百分比）

                    # 飞机信息
                    'plane': '--',  # 飞机型号
                    'age': '--',  # 飞机机龄
                    'forecast': '--',  # 预计是否延误
                    'old_state': '--',  # 前序航班状态

                    # 出发地机场信息
                    'd_weather': '--',  # 天气
                    'd_pm': '--',  # pm2.5
                    'd_state': '--',  # 机场拥堵情况

                    # 目的地机场信息
                    'a_weather': '--',  # 天气
                    'a_pm': '--',  # pm2.5
                    'a_state': '--',  # 机场拥堵情况

                    'datetime': dt,
                    "detail_url": detail_url,  # 获取详细信息url
                }
                result.append(mydict)
        else:
            print("航班不存在信息")
        return result

    # 通过url获取详细信息(具体航班)
    def get_detail_mes(self, url, dt):
        result = []
        r = requests.Session()
        req = r.get(url)
        BS = BeautifulSoup(req.text, 'html.parser')
        selector = etree.HTML(req.text)
        mylist = selector.xpath('//div[@class="detail_main"]')
        if mylist:

            # 基础信息
            airline = selector.xpath('//div[@class="tit"]/span[1]/b[1]/text()')
            airline_real = selector.xpath('//p[@id="order"]/a[3]/text()')  # 实际承运

            plan_up = selector.xpath('//div[@class="f_title f_title_a"]/span[1]/text()')[0].split()
            plan_down = selector.xpath('//div[@class="f_title f_title_c"]/span[1]/text()')[0].split()
            plan_up = plan_up[1][-5:]
            plan_down = plan_down[1][-5:]

            state = selector.xpath('//div[@class="state"]/div[1]/text()')

            depart = selector.xpath('//div[@class="f_title f_title_a"]/h2[1]/@title')
            arrive = selector.xpath('//div[@class="f_title f_title_c"]/h2[1]/@title')
            ac = selector.xpath('//li[@class="per"]/span[1]/img[1]/@src')

            if ac:
                ac = self.base_url + ac[0]
                q = r.get(ac)
                filename = './detail_ac' + '.png'
                with open(filename, 'wb') as t:
                    t.write(q.content)
                ac = pytesseract.image_to_string(Image.open(filename))
            else:
                ac = '--'

            # 航线信息
            length = selector.xpath('//div[@class="p_ti"]/span[1]/text()')  # 航程距离
            time = selector.xpath('//div[@class="p_ti"]/span[2]/text()')  # 航程所需时间
            proc = selector.xpath('//div[@class="plane"]/@style')  # 航线进度

            proc = self.check(proc)
            if proc != '--':
                proc = re.split(':|%', proc)[1]

            # 飞机信息
            plane = selector.xpath('//li[@class="mileage"]/span[1]/text()')  # 机型
            age = selector.xpath('//li[@class="time"]/span[1]/text()')  # 机龄
            forecast = selector.xpath('//li[@class="age"]/span[1]/text()')  # 预计是否准点
            old_state = selector.xpath('//div[@class="old_state"]/text()')  # 前序航班信息

            # 出发地机场信息
            d_weather = selector.xpath('//ul[@class="f_common rand_ul_dep"]/li[1]/p[1]/text()')[0].split()  # 天气
            d_pm = selector.xpath('//ul[@class="f_common rand_ul_dep"]/li[1]/p[2]/text()')  # pm2.5
            d_state = selector.xpath('//ul[@class="f_common rand_ul_dep"]/li[1]/p[3]/text()')  # 机场拥堵情况
            if (len(d_weather) < 3):
                d_weather = d_weather[0]
            else:
                d_weather = d_weather[0] + d_weather[1] + d_weather[2]

            # 目的地机场信息
            a_weather = selector.xpath('//ul[@class="f_common rand_ul_arr"]/li[1]/p[1]/text()')[0].split()  # 天气
            a_pm = selector.xpath('//ul[@class="f_common rand_ul_arr"]/li[1]/p[2]/text()')  # pm2.5
            a_state = selector.xpath('//ul[@class="f_common rand_ul_arr"]/li[1]/p[3]/text()')  # 机场拥堵情况

            if (len(a_weather) < 2):
                a_weather = a_weather[0]
            else:
                a_weather = a_weather[0] + a_weather[1]

            # 获取图片信息列表
            src = selector.xpath('//p[@class="com rand_p"]/img[1]/@src')
            test = BS.find_all('p', class_='com rand_p')
            for num in range(6):
                if (len(test[num].text.split()) != 0):
                    src.insert(num, '--')

            # 获取图片信息顺序
            data = str(selector.xpath('//div[@class="f_content"]/script/text()')[1])
            l1 = re.search("func\('rand_ul_dep', \d,\d,\d", data, flags=0).group().replace(' ', '').split(',')
            l2 = re.search("func\('rand_ul_arr', \d,\d,\d", data, flags=0).group().replace(' ', '').split(',')
            data = [l1[1], l1[2], l1[3], l2[1], l2[2], l2[3]]

            # 解析图片信息
            for num in range(3):
                if (src[num] != '--'):

                    url = self.base_url + src[num]
                    resp = r.get(url)

                    if (data[num] == '1'):
                        filename = './depart_t.png'
                        with open(filename, 'wb') as f:
                            f.write(resp.content)
                        depart_t = pytesseract.image_to_string(Image.open(filename))
                        if (len(depart_t) == 0):
                            depart_t = '--'

                    elif (data[num] == '2'):
                        filename = './depart_s.png'
                        with open(filename, 'wb') as f:
                            f.write(resp.content)
                        depart_s = pytesseract.image_to_string(Image.open(filename))
                        if (len(depart_s) == 0):
                            depart_s = '--'

                    elif (data[num] == '3'):
                        filename = './depart_e.png'
                        with open(filename, 'wb') as f:
                            f.write(resp.content)
                        depart_e = pytesseract.image_to_string(Image.open(filename))
                        if (len(depart_e) == 0):
                            depart_e = '--'

                else:
                    if (data[num] == '1'):
                        depart_t = '--'
                    elif (data[num] == '2'):
                        depart_s = '--'
                    elif (data[num] == '3'):
                        depart_e = '--'

            for num in range(3, 6):
                if (src[num] != '--'):

                    url = self.base_url + src[num]
                    resp = r.get(url)

                    if (data[num] == '1'):

                        filename = './arrive_t.png'
                        with open(filename, 'wb') as f:
                            f.write(resp.content)
                        arrive_t = pytesseract.image_to_string(Image.open(filename))
                        if (len(arrive_t) == 0):
                            arrive_t = '--'

                    elif (data[num] == '2'):
                        filename = './arrive_s.png'
                        with open(filename, 'wb') as f:
                            f.write(resp.content)
                        arrive_s = pytesseract.image_to_string(Image.open(filename))
                        if (len(arrive_s) == 0):
                            arrive_s = '--'

                    elif (data[num] == '3'):
                        filename = './arrive_e.png'
                        with open(filename, 'wb') as f:
                            f.write(resp.content)
                        arrive_e = pytesseract.image_to_string(Image.open(filename))
                        if (len(arrive_e) == 0):
                            arrive_s = '--'

                else:
                    if (data[num] == '1'):
                        arrive_t = '--'
                    elif (data[num] == '2'):
                        arrive_s = '--'
                    elif (data[num] == '3'):
                        arrive_e = '--'

            airline = airline[0].split()

            mydict = {
                # 基本信息
                'flight_id': airline[1],  # 航班号
                'company': airline[0],  # 航空公司
                'real_flight_id': self.check(airline_real),  # 实际承运航班号

                'plan_departure_time': plan_up,  # 计划起飞时间 只有时间
                'plan_arrival_time': plan_down,  # 计划到达时间 只有时间
                "actual_departure_time": depart_t,  # 实际起飞或预计起飞时间 只有时间
                "actual_arrival_time": arrive_t,  # 实际到达或预计到达时间 只有时间

                'flight_status': state[0],  # 航班状态
                'departure': depart[0],  # 出发地
                'arrival': arrive[0],  # 目的地

                'punctuality_rate': ac,  # 准点率
                'check_in': depart_s,  # 值机柜台
                'boarding_port': depart_e,  # 登机口
                'arriving_port': arrive_e,  # 到达口
                'Baggage_num': arrive_s,  # 行李转盘

                # 航程信息
                'length': self.check(length),  # 航线距离
                'time': self.check(time),  # 飞行时间
                'proc': proc,  # 飞行进度（百分比）

                # 飞机信息
                'plane': self.check(plane),  # 飞机型号
                'age': self.check(age),  # 飞机机龄
                'forecast': self.check(forecast),  # 预计是否延误
                'old_state': self.check(old_state),  # 前序航班状态

                # 出发地机场信息
                'd_weather': d_weather,  # 天气
                'd_pm': self.check(d_pm),  # pm2.5
                'd_state': self.check(d_state),  # 机场拥堵情况

                # 目的地机场信息
                'a_weather': a_weather,  # 天气
                'a_pm': self.check(a_pm),  # pm2.5
                'a_state': self.check(a_state),  # 机场拥堵情况

                'datetime': dt,
                'detail_url': '--',

            }

            result.append(mydict)
        else:
            print("航班不存在信息")

        return result

    '''
    通过航班号获取航班信息，返回字典列表
    参数num为航班号字符串,参数date为日期字符串,如2019-05-07
    '''

    def search_num(self, num, date):

        dt = date

        # 获取今日日期
        localtime = time.localtime(time.time())

        year = str(localtime.tm_year)
        mon = str(localtime.tm_mon)
        day = str(localtime.tm_mday)
        if (len(mon) == 1):
            mon = '0' + mon
        if (len(day) == 1):
            day = '0' + day

        today = year + mon + day

        # 整理传入日期格式
        date = date.split('-')
        date = date[0] + date[1] + date[2]

        # 获取当天信息
        if (int(date) == int(today)):
            url = 'http://www.variflight.com/flight/fnum/' + num + '.html?AE71649A58c77'

        # 获取历史信息
        if (int(date) < int(today)):
            url = 'http://www.variflight.com/flight/fnum/' + num + '.html?AE71649A58c77&fdate=' + date

        return self.get_mesbyurl(url, dt)

    '''
    通过其降地获取航班信息，返回字典列表
    参数depart为出发城市字符串,参数arrive为到达城市字符串,参数date为日期字符串,如2019-05-07
    '''

    def search_seg(self, depart, arrive, date):

        dt = date

        # 获取今日日期
        localtime = time.localtime(time.time())

        year = str(localtime.tm_year)
        mon = str(localtime.tm_mon)
        day = str(localtime.tm_mday)
        if (len(mon) == 1):
            mon = '0' + mon
        if (len(day) == 1):
            day = '0' + day

        today = year + mon + day

        # 整理传入日期格式
        date = date.split('-')
        date = date[0] + date[1] + date[2]

        # 获取当天信息
        if (int(date) == int(today)):
            url = 'http://www.variflight.com/flight/' + airport_dict[depart] + '-' + airport_dict[
                arrive] + '.html?AE71649A58c77'

        # 获取历史信息
        if (int(date) < int(today)):
            url = 'http://www.variflight.com/flight/' + airport_dict[depart] + '-' + airport_dict[
                arrive] + '.html?AE71649A58c77&fdate=' + date

        return self.get_mesbyurl(url, dt)


def main():
    # 初始化
    vf = variflight()

    # 通过航班号查询，返回字典列表
    # l1=vf.search_num('CA1151','2019-05-05')
    # print(json.dumps(l1,indent=2,ensure_ascii=False))

    # 通过起降地查询，返回字典列表
    # l2=vf.search_seg('北京','上海')
    # print(json.dumps(l2,indent=2,ensure_ascii=False))

    # 通过detai_url查询详细信息，返回字典列表,列表只有一个元素
    l3 = vf.get_detail_mes('http://www.variflight.com/schedule/PEK-HKG-CA111.html?AE71649A58c77=&fdate=20190513',
                           '2019-05-13')
    print(json.dumps(l3, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()

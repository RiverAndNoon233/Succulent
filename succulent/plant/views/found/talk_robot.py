import json
import urllib.parse as up
import urllib.request as ur

class Talk_robot(object):
    def __init__(self):
        self.url=r'http://www.tuling123.com/openapi/api'
        self.headers={
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        }

    def talk(self,str_words,user_id):
        values = {
            'key': 'a8ee170cf15346d8a22bfc52804a61cc',
            'info': str_words,
            'userid': str(user_id)
        }
        #将要传送给json的数据打包
        post_data = up.urlencode(values).encode('utf-8')
        #设置请求头
        request = ur.Request(self.url, data=post_data, headers=self.headers)
        #得到响应对象
        res = ur.urlopen(request)
        #根据响应对象得到返回的数据字符串
        string_html = res.read().decode('utf-8')
        #对字符串进行json解析
        json_data = json.loads(string_html)
        #得到返回json的机器人所说的话
        robot_words=json_data['text']
        #返回机器人所说的话
        return robot_words

# t=Talk_robot()
# str_words=t.talk('雾霾','w123')
# print(str_words)
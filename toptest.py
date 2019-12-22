# encoding: utf-8

from PIL import Image
from aip import AipOcr
import os
import webbrowser


def pull_screenshot():
    # 安装adb，配置好环境变量截屏
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png .')
    img = Image.open("./screenshot.png")
    # 拿到问题区域和答案区域
    # 自己多调一调参数，顺序是左 上 右 下
    question = img.crop((50, 380, 1000, 620))
    choices = img.crop((75, 600, 990, 1350))
    return question, choices


class Baiduaip(object):
    def __init__(self):
        # 找到自己创建的应用的信息并填上来
        APPID = '*****'
        APIKey = '***************'
        SecretKey = '***************'
        self.client = AipOcr(APPID,APIKey,SecretKey)
    def getText(self):
        question, choices = pull_screenshot()
        # img进行编码的时候总是出错，干脆保存成新的图
        question.save('question.png')
        with open('question.png', 'rb') as i:
            text = self.client.basicGeneral(i.read())
            # print(text)
            words_list=text["words_result"]
            for i in words_list:
                word=i["words"]
                return word

def run():
    baidu_aip=Baiduaip()
    words = baidu_aip.getText()
    webbrowser.open('https://baidu.com/s?wd=' + words)


if __name__ == '__main__':
    run()

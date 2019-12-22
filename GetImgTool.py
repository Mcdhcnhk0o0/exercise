# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/9 00:40
# @desc    : adb 获取截屏，截取图片


from PIL import Image
import os
import matplotlib.pyplot as plt

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png .')

pull_screenshot()
img = Image.open("./screenshot.png")

question  = img.crop((50, 380, 1000, 620))
choices = img.crop((75, 600, 990, 1350))

plt.subplot(221)
im = plt.imshow(img, animated=True)
plt.subplot(222)
im2 = plt.imshow(question, animated=True)
plt.subplot(212)
im3 = plt.imshow(choices, animated=True)
plt.show()

#!/usr/bin/env python3

import pynput
import os
import threading
import time
import urllib.request

class YGlobal(object):
    mouse_controller_ = pynput.mouse.Controller()
    key_map = {}
    count = 0
    flag = True

def ReDraw():
    YGlobal.flag = False
    res = sorted(YGlobal.key_map.items(),key = lambda x:x[1],reverse = True)
    os.system("cls")
    print('total: {} times.'.format(YGlobal.count))
    for i in res:
        print('{percent:>5.2f}%{times:>6}times:\t\t{key}'.format(percent = i[1]*100/YGlobal.count, times = i[1], key = i[0]))
    time.sleep(0.1)
    YGlobal.flag = True

def Send(key):
    req = urllib.request.Request('http://{}:{}/get_key_statistics?i={}&v={}'.format(YGlobal.args.domain, YGlobal.args.port, "", key))
    res = urllib.request.urlopen(req).read()
    #print(res.decode('utf-8'))

def OnRelease(key):
    key = '{}'.format(key)
    if key in YGlobal.key_map:
        YGlobal.key_map[key] = YGlobal.key_map[key] + 1
    else:
        YGlobal.key_map[key] = 1
    YGlobal.count = YGlobal.count + 1
    if YGlobal.flag:
        threading.Timer(0, ReDraw).start()
    if YGlobal.args.send:
        threading.Timer(0, Send, (key, )).start()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default='80', action='store',
        help='set the port')
    parser.add_argument('-d', '--domain', default='localhost', action='store',
        help='set the domain')
    parser.add_argument('-s', '--send', action='store_true',
        help='send info to service')
    YGlobal.args = parser.parse_args()
    with pynput.keyboard.Listener(on_release = OnRelease) as listener:
        listener.join()


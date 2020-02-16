#!/usr/bin/env python3

import pynput
import json
import os
class YGlobal(object):
    mouse_controller_ = pynput.mouse.Controller()
    key_map = {}
    count = 0
    redraw = 5

def OnRelease(key):
    key = '{}'.format(key)
    if key in YGlobal.key_map:
        YGlobal.key_map[key] = YGlobal.key_map[key] + 1
    else:
        YGlobal.key_map[key] = 1
    YGlobal.count = YGlobal.count + 1
    if YGlobal.count % YGlobal.redraw == 0:
        res = sorted(YGlobal.key_map.items(),key = lambda x:x[1],reverse = True)
        os.system("cls")
        print('total: {} times.'.format(YGlobal.count))
        for i in res:
            print('{percent:>5.2f}%{times:>6}times:\t\t{key}'.format(percent = i[1]*100/YGlobal.count, times = i[1], key = i[0]))
            

with pynput.keyboard.Listener(on_release = OnRelease) as listener:
    listener.join()

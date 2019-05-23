#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/5/22/0022 10:58

@author: ZMJ

@file: feed_recommend.py

'''

import requests

# uid_devId = {
#     '7afb177ff48541f790bdc1523a46ca15':'06B9F971-FAF3-432F-B207-6C7431144298',
#     '4fab3d323e604a13ae910dd589f97759':'e201c66648424919bbd8f0818ce52ff1',
#     'ea7c010cef734d04bf6a9d733bf4cda3':'06B9F971-FAF3-432F-B207-6C7431144298',
#     '8a31dd47393c41628082dd9659011cfe':'9F20C655-AF71-4C00-8796-03F0D616E617',
#     '478a7bbf4cfc44a1b03587f3b375d8ff':'C06FE2FF-B35D-4D8B-B8C0-B3E951E0E99E',
#     'f468b764bdff41359ab0d0631569cafc':'f468b764bdff41359ab0d0631569cafc'
# }

uid_devId = {
    'a7aee4dc4df94e0eb2e5af75b6aeae1c':'BFBE61D0-4D9B-4385-AA68-F61D21209650',
    '43b293a47b394464b62e589a1807f571':'9e6d4474a5a446a1a5a55feff1c2a9ff',
    '161735e5f8074f8f98c640f49aab850d':'BFBE61D0-4D9B-4385-AA68-F61D21209650',
    'b2531a69d7fa49e08e6f084df6beabc0':'9F20C655-AF71-4C00-8796-03F0D616E617',
    '0765cde275e340f285a37f9b9fd396cf':'BFBE61D0-4D9B-4385-AA68-F61D21209650',
    '710770994dac4a298c44f0a4ee8799dc':'BFBE61D0-4D9B-4385-AA68-F61D21209650'
}

def req_feed_recommend():
    for uid in uid_devId:
        deviceId = uid_devId.get(uid)
        url = 'http://10.202.32.6:8000/feed_recommend/deviceId/%s/uid/%s' % (deviceId, uid)
        req = requests.get(url=url)
        print(uid, deviceId, '执行完毕')

if __name__ == '__main__':
    for count in range(10):
        req_feed_recommend()
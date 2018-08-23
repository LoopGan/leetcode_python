#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/23/2018 4:21 PM
"""
import pandas as pd
import subprocess
import re


def ping_test(filename):
    df = pd.read_csv(filename)
    ips = df['Management IP']
    status = []
    for ip in ips:
        result = subprocess.Popen('ping %s -n 1' % ip, stdout=subprocess.PIPE)
        tmp_info = result.stdout.read().decode('utf-8')
        tmp_status = re.search('timed out', tmp_info)
        if tmp_status:
            print(ip, 'Not OK')
            status.append('Not OK')
        else:
            print(ip, 'OK')
            status.append('OK')
    df.insert(df.shape[1], 'status', status)
    df.to_csv('./result.csv', sep='\t')


if __name__ == "__main__":
    filename = 'C://Users//ganw//Documents//EMC//report_export.csv'
    ping_test(filename)
    print("hello imp")

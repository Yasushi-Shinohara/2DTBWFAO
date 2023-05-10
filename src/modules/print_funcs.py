#!/usr/bin/python
# coding: UTF-8
# This is created 2022/10/14 by Y. Shinohara
# This is lastly modified 2022/10/14 by Y. Shinohara
import time
import sys

def print_header():
    print(time.strftime("# Started at %a, %d %b %Y %H:%M:%S %z %Z",time.localtime()))
    print('# ===========================')
    print('# Python version: ',sys.version.replace('\n',' '))
    print('# API version: ',sys.api_version)
    print('# Platform: ',sys.platform)
    #print('Flags: ',sys.flags)
    #print('Copyright: ',sys.copyright)
    print('# ===========================')
    import numpy as np
    print('# numpy version: ',np.__version__)
    #np.show_config()
    print('# ===========================')
    import math
    #import time as timemod #To avoid overlap to "time" in real-time propagation part
    import ctypes as ct
    print('# ctypes version: ',ct.__version__)
    print('# ===========================')
#
def print_footer():
    print('# ===========================')
    print(time.strftime("# Ended at %a, %d %b %Y %H:%M:%S %z %Z",time.localtime()))
#
def print_midtime(ts,tt):
    print('# Elapse time for preparation: ', tt - ts, ' [sec]')
    print('# Preparaiton is done')
#
def print_endtime(ts,tt,te,Nt):
    print('# Elapse time for RT: ', te - tt, ' [sec] = ', (te - tt)/60.0, ' [min] = ', (te - tt)/3600, ' [hour]')
    print('# RT time per an iteration: ', (te - tt)/float(Nt), ' [sec] = ', (te - tt)/float(Nt)/60.0, ' [min]')
    print('# Total elapse time: ', te - ts, ' [sec] = ', (te - ts)/60.0, ' [min] = ', (te - ts)/3600, ' [hour]')


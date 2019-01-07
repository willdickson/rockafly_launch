#!/usr/bin/env python
from __future__ import print_function
import sys
import time
import scipy
import rospy

import std_msgs.msg
from autostep_proxy import AutostepProxy
from autostep_ros.msg import TrackingData

print()
print('* sinusoid example')
print()

jog_params = {'speed': 200, 'accel': 500, 'decel': 500}
max_params = {'speed': 1000, 'accel': 10000, 'decel': 10000}
amplitude_list = [40, 80, 100]

autostep = AutostepProxy()

autostep.set_jog_mode_params(jog_params)
print('  jog params = {}'.format(autostep.get_jog_mode_params()))

autostep.set_max_mode_params(max_params)
print('  max params = {}'.format(autostep.get_max_mode_params()))
print()

for amplitude in amplitude_list:
    print('  amplitude = {}'.format(amplitude))
    param = { 
            'amplitude': amplitude,
            'period':  2.5,
            'phase':  90.0,
            'offset': 0.0, 
            'num_cycle': 4 
            }
    print('  move to sinusoid start')
    autostep.move_to_sinusoid_start(param)
    autostep.busy_wait()
    time.sleep(1.0)

    print('  running sinusoid')
    autostep.sinusoid(param)
    autostep.busy_wait()
    time.sleep(1.0)
    print() 

autostep.set_move_mode('jog')
autostep.move_to(0.0)
autostep.busy_wait()
print()


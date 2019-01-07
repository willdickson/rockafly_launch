#!/usr/bin/env python
from __future__ import print_function
import sys
import time
import scipy
import rospy

import std_msgs.msg
from autostep_proxy import AutostepProxy
from autostep_ros.msg import TrackingData

num_cycle = 5
velocity = 600

jog_params = {'speed': 200, 'accel': 500, 'decel': 500}
max_params = {'speed': 1000, 'accel': 2000, 'decel': 2000}

print()
print('* run at velocity example')
print()

autostep = AutostepProxy()

autostep.set_jog_mode_params(jog_params)
print('  jog params = {}'.format(autostep.get_jog_mode_params()))

autostep.set_max_mode_params(max_params)
print('  max params = {}'.format(autostep.get_max_mode_params()))

print()
print('  move to position 0.0')
autostep.set_move_mode('jog')
autostep.move_to(0.0)
autostep.busy_wait()

sleep_dt = 2.0
print('  sleeping for {0} sec'.format(sleep_dt))
time.sleep(sleep_dt)
print()

print(' begin running ...')
autostep.set_move_mode('max')

for i in range(num_cycle):

    for vel in [velocity, -velocity]:
        print('  vel: {}'.format(vel))
        autostep.run(vel)
        time.sleep(2.0)
        autostep.soft_stop()
        autostep.busy_wait()

autostep.set_move_mode('jog')
autostep.run(0.0)
print()



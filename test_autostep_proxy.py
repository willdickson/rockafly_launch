#!/usr/bin/env python
from __future__ import print_function
import sys
import time
import scipy
import rospy

import std_msgs.msg
from autostep_proxy import AutostepProxy
from autostep_ros.msg import TrackingData

autostep = AutostepProxy()

# -----------------------------------------------------------------------------
if True:
    print()
    print('* testing run command')
    autostep.set_move_mode('jog')
    autostep.move_to(0.0)
    autostep.busy_wait()
    autostep.set_move_mode('max')

    for i in range(5):
        for vel in [600, -600]:
            print('  vel: {}'.format(vel))
            autostep.run(vel)
            time.sleep(2.0)
            #autostep.run(0)
            #time.sleep(2.0)
    autostep.set_move_mode('jog')
    autostep.run(0.0)
    print()

# -----------------------------------------------------------------------------
if False:
    print('* testing enable/release commands')
    dt = 2.0
    print('  releasing for  {} secs ...'.format(dt), end='')
    sys.stdout.flush()
    autostep.release()
    time.sleep(dt)
    print('done')
    print('  enabling')
    autostep.enable()
    print()

# ----------------------------------------------------------------------------
if False:
    print('* testing move_to command')
    autostep.set_move_mode('jog')
    pos_list = [0, 5, 10, 20, 45, 90, 180, 360, -360, 0]
    for pos in pos_list:
        print('  moving to pos = {}  '.format(pos), end ='')
        sys.stdout.flush()
        autostep.move_to(pos)
        autostep.busy_wait()
        print('done')
    print()

# ----------------------------------------------------------------------------
if False:
    print('* testing move_by command')
    autostep.set_move_mode('jog')
    pos_list = [0, 1, 2, 3, 4, 5, 10, 20, 45, 90, 180, 360, 0]
    for pos in pos_list:
        print('  moving to pos = {}  '.format(pos), end ='')
        sys.stdout.flush()
        autostep.move_to(pos)
        autostep.busy_wait()
        print('done')
    print('  returning to zero')
    autostep.move_to(0.0)
    autostep.busy_wait()
    print()

# -----------------------------------------------------------------------------
if False:
    print('* testing soft_stop command')
    vel = 100.0
    print('  running at vel = {}'.format(vel))
    autostep.run(100)
    time.sleep(2.0)
    print('  execute soft_stop')
    autostep.soft_stop()
    print('  returning to zero')
    autostep.move_to(0.0)
    autostep.busy_wait()
    print()
    
# -----------------------------------------------------------------------------
if False:
    print('* testing set_position command')
    position_list  = [123.0, 0.0]
    for new_position in position_list:
        print('  setting position to {}'.format(new_position))
        autostep.set_position(new_position)
        position = autostep.get_position()
        print('  checking, position = {}'.format(position))
    print()

# -----------------------------------------------------------------------------
if False:
    print('* testing get_position command')
    position = autostep.get_position()
    print('  position = {}'.format(position))
    print()

# -----------------------------------------------------------------------------
if False:
    print('* testing set move mode')
    print('  setting to max')
    autostep.set_move_mode('max')
    print('  setting to jog')
    autostep.set_move_mode('jog')
    print()

# -----------------------------------------------------------------------------
if False:
    print('* testing get_params')
    params = autostep.get_params()
    print(params)
    print()

# -----------------------------------------------------------------------------
if False: 
    print('* testing print_params')
    autostep.print_params()
    print()

# -----------------------------------------------------------------------------
if False:
    print('* testing sinusoid')
    sys.stdout.flush()
    for amplitude in [40, 80, 100]:
        print('  amplitude = {}'.format(amplitude))
        param = { 
                'amplitude': amplitude,
                'period':  2.5,
                'phase':  90.0,
                'offset': 0.0, 
                'num_cycle': 4 
                }
        autostep.move_to_sinusoid_start(param)
        autostep.busy_wait()
        time.sleep(1.0)
        autostep.sinusoid(param)
        autostep.busy_wait()
        time.sleep(1.0)
    print()
    autostep.move_to(0.0)
    autostep.busy_wait()

# -----------------------------------------------------------------------------
if False:
    print('* testing run_trajectory')
    print('  running ... ', end='')
    sys.stdout.flush()
    # Create trajectory
    dt = AutostepProxy.TrajectoryDt
    num_cycle = 6
    period = 5.0
    num_pts = int(period*num_cycle/dt)
    t = dt*scipy.arange(num_pts)
    position = 80*scipy.cos(2.0*scipy.pi*t/period) - 50*scipy.cos(4.0*scipy.pi*t/period)

    autostep.move_to(position[0])
    autostep.busy_wait()
    time.sleep(1.0)

    autostep.run_trajectory(position)
    autostep.busy_wait()
    print('done')
    time.sleep(1.0)
    autostep.set_move_mode('jog')
    autostep.move_to(0.0)
    print()


# -----------------------------------------------------------------------------
if False:
    print('* testing enable/disable tracking mode')
    print('  enabling')
    autostep.enable_tracking_mode()

    print('  disabling')
    autostep.disable_tracking_mode()


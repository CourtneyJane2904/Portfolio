%%sim_magic
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import GyroSensor
import time

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
gy_sensor = GyroSensor(INPUT_4)

MODE_GYRO_ANG = 'GYRO-ANG'
# pentagon: 5 sided shape with internal angles totalling 540 degrees and equal sides
# each angle is 108 degrees
# for i in range(1,6): drive for x seconds and then rotate 108 degrees
# fist long line = -122
for i in range(1,6):
    print(str(gy_sensor.angle))
    # as line 1 and 5 are the lines of the point, make them slightly longer so they meet
    if i == 1 or i == 5:  steering_drive.on_for_seconds(0,10,5.54)
    else:  steering_drive.on_for_seconds(0,10,5)
   
    rotated = False
    while rotated == False:
        steering_drive.on(-90,5)
        # 1 and 4 are the angles of the points
        if i == 1 or i == 4: full_turn = gy_sensor.wait_until_angle_changed_by(108)
        else: full_turn = gy_sensor.wait_until_angle_changed_by(54)
            
        if full_turn == True: rotated = True ; print("rotated after drawing line "+str(i))
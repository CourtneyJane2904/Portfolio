%%sim_magic_preloaded --background Thruxton_Circuit -r Small_Robot
import time

# I used the example for a line follower peogram (05.1 Introducing sensor based control) as a template

# Create colour sensor objects for reading RGB values
colour_l = ColorSensor(INPUT_2)
colour_r = ColorSensor(INPUT_3)

# infinite loop
while True:
    intensity_l = colorLeft.reflected_light_intensity_pc / 100
    intensity_r = colorRight.reflected_light_intensity_pc / 100
   # print(intensity_l,intensity_r)
   # print("eq_1: "+str(colorLeft.reflected_light_intensity))
   # print("eq_2: "+str(colorRight.reflected_light_intensity))
    
    # check for straight line
    eq_1 = colorLeft.reflected_light_intensity
    eq_2 = colorRight.reflected_light_intensity
    
    # after observing the values returned from the previous print statements, I determined that the safest colour values to allow for a speed boost were between 220 and 240 can probably be adjusted for speed boosts that are both safer and more frequent
    # speed boost if both sensors return a val between 220-240
    if eq_1 < 240 and eq_1 > 220 and eq_2 < 240 and eq_2 > 220:
        max_percent_speed = 80 ; print("GO")
    # if there's a corner-like section of track coming up, reduce speed and check for sharp corners    
    elif eq_1 < 100 or eq_2 < 100:
        max_percent_speed = 30 ; print("corner!")
        # the last sharp corner is successfully navigated and not skipped, again adjusting values will probably result in higher speed but also an increased chance of the corner being skipped or the robot going off course
        if (eq_1 < 50 and eq_2 > 250) or (eq_2 == 255):
            print(str(gyro.angle))
            print("sharp left corner!")
            # rotate left wheel backwards and right wheel forwards by 5, results in left turn
            tank_drive.on_for_seconds(-5, 5, 0.4)
        if (eq_2 < 50 and eq_1 > 250) or (eq_1 == 255):
            print(str(gyro.angle))
            print("sharp right corner!")
            tank_drive.on_for_seconds(5, -5, 0.4)
    # a default max speed of 40%        
    else:
        max_percent_speed = 40
        
    left_motor_speed = SpeedPercent(max_percent_speed*intensity_l)
    right_motor_speed = SpeedPercent(max_percent_speed*intensity_r)
    
    # Set the motors to the desired speeds.
    tank_drive.on(left_motor_speed, right_motor_speed)
import cv2
from djitellopy import Tello


# create and connect
tello = Tello()
tello.connect()

# configure drone
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2)

tello.takeoff()
pad = tello.get_mission_pad_id()

# detect and react to pads until we see pad #1
while pad != 3:
    if pad == 1:
        tello.disable_mission_pads()
        tello.streamon()
        frame_read = tello.get_frame_read()
        cv2.imwrite("picture18.png", frame_read.frame)
        tello.streamoff()
        tello.enable_mission_pads()

    if pad == 6:
        tello.rotate_clockwise(90)

    if pad == 2:
        tello.move_left(40)
        tello.move_right(40)

    if pad == 5:
        tello.move_up(40)
        tello.move_down(40)
        power = tello.get_battery()
        print("Power Level =", power, "%")


    pad = tello.get_mission_pad_id()

# termination
tello.disable_mission_pads()
tello.land()
tello.end()

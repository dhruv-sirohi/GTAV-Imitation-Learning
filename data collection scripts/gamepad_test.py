import vgamepad as vg
import time
import math

gamepad = vg.VX360Gamepad()
gamepad.reset()

i=0
while True:
    i += 1
    gamepad.left_trigger_float(0.5)
    gamepad.left_joystick_float(x_value_float=math.sin(i), y_value_float=0.0)
    gamepad.update()
    time.sleep(0.5)

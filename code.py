
import board
import time
import pwmio
import digitalio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.


# create a PWMOut object on Pin A2.
pwm1 = pwmio.PWMOut(board.GP2, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP4, duty_cycle=2 ** 15, frequency=50)
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm1)
my_second_servo = servo.Servo(pwm2)
while True:
    my_servo.angle = 0
    time.sleep(.5)
    my_servo.angle = 180
    time.sleep(.5)
    my_second_servo.angle = 0
    time.sleep(.5)
    my_second_servo.angle = 180
    time.sleep(.5)



# Britbot hardware: a CircuitPlayground Express (or Bluefruit)
#
# A2 => SG90 servo control wire
# i2c => 14-segment alphanumeric display [Adafruit]

import time
import board
import pwmio
import board
import busio as io

from adafruit_motor import servo
from adafruit_circuitplayground import cp
from adafruit_ht16k33 import segments

# Connect to servo on A2
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

# Connect to 14-segment alphanumeric LCD display
i2c = io.I2C(board.SCL, board.SDA)
display = segments.Seg14x4(i2c)

def up():
    """Raise flag to top, wave it, flash red neopixels, play around."""
    my_servo.angle = 140
    for i in range(3):
        cp.pixels.fill((255, 0, 0))
        cp.pixels.brightness = 0.5
        my_servo.angle = 130
        cp.play_tone(440, 0.35)
        cp.pixels.brightness = 0.25
        my_servo.angle = 150
        time.sleep(0.35)

    # Keep serving pointing up, change color to green
    display.print("BRIT")
    my_servo.angle = 140
    cp.pixels.brightness = 0.35
    cp.pixels.fill((0, 255, 0))

def down():
    """Lower flag, return to quiet mode."""
    cp.pixels.brightness = 0.01
    cp.pixels.fill((0, 0, 255))
    my_servo.angle = 15
    display.fill(0)

down()

while True:
    msg = input().strip()
    if msg == "U":
        up()
    elif msg == "D":
        down()


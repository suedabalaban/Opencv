import RPi.GPIO as GPIO
import time

# Define GPIO pins
left_front_motor_pwm_pin = 18
left_rear_motor_pwm_pin = 23
left_middle_motor_pwm_pin = 24

right_front_motor_pwm_pin = 25
right_rear_motor_pwm_pin = 8
right_middle_motor_pwm_pin = 7


def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(left_front_motor_pwm_pin, GPIO.OUT)
    GPIO.setup(left_rear_motor_pwm_pin, GPIO.OUT)
    GPIO.setup(left_middle_motor_pwm_pin, GPIO.OUT)
    GPIO.setup(right_front_motor_pwm_pin, GPIO.OUT)
    GPIO.setup(right_rear_motor_pwm_pin, GPIO.OUT)
    GPIO.setup(right_middle_motor_pwm_pin, GPIO.OUT)


def setup_pwm():
    left_front_motor_pwm = GPIO.PWM(left_front_motor_pwm_pin, 100)
    left_rear_motor_pwm = GPIO.PWM(left_rear_motor_pwm_pin, 100)
    left_middle_motor_pwm = GPIO.PWM(left_middle_motor_pwm_pin, 100)

    right_front_motor_pwm = GPIO.PWM(right_front_motor_pwm_pin, 100)
    right_rear_motor_pwm = GPIO.PWM(right_rear_motor_pwm_pin, 100)
    right_middle_motor_pwm = GPIO.PWM(right_middle_motor_pwm_pin, 100)

    left_front_motor_pwm.start(0)
    left_rear_motor_pwm.start(0)
    left_middle_motor_pwm.start(0)

    right_front_motor_pwm.start(0)
    right_rear_motor_pwm.start(0)
    right_middle_motor_pwm.start(0)

    return (left_front_motor_pwm, left_rear_motor_pwm, left_middle_motor_pwm,
            right_front_motor_pwm, right_rear_motor_pwm, right_middle_motor_pwm)


def move_forward(motors):
    left_front_motor_pwm, left_rear_motor_pwm, left_middle_motor_pwm, \
        right_front_motor_pwm, right_rear_motor_pwm, right_middle_motor_pwm = motors

    GPIO.output(left_front_motor_pwm_pin, GPIO.HIGH)
    GPIO.output(left_rear_motor_pwm_pin, GPIO.HIGH)
    GPIO.output(left_middle_motor_pwm_pin, GPIO.HIGH)

    GPIO.output(right_front_motor_pwm_pin, GPIO.HIGH)
    GPIO.output(right_rear_motor_pwm_pin, GPIO.HIGH)
    GPIO.output(right_middle_motor_pwm_pin, GPIO.HIGH)

    left_front_motor_pwm.ChangeDutyCycle(50)
    left_rear_motor_pwm.ChangeDutyCycle(50)
    left_middle_motor_pwm.ChangeDutyCycle(50)

    right_front_motor_pwm.ChangeDutyCycle(50)
    right_rear_motor_pwm.ChangeDutyCycle(50)
    right_middle_motor_pwm.ChangeDutyCycle(50)


def move_backward(motors):
    left_front_motor_pwm, left_rear_motor_pwm, left_middle_motor_pwm, \
        right_front_motor_pwm, right_rear_motor_pwm, right_middle_motor_pwm = motors

    GPIO.output(left_front_motor_pwm_pin, GPIO.LOW)
    GPIO.output(left_rear_motor_pwm_pin, GPIO.LOW)
    GPIO.output(left_middle_motor_pwm_pin, GPIO.LOW)

    GPIO.output(right_front_motor_pwm_pin, GPIO.LOW)
    GPIO.output(right_rear_motor_pwm_pin, GPIO.LOW)
    GPIO.output(right_middle_motor_pwm_pin, GPIO.LOW)

    left_front_motor_pwm.ChangeDutyCycle(50)
    left_rear_motor_pwm.ChangeDutyCycle(50)
    left_middle_motor_pwm.ChangeDutyCycle(50)

    right_front_motor_pwm.ChangeDutyCycle(50)
    right_rear_motor_pwm.ChangeDutyCycle(50)
    right_middle_motor_pwm.ChangeDutyCycle(50)

def turn_right(motors):
    left_front_motor_pwm, left_rear_motor_pwm, left_middle_motor_pwm, \
        right_front_motor_pwm, right_rear_motor_pwm, right_middle_motor_pwm = motors

    GPIO.output(left_front_motor_pwm_pin, GPIO.HIGH)
    GPIO.output(left_rear_motor_pwm_pin, GPIO.HIGH)
    GPIO.output(left_middle_motor_pwm_pin, GPIO.LOW)

    GPIO.output(right_front_motor_pwm_pin, GPIO.LOW)
    GPIO.output(right_rear_motor_pwm_pin, GPIO.LOW)
    GPIO.output(right_middle_motor_pwm_pin, GPIO.HIGH)

    left_front_motor_pwm.ChangeDutyCycle(50)
    left_rear_motor_pwm.ChangeDutyCycle(50)
    left_middle_motor_pwm.ChangeDutyCycle(25)

    right_front_motor_pwm.ChangeDutyCycle(25)
    right_rear_motor_pwm.ChangeDutyCycle(25)
    right_middle_motor_pwm.ChangeDutyCycle(50)

def turn_left(motors):
    left_front_motor_pwm, left_rear_motor_pwm, left_middle_motor_pwm, \
        right_front_motor_pwm, right_rear_motor_pwm, right_middle_motor_pwm = motors

    GPIO.output(left_front_motor_pwm_pin, GPIO.LOW)
    GPIO.output(left_rear_motor_pwm_pin, GPIO.LOW)
    GPIO.output(left_middle_motor_pwm_pin, GPIO.HIGH)

    GPIO.output(right_front_motor_pwm_pin, GPIO.HIGH)
    GPIO.output(right_rear_motor_pwm_pin, GPIO.HIGH)
    GPIO.output(right_middle_motor_pwm_pin, GPIO.LOW)

    left_front_motor_pwm.ChangeDutyCycle(25)
    left_rear_motor_pwm.ChangeDutyCycle(25)
    left_middle_motor_pwm.ChangeDutyCycle(50)

    right_front_motor_pwm.ChangeDutyCycle(50)
    right_rear_motor_pwm.ChangeDutyCycle(50)
    right_middle_motor_pwm.ChangeDutyCycle(25)

def stop_motors(motors):
    left_front_motor_pwm, left_rear_motor_pwm, left_middle_motor_pwm, \
        right_front_motor_pwm, right_rear_motor_pwm, right_middle_motor_pwm = motors

    GPIO.output(left_front_motor_pwm_pin, GPIO.LOW)
    GPIO.output(left_rear_motor_pwm_pin, GPIO.LOW)
    GPIO.output(left_middle_motor_pwm_pin, GPIO.LOW)

    GPIO.output(right_front_motor_pwm_pin, GPIO.LOW)
    GPIO.output(right_rear_motor_pwm_pin, GPIO.LOW)
    GPIO.output(right_middle_motor_pwm_pin, GPIO.LOW)

    left_front_motor_pwm.ChangeDutyCycle(0)
    left_rear_motor_pwm.ChangeDutyCycle(0)
    left_middle_motor_pwm.ChangeDutyCycle(0)

    right_front_motor_pwm.ChangeDutyCycle(0)
    right_rear_motor_pwm.ChangeDutyCycle(0)
    right_middle_motor_pwm.ChangeDutyCycle(0)

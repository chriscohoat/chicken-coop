from Adafruit_MotorHAT import Adafruit_MotorHAT

import time
import atexit

# create a default object, no changes to I2C address or frequency
# 0x60 is the default address for the first hat. 0x70 is to address all hats
motor_hat = Adafruit_MotorHAT(addr=0x60)


def turn_off_motors():
    print 'Turning off motors...'
    motor_hat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    motor_hat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    motor_hat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    motor_hat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


atexit.register(turn_off_motors)


def main():
    door_motor = motor_hat.getMotor(1)

    while True:
        print "Forward! "
        door_motor.run(Adafruit_MotorHAT.FORWARD)

        print "\tSpeed up..."
        for i in range(255):
            door_motor.setSpeed(i)
            time.sleep(0.01)

        time.sleep(5)

        print "\tSlow down..."
        for i in reversed(range(255)):
            door_motor.setSpeed(i)
            time.sleep(0.01)

        print "Backward! "
        door_motor.run(Adafruit_MotorHAT.BACKWARD)

        print "\tSpeed up..."
        for i in range(255):
            door_motor.setSpeed(i)
            time.sleep(0.01)

        print "\tSlow down..."
        for i in reversed(range(255)):
            door_motor.setSpeed(i)
            time.sleep(0.01)

        print "Release"
        door_motor.run(Adafruit_MotorHAT.RELEASE)
        time.sleep(1.0)


if __name__ == '__main__':
    main()

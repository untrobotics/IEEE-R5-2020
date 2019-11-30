"""
Motor-Movement-with-Class created by Tyler Adam Martinez
    for UNT Robotics IEEE 2020 R5 Competition team

Robot Drive Train Design:
    @     Center of Gravity of the Robot
    ||-   Wheels controlled by DC Motor for movement
    +     Rollies wheels for stability
    
    +---+
    |   |
  ||- @ -||
    |   | 
    --+--
"""
import RPi.GPIO as GPIO
import time

#pins for the Motor A
enA = 12; #PWM0
in1A = 16;
in2A = 18;
#pins for the Motor B
enB = 33; #PWM1
in1B = 31;
in2B = 29;

#intiallizing other useful varibles
dutycycle = 50; # range for pi (0 - 100) for PWM on raspberry pi
GPIO.setmode(GPIO.BOARD);  

#setting up GPIO pins for Motor A
GPIO.setup(enA, GPIO.OUT);
pwmA = GPIO.PWM(enA, 1000);
GPIO.setup(in1A, GPIO.OUT);
GPIO.setup(in2A, GPIO.OUT);


#setting up GPIO pins for Motor B
GPIO.setup(enB, GPIO.OUT);
pwmB = GPIO.PWM(enB, 1000); #The gives a PWM signal of 1000Hz;however, the Ardiuno is 16MHz
GPIO.setup(in1B, GPIO.OUT);
GPIO.setup(in2B, GPIO.OUT);

class Move: 
    """This Class defines all the movement functions for the robot"""
    def fwd():
        """This code will make the robot move forward"""
        print("Robot Moving Forward");
        GPIO.output(enA, GPIO.LOW);
        GPIO.output(enB, GPIO.LOW);
    
        GPIO.output(in1A, GPIO.HIGH);
        GPIO.output(in2A, GPIO.LOW);
    
        GPIO.output(in1B, GPIO.HIGH);
        GPIO.output(in2B, GPIO.LOW);
    
    
    def bwd():
        """This code will make the robot move backwards"""
        print("Robot Moving Backwards");
        GPIO.output(enA, GPIO.LOW);
        GPIO.output(enB, GPIO.LOW);
    
        GPIO.output(in1A, GPIO.LOW);
        GPIO.output(in2A, GPIO.HIGH);
    
        GPIO.output(in1B, GPIO.LOW);
        GPIO.output(in2B, GPIO.HIGH);

    def left():
        """This code will make the robot turn left"""
        print("Robot Turning Left");
        pwmA.start(dutycycle);
        GPIO.output(enB, GPIO.LOW);
    
        GPIO.output(in1A, GPIO.HIGH);
        GPIO.output(in2A, GPIO.LOW);
    
        GPIO.output(in1B, GPIO.HIGH);
        GPIO.output(in2B, GPIO.LOW);
    
        pwmA.stop();
    
    def right():
        """This code will make the robot turn right"""
        print("Robot Turning Right");
        GPIO.output(enA, GPIO.LOW);
        pwmB.start(dutycycle);

    
        GPIO.output(in1A, GPIO.HIGH);
        GPIO.output(in2A, GPIO.LOW);
    
        GPIO.output(in1B, GPIO.HIGH);
        GPIO.output(in2B, GPIO.LOW);
    
        pwmB.stop();

    def mstop():
        """This code will make the robot stop moving"""
        print("Robot Stopping");
        GPIO.output(enA, GPIO.HIGH);
        GPIO.output(enB, GPIO.HIGH);
        print("Robot Stopped");

    def testmotors():
        """Use this function when testing the robot movement ablility"""
        print("Begin Motor Movement Test");
        Move.fwd();
        time.sleep(5);
        Move.mstop();
        time.sleep(5);
        Move.left();
        time.sleep(5);
        Move.right();
        time.sleep(5);
        Move.bwd();
        time.sleep(5);
        print("Finnish Motor Movement Test");
    
def main():
    Move.testmotors();
    
if __name__ == "__main__":
    main()
    
    
#Safe termination of program
pwmA.stop(); pwmB.stop();
#GPIO reset to normal state after termination of program
GPIO.cleanup();

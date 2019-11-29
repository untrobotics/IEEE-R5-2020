#Motor-Movement created by Tyler Adam Martinez for UNT Robotics IEEE 2020 R5 Competition team
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
#pwmA = GPIO.PWM(enA, 100);
GPIO.setup(enA, GPIO.OUT);
GPIO.setup(in1A, GPIO.OUT);
GPIO.setup(in2A, GPIO.OUT);


#setting up GPIO pins for Motor B
#pwmB = GPIO.PWM(enB, 100);
GPIO.setup(enB, GPIO.OUT);
GPIO.setup(in1B, GPIO.OUT);
GPIO.setup(in2B, GPIO.OUT);

#defining functions to be used later on in the program
def fwd():
    #This code will make the robot move forward
    print("Robot Moving Forward");
    GPIO.output(enA, GPIO.LOW);
    GPIO.output(enB, GPIO.LOW);
    
    GPIO.output(in1A, GPIO.HIGH);
    GPIO.output(in2A, GPIO.LOW);
    
    GPIO.output(in1B, GPIO.HIGH);
    GPIO.output(in2B, GPIO.LOW);
    
    
def bwd():
    #This code will make the robot move backwards
    print("Robot Moving Backwards");
    GPIO.output(enA, GPIO.LOW);
    GPIO.output(enB, GPIO.LOW);
    
    GPIO.output(in1A, GPIO.LOW);
    GPIO.output(in2A, GPIO.HIGH);
    
    GPIO.output(in1B, GPIO.LOW);
    GPIO.output(in2B, GPIO.HIGH);

def mstop():
    #This code will make the robot stop moving
    print("Robot Stopping");
    GPIO.output(enA, GPIO.HIGH);
    GPIO.output(enB, GPIO.HIGH);
    
def main():
    print("Motor-Movement");
    fwd();
    time.sleep(5);
    mstop();
    time.sleep(5);
    bwd();
    time.sleep(5);
    print("Finnish test Motor Movement");

    
if __name__ == "__main__":
    main()
    
    
#Safe termination of program
#pwmA.stop(); pwmB.stop();
GPIO.cleanup() #GPIO reset
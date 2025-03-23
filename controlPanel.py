#import random and time modules to simulate testing
import random
import time

#add variable to keep count of rounds
var = 0

print(" ")

print("Welcome to the control panel. \nPLEASE MAKE A SELECTION")
print(" ")

#display options
print("1. Ultrasonic Testing(1-100 MHz)")
print("2. Eddy Current Testing (10-10,000 kHz)")
print("3. X-ray Testing (100-450 kV)")


method = int(input("ENTER A NUMBER BETWEEN 1-3 "
"(1 for Ultrasonic, 2 for Eddy Current, or 3 for X-Ray)\n"
" \n"
"OR PRESS ANY OTHER KEY TO EXIT: "  ))

#keep program running until user presses any key to exit
while True:
        var += 1
        print(" ")
        print(f"ROUND {var}")
        print(" ")

        #method 1
        if method == 1:
            frequency = int(input("Enter a frequency (1-100 MHz for Ultrasonic): "))
            print(f"You selected Ultrasonic testing at {frequency} MHz")
            print(" ")
            print("Performing test...")
            time.sleep(3)
            result = random.randint(1,100)
            if result >= 1 and result <= 30:
                 print("No Defects Detected")
            elif result >= 31 and result <= 70:
                 print("Minor Surface Defects")
            elif result >= 71 and result <= 100:
                 print("Internal Cracks Detected")
        #method 2
        elif method == 2:
            frequency = int(input("Enter a frequency (10-10,000 kHz for Eddy Current): "))
            print(f"You selected Eddy Current testing at {frequency} kHz")   
            print(" ")
            print("Performing test...")
            time.sleep(3)
            result = random.randint(10,10000)
            if result >= 1 and result <= 30:
                 print("No Defects Detected")
            elif result >= 31 and result <= 70:
                 print("Minor Surface Defects")
            elif result >= 71 and result <= 100:
                 print("Internal Cracks Detected")
        #method 3
        elif method == 3:
            voltage = int(input("Enter a voltage(100-450 kV for X-ray): "))
            print(f"You selected X-Ray testing at {voltage} kv")   
            print(" ")
            print("Performing test...")
            time.sleep(3)
            result = random.randint(1,100)
            if result >= 1 and result <= 30:
                 print("No Defects Detected")
            elif result >= 31 and result <= 70:
                 print("Minor Surface Defects")
            elif result >= 71 and result <= 100:
                 print("Internal Cracks Detected")
       #exit control panel          
        else:
             print("Exiting control panel...")
             time.sleep(1)
             print(" ")
             print("YOU HAVE EXITED THE CONTROL PANEL")
             break
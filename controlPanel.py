#import random and time modules to simulate testing
import random
import time

#display options
print("1. Ultrasonic Testing(1-100 MHz)")
print("2. Eddy Current Testing (10-10,000 kHz)")
print("3. X-ray Testing (100-450 kV)")


method = int(input("Enter the number for the "
"chosen method: \nPRESS ANY OTHER KEY TO EXIT\n"))

#keep program running until user presses any key to exit
while True:

        #method 1
        if method == 1:
            frequncy = int(input("Enter a frequency (1-100 MHz for Ultrasonic) "))
            print(f"You selected Ultrasonic testing at {frequency} Mhz")
            print("Performing test...")
            time.sleep(3)
            result = random.randint(1,100)
            if result >= 1 or result <= 100:
                 print("No Defects Detected")
            elif result >= 31 or result <= 70:
                 print("Minor Surface Defects")
            elif result >= 71 or result <= 1000:
                 print("Internal Cracks Detected")
        #method 2
        elif method == 2:
            frequency = int(input("Enter a frequency (10-10,000 kHz for Eddy Current) "))
            print(f"You selected Eddy Current testing at {frequency} kHz")   
            time.sleep(3)
            result = random.randint(10,10000)
            if result >= 10 or result <= 500:
                 print("No Defects Detected")
            elif result >= 31 or result <= 70:
                 print("Minor Surface Defects")
            elif result >= 71 or result <= 1000:
                 print("Internal Cracks Detected")
        elif method == 3:
            frequncy = int(input("100-450 kV for X-ray "))
        else:
             break
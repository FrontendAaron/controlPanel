

print("1. Ultrasonic Testing(1-100 MHz)")
print("2. Eddy Current Testing (10-10,000 kHz)")
print("3. X-ray Testing (100-450 kV)")

method = int(input("Enter the number for the "
"chosen method: \nPRESS ANY OTHER KEY TO EXIT\n"))

while True:

        
        if method == 1:
            frequncy = int(input("Enter a frequency (1-100 MHz for Ultrasonic) "))
        elif method == 2:
            frequency = int(input("Enter a frequency (10-10,000 kHz for Eddy Current) "))
        elif method == 3:
            frequncy = int(input("100-450 kV for X-ray "))
        else:
             break
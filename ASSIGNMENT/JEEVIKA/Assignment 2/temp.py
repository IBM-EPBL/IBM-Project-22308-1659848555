
#Temperature and Humidity sensing using random


import random
import time
while(1):
    temp = random.uniform(15.0, 40.0)
    humidity = random.randint(1, 100)
    print("\nTemperature : {:.2f}*C   Humidity : {}%" .format(temp,humidity))
    
    if temp > 30 :  #temp in celsius
        if humidity > 80:
            print("\n Alert: Abnormal condition predicted")
        else:
            print("\n Warning: Temperature is high")
    else:
        print("\n Normal Temperature")
    time.sleep(1)    
    

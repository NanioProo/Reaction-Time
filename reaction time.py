import random
import math
import time

def reaction_time():
    user_input = input('enter ready when ready..: ')
    if user_input == "ready":
        time1 = random.randint(5, 9)

        time.sleep(time1)
        print('#######################')
        start = time.time()
        reaction = input('')
        end = time.time()
        number = int((end - start) * 1000)
        print(math.ceil(number),"ms")
        
        reaction_time()
    else:
        reaction_time()

reaction_time()

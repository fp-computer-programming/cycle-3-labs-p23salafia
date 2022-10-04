import math
import time

var_1 = time.process_time()
var_2 = time.perf_counter()

var_math = math.pow(2,2)
print(var_math)
var_math_2 = (2**2)
print(var_math_2)

print(var_1) #After I hit run, it takes .039466 seconds for the comuter to finish running the code
print(var_2)

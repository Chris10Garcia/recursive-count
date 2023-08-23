
"""
Use recursion to count (print) from 0 to 9
MUST CALL ON IT'S SELF
"""

"""
The base condition is when you reach below 0
Start at 10
-1 => 9
if it's below zero, stop
call on the function again with new value
print(value)
"""

def recursiveCount(value):
    
    value -=1
    if value == -1:
        return
    recursiveCount(value)
    print(value)



if __name__ == "__main__":
    recursiveCount(10)
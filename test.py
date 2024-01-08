# Type 1:
import file1
print(file1.x)
file1.greet()

# Type 2:
from file1 import x,greet
print(x)
greet()

# Type 3:
import file1 as f1 
print(f1.x)
f1.greet()

# Type 4:
from file1 import *
print(x)
greet()
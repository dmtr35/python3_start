import globals_2
import sys

print("Из globals:", globals()['globals_2'])
print("Из sys.modules:", sys.modules['globals_2'])

print(globals()['globals_2'] is sys.modules['globals_2'])  # True



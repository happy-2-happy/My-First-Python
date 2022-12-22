# pylint: disable=missing-module-docstring
# pylint: disable=redefined-builtin
# pylint: disable=invalid-name
import logging
import logging.config
import pydash
from arithmetic import multiply
from exception import exception

logging.config.fileConfig(fname='logging.conf',
                          disable_existing_loggers=False)
print('Hello World')

# patient_name = input("What is your name?\t")
# patient_year = input("What is your Birth year?\t")
# print(f"Hello {patient_name}")
# print(f"Your age is {patient_year}")


x, y, z = [1, 2, 3]
print(x)
print(y)
print(z)

print(x, y, z)

print(complex(x))

if x > 2:
    print('Passed 1')
elif x == 1:
    print('Passed 2')
else:
    print('Default')

while x < 5:
    print('while loop')
    x = x+1

for number in range(5):
    print(f'For Loop {number}')


print(multiply(2, 5, 5, 4))

exception()
print(logging.getLogger())
logging.basicConfig(level=logging.DEBUG)
print(logging.getLogger())
logging.debug('Debug')
logging.info('Info')
logging.warning('Warning')
logging.error('Error')
logging.critical('Critical')

print("123".__eq__("1234"))
print(pydash.capitalize("gokulram"))

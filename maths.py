import math

def add(first, second):
    return first + second

def fibonacci(length):
    def internal(first, second, count):
        third = add(first, second)
        count -= 1
        if count < 2:
            return third
        else:
            return internal(second, third, count)

    return internal(0, 1, length)

HEX_CHARS = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def convert_base(num, n, add=0):
   """Change a base 10 number to a base-n number. Supports up to base 16. """
   new_num_string = ''
   current = num
   while current != 0:
       # print(current)
       remainder = current % n
       if remainder > 9:
           remainder_string = HEX_CHARS[remainder]
       elif remainder >= 36:
           remainder_string = '('+str(remainder)+')'
       else:
           remainder_string = str(remainder)
       new_num_string = remainder_string+new_num_string
       current = int(current/n)
   if add!=0:
       return convert_base(num,add)#converting to another base
   return new_num_string
def factorial(num):
    """Get the factorial of a number"""
    current = num
    result = math.factorial(current)
    return result

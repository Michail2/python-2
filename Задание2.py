import math

result = []
quantity_value = int( input() )

def factorial( x ): 
    i = 1
    result1 = []
    while i <= x:
        relust_value = math.factorial(i)
        result1.append( relust_value )
        i = i + 1
    return result1

result = factorial( quantity_value )

print( f'пусть N = { quantity_value }, тогда { result }' )
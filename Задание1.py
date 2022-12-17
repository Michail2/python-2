import random

start_random_value = float( input(' Введите начальное рандомное значение: ') )
end_random_value = float( input( ' Введите конечное рандомное значение: ' ) )

random_value = random.uniform( start_random_value, end_random_value )

def summa( x ):                           
    if float( x ) < 0:                           
        x = float( x ) * ( -1 )
    number = 0

    for i in str( x ):
        if i != '.':
            number += int( i )
    return number
 
print(f' Полученное чило: {random_value }\n Сумма чисел равна: { summa( random_value ) }')

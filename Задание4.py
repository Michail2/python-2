from random import randint

N = int( input(' Ведите количество элементов массива: ') )
first_value = int( input(' Ведите позицию первого элемента: ') )
last_value = int( input(' Ведите позицию второго элемента: ') )
dict = {}

def filling_the_array( dict1 = {} ):
    pos_value = 0
    while pos_value < N:
        dict1[ pos_value ] = randint( -N, N ) 
        pos_value = pos_value + 1
    return dict1

if first_value > N or first_value < -N:
    print(' Введена некоррекстная позиция первого элемента')
elif last_value > N or last_value < -N:
    print(' Введена некоррекстная позиция второго элемента')
else:          
    print(f' Заданный массив { filling_the_array( dict ) } \n Сумма элементов: { dict[ first_value ] } + { dict[ last_value ] } = { dict[ first_value ] + dict[ last_value ] }')

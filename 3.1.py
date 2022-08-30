# задача 1

a,b=int(input('введите число: ')),int(input('введите число: '))
def func_del(arg_1,arg_2):
    if arg_2==0:
        return ('деление на 0')
    return arg_1/arg_2
print(func_del(a,b))

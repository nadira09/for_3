# 3 задача


a,b,c=int(input('введите a: ')),int(input('введите b: ')),int(input('введите c: '))

def my_func(a,b,c):
    _max=a
    _min=b
    if b>_max:
        _max=b
        _min=a
    if c>_max:
        _max=c
    if c<_min:
        _min=c
    return a+b+c-_min
print(my_func(a,b,c))

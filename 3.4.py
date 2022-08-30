# задача 4
# 1 способ

def my_func(x,y):
    return x**y
print(my_func(1.5,-1))

# 2 способ

x = float(input('введите число: '))
y = int(input('введите степень: '))

def my_func(x,y):
    s=1
    i=1
    for i in range(y*(-1)):
        s*=1/x
    return s
print(my_func(x,y))
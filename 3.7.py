# задача 7


word=input('введите слово: ')
def int_func(word):
    return word.title()

text=input('введите текст: ')
def int_text_func(text):
    words=text.split(' ')
    i=0
    result=int_func(words[i])
    i+=1

    while i<len(words):
        result+=' '+int_func(words[i])
        i+=1
    return result
print(int_text_func(text))
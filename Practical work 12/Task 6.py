word = input('Введите слово: ')
word_list = list(word)
reverse_word_list = word_list[::-1]
if word_list == reverse_word_list:
    print('Это палиндром')
else:
    print('Это не палиндром!')
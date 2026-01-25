
# Исходя из задания мы можем представить X, Y и Z как троичную систему счисления где X = 0, Y = 1, а Z = 2
# Значит, чтобы найти 179 в этой системе мы должны перевести 179 в данную систему счисления
# Мы знаем что порядковое имя состоит из 5 символов
# Значит мы должны произвести деление на три 5 раз
# Это способ перевести число из десятичной системы в троичную систему счисления
# 179 помещается в 5 букв потому что меньше чем 3^5(243)
# 243 - количество возможных порядковых имен которые максимально помещаются в 5 букв в данном алфавите

ALPHABET = ('X', 'Y', 'Z')
num = 179

name_letter_5 = num % len(ALPHABET)
remainder_num = num // len(ALPHABET)
name_letter_4 = remainder_num % len(ALPHABET)
remainder_num //= len(ALPHABET)
name_letter_3 = remainder_num % len(ALPHABET)
remainder_num //= len(ALPHABET)
name_letter_2 = remainder_num % len(ALPHABET)
remainder_num //= len(ALPHABET)
name_letter_1 = remainder_num % len(ALPHABET)

print(f"Машине под номером {num} досталось имя: {ALPHABET[name_letter_1]}{ALPHABET[name_letter_2]}"
      f"{ALPHABET[name_letter_3]}{ALPHABET[name_letter_4]}{ALPHABET[name_letter_5]}")

password_first = input()
password_second = input()

if len(password_first) < 7:
    print('Short')
elif len(password_first) >= 7 and password_first != password_second:
    print('Difference')
elif len(password_first) >= 7 and password_first == password_second:
    print('OK')


"""
Напишите программу, которая имитирует проверку пароля, придуманного пользователем. Пользователь сперва вводит пароль, потом вводит подтверждение пароля. Вам нужно обработать следующие ситуации:

    если пароль, который ввёл пользователь (в первый раз) короче 7 символов, программа выводит "Short" 
    если пароль достаточно длинный, но введённый во второй раз пароль не совпадает с первым, программа выводит "Difference"
    если же и эта проверка пройдена успешно, программа выводит "OK" (латинскими буквами).

Sample Input 1:
  qwerty
  qwerty
    
Sample Output 1:
  Short
  
Sample Input 2:
  qwerty123
  qwerty
    
Sample Output 2:
  Difference  
"""

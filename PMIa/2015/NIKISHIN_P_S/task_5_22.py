# Задача 5. Вариант 22. 
# Напишите программу, которая бы при запуске случайным образом отображала имя одного из двух сооснователей компании Google.
# Nikishin P. S. 
# 12.05.2016

import random
print ("Программа случайным образом отображает имя одного из двух сооснователей компании Google.")

g = random.randint(1,2)

if g == 1:
    a = "Ларри Пейдж"
else:
    a = "Сергей Михайлович Брин"
print ("Один из сооснователей Google: "+(a))

input("\nДля выхода нажмите Enter") 

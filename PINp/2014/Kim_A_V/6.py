# Задача 6. Вариант 42.

import random
x=random.choice(["Томас Стаффорд", "Вэнс Бранд", "Дональд Слейтон", "Алексей Леонов", "Валерий Кубасов"])
name=input ("Программа случайным образом загадывает имя одного из пяти членов экипажей программы Союз - Апполон, попробуйте отгадать:...")
if x == name:
    print("Всё верно! Это ",x,"!")
else:
    print("Неудача, это не", name, ". Мы загадали", x)



input("\n\nНажмите Enter для выхода.")

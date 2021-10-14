"""
Výjimky v Pythonu
-----------------

Zdroje informací:
* https://naucse.python.cz/lessons/beginners/exceptions/
* https://macek.sandbox.cz/texty/python-tutorial-cz/tut/node10.html
"""
# Možné chyby v programu

# 1. Index mimo rozsah listu
numbers = [1, 2]
print(numbers[3])

age = int(input("Age: "))
xfactor = 10 / age
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
# 2. Nesprávný typ na vstupu
# Ošetření pomocí výjimky
# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except ValueError as error:
#     print("Nezadal jste číslo!")
#     print(error)
#     print(type(error))
# except ZeroDivisionError as error:
#     print("Nesmí být zadána nula!")
#     print(error)
#     print(type(error))
# else:
#     print("Vše je v pořádku")
#
# print("Pokračování kódu")


# 3. Kombinace různých výjimek
# try:
#     with open("./exception.py") as file1, open("./pokus.txt") as file2:
#         print("Soubor otevřen")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as error:
#     print("Chybné zadání!")
#     print(error)
#     print(type(error))
# except FileNotFoundError as error:
#     print("Nebylo možné otevřít soubor")
#     print(error)
#     print(type(error))
# else:
#     print("Vše je v pořádku")
# finally:
#     file1.close()
#     file2.close()
#
# print("Pokračování kódu")

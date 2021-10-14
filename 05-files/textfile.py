"""
Práce s textovými soubory v Pythonu
-----------------------------------
Zdroje informací:
* https://www.itnetwork.cz/python/soubory/prace-s-textovymi-soubory-v-pythonu
* https://naucse.python.cz/lessons/beginners/files/

Argumenty z příkazové řádky:
* https://naucse.python.cz/2020/pyladies-ostrava-podzim-pokrocili/intro/argparse/
* https://naucse.python.cz/2020/pyladies-ostrava-podzim-pokrocili/intro/click/
"""
import sys, re

count = len(sys.argv)
print("Number of arguments:", count)

for arg in sys.argv:
    print(arg)

# with open(sys.argv[1], encoding='utf-8') as file:
#     data = file.read()
#
# print(data)
#
# data = re.sub(r'[iyíý]','-',data)
#
# print(data)
#
# with open(sys.argv[2], mode='w', encoding='utf-8') as newfile:
#     newfile.write(data)
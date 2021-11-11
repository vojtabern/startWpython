import string
import sys, re

def textfile_read(path, encoding):
    try:
        with open(path, encoding=encoding) as file:
            data = file.read()
    except FileNotFoundError as error:
        return (f'Soubor nebyl nalezen: {error}')
    except Exception as error:
        return (f'Vyskytla se nejaka chyba: {error}')
    finally:
        file.close()
    return data

data = textfile_read('./zadani.txt', 'windows-1250')

def charFrequency(data):
    vystup = dict()
    for char in data:
        if char not in vystup:
            vystup[char] = 0
        vystup[char] += 1

    vystup = list(vystup.items())
    vystup.sort(key=lambda x:x[1], reverse=True)
    return vystup


vystup = charFrequency(data)
i=0
for i in range (len(vystup)-1):
    if i == 0:
        print(f"[{vystup[i]}")
    else:
        print(f"{vystup[i]}")


i += 1
print(f"{vystup[i]}]")
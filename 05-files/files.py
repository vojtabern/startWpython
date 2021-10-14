


def readFile(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError as error:
        print(f'Soubor nebyl nalezen: {error}')
    except Exception as error:
        print(f'Vyskytla se nějaká chyba: {error}')
    finally:
        file.close()
    return data

print(readFile('./python.txt'))
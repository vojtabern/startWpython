import sys, re


def textfile_read(path, encoding):
    try:
        with open(path, encoding=encoding) as file:
            data = file.read()
    except FileNotFoundError as error:
        return (f'Soubor nebyl nalezen: {error}')
    except Exception as error:
        return (f'Vyskytla se nějaká chyba: {error}')
    finally:
        file.close()
    return data

print(textfile_read('./python.txt', 'utf-8'))


def textfile_write(path, data, encoding):
    try:
        with open(path, mode='w', encoding=encoding) as file:
            file.write(data)
    except FileNotFoundError as error:
        print(f'Soubor nebyl nalezen: {error}')
        return False
    except Exception as error:
        print(f'Vyskytla se nějaká chyba: {error}')
        return False
    finally:
        file.close()
    return True

txt = input("Zadej co cheš vypsat do souboru: ");

#txt = textfile_read('./python.txt', 'utf-8')
kamarad = textfile_write('./novy.txt', txt, 'utf-8')
if  kamarad == False:
    print ("Nepovedlo se zapsat do souboru\n")
else:
    print("Bylo zapsano do souboru")



#json zacina
import json, csv

def jsonfile_read(path, encoding):
    try:
        with open(path, encoding=encoding) as file:
            data = json.load(file)
    except FileNotFoundError as error:
        return (f'Soubor nebyl nalezen: {error}')
    except Exception as error:
        return (f'Vyskytla se nějaká chyba: {error}')
    finally:
        file.close()
    return data



def jsonfile_write(path, data={}):
    try:
        with open(path, mode='w', encoding='utf-8') as file:
            json.dump(data, file)
    except FileNotFoundError as error:
        print(f'Soubor nebyl nalezen: {error}')
        return False
    except Exception as error:
        print(f'Vyskytla se nějaká chyba: {error}')
        return False
    finally:
        file.close()
    return True



def csvfile_read(path, encoding="utf-8"):
    try:
        with open(path, encoding=encoding, newline='\n') as file:
            csvreader = csv.DictReader(file, delimiter=";", quotechar='"')
            dict_list = []
            radek = []
            for row in csvreader:
                dict_list.append(row)
                if "\n" in dict_list:
                    radek += dict_list


    except FileNotFoundError as error:
        print(f'Soubor nebyl nalezen: {error}')
        return False
    except Exception as error:
        print(f'Vyskytla se nějaká chyba: {error}')
        return False
    finally:
        print(dict_list)
        file.close()
    return dict_list



jsondata = jsonfile_read('./slon.json', 'utf-8')
print(jsondata, type(jsondata))

txt = textfile_read('./python.txt', 'utf-8')
kamaradi = jsonfile_write('./novy.json', txt)
csvfile_read('./addresses.csv', 'windows-1250')







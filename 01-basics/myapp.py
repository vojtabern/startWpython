kokos = input("Zadej kolik kokosů jsi za předminulý rok snědl: ")
rok_kokos = input("Zadej kolik kokosů jsi snědl za poslední rok: ")
rozdil = int(kokos)-int(rok_kokos)
print("{pocet}x kokosů jsi snědl {pocet}x jsi člověkem" .format(pocet = kokos))
if (int(kokos)-int(rok_kokos))<1:
    print("Měl by jsi konzumovat více kokosů")
elif (int(kokos)-int(rok_kokos))>1:
    print("Jen tak dále. Za poslední rok jsi skounzumoval o {pocet} více kokosů než předminulý rok".format(pocet = rozdil))


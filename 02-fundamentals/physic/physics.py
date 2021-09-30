'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu



def rozdil_mezi_gravitacemi_earth_moon(earth, moon, jmeno1, jmeno2):
    """
    rozdil_mezi_gravitacemi_earth_moon: Vypočítá jaký je rozdíl mezi gravitací země a měsíce v m/s
    """
    substract = abs(earth - moon)
    return(print("Rozdil gravitací", jmeno1,"a",jmeno2 ,"je {:.2f} m/s".format(substract)))

rozdil_mezi_gravitacemi_earth_moon(EARTH_GRAVITY, MOON_GRAVITY, "země", "měsíce")

def rozdil_mezi_rychlost_light_sound(light, sound, jmeno1, jmeno2):
    """
    rozdil_mezi_rychlost_light_sound Vypočítá jaký je rozdíl mezi rychlostí světla a zvuku v m/s
    """
    substract_v = abs(sound - light)
    return(print("Rozdil rychlosti", jmeno1,"a", jmeno2, "je",substract_v ,"m/s"))
rozdil_mezi_rychlost_light_sound(SPEED_OF_LIGHT, SPEED_OF_SOUND, "světla", "zvuku")

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''
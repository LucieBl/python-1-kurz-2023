import json

with open("body.json", mode="r", encoding="utf-8") as soubor:
    hodnoceni = json.load(soubor)

print(hodnoceni)

for key, value in hodnoceni.items():
    if int(value) >= 60:
        hodnoceni[key] = "Pass"
    else:
        hodnoceni[key] = "Fail"
        

with open("prospech.json", mode="w", encoding="utf-8") as soubor:
    json.dump(hodnoceni, soubor, ensure_ascii=False, indent=len(hodnoceni))

print(hodnoceni)



""" Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a).
Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň 60 bodů. Pokud má méně než 60, hodnota bude "Fail".
Výsledný slovník ulož jako JSON do souboru prospech.json."""

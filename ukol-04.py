""" Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:
První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla.
Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.
Tipy:
Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420"."""


def phone_number_check(number):
    if len(number) == 9:
        return number
    elif len(number) == 13 and number[:4] == "+420":
        return number
    else:
        return False
    
def message_cost(message):
    message_lenght = len(message)
    cost = (message_lenght // 180) * 3
    if message_lenght % 180 != 0:
        cost += 3
    return cost

phone_number = (input("Zadej telefonní číslo: "))
if phone_number_check(phone_number):
    message = input("Zadej SMS zprávu: ")
    cost = message_cost(message)
    print(f"Cena SMS zprávy je {cost} Kč.")
else:
    print("Neplatný formát telefonního čísla.")

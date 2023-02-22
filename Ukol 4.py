cislo = input("Dobry den, zadejte prosim telefonni cislo:")
def zkontroluj_cislo(cislo)-> int:
    return len(cislo)==9 or (len(cislo)==12 and cislo[0:4]=="+420")
if zkontroluj_cislo: 
    print("Telefonní číslo je v pořádku")
else:  
    print("Nesprávný formát čísla")

zprava = input("Napiste zpravu:")

def urci_cenu(zprava):
    return (len(zprava)//180)*3 + 3



   




a = {
    "raichu" : "Raichu has a regional variant that is Electric/Psychic . It evolves from Pikachu when exposed to a Thunder Stone. All Pikachu in Alola will involve into this form regardless of their origin",
    "Onix" : "Onix resembles a giant chain of gray boulders that become smaller toward the tail. It has rocky spine on its head and a pair of black eye beneath it. This Pokemon has a magnet in its brain"
}
b = input("enter Pokemon name:")
c = b.lower()
if c =="raichu":
    print(a["raichu"])
elif c =="Onix":
    print(a["Onix"])
else:
    print("this Pokemon doesn't exist")
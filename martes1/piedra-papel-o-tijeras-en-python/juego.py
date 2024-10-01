import random


print("***PIEDRAS PAPEL O TIJERAS***")
Lista = ["Piedra", "Papel", "Tijeras"]

contrario = random.choice(Lista)

print("[P]iedras, [Pa]pel, [T]ijeras: ")

while True:
    
    eleccion = input("elige una de las opciones: ")
    
    if eleccion not in ["P", "Pa", "T"]:
        
        print("\nElige solo las opciones mostradas por pantalla\n")
        continue
        
    break

print(f"PC saco: {contrario}")

if eleccion == "P" and contrario == "Tijeras":
    print("Ganaste")

elif eleccion == "Pa" and contrario == "Tijeras":
    print("Perdiste")
    
elif eleccion == "T" and contrario == "Tijeras":
    iprint("Empate")

elif eleccion == "P" and contrario == "Piedra":
    print("Empate")
    
elif eleccion == "Pa" and contrario == "Piedra":
    print("Ganaste")
    
elif eleccion == "T" and contrario == "Piedra":
    print("Perdiste")

elif eleccion == "P" and contrario == "Papel":
    print("Ganaste")
    
elif eleccion == "Pa" and contrario == "Papel":
    print("Empate")
    
elif eleccion == "T" and contrario == "Papel":
    print("Perdiste")
#se que hay muchos if elif en mi codigo pero no sabia como hacer de otra manera 
#cuando sepa mas del tepa lo perfecionare

from naipe import Naipe
from mano import Mano

if __name__ == "__main__":
    naipe = Naipe()
    mano1 = Mano(naipe)
    mano2 = Mano(naipe)

    print("Mano 1:", mano1)
    print("Mano 2:", mano2)

    if mano1.comparar(mano2):
        print("Mano 1 es mayor que Mano 2")
    else:
        print("Mano 2 es mayor que Mano 1")


    


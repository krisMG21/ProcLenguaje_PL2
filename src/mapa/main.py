from Mapa import Mapa


def main():
    with open("ejemplo.field") as file:
        mapa = Mapa(file.read(), 5)

    print(mapa)
    for barco in mapa.get_barcos():
        if barco:
            print(barco)

    print(mapa.as_tree())


if __name__ == "__main__":
    main()

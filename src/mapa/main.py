from Mapa import Mapa


def main():
    with open("ejemplo.field") as file:
        mapa = Mapa(file.read())

    with open("mapa.tree", "w") as file:
        file.write(mapa.as_tree())

    print("Tree succesfully written in 'mapa.tree'")
    return 0


def test_mapa():
    with open("ejemplo.field") as file:
        mapa = Mapa(file.read())

    print("as_map: \n" + mapa.as_map())
    print("as_matrix: \n" + mapa.as_matrix())
    print("as_tree: \n" + mapa.as_tree())

    print("get_barcos: \n")
    for barco in mapa.get_barcos():
        if barco:
            print(barco)


if __name__ == "__main__":
    main()

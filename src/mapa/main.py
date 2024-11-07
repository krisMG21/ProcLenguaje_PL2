from Mapa import Mapa


def main():
    test_mapa()
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

    print("\nget_obstaculos: \n")
    for obs in mapa.get_obstaculos():
        if obs:
            print(obs)


if __name__ == "__main__":
    main()

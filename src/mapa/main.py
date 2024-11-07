from Nivel import Nivel


def main():
    test_nivel()
    return 0


def test_nivel():
    with open("ejemplo.field") as file:
        nivel = Nivel(file.read())

    print("as_map: \n" + nivel.as_map())
    print("as_matrix: \n" + nivel.as_matrix())
    print("as_tree: \n" + nivel.as_tree())

    print("get_barcos: \n")
    for barco in nivel.get_barcos():
        if barco:
            print(barco)

    print("\nget_obstaculos: \n")
    for obs in nivel.get_obstaculos():
        if obs:
            print(obs)


if __name__ == "__main__":
    main()

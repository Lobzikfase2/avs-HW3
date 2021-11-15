from sys import argv, exit
from timeit import timeit
from container import Container


def main():
    if len(argv) != 5:
        print("Incorrect command line!\n"
              "  Waited:\n"
              "     command -i input_file output_file01 output_file02\n"
              "  Or:\n"
              "     command -g number output_file01 output_file02\n")
        exit(1)

    mode = argv[1]
    if mode not in ["-i", "-g"]:
        print("Incorrect qualifier value!\n"
              "  Waited:\n"
              "     command -i input_file output_file01 output_file02\n"
              "  Or:\n"
              "     command -g number output_file01 output_file02\n")
        exit(2)

    container = Container()

    if mode == "-i":
        container.read_films_from_file(argv[2])
    elif mode == "-g":
        count = int(argv[2])
        if count < 1 or count > 10000:
            print(f"Incorrect number of films = {count}! Choose from [1, 10000].")
            exit(3)
        container.generate_films_list(count)

    container.write_films_to_file(argv[3])
    container.delete_elements()
    container.write_films_to_file(argv[4])


if __name__ == '__main__':
    print(f"Success! Time has passed: {round(timeit(main, number=1), 6)}s.")

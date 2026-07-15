import alchemy

if __name__ == "__main__":
    print(f"{alchemy.create_air()}")

    try:
        print(f"{alchemy.create_earth()}")
    except AttributeError as e:
        print(f"{e}")

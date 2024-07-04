def calculate_ares(base, height):
    print("__name__: ", __name__)
    return 1 / 2 * (base * height)


"""
if __name__ == "__main__" : It works like an entry point of any python program.
"""
if __name__ == "__main__":
    print("I am in area.py")
    a = calculate_ares(10, 20)
    print("area: ", a)

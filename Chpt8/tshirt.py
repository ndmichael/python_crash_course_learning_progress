def make_tshirt(size, writeup):
    print(f"Shirt size is {size},")
    print(f"{writeup}.")
    print("\n")

def cities(city, country="Nigeria"):
    print(f"{city} is in {country}.", end="\n")


make_tshirt(36, "Legendary")
make_tshirt(writeup="2Pac Shakur", size=34)

cities("Lagos")
cities("Aba")
cities("Munich", country="Germany")
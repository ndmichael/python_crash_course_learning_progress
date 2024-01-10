def city_country(city: str, country: str)->str:
    func_str = f"{city}, {country}".title()

    return func_str

for i in range(3):
    city = input("Enter a city: ")
    country = input("Enter the country: ")

    result = city_country(city, country)
    print(result, end="\n\n")
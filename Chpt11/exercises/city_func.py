def city_country(city: str, country: str, population: str='')-> str:
    """Returs a neatly formatted location"""
    if population:
        location = f"{city}, {country} - population {population}"
    else:
        location = f"{city}, {country}"
    return location.title()



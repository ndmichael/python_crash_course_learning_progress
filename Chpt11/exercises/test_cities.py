from city_func import city_country

def test_city_country():
    "is Lagos Nigera overhyped?"
    location = city_country('lagos', 'nigeria')
    assert location == "Lagos, Nigeria"


def test_city_country_population():
    "is Kano more populated than lagos?"
    location = city_country('kano', 'nigeria', "11,000,000")

    assert location == "Kano, Nigeria - Population 11,000,000"
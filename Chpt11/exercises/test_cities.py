from city_func import city_country


def test_city_country():
    "is Lagos, Nigeria overhyped"
    location = city_country('lagos', 'nigeria')

    assert location == "Lagos, Nigeria"
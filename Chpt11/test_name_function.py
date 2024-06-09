from name_func import get_formatted_name

def test_first_last_name():
    """Do names like janis and joplin work"""
    formatted_name = get_formatted_name("janis", "joplins")
    assert formatted_name == "Janis Joplins"

def test_first_last_middle_name():
    """Do you like Wolgang Amadeus Mozart"""
    formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
    assert formatted_name == "Wolfgang Amadeus Mozart"

from name_func import get_formatted_name

def test_first_last_name():
    """Do names like janis and joplin work"""
    formatted_name = get_formatted_name("janis", "joplins")
    assert formatted_name == "Janis Joplins"

def get_formatted_name(fname: str, lname: str, middle: str='')-> str:
    """Generate a neatly formatted fullname"""
    if middle:
        fullname = f"{fname} {middle} {lname}"
    else:
        fullname = f"{fname} {lname}"
    return fullname.title()



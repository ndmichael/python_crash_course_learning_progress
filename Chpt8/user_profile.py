def build_profile(fname='', lname='', *args):
    print("****--- MY PROFILE ---****")
    print("-" * 26)
    print(f"firstname: {fname.title()}")
    print(f"lastname: {lname.title()}")

    if args:
        for arg in args:
            print(f"{arg.capitalize()}")



build_profile("michael", "ukeje", "A software engineer", "30yrs old thug nigga")
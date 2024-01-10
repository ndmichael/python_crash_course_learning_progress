def make_cars(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs["model"] = model

    return kwargs


def car_details(details = {}):
    print("**** Car Details ****")
    print("-" * 21)
    if details:
        for k, v in details.items():
            print(f"{k}: {v}")


cars = make_cars("BENZ","S classics", color="red", sound=True)
car_details(cars)

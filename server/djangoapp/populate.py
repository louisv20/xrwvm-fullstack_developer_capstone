from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instance, created = CarMake.objects.get_or_create(name=data['name'], description=data['description'])
        car_make_instances.append(car_make_instance)

    # Print CarMake instances
    print("CarMakes:")
    for car_make in car_make_instances:
        print(car_make.name, car_make.description)

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = []

    car_models = [
        {"name": "Pathfinder", "car_type": "SUV"},
        {"name": "Qashqai", "car_type": "SUV"},
        {"name": "XTRAIL", "car_type": "SUV"},
        {"name": "A-Class", "car_type": "SUV"},
        {"name": "C-Class", "car_type": "SUV"},
        {"name": "E-Class", "car_type": "SUV"},
        {"name": "A4", "car_type": "SUV"},
        {"name": "A5", "car_type": "SUV"},
        {"name": "A6", "car_type": "SUV"},
        {"name": "Sorrento", "car_type": "SUV"},
        {"name": "Carnival", "car_type": "SUV"},
        {"name": "Cerato", "car_type": "Sedan"},
        {"name": "Corolla", "car_type": "Sedan"},
        {"name": "Camry", "car_type": "Sedan"},
        {"name": "Kluger", "car_type": "SUV"},
    ]

    for car_model_info in car_models:
        car_make_index = int(car_model_info['name'][0]) - 1  # Assuming the index corresponds to car make index
        car_model_info['car_make'] = car_make_instances[car_make_index]

        car_model_data.append(car_model_info)

    for data in car_model_data:
        CarModel.objects.create(name=data['name'], car_make=data['car_make'], car_type=data['car_type'], year=2023)  # Assuming year is constant

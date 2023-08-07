def get_value(data, key):
    """_summary_

    Args:
        nested_dict (_type_): _description_
        key (_type_): _description_
    """
    if key in data:
        return data[key]
    for _, v in data.items():
        if isinstance(v, dict):
            value = get_value(v, key)
            if value is not None:
                return value



if __name__ == "__main__":
    my_dict = {'firstName': 'Тимур',
            'lastName': 'Гуев',
            'birthDate': {'day': 10,
                          'month': 'October',
                          'year': 1993},
            'address': {'streetAddress': 'Часовая 25, кв. 127', 
                        'city': {'region': 'Московская область',
                                 'type': 'город',
                                 'cityName': 'Москва'},
                        'postalCode': '125315'}}
    print(get_value(my_dict, "cityName"))
def dict_travel(data):
    def rec(data, current_key=''):
        for k, v in sorted(data.items()):
            k = f"{current_key}.{k}" if current_key else k
            if isinstance(v, dict):
                rec(v, k)
            else:
                print(f"{k}: {v}")
    rec(data)


if __name__ == "__main__":
    my_data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
    dict_travel(my_data)
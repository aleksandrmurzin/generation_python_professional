def get_all_values(data, key):
    results = set()
    def rec(data, key):
        if key in data:
            results.add(data[key])
        for v in data.values():
            if isinstance(v, dict):
                rec(v, key)
    rec(data, key)
    return results

if __name__ == "__main__":
    my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
               'Timur': {'hobby': 'math'}}
    result = get_all_values(my_dict, "hs")
    print(*sorted(result))

    my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
    result = get_all_values(my_dict, 'top_grade')
    print(*sorted(result))

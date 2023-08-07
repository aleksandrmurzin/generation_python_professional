def linear(array):
    """_summary_

    Args:
        my_list (_type_): _description_

    Returns:
        _type_: _description_
    """
    linearized_list = []

    def rec(array):
        for i in array:
            if not isinstance(i, list):
                linearized_list.append(i)
            else:
                rec(array=i)
    rec(array=array)
    return linearized_list


if __name__ == "__main__":
    example = [3, [4], [5, [6, [7, 8]]]]
    print(linear(example))

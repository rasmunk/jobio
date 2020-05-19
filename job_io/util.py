def present_in(var, collection):
    if var not in collection:
        print("variable: {} not present in: {}".format(var, collection))
        return False
    return True


def validate_dict_types(input_dict, required_fields=None):
    if not required_fields:
        required_fields = {}
    for var, _type in required_fields.items():
        if not present_in(var, input_dict):
            return False
        if not isinstance(input_dict[var], _type):
            print(
                "variable: {} value: {} is of incorrect type: {}".format(
                    var, input_dict[var], type(input_dict[var])
                )
            )
            return False
    return True


def validate_dict_values(input_dict, required_values=None):
    if not required_values:
        required_values = {}

    for var, required_value in required_values.items():
        if not present_in(var, input_dict):
            return False
        if required_value and not input_dict[var]:
            print(
                "The required variable: {} was not set in: {}".format(var, input_dict)
            )
            return False
    return True
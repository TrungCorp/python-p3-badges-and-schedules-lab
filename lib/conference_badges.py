def badge_maker(name):
    name_string = f'Hello, my name is {name}.'
    return name_string

def batch_badge_creator(names):
    list_obj = []
    for name in names:
        string_obj = f"Hello, my name is {name}."
        list_obj.append(string_obj)
    return list_obj

def assign_rooms(names):
    list_obj = []
    counter = 1
    for name in names:
        string_obj = f"Hello, {name}! You'll be assigned to room {counter}!"
        list_obj.append(string_obj)
        counter += 1
    return list_obj

def printer(names):
    counter = 1
    for name in batch_badge_creator(names):
        print(name)
    for name in assign_rooms(names):
        print(name)
    return None

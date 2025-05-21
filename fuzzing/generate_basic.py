import random


def generate_char():
    return chr(random.randint(0, 0x10FFFF))


def generate_string():
    length = random.randint(0, 5)
    return ''.join(generate_char() for _ in range(length))


def generate_big_int():
    return random.randint(-2 ** 63, 2 ** 63 - 1) ** 100


def generate_int():
    return random.randint(-2 ** 63, 2 ** 63 - 1)


def generate_float():
    choice = random.choice(['normal', 'large', 'small', 'special'])

    if choice == 'normal':
        return random.uniform(-1e3, 1e3)

    elif choice == 'large':
        return random.uniform(1e100, 1e308) * random.choice([-1, 1])

    elif choice == 'small':
        return random.uniform(1e-308, 1e-100) * random.choice([-1, 1])

    elif choice == 'special':
        return random.choice([float('inf'), float('-inf'), float('nan')])


def generate_b_string():
    s = generate_string()
    return s.encode()


def generate_random_value(depth):
    options = [
        generate_int,
        generate_big_int,
        generate_string,
        generate_float,
        generate_b_string,
        lambda: None,
        lambda: True,
        lambda: False
    ]

    if depth <= 3:
        options += [
            lambda: generate_array(depth),
            lambda: generate_dict(depth)
        ]

    return random.choice(options)()


def generate_array(depth):
    arr = []
    for _ in range(random.randint(1, 5)):
        arr.append(generate_random_value(depth + 1))
    return arr


def generate_dict(depth):
    d = {}
    for _ in range(random.randint(1, 5)):
        key = generate_string()
        value = generate_random_value(depth + 1)
        d[key] = value
    return d


def generate_deep_array():
    a = []
    for i in range(300):
        a = [generate_int(), a]
    return a


def generate_deep_dict():
    a = {}
    for i in range(300):
        a = {generate_string(): a}
    return a

"""
    Module name :- utils.py
    Method(s) :- nested_prime(n), old_reverse_scholl(string), dict_a_noodle(a),
    fibonacci(n), fib_squares(a, b), flatten(list1), dict_of_lists(data),
    list_of_lists(data), compare_dict(dict1, dict2), dict_compare(*args),
    dict_from_lists(list1, list2), secret_message(message),
    combination_words(words, rows, cols, string = '', x=0, y=-1, words_combination = []),
    phone_words(ph1, ph2)
"""


def nested_prime(n):
    """
    Generates prime numbers upto n.

    Args:-
        n(int) :- End number.

    Return
        Prime numbers upto n.
    """
    return [
        num
        for num in range(2, n + 1)
        if not any(num % i == 0 for i in range(2, int(num**0.5) + 1))
    ]


def old_school_reverse(string):
    """
    Reverses a given string.

    Args:-
        string(str) :- String of characters.

    Return
        Reversed string.
    """
    return "".join(alpha for alpha in reversed(string))


def dict_a_noodle(a):
    """
    Swaps key-value pair if key is string.

    Args:-
        a(dict) :- A dictionary

    Return
        Modified dictionary.
    """
    return {
        (value if isinstance(key, str) else key): (
            key if isinstance(key, str) else value
        )
        for key, value in a.items()
    }


def fibonacci(n):
    """
    Generates fibonacci numbers upto n one at a time.

    Args:-
        n(int) :- End number.

    Return
        Fibonacci number.
    """
    a, b = 0, 1

    while a <= n:
        a, b = b, a + b
        yield a


def fib_squares(a, b):
    """
    Generates a list of numbers containing squares if number is
    fibonacci else a number.

    Args:-
        a(int):- Starting point of range.
        b(int) :- Ending point of range.

    Return
        Returns a list of numbers containing squares if number is
        fibonacci else a number
    """
    return [num**2 if num in fibonacci(b) else num for num in range(a, b + 1)]


def flatten(list1):
    """
    Flattens a Multi-dimensional list into 1D list.

    Args:-
        list1(list) :- A multi-dimensional lists.

    Return
        Flatten list.
    """
    list2 = []

    for element in list1:
        if isinstance(element, list):
            list2 += flatten(element)
        elif isinstance(element, dict):
            continue
        else:
            list2.append(element)

    return list2


def dict_of_lists(data):
    """
    Flatten a list of lists.

    Args:-
        data(dict) :- A list of lists.

    Return
        A dict containing element as key and their
        ocuurence as value.
    """
    data_list = flatten(data)
    key_value = {}

    for element in data_list:
        key_value[element] = key_value.get(element, 0) + 1

    return key_value


def list_of_lists(data):
    """
    Flatten a list of lists.

    Args:-
        data(dict) :- A list of lists.

    Return
        A list containing all elements.
    """
    data_list = flatten(data)
    numbers = []
    characters = []

    for element in set(data_list):
        if isinstance(element, str):
            characters.append(element)
        else:
            numbers.append(element)

    return sorted(numbers) + sorted(characters)


def compare_dict(dict1, dict2):
    """
    Compare two dictionaries.

    Args:
        dict1(dict) :- Dictionary 1
        dict2(dict) :- Dictionary 2

    Return
        True if both dictionaries are same else False.
    """

    if type(dict1) != type(dict2):
        return False

    if not (isinstance(dict1, dict) or isinstance(dict2, dict)):
        if (isinstance(dict1, list) and isinstance(dict2, list)) or (
            isinstance(dict1, tuple) and isinstance(dict2, tuple)
        ):
            return sorted(dict1) == sorted(dict2)
        return dict1 == dict2

    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1:
        if not compare_dict(dict1[key], dict2[key]):
            return False

    return True


def dict_compare(*args):
    """
    Compare list of dictionaries.

    Args:
        args(list) :- List of dictionaries

    Return
        List of compared dictionaries.
    """
    same_dict = []
    for index, dict1 in enumerate(args[: len(args) - 1]):
        for dict2 in args[index + 1 :]:
            if compare_dict(dict1, dict2):
                same_dict.append((dict1, dict2))

    return same_dict


def dict_from_lists(list1, list2):
    """
    Create a dictionary having elements of list1 as keys
    and list2 as values.

    Args:-
        list1(list) :- List 1
        list2(list) :- List 2

    Return
        Dictionary having elements of list1 as keys
        and list2 as values
    """
    return {str(key): value for key, value in zip(list1, list2)}


def secret_message(message):
    """
    Encode a message.

    Args:-
        message(str) :- Message

    Return
        Encoded message.
    """
    stripped_message = message.replace(" ", "")
    length = len(stripped_message)

    if length > 81:
        return None

    size = length**0.5
    size = int(size) if size == int(size) else int(size) + 1

    message_list = [stripped_message[i : i + size] for i in range(0, length, size)]

    coded_list = []

    for i in range(size):
        coded_message = ""
        for message in message_list:
            try:
                coded_message += message[i]
            except:
                pass
        coded_list.append(coded_message)

    return " ".join(coded_list)


def combination_words(words, rows, cols, string="", x=0, y=-1, words_combination=[]):
    """
    Combination of words in a list.

    Args:-
        words(list) :- List of words.
        rows(int) :- Length of list.
        cols(int) :- Length of string.

    Return
        All possible combination of words.
    """
    if y >= 0:
        string += words[y][x]

    if y == rows - 1:
        return words_combination.append(string)

    for x in range(cols):
        combination_words(words, rows, cols, string, x, y=y + 1)

    return words_combination


def phone_words(ph1, ph2):
    """
    Generates a dictionary containing phone number as key and all
    possible combination of words of the character on phone number.

    Args:
        ph1(int) :- Phone number 1.
        ph1(int) :- Phone number 2.

    Return
        Dictionary containing phone number as key and all
        possible combination of words of the character on phone number.
    """
    phone_list = [ph1, ph2]
    words = {
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PRS",
        "8": "TUV",
        "9": "XYZ",
    }

    words_list = []

    for i in range(2):
        phone_num_words = []
        phone_num = str(phone_list[i])
        for digit in phone_num:
            if "1" in phone_num or "0" in phone_num:
                break
            phone_num_words.append(words[digit])
        words_list.append(phone_num_words)

    phone_words_combination = {}

    for i in range(2):
        if words_list[i]:
            cols = len(words_list[i][0])
            phone_words_combination[str(phone_list[i])] = combination_words(
                words_list[i], len(words_list[i]), cols
            )
        else:
            phone_words_combination[str(phone_list[i])] = []

    return phone_words_combination


def set_complement(*args, verbose=False):
    """
    Find set complement of all posiible combination of
    lists in args.

    Args:-
        args(list) :- List of lists

    Return
        Set complement of all posiible combination of
        lists in args
    """
    complements = []

    for index, list1 in enumerate(args[: len(args) - 1]):
        for list2 in args[index + 1 :]:
            set_list1 = set(list1)
            set_list2 = set(list2)
            complements.append(list(set_list1 - set_list2))

    if verbose:
        complements += args

    return complements


def set_intersection(*args, verbose=False):
    """
    Find set intersection of all posiible combination of
    lists in args.

    Args:-
        args(list) :- List of lists

    Return
        Set intersection of all posiible combination of
        lists in args
    """
    complements = []

    for index, list1 in enumerate(args[: len(args) - 1]):
        for list2 in args[index + 1 :]:
            set_list1 = set(list1)
            set_list2 = set(list2)
            complements.append(list(set_list1 & set_list2))

    if verbose:
        complements += args

    return complements


if __name__ == "__main__":
    print(nested_prime(10))
    print(old_school_reverse("Akbar"))
    print(dict_a_noodle({1: "one", 2: "two", "three": 3}))
    print(fib_squares(2, 10))
    print(
        dict_of_lists(
            [
                [
                    [1, 2, 3],
                    [4, [5, 6]],
                    6,
                    [7, 8, 9],
                    [8, [8, 9, "a"], {5: 6}, ["b"], "ab"],
                ],
                [5, 2, 1],
                1,
            ]
        )
    )
    print(
        list_of_lists(
            [
                [
                    [1, 2, 3],
                    [4, [5, 6]],
                    6,
                    [7, 8, 9],
                    [8, [8, 9, "a"], {5: 6}, ["b"], "ab"],
                ],
                [5, 2, 1],
                1,
            ]
        )
    )
    print(
        dict_compare(
            {"a": 1, "b": {"c": 2, "d": 3}},
            {"a": 1, "b": {"c": 2, "d": 3}},
            {"a": 1, "b": {"c": 2, "d": [1, 4]}},
        )
    )
    print(dict_from_lists([1, 2, 3], ["a", "b", "c"]))
    print(
        secret_message(
            "If man was meant to stay on the ground god would have given us roots"
        )
    )
    print(set_complement([1, 2, 3], [1, 2], [2, 4]))
    print(set_intersection([1, 2, 3], [1, 2], [2, 4]))
    print(phone_words(1234567, 2345678))

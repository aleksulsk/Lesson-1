calls = 0


def count_calls():
    global calls
    calls = calls + 1
    return


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    global a
    count_calls()
    for i in list_to_search:
        if i.upper() == string.upper():
            return True
        elif i is not list_to_search:
            a = False
    return a


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

# Домашняя работа по уроку "Пространство имён"
#Задача "Счётчик вызовов"

calls = 0
def count_calls() :
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [string.lower() for string in list_to_search]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
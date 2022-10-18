list_of_words = ['python', 'java', 'c++', 'c']


# map function
def get_string_and_uppercase(word):
    return word.upper()


# first argument - function, second argument - iterable(collection like list, set)
# result is a iterator -> map object
result_map = map(get_string_and_uppercase, list_of_words)
result_map_with_lambda = map(lambda word: word.upper(), list_of_words)


# filter function
def filter_words(words):
    if words[0] == 'P' or words[0] == 'p':
        return True
    return False


result_filter = filter(filter_words, list_of_words)

# first argument - function, second argument - iterable(collection like list, set)
# result is a iterator -> filter object
result_filter_with_lambda = filter(lambda expression: expression[0] == 'p' or expression[0] == 'P', list_of_words)

# zip function
names = ['Marek', 'Janek', 'Piotrek']
ages = [11, 22, 33]
cities = ['Krakow', 'Warszawa', 'Poznan']

# first argument - iterable(collection like list, set)  * many iterables
# result is a iterator -> zip object
result_zip = zip(names, ages, cities)

if __name__ == '__main__':
    print(result_map)
    print(list(result_map))  # execute map function
    print(list(result_map_with_lambda))  # execute map function
    print(list(result_filter))  # execute filter function
    print(list(result_filter_with_lambda))  # execute filter function
    unzip = list(result_zip)  # execute zip function
    print(unzip)
    result_zip = zip(names, ages, cities)
    name, age, city = zip(*unzip)  # unzip data from list
    print(f'{name}, {age}, {city}')

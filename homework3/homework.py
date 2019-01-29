
def combine(_list1, _list2):
    """"Написать функцию, которая создаёт комбинацию
    двух списков таким образом:
    [a1, b1, c1, ...], [a2, b2, c2,...] -> [a1, a2, b1, b2, ...]
    """


def is_increase(_list):
    """
    Написать функцию, которая определяет , является ли список монотонно
    возрастающим(то есть верно ли, что каждый элемент
    этого списка больше предыдущего).
    """


def max_number_count(_list):
    """
    Написать функцию, которая
    определяет в списке наиболее встречаемое значение.
    Вернуть значение и количество повторений.
    """


def get_anagrams(_str, _list):
    """
    Написать функцию, которая находит все
    анаграмы заданного слова из списка слов
    """


# ## HARD ## #

def max_number(_list):
    """(*) Написать функцию, которая из списка чисел составляет
    максимальное число
    [234, 123, 98] -> 98234123
    """


if __name__ == '__main__':
    assert combine([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert combine([1, 2, 3], []) == [1, 2, 3]
    assert combine([1, 2], [3, 4, 5, 6]) == [1, 3, 2, 4, 5, 6]
    print('combine - OK')

    assert is_increase([1, 3, 4, 5]) is True
    assert is_increase([1, 3, 4, 4, 5]) is False
    assert is_increase([1, 6, 4]) is False
    assert is_increase([1]) is True
    assert is_increase([]) is None
    print('is_increase - OK')

    assert max_number_count([1, 2, 2, 3, 3, 3]) == (3, 2)
    assert max_number_count([1, 2, 3, 1, 1]) == (1, 3)
    print('max_number_count - OK')

    assert get_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']  # noqa
    assert get_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']  # noqa
    assert get_anagrams('laser', ['lazing', 'lazy',  'lacer']) == []
    print('get_anagrams - OK')

    assert max_number([234, 123, 98]) == 98234123
    assert max_number([1, 2, 3, 4]) == 4321
    assert max_number([]) is None
    assert max_number([98, 9, 34]) == 99834
    print('max_number - OK')
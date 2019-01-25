# 1. Написать функцию такую что
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"


def accum(_str):
    pass


assert accum("abcd") == "A-Bb-Ccc-Dddd"
assert accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
assert accum("cwAt") == "C-Ww-Aaa-Tttt"
print('1 - OK')


"""
2. You received a whatsup message from an unknown number. Could it be from
that girl/boy with a foreign accent you met yesterday evening?
Write a simple regex to check if the string contains the word hallo in
different languages.
These are the languages of the possible people you met the night before:

hello - english
ciao - italian
salut - french
hallo - german
hola - spanish
ahoj - czech republic
czesc - polish
By the way, how cool is the czech republic hallo!!
PS. you can assume the input is a string. PPS. to keep this a beginner
exercise you don't need to check if the greeting is a subset of word
('Hallowen' can pass the test)
PS. regex should be case insensitive to pass the tests
"""


def validate_hello(_str):
    pass


assert validate_hello('hello') is True
assert validate_hello('ciao bella!') is True
assert validate_hello('salut') is True
assert validate_hello('hallo, salut') is True
assert validate_hello('hombre! Hola!') is True
assert validate_hello('Hallo, wie geht\'s dir?') is True
assert validate_hello('AHOJ!') is True
assert validate_hello('czesc') is True
assert validate_hello('meh') is False
assert validate_hello('Ahoj') is True
assert validate_hello('Hallowen') is False
print('2 - ok')


"""
Exercise 3
Our football team finished the championship.
The result of each match look like "x:y".
Results of all matches are recorded in the array.

For example: ["3:1", "2:2", "0:1", ...]

Write a function that takes such list and counts
the points of our team in the championship.
Rules for counting points for each match:

if x>y - 3 points
if x<y - 0 point
if x=y - 1 point
Notes:

there are 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
"""


def points(games):
    pass


print("Basic Tests")
assert points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']) == 30  # noqa
assert points(['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '4:4']) == 10  # noqa
assert points(['0:1', '0:2', '0:3', '0:4', '1:2', '1:3', '1:4', '2:3', '2:4', '3:4']) == 0  # noqa
assert points(['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4', '3:4']) == 15  # noqa
assert points(['1:0', '2:0', '3:0', '4:4', '2:2', '3:3', '1:4', '2:3', '2:4', '3:4']) == 12  # noqa
print('3 - ok')

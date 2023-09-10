from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


#                                   ██
#              ██                   ▀▀
#  ▄▄█████▄  ███████    ██▄████   ████     ██▄████▄   ▄███▄██  ▄▄█████▄
#  ██▄▄▄▄ ▀    ██       ██▀         ██     ██▀   ██  ██▀  ▀██  ██▄▄▄▄ ▀
#   ▀▀▀▀██▄    ██       ██          ██     ██    ██  ██    ██   ▀▀▀▀██▄
#  █▄▄▄▄▄██    ██▄▄▄    ██       ▄▄▄██▄▄▄  ██    ██  ▀██▄▄███  █▄▄▄▄▄██
#   ▀▀▀▀▀▀      ▀▀▀▀    ▀▀       ▀▀▀▀▀▀▀▀  ▀▀    ▀▀   ▄▀▀▀ ██   ▀▀▀▀▀▀
#                                                     ▀████▀▀

message = "john is really cool. don't we think so?"
another_message = "HoNeY bAdGeR dOn'T cArE"
print(message.title())
print(message.upper())
print(message.swapcase())
print("john" in message)
print("badger" in another_message.casefold())
print("---[", "   wasted space   ".strip(), "]---")

for letter in "john":
    print(letter)

for index, letter in enumerate("durango"):
    print(index, letter)

# for each letter in "ziggy", replace it with a random letter from the alphabet 50% of the time and print the result
import random
import string

for letter in "ziggy":
    if random.random() < 0.5:
        print(random.choice(string.ascii_lowercase), end="")
    else:
        print(letter, end="")
print()

# print each character of "tux" in reverse order
for letter in reversed("tux"):
    print(letter, end="")
print()

#  ▄▄▄▄         ██
#  ▀▀██         ▀▀                 ██
#    ██       ████     ▄▄█████▄  ███████   ▄▄█████▄
#    ██         ██     ██▄▄▄▄ ▀    ██      ██▄▄▄▄ ▀
#    ██         ██      ▀▀▀▀██▄    ██       ▀▀▀▀██▄
#    ██▄▄▄   ▄▄▄██▄▄▄  █▄▄▄▄▄██    ██▄▄▄   █▄▄▄▄▄██
#     ▀▀▀▀   ▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀      ▀▀▀▀    ▀▀▀▀▀▀

# get a list from a string
print(list("john"))

# get a list from a comma-separated string
print("john, paul, george, ringo".split(", "))

# get a list from a string with a newline character
print("john\npaul\ngeorge\nringo".splitlines())

# split a string on whitespace
print("john paul george ringo".split())

# reverse a list
print(list(reversed("john")))

# reverse a list in place
beatles = ["john", "paul", "george", "ringo"]
beatles.reverse()
print(beatles)

# the second to last beatle
print(beatles[-2])

# the first two beatles
print(beatles[:2])

# the middle two beatles
print(beatles[1:3])

# all states that begin with "C"
states = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
]
print([state for state in states if state.startswith("C")])

# combine states and beatles
print("states and, uh, beatles:", states + beatles)

# is "john" in beatles?
print("is john in the beatles?", "john" in beatles)

# is "john" not in beatles?
print("is john not in the beatles?", "john" not in beatles)


#                                ▄▄▄▄
#    ██                          ▀▀██
#  ███████   ██    ██  ██▄███▄     ██       ▄████▄   ▄▄█████▄
#    ██      ██    ██  ██▀  ▀██    ██      ██▄▄▄▄██  ██▄▄▄▄ ▀
#    ██      ██    ██  ██    ██    ██      ██▀▀▀▀▀▀   ▀▀▀▀██▄
#    ██▄▄▄   ██▄▄▄███  ███▄▄██▀    ██▄▄▄   ▀██▄▄▄▄█  █▄▄▄▄▄██
#     ▀▀▀▀    ▀▀▀▀ ▀▀  ██ ▀▀▀       ▀▀▀▀     ▀▀▀▀▀    ▀▀▀▀▀▀
#                      ██
#
# - They're like lists, but immutable.
# - Parentheses instead of square brackets.
# - Can also just leave off the parentheses.
# - Many of the same operations as lists.

led_zeppelin = ("Jimmy Page", "Robert Plant", "John Bonham", "John Paul Jones")
print(led_zeppelin)

# A tuple with one element is a little weird. You have to include a trailing comma.
print(("john",))

#                        ██
#  ▄▄█████▄   ▄████▄   ███████   ▄▄█████▄
#  ██▄▄▄▄ ▀  ██▄▄▄▄██    ██      ██▄▄▄▄ ▀
#   ▀▀▀▀██▄  ██▀▀▀▀▀▀    ██       ▀▀▀▀██▄
#  █▄▄▄▄▄██  ▀██▄▄▄▄█    ██▄▄▄   █▄▄▄▄▄██
#   ▀▀▀▀▀▀     ▀▀▀▀▀      ▀▀▀▀    ▀▀▀▀▀▀
#
# - Like tuples, but mutable, and repeated elements are ignored.
# - Curly braces instead of parentheses.
# - Order is not guaranteed.

# a set of desserts
desserts = {"ice cream", "cookies", "pie", "cake", "ice cream", "cookies"}

# add "candy" to desserts
desserts.add("candy")

# remove "cookies" from desserts
desserts.remove("cookies")

# a set of birthday party foods
party_foods = {"ice cream", "cake", "cookies", "chips", "dip"}

# desserts that are also party foods (intersection)
print("desserts that are also party foods:", desserts & party_foods)

# desserts that are not party foods (difference)
print("desserts that are not party foods:", desserts - party_foods)

# foods that are desserts or party foods, but not both (symmetric difference)
print("foods that are desserts or party foods, but not both:", desserts ^ party_foods)

# foods that are desserts or party foods (union)
print("foods that are desserts or party foods:", desserts | party_foods)

# is "ice cream" in desserts?
print("is ice cream in desserts?", "ice cream" in desserts)

# how many desserts are also party foods?
print("how many desserts are also party foods?", len(desserts & party_foods))

#                                ▄▄
#                        ██      ██
#  ████▄██▄   ▄█████▄  ███████   ██▄████▄
#  ██ ██ ██   ▀ ▄▄▄██    ██      ██▀   ██
#  ██ ██ ██  ▄██▀▀▀██    ██      ██    ██
#  ██ ██ ██  ██▄▄▄███    ██▄▄▄   ██    ██
#  ▀▀ ▀▀ ▀▀   ▀▀▀▀ ▀▀     ▀▀▀▀   ▀▀    ▀▀
# aaaand some namespaces

import math

print("math.pi:", math.pi)
print("math.e:", math.e)
print("math.inf:", math.inf)

# now we can use these without the "math." prefix
# can also do "from math import *" to import everything,
# but that's not recommended because it can cause name collisions
from math import sin, cos, tau

print("tau:", tau)
print("sin(tau):", sin(tau))
print("cos(tau):", cos(tau))

#                                                                           ██
#                                                                           ▀▀
#   ▄█████▄   ▄████▄   ██▄████▄  ██▄  ▄██   ▄████▄    ██▄████  ▄▄█████▄   ████      ▄████▄   ██▄████▄  ▄▄█████▄
#  ██▀    ▀  ██▀  ▀██  ██▀   ██   ██  ██   ██▄▄▄▄██   ██▀      ██▄▄▄▄ ▀     ██     ██▀  ▀██  ██▀   ██  ██▄▄▄▄ ▀
#  ██        ██    ██  ██    ██   ▀█▄▄█▀   ██▀▀▀▀▀▀   ██        ▀▀▀▀██▄     ██     ██    ██  ██    ██   ▀▀▀▀██▄
#  ▀██▄▄▄▄█  ▀██▄▄██▀  ██    ██    ████    ▀██▄▄▄▄█   ██       █▄▄▄▄▄██  ▄▄▄██▄▄▄  ▀██▄▄██▀  ██    ██  █▄▄▄▄▄██
#    ▀▀▀▀▀     ▀▀▀▀    ▀▀    ▀▀     ▀▀       ▀▀▀▀▀    ▀▀        ▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀    ▀▀▀▀    ▀▀    ▀▀   ▀▀▀▀▀▀

str(42)
int(42)
# int("42.459")  # ValueError: invalid literal for int() with base 10: '42.459'
float(3)
float("3.14")

#               ██
#    ██         ▀▀
#  ███████    ████     ████▄██▄   ▄████▄   ▄▄█████▄
#    ██         ██     ██ ██ ██  ██▄▄▄▄██  ██▄▄▄▄ ▀
#    ██         ██     ██ ██ ██  ██▀▀▀▀▀▀   ▀▀▀▀██▄
#    ██▄▄▄   ▄▄▄██▄▄▄  ██ ██ ██  ▀██▄▄▄▄█  █▄▄▄▄▄██     ██
#     ▀▀▀▀   ▀▀▀▀▀▀▀▀  ▀▀ ▀▀ ▀▀    ▀▀▀▀▀    ▀▀▀▀▀▀      ██
#                                                      ▀▀
#        ▄▄                                             ██
#        ██              ██                  ██         ▀▀
#   ▄███▄██   ▄█████▄  ███████    ▄████▄   ███████    ████     ████▄██▄   ▄████▄   ▄▄█████▄
#  ██▀  ▀██   ▀ ▄▄▄██    ██      ██▄▄▄▄██    ██         ██     ██ ██ ██  ██▄▄▄▄██  ██▄▄▄▄ ▀
#  ██    ██  ▄██▀▀▀██    ██      ██▀▀▀▀▀▀    ██         ██     ██ ██ ██  ██▀▀▀▀▀▀   ▀▀▀▀██▄
#  ▀██▄▄███  ██▄▄▄███    ██▄▄▄   ▀██▄▄▄▄█    ██▄▄▄   ▄▄▄██▄▄▄  ██ ██ ██  ▀██▄▄▄▄█  █▄▄▄▄▄██
#    ▀▀▀ ▀▀   ▀▀▀▀ ▀▀     ▀▀▀▀     ▀▀▀▀▀      ▀▀▀▀   ▀▀▀▀▀▀▀▀  ▀▀ ▀▀ ▀▀    ▀▀▀▀▀    ▀▀▀▀▀▀

import time

# time in seconds since the epoch
print("time.time():", time.time())

# time in seconds since the epoch, as a tuple
print("time.gmtime():", time.gmtime())

# time in seconds since the epoch, as a tuple, but in local time
print("time.localtime():", time.localtime())

# time in seconds since the epoch, as a string
print("time.asctime():", time.asctime())  # same as time.asctime(time.localtime())

# time formatted as a string
print("time.strftime():", time.strftime("%Y-%m-%d %H:%M:%S"))

# time formatted as a string, but in local time
print("time.strftime():", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# time in seconds since the epoch, as ctime
print("time.ctime():", time.ctime())  # same as time.asctime(time.localtime())

from datetime import datetime  # common convention

moon_landing = datetime(1969, 7, 20, 20, 17, 40)
print("moon_landing:", moon_landing)


#   ██▄████   ▄████▄    ▄███▄██   ▄████▄   ▀██  ██▀
#   ██▀      ██▄▄▄▄██  ██▀  ▀██  ██▄▄▄▄██    ████
#   ██       ██▀▀▀▀▀▀  ██    ██  ██▀▀▀▀▀▀    ▄██▄
#   ██       ▀██▄▄▄▄█  ▀██▄▄███  ▀██▄▄▄▄█   ▄█▀▀█▄
#   ▀▀         ▀▀▀▀▀    ▄▀▀▀ ██    ▀▀▀▀▀   ▀▀▀  ▀▀▀
#                       ▀████▀▀

import re

# simple matching
result1 = re.search(r"optimus", "optimus prime, leader of the autobots")
result2 = re.search(r"optimus", "megatron, leader of the decepticons")
print("result1:", result1)  # <re.Match object; span=(0, 7), match='optimus'>
print("result2:", result2)  # None

if re.search(r"optimus", "optimus prime, leader of the autobots"):
    print("optimus found")
else:
    print("optimus not found")

# get all matches
names_beginning_with_j = re.findall(
    r"\b[jJ]\w+", "john paul george ringo jimi janis jim fred"
)
print(
    "names beginning with j:", names_beginning_with_j
)  # ['john', 'jimi', 'janis', 'jim']

# split on regexen. with no arguments, splits on whitespace
spacy_string = "a b     c"
print('re.split(r"s+"):', re.split(r"\s+", spacy_string))  # ['a', 'b', 'c']', 'c']
print(
    "spacy_string.split(' '):", spacy_string.split(" ")
)  # ['a', 'b', '', '', '', 'c']
print("spacy_string.split():", spacy_string.split())  # ['a', 'b', 'c']

#        ▄▄     ██
#        ██     ▀▀                 ██
#   ▄███▄██   ████      ▄█████▄  ███████   ▄▄█████▄
#  ██▀  ▀██     ██     ██▀    ▀    ██      ██▄▄▄▄ ▀
#  ██    ██     ██     ██          ██       ▀▀▀▀██▄
#  ▀██▄▄███  ▄▄▄██▄▄▄  ▀██▄▄▄▄█    ██▄▄▄   █▄▄▄▄▄██
#    ▀▀▀ ▀▀  ▀▀▀▀▀▀▀▀    ▀▀▀▀▀      ▀▀▀▀    ▀▀▀▀▀▀
# just like hashes in ruby or other, cooler languages
# as of Python 3.6, dictionaries are ordered by insertion order

# create a dictionary of companies and their stock symbols
companies = {"AAPL": "Apple", "GOOG": "Google", "MSFT": "Microsoft"}

print(companies.keys())  # dict_keys(['AAPL', 'GOOG', 'MSFT'])
print(companies.values())  # dict_values(['Apple', 'Google', 'Microsoft'])
print(companies["AAPL"])  # Apple

# iterate over the keys
for key in companies:
    print(key, companies[key])

for symbol, name in companies.items():
    print(name, ":", symbol)

# create a dictionary common elements and their symbols
elements_i_have = {"hydrogen": "H", "helium": "He", "carbon": "C", "oxygen": "O"}
# create a dictionary of rare elements and their symbols
rare_earth_elements = {"lanthanum": "La", "cerium": "Ce", "praseodymium": "Pr"}

# create a new dictionary that combines the two
elements = elements_i_have | rare_earth_elements
print("elements:", elements)

# combine the two dictionaries permanently
elements_i_have.update(rare_earth_elements)
print("elements_i_have:", elements_i_have)

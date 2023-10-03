import numbers
import string

#  This is how you would sort by values and return just the 3 highest ones
# myl = []
# medals = {
#     "Japan": 41,
#     "Russia": 56,
#     "South Korea": 21,
#     "United States": 121,
#     "Germany": 42,
#     "China": 70,
# }
# top_three = sorted(medals.items(), key=lambda x: x[1], reverse=True)
# # print(top_three)
# for t in top_three:
#     print(t[0])
#     if len(myl) < 3:
#         myl.append(t[0])
# # print(myl)
# print(myl)

# This is how you would create a new list that contained the keys of the dictionary in order by who has the most value
# most_needed = []
# groceries = {
#     "apples": 5,
#     "pasta": 3,
#     "carrots": 12,
#     "orange juice": 2,
#     "bananas": 8,
#     "popcorn": 1,
#     "salsa": 3,
#     "cereal": 4,
#     "coffee": 5,
#     "granola bars": 15,
#     "onions": 7,
#     "rice": 1,
#     "peanut butter": 2,
#     "spinach": 9,
# }

# for g, i in sorted(groceries.items(), key=lambda x: x[1], reverse=True):
#     print(g, i)
#     most_needed.append(g)
# print(most_needed)


# def last_four(x):
#     x = str(x)
#     print(x[-4:])
#     x = int(x[-4:])
#     return x


# print(last_four(123456789))


# def last_four(x):
#     myl = []
#     for i in x:
#         tos = str(i)
#         print(tos[-4:])
#         myl.append(tos[-4:])
#     return myl


# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
# sorted_ids = sorted(ids, key=lambda x: x[)
# # print(last_four(ids))
# print(sorted_ids)


# non-functional code
# punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", "#", "@", "%"]
# new_str = ""


# def strip_punctuation(x):
#     new_str = ""
#     print("This is the old string:" + x)
#     for ele in x:
#         if ele in punctuation_chars:
#             new_str = x.replace(ele, "")
#             print("This is the new string: " + new_str)
#     return new_str


# a = "%Amazing"
# b = "wow!"
# c = "Incrediable^$"
# d = "wonderful"
# strip_punctuation(a)
# strip_punctuation(b)
# strip_punctuation(c)
# strip_punctuation(d)


# c_chars = ["'", '"', ",", ".", "!", ":", ";", "#", "@"]


# def strip_punctuation(x):
#     myw = ""
#     table = str.maketrans("", "", string.punctuation)
#     stripped = [w.translate(table) for w in x]
#     # print(stripped)
#     print(myw.join(stripped))


# strip_punctuation("Amazing!")


# punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", "#", "@"]
# mypostotal = 0
# mynegtotal = 0
# mypos = 0
# myneg = 0
# mydata = []


# myfinal = []


# def my_fnc():
#     mydatalist = []
#     with open("project_twitter_data.csv") as projectfile:
#         for line in projectfile:
#             # print(line)
#             mypostotal = 0
#             mynegtotal = 0
#             mypos = 0
#             myneg = 0
#             mynet = 0
#             # print(line.split())
#             mypos = get_pos(line)
#             mypostotal = mypos + mypostotal
#             myneg = get_neg(line)
#             mynegtotal = myneg + mynegtotal
#             mynet = mypostotal - mynegtotal
#             myret = get_retweet(line)
#             myrep = get_replies(line)
#             print(myret, myrep, mypostotal, mynegtotal, mynet)
#             mydata = [myret, myrep, mypostotal, mynegtotal, mynet]
#             if myret != "retweet_count":
#                 print("Printing my information")
#                 myconvertdata = []
#                 for d in mydata:
#                     myconvertdata.append(str(d))
#                 print(myconvertdata)
#                 mydatalist.append(myconvertdata)
#     print("My datalist")
#     print(mydatalist)
#     input_data(mydatalist)


# # lists of words to use
# positive_words = []
# with open("positive_words.txt") as pos_f:
#     for lin in pos_f:
#         if lin[0] != ";" and lin[0] != "\n":
#             positive_words.append(lin.strip())


# negative_words = []
# with open("negative_words.txt") as pos_f:
#     for lin in pos_f:
#         if lin[0] != ";" and lin[0] != "\n":
#             negative_words.append(lin.strip())


# def strip_punctuation(x):
#     for char in punctuation_chars:
#         x = x.replace(char, "")
#     return x


# def get_neg(y):
#     mynegitivecount = 0
#     for word in y.split():
#         word = strip_punctuation(word)
#         # print(word)
#         for neg in negative_words:
#             if word.lower() == neg:
#                 mynegitivecount = mynegitivecount + 1
#     return mynegitivecount


# def get_pos(y):
#     mypositivecount = 0

#     for word in y.split():
#         word = strip_punctuation(word)
#         for pos in positive_words:
#             if word.lower() == pos:
#                 mypositivecount = mypositivecount + 1
#     return mypositivecount


# def get_retweet(y):
#     x = y.split()
#     # This is what gets the last string in line with the numbers
#     # print(x[-1:])
#     z = x[-1:]
#     for a in z:
#         # print(a.split(','))
#         b = a.split(",")
#         retweetc = b[1]
#         # print(retweetc)

#     # print('retweet slice: ' + y[3:0])
#     return retweetc


# def get_replies(y):
#     x = y.split()
#     z = x[-1:]
#     for a in z:
#         replyc = a[-1:]
#     return replyc


# filename = "resulting_data.csv"
# header = [
#     "Number of Retweets",
#     " Number of Replies",
#     " Positive Score",
#     " Negative Score",
#     " Net Score",
# ]
# data = []


# def input_data(mydatalist):
#     with open(filename, "w") as csvfile:

#         csvfile.write(",".join(header) + "\n")
#         for row in mydatalist:
#             csvfile.write(",".join(row) + "\n")


# my_fnc()

# the following is the last little bit of the project i was working on through coursera. It starts with you making function to strip punc, then you make a fnc that goes line by
# to strip punc, then ho wmany words are positive words, how many are negitive words, and stripping and splitting the last end of the lines to get the rt and the likes or something
# then once you go line by line and add this information into a list of lists, you then write the list os lists to a csv file which you can then work with in here!
# the code below takes that outputted csv file from coursera , goes through line by line getting the number of rt and net score, then adds then both to new separate lists which
# are then passed as arguements to matlabs fnc that display information for us.


# import itertools
# import matplotlib.pyplot as plt

# myretlist = []
# mynetlist = []
# myfinalnet = []
# with open("resulting_data.csv", "r") as pf:
#     for row in pf:
#         # print(row.split())
#         row = row.split(",")
#         print("Printing split row")
#         print(row)
#         print("~~~~~~~~~~~~~~~~")
#         print(row[-1])
#         net_score = row[-1]
#         print(row[0])
#         retweets = row[0]
#         mynetlist.append(net_score)
#         myretlist.append(retweets)
#     print(myretlist)
#     print(mynetlist)
#     myretlist.pop(0)
#     mynetlist.pop(0)
#     print(mynetlist)
#     for r in mynetlist:
#         r = r.split("\n")
#         print(r)
#         u = r[0]
#         myfinalnet.append(u)
#     print(myretlist)
#     print(myfinalnet)
#     # plt.scatter(myfinalnet, myretlist, s=30)
#     plt.xlabel("Net Score")
#     plt.ylabel("Number of Retweets")
#     plt.title("Twitter Sentiment Classifier")

#     int_list = list(map(int, myretlist))
#     print("int list")
#     # int_list.sort()
#     print(int_list)
#     net_list = list(map(int, myfinalnet))
#     print("net to int")
#     # net_list.sort()
#     print(net_list)
#     # newnet, newret = zip(*sorted(zip(net_list, int_list)))
#     # newnet, newret = zip(*sorted(zip(myfinalnet, myretlist)))
#     # plt.scatter(newnet, newret, s=30)
#     # myretlist.sort()
#     # myfinalnet.sort(reverse=False)
#     # print(myretlist)
#     # print(myfinalnet)
#     plt.scatter(net_list, int_list)

#     # plt.xlim(-10, 100)
#     # plt.ylim(-5, 5)
#     plt.show()

# the following is an example of how to get snake though indexing.

# nested = [
#     ["dog", "cat", "horse"],
#     ["frog", "turtle", "snake", "gecko"],
#     ["hamster", "gerbil", "rat", "ferret"],
# ]
# output = nested[1][2]
# print(str(output))

# Below is examples of using if and indexing to see if something exists.
# lst = [
#     ["apple", "orange", "banana"],
#     [5, 6, 7, 8, 9.9, 10],
#     ["green", "yellow", "purple", "red"],
# ]
# yellow = bool
# four = bool
# orange = bool
# # Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
# if "yellow" in lst[2]:
#     yellow = True
# if 4 in lst[1]:
#     four = True
# if "orange" in lst[0]:
#     orange = True

# Test to see if 4 is in the second list of lst. Save to variable ``four``


# Test to see if 'orange' is in the first element of lst. Save to variable ``orange``

# L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# # Test if 'hola' is in the list L. Save to variable name test1
# if 'hola' in L[1]:
#     test1 = True
# # Test if [5, 8, 7] is in the list L. Save to variable name test2
# if [5, 8, 7] in L:
#     test2 = True
# # Test if 6.6 is in the third element of list L. Save to variable name test3
# if 6.6 in L[2]:
#     test3 = True


# nested = {
#     "data": ["finding", 23, ["exercises", "hangout", 34]],
#     "window": [
#         "part",
#         "whole",
#         [],
#         "sum",
#         [
#             "math",
#             "calculus",
#             "algebra",
#             "geometry",
#             "statistics",
#             ["physics", "chemistry", "biology"],
#         ],
#     ],
# }

# Check to see if the string 'data' is a key in nested, if it is, assign True to the variable data, otherwise assign False.
# print(list(nested))
# if "data" in list(nested):
#     data = True
# else:
#     data = False
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
# for k, v in nested.items():
#     print(k, v)
#     if k == "data":
#         if v == 24:
#             twentyfour = True
#         else:
#             twentyfour = False
# print(twentyfour)
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
# for k, v in nested.items():
#     print(k, v)
#     if k == "window":
#         whole = False
#     else:
#         whole = True
# # Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
# for k, v in nested.items():
#     print(k, v)
#     if k == "Physics":
#         physics = True
#     else:
#         physics = False

# Getting at elements with indexing. first the list, then the key, then key within the dictionary
# nested_d = {
#     "Beijing": {"China": 51, "USA": 36, "Russia": 22, "Great Britain": 19},
#     "London": {"USA": 46, "China": 38, "Great Britain": 29, "Russia": 22},
#     "Rio": {"USA": 35, "Great Britain": 22, "China": 20, "Germany": 13},
# }
# london_gold = nested_d["London"]["Great Britain"]
# print(london_gold)


# sports = {
#     "swimming": ["butterfly", "breaststroke", "backstroke", "freestyle"],
#     "diving": ["springboard", "platform", "synchronized"],
#     "track": ["sprint", "distance", "jumps", "throws"],
#     "gymnastics": {
#         "women": ["vault", "floor", "uneven bars", "balance beam"],
#         "men": ["vault", "parallel bars", "floor", "rings"],
#     },
# }

# # Assign the string 'backstroke' to the name v1
# v1 = sports["swimming"][2]
# # Assign the string 'platform' to the name v2
# v2 = sports["diving"][1]
# # Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
# v3 = sports["gymnastics"]["women"]
# # Assign the string 'rings' to the name v4
# v4 = sports["gymnastics"]["men"][-1]
# print(v4)

# US_count = []
# nested_d = {
#     "Beijing": {"China": 51, "USA": 36, "Russia": 22, "Great Britain": 19},
#     "London": {"USA": 46, "China": 38, "Great Britain": 29, "Russia": 22},
#     "Rio": {"USA": 35, "Great Britain": 22, "China": 20, "Germany": 13},
# }
# total = 0
# for k, v in nested_d.items():
#     print(k, v)
#     for name, count in v.items():
#         if name == "USA":
#             US_count.append(count)
# print(US_count)
# third = []
# l_of_l = [
#     ["purple", "mauve", "blue"],
#     ["red", "maroon", "blood orange", "crimson"],
#     ["sea green", "cornflower", "lavender", "indigo"],
#     ["yellow", "amarillo", "mac n cheese", "golden rod"],
# ]

# for i in l_of_l:
#     print(i[2])
#     third.append(i[2])
# for a in i:
#     print(a)

# How to append the name if it has the letter 't', if it DOES - append to list t. ELSE - adds to list other

# other = []
# t = []
# athletes = [
#     ["Phelps", "Lochte", "Schooling", "Ledecky", "Franklin"],
#     ["Felix", "Bolt", "Gardner", "Eaton"],
#     ["Biles", "Douglas", "Hamm", "Raisman", "Mikulak", "Dalton"],
# ]
# for a in athletes:
#     print(a)
#     for b in a:
#         # print(b)
#         for c in b:
#             if c == "t":
#                 print(c)
#                 t.append(b)

# for a in athletes:
#     for b in a:
#         if b not in t:
#             other.append(b)
# print(t)
# print(other)

# how you would add a 'fruit :' string to the beginning of each string element in the list to create a new string 'fruit + x' using the map function. It takes a function
# and a paramenter as an arguement and returns values that are only easily displayed within the list() function.

# map_testing = []
# lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
# def add_fruit(x):
#     return "Fruit: " + x
# map_testing = map(add_fruit, lst_check)
# map_testing = list(map_testing)
# print(list(map_testing))


# countries = [
#     "Canada",
#     "Mexico",
#     "Brazil",
#     "Chile",
#     "Denmark",
#     "Botswana",
#     "Spain",
#     "Britain",
#     "Portugal",
#     "Russia",
#     "Thailand",
#     "Bangladesh",
#     "Nigeria",
#     "Argentina",
#     "Belarus",
#     "Laos",
#     "Australia",
#     "Panama",
#     "Egypt",
#     "Morocco",
#     "Switzerland",
#     "Belgium",
# ]
# b_countries = []
# for c in countries:
#     if c.startswith("B"):
#         print(c)
#         b_countries.append(c)
# print(b_countries)


# this is how you would use filter to seperate the countries that start with B from the ones that don't.
# myl = []
# countries = [
#     "Canada",
#     "Mexico",
#     "Brazil",
#     "Chile",
#     "Denmark",
#     "Botswana",
#     "Spain",
#     "Britain",
#     "Portugal",
#     "Russia",
#     "Thailand",
#     "Bangladesh",
#     "Nigeria",
#     "Argentina",
#     "Belarus",
#     "Laos",
#     "Australia",
#     "Panama",
#     "Egypt",
#     "Morocco",
#     "Switzerland",
#     "Belgium",
# ]

# myl = []


# def clear(alist):
#     if "B" in alist:
#         return True
#     else:
#         return False


# b_countries = filter(clear, countries)
# b_countries = list(b_countries)
# print(list(b_countries))


# def clear(word):
#     if "b" in word:
#         return True
#     else:
#         return False


# def fun(asslist):
#     for word in asslist:
#         filter(clear, word)


# print(fun(countries))

# How you would use list comprehesion to get the first item of every element of the list
# people = [
#     ("Snow", "Jon"),
#     ("Lannister", "Cersei"),
#     ("Stark", "Arya"),
#     ("Stark", "Robb"),
#     ("Lannister", "Jamie"),
#     ("Targaryen", "Daenerys"),
#     ("Stark", "Sansa"),
#     ("Tyrell", "Margaery"),
#     ("Stark", "Eddard"),
#     ("Lannister", "Tyrion"),
#     ("Baratheon", "Joffrey"),
#     ("Bolton", "Ramsey"),
#     ("Baelish", "Peter"),
# ]


# myl = [p[1] for p in people]
# print(myl)

# using list comprehesion to double elements
# lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

# myl = [w * 2 for w in lst]
# print(myl)


# how you would use list comp to get all students who got 70 or greater, and then add their first names to a list


# students = [
#     ("Tommy", 95),
#     ("Linda", 63),
#     ("Carl", 70),
#     ("Bob", 100),
#     ("Raymond", 50),
#     ("Sue", 75),
# ]

# myl = [s[0] for s in students if s[1] > 70]
# print(myl)

# import string

# l1 = ["left", "up", "front"]
# l2 = ["right", "down", "back"]

# myl = list(zip((l1), (l2), strict=True))
# # print(myl)


# # def char_test(myl, myl2):
# #     opposites = []
# #     myl = [a for a in myl if len(a) > 3]
# #     myl2 = [b for b in myl2 if len(b) > 3]
# #     for a in l1:
# #         for b in l2:
# #             opposites = list(zip((l1), (l2)))
# #     for l, n in opposites:
# #         if len(l) < 2:
# #             l = ""
# #         if len(n) < 2:
# #             n = ""
# #     print(opposites)
# #     return opposites


# def char_test(l1, l2):
#     print(l1, l2)
#     for x, y in l1, l2:
#         if len(x) > 3 and len(y) > 3:
#             myz = zip(x, y)
#             print(myz)


# char_test(l1, l2)


# class Solution(object):
#     def longestPalindrome(s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         char_count = {}
#         for char in s:
#             char_count[char] = char_count.get(char, 0) + 1
#         final_count = 0
#         for char in char_count:
#             if char_count[char] % 2 == 0:
#                 print(char_count[char])


# Solution.longestPalindrome("abccccdd")


l1 = ["left", "up", "front"]
l2 = ["right", "down", "back"]
new1 = []
new2 = []
opposites = []
i = 0


def check_length(word):
    if len(word) > 3:
        return True
    else:
        return False


# def char_test(myl1, myl2):
#     myf = filter(check_length, myl1)
#     # print(list(myf))
#     myf2 = filter(check_length, myl2)
#     # print(list(myf2))
#     as1 = list(myf)
#     as2 = list(myf2)
#     # print(as1, as2)
#     # opposites = zip(as1, as2)
#     # print(list(opposites))
#     # print(as1, as2)
#     tryingnew = [a for a in zip(as1, as2) if len(a[0]) > 3 and len(a[1]) > 3]
#     for item in tryingnew:
#         print(list(item))
#     opposites = list(
#         filter(
#             lambda x: len(x[0]) > 3 and len(x[1]) > 3,
#         )
#     )


# char_test(l1, l2)
# # print(char_test)
# # print(new1, new2)


# species = [
#     "golden retriever",
#     "white tailed deer",
#     "black rhino",
#     "brown squirrel",
#     "field mouse",
#     "orangutan",
#     "sumatran elephant",
#     "rainbow trout",
#     "black bear",
#     "blue whale",
#     "water moccasin",
#     "giant panda",
#     "green turtle",
#     "blue jay",
#     "japanese beetle",
# ]

# population = [
#     10000,
#     90000,
#     1000,
#     2000000,
#     500000,
#     500,
#     1200,
#     8000,
#     12000,
#     2300,
#     7500,
#     100,
#     1800,
#     9500,
#     125000,
# ]


# myz = list(zip(species, population))
# print(list(myz))
# new12 = [a for (a, b) in myz if b < 2500]
# print(new12)


# import requests
# import json

# page = requests.get("https://dog.ceo/api/breeds/list/all")
# print(page.text)

# x = page.json()
# print(json.dumps(x, indent=2))
# # y = json.loads(page.text)
# # print(y)

# import requests
# import json

# kval_pairs = {"ml": "acid"}
# page = requests.get("https://api.datamuse.com/words", params=kval_pairs)

# # print(page.text)

# x = page.json()
# print(json.dumps(x, indent=2))

# import requests

# # def get_movies_from_tastedive(movie):
# #     q = movie
# #     kval_pairs = {'q':movie,'type':'movies'}
# #     print(q)
# #     page = requests_with_caching.get('https://tastedive.com/api', params=kval_pairs)

# def get_movie_data(user_input):
#     url = 'http://www.omdbapi.com/'
#     params = {}
#     params['r'] = 'json'
#     params['t'] = user_input
#     mycache = requests_with_caching.get(url, params=params)
#     return json.loads(mycache.text)

# def get_movie_rating(dic):
#     print(dic)


#    # some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2")


# class Pokemon(object):
#     attack = 12
#     defense = 10
#     health = 15
#     p_type = "Normal"

#     def __init__(self, name, level=5):
#         self.name = name
#         self.level = level

#     def train(self):
#         self.update()
#         self.attack_up()
#         self.defense_up()
#         self.health_up()
#         self.level = self.level + 1
#         if self.level % self.evolve == 0:
#             return self.level, "Evolved!"
#         else:
#             return self.level

#     def attack_up(self):
#         self.attack = self.attack + self.attack_boost
#         return self.attack

#     def defense_up(self):
#         self.defense = self.defense + self.defense_boost
#         return self.defense

#     def health_up(self):
#         self.health = self.health + self.health_boost
#         return self.health

#     def update(self):
#         self.health_boost = 5
#         self.attack_boost = 3
#         self.defense_boost = 2
#         self.evolve = 10

#     def __str__(self):
#         return "Pokemon name: {}, Type: {}, Level: {}".format(
#             self.name, self.p_type, self.level
#         )


# class Grass_Pokemon(Pokemon):
#     attack = 15
#     defense = 14
#     health = 12
#     p_type = "Grass"

#     def update(self):
#         self.health_boost = 6
#         self.attack_boost = 2
#         self.defense_boost = 3
#         self.evolve = 12

#     def moves(self):
#         self.p_moves = ["razor leaf", "synthesis", "petal dance"]

#     def attack_boost(self):
#         self.attack = self.attack + self.attack_boost


# p2 = Grass_Pokemon("Bulby")
# p3 = Grass_Pokemon("Pika", 11)
# print(p2.attack)
# print(p3.attack)


# PASTE YOUR WOFPlayer CLASS (from part A) HERE
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return f"{self.name} (${self.prizeMoney})"


# PASTE YOUR WOFHumanPlayer CLASS (from part B) HERE
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        print(
            f"""{self.name} has ${self.prizeMoney}

Category: {category}
Phrase:  {obscuredPhrase}
Guessed: {guessed}

Guess a letter, phrase, or type 'exit' or 'pass':"""
        )
        userin = input()

        return userin


# PASTE YOUR WOFComputerPlayer CLASS (from part C) HERE
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"

    def __init__(self, name, difficulty):
        self.difficulty = difficulty
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def smartCoinFlip(self):
        myr = random.randint(1, 10)
        if self.difficulty > myr:
            return True
        else:
            return False

    def getPossibleLetters(gussed):
        for g in gussed:
            if g in letters:
                letters.remove(g)
        return letters

    def getMove(self, category, obscuredPhrase, guessed):
        return f"""{self.name} has ${self.prizeMoney}

Category: {category}
Phrase:  {obscuredPhrase}
Guessed: {guessed}

Guess a letter, phrase, or type 'exit' or 'pass':"""


import sys

# sys.setExecutionLimit(600000)  # let this take up to 10 minutes

import json
import random
import time

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
VOWELS = "AEIOU"
VOWEL_COST = 250

# Repeatedly asks the user for a number between min & max (inclusive)
def getNumberBetween(prompt, min, max):
    userinp = input(prompt)  # ask the first time

    while True:
        try:
            n = int(userinp)  # try casting to an integer
            if n < min:
                errmessage = "Must be at least {}".format(min)
            elif n > max:
                errmessage = "Must be at most {}".format(max)
            else:
                return n
        except ValueError:  # The user didn't enter a number
            errmessage = "{} is not a number.".format(userinp)

        # If we haven't gotten a number yet, add the error message
        # and ask again
        userinp = input("{}\n{}".format(errmessage, prompt))


# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }
def spinWheel():
    with open("wheel.json", "r") as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)


# Returns a category & phrase (as a tuple) to guess
# Example:
#     ("Artist & Song", "Whitney Houston's I Will Always Love You")
def getRandomCategoryAndPhrase():
    with open("phrases.json", "r") as f:
        phrases = json.loads(f.read())

        category = random.choice(list(phrases.keys()))
        phrase = random.choice(phrases[category])
        return (category, phrase.upper())


# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"
def obscurePhrase(phrase, guessed):
    rv = ""
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv + "_"
        else:
            rv = rv + s
    return rv


# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(
        category, obscuredPhrase, ", ".join(sorted(guessed))
    )


# GAME LOGIC CODE
print("=" * 15)
print("WHEEL OF PYTHON")
print("=" * 15)
print("")

num_human = getNumberBetween("How many human players?", 0, 10)

# Create the human player instances
human_players = [
    WOFHumanPlayer(input("Enter the name for human player #{}".format(i + 1)))
    for i in range(num_human)
]

num_computer = getNumberBetween("How many computer players?", 0, 10)

# If there are computer players, ask how difficult they should be
if num_computer >= 1:
    difficulty = getNumberBetween("What difficulty for the computers? (1-10)", 1, 10)

# Create the computer player instances
computer_players = [
    WOFComputerPlayer("Computer {}".format(i + 1), difficulty)
    for i in range(num_computer)
]

players = human_players + computer_players

# No players, no game :(
if len(players) == 0:
    print("We need players to play!")
    raise Exception("Not enough players")

# category and phrase are strings.
category, phrase = getRandomCategoryAndPhrase()
# guessed is a list of the letters that have been guessed
guessed = []

# playerIndex keeps track of the index (0 to len(players)-1) of the player whose turn it is
playerIndex = 0

# will be set to the player instance when/if someone wins
winner = False


def requestPlayerMove(player, category, guessed):
    while (
        True
    ):  # we're going to keep asking the player for a move until they give a valid one
        time.sleep(
            0.1
        )  # added so that any feedback is printed out before the next prompt

        move = player.getMove(category, obscurePhrase(phrase, guessed), guessed)
        move = move.upper()  # convert whatever the player entered to UPPERCASE
        if move == "EXIT" or move == "PASS":
            return move
        elif len(move) == 1:  # they guessed a character
            if (
                move not in LETTERS
            ):  # the user entered an invalid letter (such as @, #, or $)
                print("Guesses should be letters. Try again.")
                continue
            elif move in guessed:  # this letter has already been guessed
                print("{} has already been guessed. Try again.".format(move))
                continue
            elif (
                move in VOWELS and player.prizeMoney < VOWEL_COST
            ):  # if it's a vowel, we need to be sure the player has enough
                print("Need ${} to guess a vowel. Try again.".format(VOWEL_COST))
                continue
            else:
                return move
        else:  # they guessed the phrase
            return move


while True:
    player = players[playerIndex]
    wheelPrize = spinWheel()

    print("")
    print("-" * 15)
    print(showBoard(category, obscurePhrase(phrase, guessed), guessed))
    print("")
    print("{} spins...".format(player.name))
    time.sleep(2)  # pause for dramatic effect!
    print("{}!".format(wheelPrize["text"]))
    time.sleep(1)  # pause again for more dramatic effect!

    if wheelPrize["type"] == "bankrupt":
        player.goBankrupt()
    elif wheelPrize["type"] == "loseturn":
        pass  # do nothing; just move on to the next player
    elif wheelPrize["type"] == "cash":
        move = requestPlayerMove(player, category, guessed)
        if move == "EXIT":  # leave the game
            print("Until next time!")
            break
        elif move == "PASS":  # will just move on to next player
            print("{} passes".format(player.name))
        elif len(move) == 1:  # they guessed a letter
            guessed.append(move)

            print('{} guesses "{}"'.format(player.name, move))

            if move in VOWELS:
                player.prizeMoney -= VOWEL_COST

            count = phrase.count(
                move
            )  # returns an integer with how many times this letter appears
            if count > 0:
                if count == 1:
                    print("There is one {}".format(move))
                else:
                    print("There are {} {}'s".format(count, move))

                # Give them the money and the prizes
                player.addMoney(count * wheelPrize["value"])
                if wheelPrize["prize"]:
                    player.addPrize(wheelPrize["prize"])

                # all of the letters have been guessed
                if obscurePhrase(phrase, guessed) == phrase:
                    winner = player
                    break

                continue  # this player gets to go again

            elif count == 0:
                print("There is no {}".format(move))
        else:  # they guessed the whole phrase
            if move == phrase:  # they guessed the full phrase correctly
                winner = player

                # Give them the money and the prizes
                player.addMoney(wheelPrize["value"])
                if wheelPrize["prize"]:
                    player.addPrize(wheelPrize["prize"])

                break
            else:
                print("{} was not the phrase".format(move))

    # Move on to the next player (or go back to player[0] if we reached the end)
    playerIndex = (playerIndex + 1) % len(players)

if winner:
    # In your head, you should hear this as being announced by a game show host
    print("{} wins! The phrase was {}".format(winner.name, phrase))
    print("{} won ${}".format(winner.name, winner.prizeMoney))
    if len(winner.prizes) > 0:
        print("{} also won:".format(winner.name))
        for prize in winner.prizes:
            print("    - {}".format(prize))
else:
    print("Nobody won. The phrase was {}".format(phrase))

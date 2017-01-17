from nationLoader import *
from visualizationinsteps import *
from visualization import *
import json

map = {"Volyn": [["Lviv", "Rivne"], 1], "Kiev": [["Vinnytsia", "Cherkasy", "Chernihiv", "Zhytomyr", "Poltava"], 2], "Mykolaiv": [["Odessa", "Kirovohrad", "Dnipropetrovsk", "Kherson"], 1], "Khmelnytskyi": [["Zhytomyr", "Vinnytsia", "Chernivtsi", "Ternopil", "Rivne"], 2], "Zakarpattia": [["Lviv", "Ivano"], 1], "Chernivtsi": [["Ivano", "Ternopil", "Khmelnytskyi", "Vinnytsia"], 1], "Odessa": [["Mykolaiv", "Kirovohrad", "Vinnytsia"], 2], "Chernihiv": [["Kiev", "Poltava", "Sumy"], 1], "Kherson": [["Mykolaiv", "Dnipropetrovsk", "Zaporizhia", "Crimea"], 3], "Sumy": [["Chernihiv", "Poltava", "Kharkiv"], 2], "Cherkasy": [["Kiev", "Poltava", "Kirovohrad", "Vinnytsia"], 1], "Lviv": [["Volyn", "Rivne", "Ternopil", "Ivano", "Zakarpattia"], 2], "Zhytomyr": [["Rivne", "Khmelnytskyi", "Vinnytsia", "Kiev"], 1], "Dnipropetrovsk": [["Poltava", "Kharkiv", "Donetsk", "Zaporizhia", "Kherson", "Mykolaiv", "Kirovohrad"], 2], "Kirovohrad": [["Mykolaiv", "Dnipropetrovsk", "Poltava", "Cherkasy", "Vinnytsia", "Odessa"], 4], "Poltava": [["Sumy", "Kharkiv", "Dnipropetrovsk", "Kirovohrad", "Cherkasy", "Kiev", "Chernihiv"], 3], "Zaporizhia": [["Kherson", "Dnipropetrovsk", "Donetsk"], 1], "Kharkiv": [["Sumy", "Poltava", "Dnipropetrovsk", "Donetsk", "Luhansk"], 1], "Vinnytsia": [["Khmelnytskyi", "Chernivtsi", "Zhytomyr", "Kiev", "Cherkasy", "Kirovohrad", "Odessa"], 3], "Rivne": [["Volyn", "Lviv", "Ternopil", "Khmelnytskyi", "Zhytomyr"], 3], "Ternopil": [["Chernivtsi", "Ivano", "Lviv", "Rivne", "Khmelnytskyi"], 4], "Donetsk": [["Zaporizhia", "Dnipropetrovsk", "Kharkiv", "Luhansk"], 3], "Luhansk": [["Kharkiv", "Donetsk"], 2], "Crimea": [["Kherson"], 1], "Ivano": [["Zakarpattia", "Lviv", "Ternopil", "Chernivtsi"], 3]}
nation = nationLoader("Ukraine.txt")

colorNation(nation, "UkraineBnB")

counter = 0
for key in nation:
    counter += 1
    jsonPath = "JSON/" + "UkraineBnB" + "/Step" + str(counter) + ".txt"
    nation[key][1] = map[key][1]
    json.dump(nation, open(jsonPath, 'w'))

colorNationInSteps("UkraineBnB")


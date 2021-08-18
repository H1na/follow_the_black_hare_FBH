import sqlite3
import xml.etree.ElementTree as ET
from html import unescape  

import sys

def get_scenario_xml(filename):
    con = sqlite3.connect(filename)
    cursor = con.cursor()
    res = cursor.execute("SELECT text FROM scenario WHERE is_draft = 0").fetchall()
    return res[0][0]

def save_file(scenario, filename):
    with open(filename, "w") as f:
        print(scenario, file=f)

def prepate_renpy_output(res):
    output = "\n".join(res)
    return output.replace("\t", "    ")

characters = {
    "АШ": "black",
    "ВЕЧНА": 'vechna',
    
    "ВЕЧНА ЦИФРОВАЯ": 'digital_vechna',
    "МАКСИМ": 'max',
    "ОНКА": 'onka',
    "ОБЛАЧНЫЙ ЛИС": 'fox',
    "ЛИС": 'fox',

    "РОБОТИЗИРОВАННЫЙ ГОЛОС ЦК": '',
    "ГОЛОС ИЗ СЕТИ": '',
    "ЦЕНТР ПОМОЩИ": '',
    "КАМЕРА": "",
    "ГОЛОС МУЛЬТЯШКИ": '',
    "МОБИЛЬНАЯ КАМЕРА": '',
    "АЛИСА": '',
    "ЖУРНАЛИСТ": '',

    "НАТАША": 'stub_character',
    "ДРУГОЙ ЛИС": 'stub_character',
    "ЛИС ИЗ КАСТЫ 3": 'stub_character',
    
    "МУЖЧИНА": 'stub_character',
    "ЧЕРНЫЙ ЗАЯЦ": "black",
}

characters_mood = {
    "black": "regular",
    'vechna': 'regular',
    'digital_vechna': 'regular',
    'stub_character': 'mouse1',
    'fox': 'regular',
}

file = "./Follow The Black Hare [FBH].kitsp"

if(len(sys.argv) > 1):
    file = sys.argv[1]

scenario = get_scenario_xml(file)
save_file(scenario, "scenario.xml")

root = ET.fromstring(scenario)

res = []
scene_counter = 1

character = None

for item in root:
    # print(item.tag)
    
    text = item.find("v").text
    print(text)
    if(text):
        text = text.replace("&quot;", "\\\"")

    if(not text): #skipping empty blocks
        continue
    
    if(item.tag == "scene_heading"): #scene title/heading 
        if(scene_counter > 1):
            res.append("\n")            

        res.append("label {}:".format(text))
        character = None
        scene_counter += 1            
        
    elif(item.tag=="dialog"): #character diaglog
        if(not character):
            print("person not found: ", )
            break
        res.append('\t{} "{}"'.format(character, text))
        
    elif(item.tag == "action"): #action/author block
        if(not text):
            res.append('\tnarrator ""')    
            continue
        else:
            res.append('\tnarrator "{}"'.format(text))
            
    elif(item.tag == "noprintable_text"): #commands block
        result = text.split(' ')
        command = result[0].lower()
        
        #parsing commands
        if(command == "jump"):
            res.append("\t{}".format(text))
        elif(command == "scene"):
            res.append("\t{}".format(text))
        elif(command == "choose"):
            res.append("\tcall {}".format(result[1]))
        elif(command =="emotion"):
            characters_mood[result[1]] = result[2]
        else:
            print("Unknown command: ", text)

    elif(item.tag == "character"): #character block
        ch = text.strip().upper()
        # if(ch != character):
        if characters[ch] == '':
            continue

        if character and (characters[ch] != character):
            res.append("\thide {}".format(character)) 
        
        character = characters[ch]
        res.append("\tshow {} {}".format(character, characters_mood[character]))

    elif(item.tag in ("parenthetical", "scene_description")): #comments block
        res.append("\t#{}".format(text))  
    else:
        print("Found unknown tag: ", item.tag)       
        
        
output = prepate_renpy_output(res)

save_file(output, "../src/game/frb.rpy")
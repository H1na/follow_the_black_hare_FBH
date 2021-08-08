import sqlite3
import xml.etree.ElementTree as ET
from html import unescape  

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
    "АШ": ["black", "black_regular"],
    "ВЕЧНА": ['vechna', 'vechna_smile2'],
    "РОБОТИЗИРОВАННЫЙ ГОЛОС ЦК": ['stub_character', 'mouse1'],
    "ВЕЧНА ЦИФРОВАЯ": ['digital_vechna', 'mouse1'],
    "МАКСИМ": ['stub_character', 'mouse1'],
    "ОНКА": ['stub_character', 'mouse1'],
    "ОБЛАЧНЫЙ ЛИС": ['fox', 'mouse1'],
    "ЛИС": ['fox', 'mouse1'],
    "ГОЛОС ИЗ СЕТИ": ['stub_character', 'mouse1'],
    "ГОЛОС С ФАБРИКИ": ['stub_character', 'mouse1'],
    "ЖУРНАЛИСТ": ['stub_character', 'mouse1'],
    "НАТАША": ['stub_character', 'mouse1'],
    "ДРУГОЙ ЛИС": ['stub_character', 'mouse1'],
    "ЛИС ИЗ КАСТЫ 3": ['stub_character', 'mouse1'],
    "ГОЛОС МУЛЬТЯШКИ": ['stub_character', 'mouse1'],
    "МОБИЛЬНАЯ КАМЕРА": ['stub_character', 'mouse1'],
    "АЛИСА": ['stub_character', 'mouse1'],
    "ЦЕНТР ПОМОЩИ": ['stub_character', 'mouse1'],
    "МУЖЧИНА": ['stub_character', 'mouse1'],
    "ЧЕРНЫЙ ЗАЯЦ": ["black", "black_regular"],
    # "ВЕЧНА ЦИФРОВАЯ": ['stub_character', 'mouse1'],
    # "ВЕЧНА ЦИФРОВАЯ": ['stub_character', 'mouse1'],
    # "ВЕЧНА ЦИФРОВАЯ": ['stub_character', 'mouse1'],
}


file = "./Follow The Black Hare [FBH].kitsp"
scenario = get_scenario_xml(file)

root = ET.fromstring(scenario)

res = []
scene_counter = 1

character = None

for item in root:
    # print(item.tag)
    
    text = item.find("v").text
    # print(text)
    if(text):
        text = text.replace("&quot;", "\\\"")
    
    if(item.tag == "scene_heading"):
        if(scene_counter > 1):
            res.append("\n")            

        res.append("label {}:".format(text))
        character = None
        scene_counter += 1            
        
    elif(item.tag=="dialog"):
        if(not character):
            print("not found person")
            break
        res.append('\t{} "{}"'.format(characters[character][0], text))
        
    elif(item.tag == "action"):
        if(not text):
            res.append('\tnarrator ""')    
            continue
        else:
            res.append('\tnarrator "{}"'.format(text))
            
    elif(item.tag == "noprintable_text"):
        result = text.split(' ')
        if(result[0] == "jump"):
            res.append("\t{}".format(text))
        elif(result[0] == "scene"):
            res.append("\t{}".format(text))            
        else:
            print("Unknown command: ", text)
    elif(item.tag == "character"):
        ch = text.strip().upper()
        if(ch != character):
            if(character):
               res.append("\thide {}".format(characters[character][1])) 
        character = ch
        # print(ch, character)
        res.append("\tshow {}".format(characters[character][1]))
    else:
        print("Found unknown tag: ", item.tag)       
        
        
output = prepate_renpy_output(res)

save_file(output, "../src/game/frb.rpy")
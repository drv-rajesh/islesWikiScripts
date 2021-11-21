import pywikibot as pwb
import json, os

#setup
wik = pwb.Site("en", "isles")
with open("Items.json") as f: data = json.load(f)

#parsing + adding
for ele in data:
    title = ele["meta"].title()
    pg = pwb.Page(wik, title)

    if ele["quest_item"] == True: quest_item = "Yes"
    else: quest_item = "No"
    
    if ele["transferable"] == True: transferable = "Yes"
    else: transferable = "No"

    equipable = "no"
    try:
        if ele["equipment_slots"]: equipable = "Yes"
    except:
        equipable = "No"
        
    if ele["stackable"] == True: stackable = "Yes"
    else: stackable = "No"

    if ele["crateable"] == True: crateable = "Yes"
    else: crateable = "No"

    quality = ele["quality"].title()
    if quality in ["Resource", "Consumable", "Quest", "Utility", "Ammo"]:
        quality = "None"
    
    value = ele["value"]

    if value == -1:
        value = 0

    text = "{{ItemBlock"
    text += "|questItem=" + quest_item
    text += "|tradeable="+ transferable
    text += "|equipable="+ equipable
    text += "|stackable="+ stackable
    text += "|rarity="+ quality
    text += "|value="+ str(value)
    text += "}}"

    temp = pg.text[pg.text.index("{"):pg.text.index("}")+2]
    pg.text = pg.text.replace(temp, text)

    pg.save("Items commit")

import pywikibot as pwb
import json

#setup
wik = pwb.Site("en", "isles")
with open("Items.json") as f: data = json.load(f)

#parsing + adding
for ele in data:
    title = ele["meta"].title()
    pg = pwb.Page(wik, title)
    
    #parameters
    if ele["quest_item"] == True: quest_item = "Yes"; else: quest_item = "No"
    if ele["transferable"] == True: transferable = "Yes"; else: transferable = "No"
    equipable = "no"
    try: if ele["equipment_slots"]: equipable = "Yes"; except: equipable = "No"
    if ele["stackable"] == True: stackable = "Yes"; else: stackable = "No"
    quality = ele["quality"].title()
    value = ele["value"]; if value == -1: value = 0

    text = "{{ItemBlock"
    text += "|questItem=" + quest_item
    text += "|tradeable="+ transferable; text += "|equipable="+ equipable; text += "|stackable="+ stackable
    text += "|rarity="+ quality
    text += "|value="+ str(value)
    text += "}}"

    text += "\n" + "=== Store Locations ===" + "\n" + "{{StoreLocations}}"; text += "\n" + "=== Drop Locations ===" + "\n" + "{{DropLocations}}"

    pg.text = text
    pg.save("Items commit")

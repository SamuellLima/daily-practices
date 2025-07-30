
dict_to_invert = {
    "apple": "fruit",
    "banana": "fruit",
    "carrot": "vegetable",
    "broccoli": "vegetable",
    "chicken": "meat",
    "beef": "meat",
    "salmon": "fish",
    "tuna": "fish"}
   
def dict_invert(dict_to_invert: dict) -> dict:
    dict_inverted = {}
    for key, value in dict_to_invert.items():
        if value not in dict_inverted:
            dict_inverted[value] = key
        else:
            if isinstance(dict_inverted[value], list):
                dict_inverted[value].append(key)
            else:
                dict_inverted[value] = [dict_inverted[value], key]
    return dict_inverted
    
dict_inverted = dict_invert(dict_to_invert)

print(f"Original dictionary: {dict_to_invert}")
print(f"Inverted dictionary: {dict_inverted}")

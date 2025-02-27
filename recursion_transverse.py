import json
def recursive_parse(data, path_key=[], path_value =[]):
    """extract_names(json_obj, lineage): This function takes two arguments:
    json_obj: The current JSON object (could be a dictionary, list, or value).
    lineage: A list that keeps track of the path to the current element.
    It returns a string displaying the lineage of each item"""

    # Base Case: If json_obj is a dictionary, we check if it has a 'name' key.
    # If it does, we print the full lineage with the name value.
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'name' and value != None:
                path_value = path_value + [value]
            # If the value is another dictionary, it recursively calls the function.
            recursive_parse(value, path_key + [key], path_value  )

    elif isinstance(data, list):
        for item in data:
            # If a list, we recursively call recursive_parse to go deeper into the structure while updating the lineage.
            recursive_parse(item, path_key, path_value)

    else:
        # If the data is a string (which is the case for 'name')
        # and the key 'name' is in the path, print the path
        if isinstance(data, str) and 'name' in path_key:
                # targeting is the last key we want, if preent print out the lineage
                if 'targeting' in path_key:
                    print(" -> ".join(path_value))

with open("test52.json") as f:
    json_data = json.load(f)
# Call the function to start extraction
recursive_parse(json_data)

testdict = {'apples':'fruit', 'dictionary':{'cabbage':'iceberg', 'dictionar':{'deep':'deacons'}}, 'oranges': 'fruit'}

def iterdict(dict1, tab):
    for key in dict1:
        if type(dict1[key]) is dict:
            tab += "\t"
            print(tab + str(key) + " : ")
            iterdict(dict1[key], tab)
        else:
            print(tab + str(key) + " : " + dict1[key])

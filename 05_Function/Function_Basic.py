str = 'led=on&motor=off&switch=off'

def query_parse(str):
    items = str.split('&')
    print(items)
    temp = []
    for item in items:
        temp.append(item.split("="))    
    return dict(temp)
    
print(query_parse(str))
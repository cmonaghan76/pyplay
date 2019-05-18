def value(colors):
    bandcolors = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]
    values = list() #list to store numerical resistor values
    for color in colors:
        values.append(bandcolors.index(color))
    return int(''.join(str(e) for e in values))
from random import uniform
import re
from datetime import datetime


def getConfig() :
    with open(".paths", 'r') as f :
        data = f.readlines()
    sl = data[0].strip('\n')
    o = []
    configExpr = r"(.+)\s([01]\.\d+)\n"
    defaultExpr = r"(.+)\n"
    for i in data[2:] :
        z = re.match(configExpr, i)
        y = re.match(defaultExpr, i)
        if z :
            o.append((z.groups()[0], z.groups()[1]))
        elif y :
            o.append((y.groups()[0], 0))
    return (o, sl)


def main() :
    options, settingsLocation = getConfig()
    with open(settingsLocation, 'r') as f :
        data = f.readlines()
        zData, zIndex = (), 0
        yData, yIndex = (), 0
        logString = ''
        zData = ()
        for i, l in enumerate(data) :
            y = re.match(r'(.*"backgroundImageOpacity":\s)([01]\.\d+)(.*?\n)', l)
            z = re.match(r'(.*"backgroundImage":\s")(.+?)(".*?\n)', l)
            if z :
                zData = z.groups()
                zIndex = i
            elif y :
                yData = y.groups()
                yIndex = i

    cumDist = [10/(10*len(options)-1) if j != zData[1]
               else 9/(10*len(options)-1) for j in options]
    cumDist = [sum(cumDist[:j]) for j in range(1, len(cumDist)+1)]
    selection = uniform(0,cumDist[-1])
    s = 0
    while selection > cumDist[s] :
        s += 1

    yVal = yData[1] if not options[s][1] else options[s][1]
    newImage = f'{zData[0]}{options[s][0]}{zData[2]}'
    newOpacity = f'{yData[0]}{yVal}{yData[2]}'
    logString = f'Sample {selection} over distribution {cumDist}'

    newData = data
    newData[zIndex] = newImage
    newData[yIndex] = newOpacity
    newData[-1] = f"// Last updated at {datetime.now().strftime('%d:%m:%Y:%H:%M:%S')} - {logString}\n"
    with open(settingsLocation, 'w') as f :
        f.writelines(newData)
    return 1

main()

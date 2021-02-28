from random import uniform 
import re
from datetime import datetime


def getPaths() : 
    with open(".paths", 'r') as f : 
        data = f.readlines()
    sl = data[0].strip('\n')
    o = [] 
    for i in data[2:] : 
        o.append(i.strip('\n'))
    return (o, sl)  


def main() :
    with open(settingsLocation, 'r') as f :
        data = f.readlines()
        lineIndex = 0 
        newString = ''
        for i, l in enumerate(data) :
            z = re.match(r'(.*"backgroundImage":\s")(.+?)(".*?\n)', l)
            if z :
                cumDist = [10/(10*len(options)-1) if j != z.groups()[1] 
                        else 9/(10*len(options)-1) for j in options]     
                cumDist = [sum(cumDist[:j]) for j in range(1, len(cumDist)+1)] 
                lineIndex = i
                selection = uniform(0,1)
                s = 0
                while selection > cumDist[s] : 
                    s += 1 
                newString = f'{z.groups()[0]}{options[s]}{z.groups()[2]}'
                break
    newData = data
    newData[lineIndex] = newString
    newData.append(f"// Last updated at {datetime.now().strftime('%d:%m:%Y:%H:%M:%S')}")
    with open(settingsLocation, 'w') as f : 
        f.writelines(newData)
    return 1 

options, settingsLocation = getPaths() 
main()

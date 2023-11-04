import csv
import os
import json
import shutil
import copy
import cairosvg

rows = []

# Making a Temporary Directory for Generation of Files

tmpDirectory = 'test'
try:
    print("Removing Old Temporary Directory")
    shutil.rmtree(tmpDirectory)
except OSError as error:  
    print(error) 


try:
    print("Creating Temporary Directory")
    os.mkdir(tmpDirectory)  
except OSError as error:  
    print(error) 


# Reading SVG Template

with open('ParticipationCertificate-Template.svg', 'r') as file:
  filedata = file.read()


# Reading Mapper File
 
f = open('CSVHeaderSVGMapper.json')
mapperData = json.load(f)
f.close()

print(mapperData)

headWithRow = {}
with open("data.csv", 'r',encoding="utf-8-sig") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    counter = 1
    for index in range(len(header)):
        print(index, header[index])
        headWithRow[header[index]] = index
    for row in csvreader:
        # Replace the target string
        print(row)
        certData = copy.deepcopy(filedata)
        for key in mapperData:
            certData = certData.replace(mapperData[key], row[headWithRow[key]])
        rows.append(row)
        with open(tmpDirectory +'/Certificate'+str(counter)+'.svg', 'w') as file:
           file.write(certData)
        cairosvg.svg2png(url=tmpDirectory +'/Certificate'+str(counter)+'.svg', write_to=tmpDirectory +'/Certificate'+str(counter)+'.png')
        counter = counter + 1
# print(header)
# print(rows)
print(headWithRow)
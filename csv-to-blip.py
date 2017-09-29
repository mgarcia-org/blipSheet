#save as csv-to-plip.py
#requires python 2
#Converts csv (in.csv) file to blip (out.blip) by mike@mgarcia.org
#from https://askubuntu.com/questions/74686/is-there-a-utility-to-transpose-a-csv-file


import csv
import sys
infile = 'in.csv'
outfile = 'out.csv'

with open(infile) as f:
    reader = csv.reader(f)
    cols = []
    for row in reader:
        cols.append(row)

with open(outfile, 'wb') as f:
    writer = csv.writer(f)
    for i in range(len(max(cols, key=len))):
        writer.writerow([(c[i] if i<len(c) else '') for c in cols])
        
#from https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file-using-python
f1 = open('out.csv', 'r')
f2 = open('out.blip', 'w')
for line in f1:
	line = line.replace(',,', ',').replace(',,', ',') #hacky, i'm no python expert :/
	line = line.replace(',,', ',').replace(',,', ',')
	line = line.replace(',', '\n').replace('"', '').replace('\r', '') # replace commas to new line,  delete all double quotes and ^M 
	line = line.replace('`', '"')
	line = line.strip()
	if not line:  continue # skip the empty line
	f2.write(line) # replace replace `(next to 1) to "(double quotes)
f1.close()
f2.close()



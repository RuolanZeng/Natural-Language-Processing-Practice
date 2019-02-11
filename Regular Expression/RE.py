import re
import sys

input_file = open(sys.argv[1])
source = input_file.read()

l1 = source.split('</p>')
n = 1
output = open(sys.argv[2], 'w')

for i in l1:
    title = str(re.findall(r'[a-z A-Z]*\sProfessor', i))
    if title != "[]":
        name = str(re.findall(r'[a-z A-Z]*\,\s?[a-z A-Z - \.]*', i))
        email = str(list(set(re.findall(r'[a-z A-Z\.]*@utdallas\.edu|[a-z A-Z\.]*@hlt.utdallas\.edu', i))))
        number = str(re.findall(r'[(][\d]{3}[)][ ][\d]{3}-[\d]{4}|[\d]{3}-[\d]{3}-[\d]{4}', i))
        result = str(n)+ "  " + name + "            " + title + "           " + email + "       " + number[-6:-2]
        result = result.replace("'","").replace("\\n","")
        n += 1
        output.write('\n' + result)

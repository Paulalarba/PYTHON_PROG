#Opening a file is done by open()
# ising open() handle = open('filename.txt)

fhundle = open('test.txt')
print(fhundle)

for cheese in fhundle:
    print(cheese)

#counting how many line
count = 0
for line in fhundle:
    count = count + 1
print(f"Line count: {count}")

#reading the whole file
read = fhundle.read()
print(len(read))
count = []
for i in range(1,100000):
    count.append(i)
with open("outfile", "w+") as outfile:
    for i in count:
        outfile.write(str(i)+",");
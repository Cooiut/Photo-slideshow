#  Copyright (c) 2020.
#  This problem is from Online Qualication Round of Hash Code 2019
#  Contributor: Cooiut, Jason, Jiahao Chen


photo = dict()
tag = dict()
# image_orientation = dict()
output = []

# original = "Test/a_example.txt"
# original = "Test/b_lovely_landscapes.txt"
original = "Test/c_memorable_moments.txt"
# original = "Test/d_pet_pictures.txt"
# original = "Test/e_shiny_selfies.txt"

# Read file to photo dict
fin = open(original, 'r')
numOfPhoto = int(fin.readline())
lines = fin.readlines()
fin.close()

assert numOfPhoto == len(lines)

for i in range(numOfPhoto):
    line = lines[i].rstrip().split(" ")
    photo[i] = set(line[2:])

# Read file to tag dict
for _photo, _tags in photo.items():
    for _tag in _tags:
        if _tag not in tag:
            tag[_tag] = set()
        tag[_tag].add(_photo)

# Prepare to order
# Choose first one
mini = min({len(i) for i in tag.values()})


#############################################
all_conbinations = []

for x in photo.keys():
    single = set()
    single.add(x)
    single.add("\n")
    for y in photo.keys():
        single.add(y)
        single.add("\n")
    all_conbinations.append(single)

print(all_conbinations)
print(len(all_conbinations[0]))


f = open("Test/Final_output.txt", 'w')
f.write(str(numOfPhoto))
f.write('\n')
for x in all_conbinations:
    for y in x:
        f.write (str(y))
        f.write("\n")
    break



f.close()
#########################################

# Finish!

# Helper function
def compare(p1, p2):
    same = p1 & p2
    return min(len(p1 - same), len(same), len(p2 - same))


# Write output.txt
f = open("Test/output.txt", 'w')
f.write(str(numOfPhoto))
f.write('\n')
for x in tag.items():
    f.write(str(x))
    f.write("\n")
f.close()

# main
if __name__ == '__main__':
    # print(photo)
    # print(tag)
    pass

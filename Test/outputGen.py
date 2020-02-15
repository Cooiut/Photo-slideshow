#  Copyright (c) 2020.
#  This problem is from Online Qualication Round of Hash Code 2019
#  Contributor: Cooiut, Jason, Jiahao Chen

if __name__ == '__main__':

    import random

    x = 80000

    f = open('output.txt', 'w')
    ls = [str(i) for i in range(x)]
    random.shuffle(ls)
    f.write(str(x))
    f.write('\n')
    for x in ls:
        f.write(x)
        f.write("\n")
    f.close()

#  Copyright (c) 2020.
#  This problem is from Online Qualication Round of Hash Code 2019
#  Contributor: Cooiut, Jason, Jiahao Chen

import photoSlideshow

photo_tags = {}
photo_scores = {}


def open_file(infile):
    fin = open(infile, 'r')
    photo_sec = fin.readlines()[1:]
    fin.close()
    return photo_sec


def file_operation(sec):
    i = 0
    for x in sec:
        if x[4] != " ":
            photo_tags[i] = set(x[4:].rstrip().split(" "))
        else:
            photo_tags[i] = set(x[5:].rstrip().split(" "))

        i += 1
    return


def score(outfile):
    # for x, y in dic.items():
    #     for i, j in dic.items():
    #         if i in photo_scores
    #             photo_scores[x] = {i: [len(y.difference(j)), len(y.intersection(j)), len(j.difference(i))]}
    fout = open(outfile, 'r')
    out_list = fout.readlines()[1:]
    result = 0

    for x in range(len(out_list)):
        out_list[x] = out_list[x].rstrip()
    # print(out_list)
    for x in range(len(out_list) - 1):
        left, right = photo_tags[int(out_list[x])], photo_tags[int(out_list[x + 1])]
        intersection = len(photo_tags[int(out_list[x])].intersection(photo_tags[int(out_list[x + 1])]))
        minimum = min(abs(len(left) - intersection), intersection, abs(len(right) - intersection))
        result += minimum
        # print(result)

    return result


if __name__ == '__main__':
    # original = "a_example.txt"
    original = "b_lovely_landscapes.txt"
    # original = "c_memorable_moments.txt"
    # original = "d_pet_pictures.txt"
    # original = "e_shiny_selfies.txt"

    photo_sec = open_file(original)
    file_operation(photo_sec)
    # print(photo_sec)
    print(len(photo_tags))
    print("Your Score is " + str(score("output")))

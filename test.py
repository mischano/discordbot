import random
from PIL import Image


attack = {1: "Rome", 2: "Arverni", 3: "Carthage", 4: "Egypt", 5: "Macedon", 6: "Suebi", 7: "Seleucid", 8: "Getae",
          9: "Boii", 10: "Galatia", 11: "Syracuse", 12: "Epirus", 13: "Tylis", 14: "Athens", 15: "Parthia",
          16: "Pontus", 17: "Baktria", 18: "Massilia", 19: "Lusitani"}
defense = {1: "Iceni", 2: "Parthia", 3: "Pontus", 4: "Baktria", 5: "Armenia", 6: "Massilia", 7: "Nervii", 8: "Syracuse",
           9: "Sparta", 10: "Athens", 11: "Syracuse", 12: "Epirus", 13: "Colchis", 14: "Lusitani"}


def randomize(num):
    rand_num_list = []
    if num % 2 == 0:
        result = (int(num / 2), int(num / 2))
    else:
        result = (int(num / 2) + 1, int(num / 2))

    rand_num_list.append(random.sample(range(1, 19), result[0]))
    rand_num_list.append(random.sample(range(1, 19), result[1]))

    return rand_num_list


def get_concat_h_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def get_concat_h_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_h_blank(_im, im)
    return _im


def get_concat_h(im1, im2):
    dst = Image.new('RGBA', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


temp = randomize(8)
im1 = Image.open('images/' + attack[temp[0][0]] + str('.png'))
im2 = Image.open('images/' + attack[temp[0][1]] + str('.png'))
# get_concat_h(im1, im2).save('temp_img2.png')
im3 = Image.open('images/' + attack[temp[0][2]] + str('.png'))
get_concat_h_multi_blank([im1, im2, im3]).save('temp_img2.png')
# im1.show()

rand_list = [[1, 2, 3], [4, 5, 6]]
for i in rand_list[1]:
    print(i)


import discord
import re
import os.path
import random
from PIL import Image

client = discord.Client()
TOKEN = 'NzY5NDMyNzk1ODAxNTgzNjM2.X5O8IQ.dAmZNy8gGNjasGGqFnnCgpe2NB0'
attack = {1: "Rome", 2: "Arverni", 3: "Carthage", 4: "Egypt", 5: "Macedon", 6: "Suebi", 7: "Seleucid", 8: "Getae",
          9: "Boii", 10: "Galatia", 11: "Syracuse", 12: "Epirus", 13: "Tylis", 14: "Athens", 15: "Parthia",
          16: "Pontus", 17: "Baktria", 18: "Massilia", 19: "Lusitani"}
defense = {1: "Iceni", 2: "Parthia", 3: "Pontus", 4: "Baktria", 5: "Armenia", 6: "Massilia", 7: "Nervii", 8: "Syracuse",
           9: "Sparta", 10: "Athens", 11: "Syracuse", 12: "Epirus", 13: "Colchis", 14: "Lusitani", 15: "Ardiaei",
           16: "Odrysian", 17: "Athens", 18: "Cimmeria", 19: "Pergamon", 20: "Arevaci"}


def resize_image(file_name, size, all=None):
    image = Image.open(os.path.join('images', file_name + str('.png')))
    resized_image = image.resize(size)
    resized_image.save(os.path.join('images', file_name + str('.png')))

    return resized_image


def get_concat_h_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_h_blank(_im, im)
    return _im


def get_concat_h_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGBA', (im1.width + im2.width, max(im1.height, im2.height)), color=(0, 0, 0, 0))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def create_image(rand_list, index):
    image_name = 'temp_img.png'
    image_list = []
    for i in rand_list[index]:
        image_list.append(Image.open('images/' + attack[i] + str('.png')))
    get_concat_h_multi_blank(image_list).save(image_name)

    return image_name


def get_concat_h(im1, im2):
    dst = Image.new('RGBA', (im1.width + im2.width, im1.height), color=(0, 0, 0, 0))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def randomize(num):
    rand_num_list = []
    if num % 2 == 0:
        result = (int(num / 2), int(num / 2))
    else:
        result = (int(num / 2) + 1, int(num / 2))

    rand_num_list.append(random.sample(range(1, 19), result[0]))
    rand_num_list.append(random.sample(range(1, 19), result[1]))

    return rand_num_list


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!roll'):
        arg = re.search(r'\d+|$', message.content)[0]
        if arg is None:
            return
        arg = int(arg)
        if 9 > arg > 1:
            '''for i in range(1, 20):
                resize_image(attack[i], (50, 50))
            for i in range(1, 21):
                resize_image(defense[i], (50, 50))'''

            rand_list = randomize(arg)
            for i in range(2):
                image = create_image(rand_list, i)
                await message.channel.send(file=discord.File(image))

            '''while arg != 0:
                image_name = attack[arg] + str('.png')
                # await message.channel.send(file=discord.File(os.path.join('images', image_name)))
                await message.channel.send(file=discord.File('temp_img2.png'))
                arg -= 1'''
        else:
            await message.channel.send("Usage: arg: 2-8\n'!help' for command list")


client.run(TOKEN)






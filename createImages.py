from PIL import Image
import os


DIRPATH = "/Users/bilaldastagir/Documents/vscode/NFT/NFTWebsite/"


def getPNGFiles(dirr):
    filelist= [file for file in os.listdir(dirr) if file.endswith('.png')]
    return filelist


im_base = Image.open(DIRPATH+"images/base.png")
w, h = im_base.size

assesstAddress = DIRPATH+"images/assets"
colorAddress = DIRPATH+"images/colors"
assesstList = getPNGFiles(assesstAddress)
colorList = getPNGFiles(colorAddress)

k = 1
for ass in assesstList:
    ass_img = Image.open(assesstAddress + "/" + ass)
    for color in colorList:
        color_img = Image.open(colorAddress + "/" + color)

        imageName = DIRPATH+"images/results/"  + "nft" + str(k) + ".png"
        img = Image.new("RGBA", im_base.size)

        img.paste(color_img, (0,0), color_img)
        img.paste(im_base, (0,0), im_base)
        img.paste(ass_img, (0,0), ass_img)
        img.save(imageName, "PNG")

        k += 1




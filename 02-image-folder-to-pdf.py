# pip install Pillow
from PIL import Image
import os
import shutil

cwd = os.getcwd()
srcFolder = os.path.join(cwd, 'chaptersFolders')
dstFolder = os.path.join(cwd, 'NarutoPdfs')
dirpaths, dirnames, filenames = next(os.walk(srcFolder))
if not os.path.exists(dstFolder):
    os.mkdir(dstFolder)
for d in dirnames:
    dpath = os.path.join(srcFolder, d)
    images = []
    _,_,ipaths = next(os.walk(dpath))
    for i in ipaths:
        ipath = os.path.join(srcFolder, d, i)
        if i.split('.')[-1] == 'png':
            png = Image.open(ipath)
            png.load() # required for png.split()
            background = Image.new("RGB", png.size, (255, 255, 255))
            pngLayers = png.split()
            background.paste(png, mask= pngLayers[3] if len(pngLayers)>3 else None) # 3 is the alpha channel
            images.append(background)
        else:
            img = Image.open(ipath)
            img.convert()
            images.append(img)
    dstFile = os.path.join(dstFolder, d+'.pdf')
    print(dstFile)
    images[0].save(dstFile, save_all=True, append_images = images[1:])
shutil.rmtree(srcFolder)
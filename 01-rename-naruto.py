# link to images: https://drive.google.com/file/d/1-mRwxqNFbx2_sCsvQbo7blbL2T7pzZjc/view
import os
from shutil import copyfile

cwd = os.getcwd()
srcPath = os.path.join(cwd, 'srcImgs')
dstPath = os.path.join(cwd, 'chaptersFolders')
dirpaths, dirnames, filenames = next(os.walk(srcPath))
print(dirpaths)
print(dirnames)
print(len(filenames))
c = 0
for i in filenames:
    parts = [j.strip() for j in i.split('-')]
    chapter = parts[0]
    if c != chapter:
        print(chapter)
        c = chapter
    series = parts[-1] #'-'.join(parts[1:])
    chapter = os.path.join(dstPath, chapter)
    if not os.path.exists(chapter):
        os.makedirs(chapter, exist_ok=True)
    dst = os.path.join(chapter, series)
    copyfile(os.path.join(srcPath, i), dst)
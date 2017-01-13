import ctypes
import random
import os

SPI_SETDESKWALLPAPER = 20
PATH_TO_WALLPAPERS = ""
wallpaperDirPath = PATH_TO_WALLPAPERS

wallpaperEntries = os.listdir(wallpaperDirPath)

numOfWallpapers = wallpaperEntries.__len__()

for wallpapers in wallpaperEntries:
    if wallpapers.endswith(".db"):
        wallpaperEntries.remove(wallpapers)

#for wallpapers in wallpaperEntries:
#    print(wallpapers)

random.seed(None)
randomNumber = random.randint(0,numOfWallpapers-1)

print("wallpaper selected is " + wallpaperEntries[randomNumber])
pathOfWallpaper = wallpaperDirPath + "\\" + wallpaperEntries[randomNumber]

print("Complete path of wallpaper which will be put on desktop now is : " + pathOfWallpaper)

ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, pathOfWallpaper, 1)

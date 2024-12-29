from matplotlib import font_manager
fonts = []
for x in font_manager.win32InstalledFonts():
    x = x[::-1]
    dot = x.find('.')
    slash = x.find('\\')
    x = x[slash-1:dot:-1]
    fonts += [x]
fonts.sort()
for x in fonts: print(x)

from PIL import Image
from os.path import splitext

#name of input hat filename
filename = "duck.png"

#color of input hat
incolor = 'white'

#colors of output hats
outcolors = ['brown', 'black', 'yellow', 'grey', 'purple']

#RGBA color maps for each duck's color scheme.
#
#'light' refers to the main color
#'dark' refers to the shaded area
#'black' refers to the outline


maps = {
	'white'  : {'light': (255,255,255,255), 'dark' : (157,157,157,255), 'black' : (0,0,0,255), 'color': 'white'},
	'grey'   : {'light': (125,125,125,255), 'dark' : (82,82,82,255),    'black' : (0,0,0,255), 'color': 'grey'},
	'yellow' : {'light': (255,250,91,255),  'dark' : (177,170,63,255),  'black' : (0,0,0,255), 'color': 'yellow'},
	'brown'  : {'light': (207,99,18,255),   'dark' : (141,63,5,255),    'black' : (0,0,0,255), 'color': 'brown'},
	'black'  : {'light': (0,0,0,255),       'dark' : (82,82,82,255),    'black' : (0,0,0,255), 'color': 'black'},
	'purple'  : {'light': (150,0,150,255),       'dark' : (82,0,82,255),    'black' : (0,0,0,255), 'color': 'purple'}
		}


def generateNewImage(image, outimage, inmap, outmap):
	

	pixels = image.load()
	outpixels = outimage.load()
	
	for x in range(image.size[0]):
		for y in range(image.size[1]):
			if pixels[x,y] == inmap['light']:
				outpixels[x,y] = outmap['light']
			if pixels[x,y] == inmap['dark']:
				outpixels[x,y] = outmap['dark']
			if pixels[x,y] == inmap['black']:
				outpixels[x,y] = outmap['black']
					
	outimage.save("{name}_{color}.png".format(name=basefilename, color=outmap['color']),'png')

	
basefilename = splitext(filename)[0]

outmaps = []
for color in outcolors:
	outmaps.append(maps[color])

inmap = maps[incolor]

for outmap in outmaps:
	
	generateNewImage(Image.open(filename).convert('RGBA'),
					 Image.open(filename).convert('RGBA'), 
					 inmap, 
					 outmap)


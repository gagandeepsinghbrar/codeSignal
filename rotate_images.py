from __future__ import print_function
import os, sys
from PIL import Image

# could be customized to be of a certain size if we need
# size = (160, 160)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] 
    if infile != outfile:
        try:
            im = Image.open(infile)
            # im.thumbnail(size)
            for degree in range(int(sys.argv[2]),int(sys.argv[3]),5):

            	im=im.rotate(degree)
            	im.save("_{}by{}.jpg".format(outfile,degree), "JPEG")
        except IOError:
            print("There was a problem creating a thumbnail for the file !", infile)
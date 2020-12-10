from PIL import Image
import os

def openimage( fn )
  img = Image.open( fn )
  scaling = [ img.size[0]/2, img.size[1]/2 ]
  return img.resize( tuple( scaling ) )

def createMap(img1, img2, threshold):
  imgout = Image.new('RGB', img1.size )
  count = 0
  width = img1.size[0]
  height = img1.size[1]
  for w in range( width ):
    for h in range( height ):
      color=[]
      pixel1 = img1.getpixel( (w, h) )
      pixel2 = img2.getpixel( (w, h) )
      for n in range( 3 ):
        diff = abs( pixel1[n] - pixel2[n] )
        if diff > threshold:
          color.append( 255 )
          count += 1
        else:
          color.append( 0 )
      imgout.putpixel( (w,h), tuple(color) )
  return imgout 

imgout,count = createMap(img1s, img2s, 128)
imgout.save( fn+'.png')

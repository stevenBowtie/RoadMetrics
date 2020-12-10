from PIL import Image
import os

logfp = open('Traffic.log','a')

def openimage( fn ):
  img = Image.open( fn )
  scaling = [ int(img.size[0]/2), int(img.size[1]/2) ]
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
  return imgout, count 

def getFilelist( exten ):
  fl_out = []
  for x in os.listdir() :
    if x.__contains__( exten ):
      fl_out.append(x)
  return fl_out

filelist = getFilelist('.jpg')

prev_image = openimage( filelist[0] )
for images in range( filelist.__len__() - 1 ):
  basefn = filelist[images+1]
  ts = basefn.replace('.jpg','')
  next_image = openimage( basefn )
  imgout,count = createMap( prev_image, next_image, 128 )
  prev_image = next_image
  imgout.save( ts +'.png')
  logfp.write( ts + ', ' + str( count ) + '\n' )
  logfp.flush()

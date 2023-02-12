from PIL import ImageColor
print(ImageColor.getcolor('red','RGBA'))
#prints RGBA value of red color
#r-red , g-green , b-blue , a-aplha (a number from 0.0(fully transparent) to 1.0(fully opaque))
print(ImageColor.getcolor('chocolate','RGBA'))
#prints RGBA value of chocolate color
print(ImageColor.getcolor('black','RGBA'))

from PIL import Image
img = Image.open('image.jpg')
print(img.size)                  #prints height and width of image
w , h = img.size
print("Image width is :- " , w , "\tand height is :- " , h)
print(img.filename)           #prints file name
print(img.format_description)   
img.save('image.jpg')           #we can save image
i = Image.new('RGBA' , (100,200) , 'purple')   #we created a new image with RGBA value of purple and 200 height,100 widht
i.save('purpleimage.png')     #created image is save as specified filename
i2 = Image.new('RGBA' , (1000,1080) , 'brown')
i2.save('brownimage.png')
#we created 2 pictures

#croping
c = i2.crop((365,345,565,560))
c.save('croppedBrownimage.png')
from PIL import Image , ImageDraw, ImageFont
import math
import time
import tkinter
from tkinter import filedialog
import os



def sober():        
        root=tkinter.Tk()
        root.withdraw()
        print(":: Welcome To Sober Edge Detection ::")
        time.sleep(0.5)
        print("Select File Path")
        time.sleep(1)
        path = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*"))) # Your image path 
        print(path)
        img = Image.open(path)

        print(img)
        newimg = Image.new("RGB", (img.width, img.height), "white")
        for x in range(1, img.width-1):  # ignore the edge pixels for simplicity (1 to width-1)
         for y in range(1, img.height-1): # ignore edge pixels for simplicity (1 to height-1)

                # initialise Gx to 0 and Gy to 0 for every pixel
                Gx = 0
                Gy = 0

                # top left pixel
                p = img.getpixel((x-1, y-1))
                r = p[0]
                g = p[1]
                b = p[2]

                # intensity ranges from 0 to 765 (255 * 3)
                intensity = r + g + b

                # accumulate the value into Gx, and Gy
                Gx += -intensity
                Gy += -intensity

                # remaining left column
                p = img.getpixel((x-1, y))
                r = p[0]
                g = p[1]
                b = p[2]

                Gx += -2 * (r + g + b)

                p = img.getpixel((x-1, y+1))
                r = p[0]
                g = p[1]
                b = p[2]

                Gx += -(r + g + b)
                Gy += (r + g + b)

                # middle pixels
                p = img.getpixel((x, y-1))
                r = p[0]
                g = p[1]
                b = p[2]

                Gy += -2 * (r + g + b)

                p = img.getpixel((x, y+1))
                r = p[0]
                g = p[1]
                b = p[2]

                Gy += 2 * (r + g + b)

                # right column
                p = img.getpixel((x+1, y-1))
                r = p[0]
                g = p[1]
                b = p[2]

                Gx += (r + g + b)
                Gy += -(r + g + b)

                p = img.getpixel((x+1, y))
                r = p[0]
                g = p[1]
                b = p[2]

                Gx += 2 * (r + g + b)

                p = img.getpixel((x+1, y+1))
                r = p[0]
                g = p[1]
                b = p[2]

                Gx += (r + g + b)
                Gy += (r + g + b)

                # calculate the length of the gradient (Pythagorean theorem)
                length = math.sqrt((Gx * Gx) + (Gy * Gy))

                # normalise the length of gradient to the range 0 to 255
                length = length / 4328 * 255

                length = int(length)

                # draw the length in the edge image
                #newpixel = img.putpixel((length,length,length))
                newimg.putpixel((x,y),(length,length,length))
                print("Placing Pixel : " + str(x) + " " + str(y))

        idraw = ImageDraw.Draw(newimg)
        text = "\N{COPYRIGHT SIGN}"+"mjindal585"

        font = ImageFont.truetype("arial.ttf", size=12)

        idraw.text((0, 0), text, font=font)
        
                
                
        savepath = input("Enter destination path (with file name and extension) : ")   
        print(savepath)     
        newimg.save(savepath) 
        newimg.show()  
        print(newimg)


        print("Type exit to terminate")

if __name__ == '__main__' : 
	
	# Calling main function 
	sober() 

import tkinter as tk
from tkinter import messagebox 
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
from collections import Counter

infoLabel_list = []
def showInfo(info, PIL_image, sno, fileType):
    if(fileType == '') :
        infos = info + str(PIL_image.width) + 'x' + str(PIL_image.height)
    else :
        infos = info + fileType
    
    label = tk.Label(infoFrame, text = infos)
    label.place(x = 5, y = 20 * sno)
    infoLabel_list.append(label) # record infoLabels

def drawHistogram(pixels, max_pixel):
    global histogram 
    histogram = Image.new("RGB", (demoFrame2.winfo_width() - 10, demoFrame2.winfo_height() - 30), (255, 255, 255))
    drawHist = ImageDraw.Draw(histogram)
    
    xAxis = (demoFrame2.winfo_width() - 10) - 10
    yAxis = (demoFrame2.winfo_height() - 30) - 10
    xRectWidth = xAxis / 255
    yScale = max_pixel / yAxis

    for x in range(255) :
        if pixels.get(x): 
            yRectHeight = 5 + yAxis - (pixels.get(x) / yScale)
            vertices = [
                (5 + x * xRectWidth , 5 + yAxis),
                (5 + (x+1) * xRectWidth, yRectHeight )
            ]
            drawHist.rectangle(vertices, fill = '#20b2aa')      # draw histogram

    # show histogram image on screen
    histTkImg = ImageTk.PhotoImage(histogram)
    histImg.config(image = histTkImg)
    histImg.histogram = histTkImg
    histImg.place(x = 2, y = 3, width =  demoFrame2.winfo_width() - 10 , height = demoFrame2.winfo_height() - 30 ) 
    showInfo("histogram size : ", histogram, 3, '')  
    saveBtn['state'] = tk.NORMAL
    
def calcHistogram(PIL_image):
    global pixels, max_pixel
    pixel_list = []
    for i in range(PIL_image.height): # row
        for j in range(PIL_image.width): # column
            pixel_list.append(PIL_image.getpixel((j, i)))
    # pixels = {nums : pixel_list.count(nums) for nums in pixel_list}
    pixels = Counter(pixel_list) # group pixel_list and store in dict
    max_pixel = max(pixels.values())
    drawHistogram(pixels, max_pixel)

def showInputImg(PIL_image):  
    inputTkImg = ImageTk.PhotoImage(PIL_image) # Load PIL_image to Tk image
    inputImg = tk.Label(demoFrame1, image = inputTkImg)
    inputImg.PIL_image = inputTkImg
    inputImg.place(x = 2, y = 3, width =  demoFrame1.winfo_width() - 10  , height = demoFrame1.winfo_height() - 30 )

def uploadFile():   
    global PIL_image
    filePath = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("jpeg files","*.jpg"),("BMP files","*.bmp"),("PPM files","*.ppm"),("all files","*.*")])
    if not filePath:
         return 
    else : 
        lastDot = filePath.count('.')  # Ensure to get the last dot
        fileType = filePath.split(".") 
    PIL_image = Image.open(filePath).convert('L')

    # Need to clear label text before new upload file
    if infoLabel_list : 
        histImg.config(image = '')
        saveBtn['state'] = tk.DISABLED
        for x in range(len(infoLabel_list)):
            infoLabel_list[x].destroy()  # clear exist label text
        
    showInfo("Inupt Format : ", PIL_image, 0, fileType[lastDot].upper())
    showInfo("Input Size : ", PIL_image, 1, '')  
    PIL_image = PIL_image.resize((demoFrame1.winfo_width() - 20 , demoFrame1.winfo_height() - 20), Image.ANTIALIAS )
    showInfo("Input Resize : " , PIL_image, 2, '')
    showInputImg(PIL_image) # Load "input" PIL_image to tk GUI & show "inputImg"
    histBtn['state'] = tk.NORMAL

def saveFile(histogram):
    files = [("jpeg files","*.jpg"),("BMP files","*.bmp"),("PPM files","*.ppm"),("all files","*.*")] 
    filePath = filedialog.asksaveasfile(mode='wb+' , filetypes = files, defaultextension = files)
    if not filePath: return
    else : 
        lastDot = filePath.name.count('.')
        fileType = filePath.name.split(".")
    histogram.save(filePath)
    showInfo("Save Format : ", histogram, 4, fileType[lastDot].upper())
    showInfo("Save Size : ", histogram, 5, '')  
    tk.messagebox.showinfo('Info','Success!' + '\n'+ 'Histogram Image Size : ' + str(histogram.width) + 'x' + str(histogram.height))

window = tk.Tk()
window.title('AIP60947071S')
sw = int(window.winfo_screenwidth() / 1.2) # screen width
sh = int(window.winfo_screenheight() / 2)  # screen height
screen_resolution = str(sw) + 'x' + str(sh)
window.geometry(screen_resolution) 
window.resizable(False, False)

""" Interface Design (using Frame & LabelFrame) """
# mainFrame (include demoFrame1、demoFrame2、funcFrame)
mainFrame = tk.Frame(window, width = sw , height = sh)
mainFrame.pack(padx = 10, pady =10)
mainFrame.update()

# demoFrame1 to show input image result on screen
demoFrame1 = tk.LabelFrame(mainFrame, text = 'Input image (Gray image)', width = (sw / 5) * 2   , height = mainFrame.winfo_height() )
demoFrame1.pack(side = 'left')
# demoFrame2 to show output img result on screen
demoFrame2 = tk.LabelFrame(mainFrame, text = 'Histogram image', width = (sw / 5) * 2   , height = mainFrame.winfo_height() )
demoFrame2.pack(side = 'left')

# funcFrame to place the function buttons
funcFrame = tk.LabelFrame(mainFrame, text = 'Function', width = (sw / 5)  , height = mainFrame.winfo_height() /  3)
funcFrame.pack(anchor = tk.NE)
funcFrame.update()
# infoFrame to record image informations
infoFrame = tk.LabelFrame(mainFrame, text = 'Infomation', width = (sw / 5)  , height = mainFrame.winfo_height() / 3 * 2)
infoFrame.pack(anchor = tk.SE)
infoFrame.update()
""" --------- End Interface Design ---------- """

histImg = tk.Label(demoFrame2)   

# Function Button setting (include uploadBtn、saveBtn)
uploadBtn = tk.Button(funcFrame, text = 'Upload Image', command = uploadFile )
uploadBtn.place(x = 5 , y = 5 , width = funcFrame.winfo_width() - 15)
uploadBtn.update()

histBtn = tk.Button(funcFrame, text = 'Output Histogram', state = tk.DISABLED, command = lambda: calcHistogram(PIL_image) )
histBtn.place(x = 5 , y = 5 + uploadBtn.winfo_height() + 5 , width = funcFrame.winfo_width() - 15)

saveBtn = tk.Button(funcFrame, text = 'Save Image', state = tk.DISABLED , command = lambda: saveFile(histogram))
saveBtn.place(x = 5 , y = 5 + (uploadBtn.winfo_height()+ 5) * 2  , width = funcFrame.winfo_width() - 15)

window.mainloop()
    




import tkinter as tk
from tkinter import messagebox 
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
from math import cos, sin, pi, sqrt, log

infoLabel_list = []

# Let picture size is pow of 2
def powSet(x): 
    powers = []
    i = 1
    while i <= x:
        if i & x:
            powers.append(i)
        i <<= 1
    return powers[-1]

def showInfo(info, PIL_image, sno, fileType):
    if(fileType == '') :
        infos = info + str(PIL_image.width) + 'x' + str(PIL_image.height)
    else :
        infos = info + fileType
    
    label = tk.Label(infoFrame, text = infos)
    label.place(x = 5, y = 20 * sno)
    infoLabel_list.append(label) # record infoLabels

def haarWavelet(event): 
    ww = pw # picture width(height)
    level = event.widget.cget("text") # get 'level' value

    if infoLabel_list == []:
        levelLabel.config(text = '') 
        levelLabel.config(text = '[Info] Need Input Image!') 
        return
    if (log(ww,2) < level) :
        levelLabel.config(text = '') 
        levelLabel.config(text = '[Info] At most ' + str(int(log(ww,2))) + ' levels') 
        return

    levelLabel.config(text = '') 
    levelLabel.config(text = '(Level : ' + str(level) + ')') 
    showInfo("--- Haar Wavelet", PIL_image, 3, ' ---')
    showInfo("level(s) : " , PIL_image, 4, str(level))

    hwtImg = PIL_image.copy()

    q = 0
    while(q < level):
        # Step 1 : (1D) row pass filter
        s = []
        b = []
        for i in range(ww):
            for j in range(0, ww, 2):
                tmp1 = (hwtImg.getpixel((i,j)) + hwtImg.getpixel((i, j+1))) / 2 # Average(low pass filter)
                tmp2 = hwtImg.getpixel((i,j))  - tmp1 + int(255/2) # Difference(high pass filter)
                s.append(tmp1) # store 'Average' result pixels
                b.append(tmp2) # store 'Difference' result pixels

        k = 0
        for i in range(ww):
            for j in range(int(ww/2)):
                hwtImg.putpixel((i,j), int(s[k]))
                hwtImg.putpixel((i,j+int(ww/2)), int(b[k]))
                k = k+1 
        
        # Step 2 : (1D) column pass filter
        s = []
        b = []
        for i in range(ww):
            for j in range(0, ww, 2):
                tmp1 = (hwtImg.getpixel((j,i)) + hwtImg.getpixel((j+1, i))) / 2 # Average(low pass filter)
                tmp2 =  hwtImg.getpixel((j,i)) - tmp1  +int(255/2) # Difference(high pass filter)
                s.append(tmp1)  # store 'Average' result pixels
                b.append(tmp2) # store 'Difference' result pixels
        k = 0
        for i in range(ww):
            for j in range(int(ww/2)):
                hwtImg.putpixel((j,i), int(s[k]))
                hwtImg.putpixel((j+int(ww/2),i), int(b[k]))
                k = k+1 

        q = q + 1
        ww = int (ww/2)

    # Show haar wavelet result image
    TkImg = ImageTk.PhotoImage(hwtImg)
    haarWaveletImg.config(image = TkImg)
    haarWaveletImg.hwtImg = TkImg
    haarWaveletImg.place(x = 2, y = 2, width = pw  , height = pw )
    showInfo("Result Size : ", hwtImg, 5, '')

def showInputImg(PIL_image):  
    inputTkImg = ImageTk.PhotoImage(PIL_image) # Load PIL_image to Tk image
    #inputImg = tk.Label(demoFrame1, image = inputTkImg)
    inputImg.config(image = '')
    inputImg.config(image = inputTkImg)
    inputImg.PIL_image = inputTkImg
    inputImg.place(x = 2, y = 2, width =  pw  , height = pw )

def uploadFile():   
    global PIL_image
    filePath = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("jpeg files","*.jpg"),("BMP files","*.bmp"),("PPM files","*.ppm"),("all files","*.*")])
    if not filePath:
         return 
    else : 
        lastDot = filePath.count('.')  # Ensure to get the last dot
        fileType = filePath.split(".") 
    PIL_image = Image.open(filePath).convert('L')
    
    # Reset setting
    levelLabel.config(text = '') 
    if infoLabel_list : 
        haarWaveletImg.config(image = '')
        for x in range(len(infoLabel_list)):
            infoLabel_list[x].destroy()  # clear exist label text

    showInfo("Inupt Format : ", PIL_image, 0, fileType[lastDot].upper())
    showInfo("Input Size : ", PIL_image, 1, '')  
    PIL_image = PIL_image.resize((pw, pw), Image.ANTIALIAS )
    showInfo("Input Resize : " , PIL_image, 2, '')
    showInputImg(PIL_image) # Load "input" PIL_image to tk GUI & show "inputImg"

window = tk.Tk()
window.title('AIP60947071S')
sw = int(window.winfo_screenwidth()) # screen width
#sh = int(window.winfo_screenheight())  # screen height

pw = powSet( int(sw/5) * 2 ) # powSet of 2
sh = pw + 30 # screen hiehgt

screen_resolution = str(sw) + 'x' + str(sh)
window.geometry(screen_resolution) 

""" Interface Design (using Frame & LabelFrame) """
# mainFrame (include demoFrame1、demoFrame2、funcFrame)
mainFrame = tk.Frame(window, width = sw , height = sh )
mainFrame.pack(padx = 5, pady = 2)
mainFrame.update()

# demoFrame1 to show input image result on screen
demoFrame1 = tk.LabelFrame(mainFrame, text = 'Input image (Gray image)', width = pw + 10  , height = sh + 100   )
demoFrame1.pack(side = 'left')
# demoFrame2 to show output img result on screen
demoFrame2 = tk.LabelFrame(mainFrame, text = 'Haar wavelet image', width = pw + 10    , height = sh + 100  )
demoFrame2.pack(side = 'left')

# funcFrame to place the function buttons
funcFrame = tk.LabelFrame(mainFrame, text = 'Function', width = ((sw-20) / 5)  , height = (sh+ 100) / 5 * 0.5)
funcFrame.pack(anchor = tk.NE)
funcFrame.update()

# Haar Wavelet (Level Choose)
hwtFrame = tk.LabelFrame(mainFrame, text = 'Haar wavelet (Level)', width = ((sw-20) / 5)  , height = (sh+ 100)/ 5 * 1.5 )
hwtFrame.pack(anchor = tk.NE)
hwtFrame.update()

# infoFrame to record image informations
infoFrame = tk.LabelFrame(mainFrame, text = 'Infomation', width = ((sw-20) / 5)  , height = (sh+100) / 5 * 4)
infoFrame.pack(anchor = tk.SE)
infoFrame.update()
""" --------- End Interface Design ---------- """

inputImg = tk.Label(demoFrame1)
haarWaveletImg = tk.Label(demoFrame2)   

# Function Button setting (include uploadBtn、saveBtn)
uploadBtn = tk.Button(funcFrame, text = 'Upload Image', command = uploadFile )
uploadBtn.place(x = 5 , y = 5 , width = funcFrame.winfo_width() - 15)
uploadBtn.update()

# Show level text
levelLabel = tk.Label(hwtFrame)
levelLabel.place(x = 5, y = 5)
for x in range(5):
    for y in range(2):
        levelVal =  2 * (x+1) 
        if y == 0 : levelVal = levelVal - 1
        levels = tk.Label(hwtFrame, text = levelVal, fg="blue", cursor="hand1")
        levels.place(x =  23 * (x+1)  ,y = 35 + 30 * y)
        levels.bind("<Button-1>",  haarWavelet)

window.mainloop()
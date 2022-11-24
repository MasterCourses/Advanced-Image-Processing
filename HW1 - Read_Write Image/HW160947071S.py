import tkinter as tk
from tkinter import messagebox 
from tkinter import filedialog
from PIL import ImageTk, Image

infoLabel_list = []
def showInfo(info, PIL_image, sno, fileType):
    global infoLabel_list
    if(fileType == '') :
        infos = info + str(PIL_image.width) + 'x' + str(PIL_image.height)
    else :
        infos = info + fileType
    
    label = tk.Label(infoFrame, text = infos)
    label.place(x = 5, y = 20 * sno)
    infoLabel_list.append(label) # record infoLabels
    
def showOutputImg(PIL_image):
    showInfo("Output Size : ", PIL_image, 3, '')  
    outputTkImg = ImageTk.PhotoImage(PIL_image)
    outputImg = tk.Label(demoFrame2, image = outputTkImg)
    outputImg.PIL_image = outputTkImg
    outputImg.place(x = 2, y = 3, width =  demoFrame2.winfo_width() - 10 , height = demoFrame2.winfo_height() - 30 )
    saveBtn['state'] = tk.NORMAL

def showInputImg(PIL_image):  
    inputTkImg = ImageTk.PhotoImage(PIL_image) # Load PIL_image to Tk image
    inputImg = tk.Label(demoFrame1, image = inputTkImg)
    inputImg.PIL_image = inputTkImg
    inputImg.place(x = 2, y = 3, width =  demoFrame1.winfo_width() - 10  , height = demoFrame1.winfo_height() - 30 )
    showOutputImg(PIL_image) # Load "output" PIL_image to tk GUI & show "outputImg"
    
def uploadFile():   
    global PIL_image
    filePath = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("jpeg files","*.jpg"),("BMP files","*.bmp"),("PPM files","*.ppm"),("all files","*.*")])
    if not filePath:
         return 
    else : 
        lastDot = filePath.count('.')  # Ensure to get the last dot
        fileType = filePath.split(".") 
    PIL_image = Image.open(filePath)

    # Need to clear label text before new upload file
    if infoLabel_list : 
        for x in range(len(infoLabel_list)):
            infoLabel_list[x].destroy()  # clear exist label text

    showInfo("Inupt Format : ", PIL_image, 0, fileType[lastDot].upper())
    showInfo("Input Size : ", PIL_image, 1, '')  
    PIL_image = PIL_image.resize((demoFrame1.winfo_width() - 20 , demoFrame1.winfo_height() - 20), Image.ANTIALIAS )
    showInfo("Input Resize : " , PIL_image, 2, '')
    showInputImg(PIL_image) # Load "input" PIL_image to tk GUI & show "inputImg"

def saveFile(PIL_image):
    files = [("jpeg files","*.jpg"),("BMP files","*.bmp"),("PPM files","*.ppm"),("all files","*.*")] 
    filePath = filedialog.asksaveasfile(mode='wb+' , filetypes = files, defaultextension = files)
    if not filePath: return
    else : 
        lastDot = filePath.name.count('.')
        fileType = filePath.name.split(".")
    PIL_image.save(filePath)
    showInfo("Save Format : ", PIL_image, 4, fileType[lastDot].upper())
    showInfo("Save Size : ", PIL_image, 5, '')  
    tk.messagebox.showinfo('Info','Success! Save Image Size : ' + str(PIL_image.width) + 'x' + str(PIL_image.height) + '\n(Tip - Not Original Image Size)')

window = tk.Tk()
window.title('AIP60947071S')
sw = int(window.winfo_screenwidth() / 1.3) # screen width
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
demoFrame1 = tk.LabelFrame(mainFrame, text = 'Input image', width = (sw / 5) * 2   , height = mainFrame.winfo_height() )
demoFrame1.pack(side = 'left')
# demoFrame2 to show output img result on screen
demoFrame2 = tk.LabelFrame(mainFrame, text = 'Output image', width = (sw / 5) * 2   , height = mainFrame.winfo_height() )
demoFrame2.pack(side = 'left')

# funcFrame to place the function buttons
funcFrame = tk.LabelFrame(mainFrame, text = 'Function', width = (sw / 5)  , height = mainFrame.winfo_height() /  3 )
funcFrame.pack(anchor = tk.NE)
funcFrame.update()
# infoFrame to record image informations
infoFrame = tk.LabelFrame(mainFrame, text = 'Infomation', width = (sw / 5)  , height = mainFrame.winfo_height() / 3 * 2)
infoFrame.pack(anchor = tk.SE)
infoFrame.update()
""" --------- End Interface Design ---------- """

# Function Button setting (include uploadBtn、saveBtn)
uploadBtn = tk.Button(funcFrame, text = 'Upload Image', height = 2, command = uploadFile )
uploadBtn.place(x = 5 , y = 5 , width = funcFrame.winfo_width() - 15)
uploadBtn.update()

saveBtn = tk.Button(funcFrame, text = 'Save Image' , height = 2 , state = tk.DISABLED , command = lambda: saveFile(PIL_image))
saveBtn.place(x = 5 , y = uploadBtn.winfo_height() + 10 , width = funcFrame.winfo_width() - 15)

window.mainloop()
    




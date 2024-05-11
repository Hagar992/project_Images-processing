import tkinter.filedialog
import time
import os
from image_capture import *

# create folder directory to save images
folder = r"\images"
cwd = os.getcwd()
path = cwd + folder
if not os.path.exists(path):
    os.makedirs(path)
    

# create a dictionary for the filters
fil = ['color', 'gray', 'threshold', 'increaseContrast', 'decreaseContrast', 'opening','hough_transform', 'erosion','closing',
       'dilation', 'gauss', 'sobel', 'laplace', 'median','mean', 'lpf', 'hpf', 'prewitt','Robert',
       'histogramEqualization']
filter_dic = {}


def select_filter(filter, status):
    # change required filter to true
    filter_dic = {x: False for x in fil}  # change all values to false in dictionary to make only filter to true
    if filter in filter_dic:
        assert type(status) == bool
        filter_dic[filter] = status
    return filter_dic


class App:
    isImageInstantiated = False

    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Labels
        label1 = tkinter.Label(window, text="Filters", bd=2, relief="solid")
        label1.grid(row=3, column=13, columnspan=5)

        self.canvas = tkinter.Canvas(self.window, width=200, height=200)
        self.canvas.grid(row=0, column=1, rowspan=12, columnspan=6)

        # buttons of choose
        self.b_snap = tkinter.Button(window, text="Choose an image", command=self.select_image)
        self.b_snap.grid(row=3, column=2)

        # Button for applying the other filters!
        self.b1 = tkinter.Button(window, text="Increase Contrast", width=15, command=self.increaseContrast_filter, bg="pink", fg="black")
        self.b1.grid(row=4, column=13)

        self.b2 = tkinter.Button(window, text="Decrease Contrast", width=15, command=self.decreaseContrast_filter , bg="pink", fg="black")
        self.b2.grid(row=4, column=17)

        self.b3 = tkinter.Button(window, text="Gauss", width=15, command=self.gauss_filter , bg="pink", fg="black")
        self.b3.grid(row=5, column=13)

        self.b4 = tkinter.Button(window, text="Laplace", width=15, command=self.laplace_filter , bg="pink", fg="black")
        self.b4.grid(row=5, column=17)

        self.b5 = tkinter.Button(window, text="Robert", width=15, command=self.threshold_filter , bg="pink", fg="black")
        self.b5.grid(row=6, column=17)

        self.b6 = tkinter.Button(window, text="Sobel", width=15, command=self.sobel_filter , bg="pink", fg="black")
        self.b6.grid(row=6, column=13)

        self.b7 = tkinter.Button(window, text="Prewitt", width=15, command=self.prewitt_filter , bg="pink", fg="black")
        self.b7.grid(row=8, column=13)

        self.b8 = tkinter.Button(window, text="Threshold", width=15, command=self.threshold_filter , bg="pink", fg="black")
        self.b8.grid(row=8, column=17)

        self.b9 = tkinter.Button(window, text="Median", width=15, command=self.median_filter , bg="pink", fg="black")
        self.b9.grid(row=9, column=13)

        self.b10 = tkinter.Button(window, text="Mean", width=15, command=self.mean_filter, bg="pink", fg="black")
        self.b10.grid(row=9, column=17)

        self.b11 = tkinter.Button(window, text="opening", width=15, command=self.opening, bg="pink", fg="black")
        self.b11.grid(row=13, column=13)

        self.b12 = tkinter.Button(window, text="Hpf", width=15, command=self.hpf_filter, bg="pink", fg="black")
        self.b12.grid(row=10, column=17)

        self.b13 = tkinter.Button(window, text="Dilation", width=15, command=self.dilation , bg="pink", fg="black")
        self.b13.grid(row=11, column=13)

        self.b14 = tkinter.Button(window, text="Erosion", width=15, command=self.erode , bg="pink", fg="black")
        self.b14.grid(row=12, column=13)

        self.b15 = tkinter.Button(window, text="Color/No Filter", width=15, command=self.no_filter , bg="pink", fg="black")
        self.b15.grid(row=12, column=17)

        self.b16 = tkinter.Button(window, text="Gray", width=15, command=self.gray_filter , bg="pink", fg="black")
        self.b16.grid(row=11, column=17)

        self.b17 = tkinter.Button(window, text="Histogram Equaliz...", width=15, command=self.histogram_filter , bg="pink", fg="black")
        self.b17.grid(row=13, column=17, columnspan=2)

        self.b18 = tkinter.Button(window, text="LPF", width=15, command=self.lpf_filter , bg="pink", fg="black")
        self.b18.grid(row=10, column=13, columnspan=2)

        self.b19 = tkinter.Button(window, text="Snap or Save image", width=15, command=self.snapshot )
        self.b19.grid(row=16, rowspan=2, column=13, columnspan=4)

        self.b20 = tkinter.Button(window, text="Close Program", command=window.destroy,bg="red", fg="white")
        self.b20.grid(row=16, rowspan=2, column=17, columnspan=2)

        self.b21 = tkinter.Button(window, text="Hough_transform", width=15, command=self.hough_transform, bg="pink", fg="black")
        self.b21.grid(row=15, column=17)

        self.b22 = tkinter.Button(window, text="closing", width=15, command=self.closing , bg="pink", fg="black")
        self.b22.grid(row=15, column=13)


        # After	it is called once, the update method will be automatically called every loop
        self.delay = 15
        self.window.mainloop()


    def select_image(self):
        # create instance from image capture
        self.img = ImageCap()
        self.img.all_filters = select_filter('color', True)
        self.img.update()
        self.isImageInstantiated = True

    def snapshot(self):
        if self.isImageInstantiated:
            cv2.imwrite(path + r"\image-" + time.strftime("%d-%m-%Y-%H-%M-%S") + '.jpg', self.img.filtered_image)
            print('Image saved :)')
    

    # all filters
    def gray_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('gray', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('gray', True)

    def gauss_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('gauss', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('gauss', True)

    def laplace_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('laplace', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('laplace', True)

    def threshold_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('threshold', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('threshold', True)

    def sobel_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('sobel', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('sobel', True)

    def no_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('color', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('color', True)

    def median_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('median', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('median', True)

    def mean_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('mean', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('mean', True)        

    def lpf_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('lpf', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('lpf', True)

    def hpf_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('hpf', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('hpf', True)

    def opening(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('opening', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('opening', True)

    def closing(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('closing', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('closing', True)    

    def dilation(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('dilation', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('dilation', True)

    def hough_transform(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('hough_transform', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('hough_transform', True)        

    def erode(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('erosion', True)  
            kernel = np.ones((3, 3), np.uint8) 
            self.img.filtered_image = cv2.erode(self.img.original_image, kernel)                        
            self.img.update() 

    def increaseContrast_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('increaseContrast', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('increaseContrast', True)

    def decreaseContrast_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('decreaseContrast', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('decreaseContrast', True)

    def prewitt_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('prewitt', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('prewitt', True)

    def Robert_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('Robert', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('Robert', True)       

    def histogram_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('histogramEqualization', True)
            self.img.update()
        elif self.isVideoInstantiated:
            self.vid.all_filters = select_filter('histogramEqualization', True)


# Create a window and pass it to the Application object
App(tkinter.Tk(), 'Filters BY "Hagar"')

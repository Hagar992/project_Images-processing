import tkinter
import tkinter.filedialog
import cv2
import PIL.ImageTk
import PIL.ImageFilter
import numpy as np
import random

class ImageCap:
    def __init__(self, window=None):
        self.window = window
        # open a file chooser dialog and allow the user to select an input image
        img_path = tkinter.filedialog.askopenfilename()
        if len(img_path) > 0:
            # read image
            self.original_image = cv2.imread(img_path)
            self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
            self.filtered_image = None
            self.panelA = None
            self.panelB = None

            # initialize the filters
            self.all_filters = None

            self.update_panel(self.original_image, self.original_image)

    def update_panel(self, original_image, filtered_image):

        # convert the images to PIL and ImageTK format
        original_image = PIL.Image.fromarray(original_image)
        filtered_image = PIL.Image.fromarray(filtered_image)

        original_image = original_image.resize((400, 400))
        filtered_image = filtered_image.resize((400, 400))

        original_image = PIL.ImageTk.PhotoImage(original_image)
        filtered_image = PIL.ImageTk.PhotoImage(filtered_image)

       

        # if the panels are None, initialize them
        if self.panelA is None or self.panelB is None:
            # the first panel will store our original image
            self.panelA = tkinter.Label(image=original_image)
            self.panelA.image = original_image
            self.panelA.grid(row=3, column=2, sticky="nsew")
            # while the second panel will store the edge map
            self.panelB = tkinter.Label(image=filtered_image)
            self.panelB.image = filtered_image
            self.panelB.grid(row=3, column=3, sticky="nsew")
        # otherwise, update the image panels
        else:
            # update the pannels
            self.panelA.configure(image=original_image)
            self.panelB.configure(image=filtered_image)
            self.panelA.image = original_image
            self.panelB.image = filtered_image

    def update(self):
        # check if this class has assigned/has attribute original_image
        # to know if the user choose image and don't close options window

        if hasattr(self, 'original_image'):
            gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)

            if self.all_filters['color']:
                self.update_panel(self.original_image, self.original_image)    

            elif self.all_filters['gray']:
                self.update_panel(self.original_image, gray)

            elif self.all_filters['hpf']:
            # High-pass filter (Laplacian)
               kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
               filtered_image = cv2.filter2D(gray, cv2.CV_32F, kernel)
               self.update_panel(self.original_image, filtered_image) 

            elif self.all_filters['lpf']:
                   # Low-pass filter (averaging)
                kernel = np.ones((3, 3), np.float32) / 9  # Averaging kernel
                filtered_image = cv2.filter2D(gray, cv2.CV_32F, kernel)
                self.update_panel(self.original_image, filtered_image)
   

            elif self.all_filters['gauss']:
                self.filtered_image = cv2.GaussianBlur(gray, (21, 21), 0)
                self.update_panel(self.original_image, self.filtered_image)

            elif self.all_filters['sobel']:
                self.filtered_image = cv2.Sobel(gray, -1, dx=1, dy=0, ksize=11, scale=1, delta=0,
                                                borderType=cv2.BORDER_DEFAULT)
                self.update_panel(self.original_image, self.filtered_image)

            elif self.all_filters['laplace']:
                self.filtered_image = cv2.Laplacian(gray, -1, ksize=17, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
                self.update_panel(self.original_image, self.filtered_image)


            elif self.all_filters['median']:
                self.filtered_image = cv2.medianBlur(self.original_image, 5)
                self.update_panel(self.original_image, self.filtered_image)
            
            elif self.all_filters['mean']:
                self.filtered_image = cv2.blur(self.original_image, (5,5))
                self.update_panel(self.original_image, self.filtered_image)
           

            elif self.all_filters['opening']:
                 kernel = np.ones((3, 3), np.uint8)  
                 eroded_image = cv2.erode(self.original_image, kernel) 
                 self.filtered_image = cv2.dilate(eroded_image, kernel)
                 self.update_panel(self.original_image, self.filtered_image)
  

            elif self.all_filters['closing']:
                 kernel = np.ones((3, 3), np.uint8)  
                 dilated_image = cv2.dilate(self.original_image, kernel)
                 self.filtered_image = cv2.erode(dilated_image, kernel) 
                 self.update_panel(self.original_image, self.filtered_image)
     

            elif self.all_filters['dilation']:
                 kernel = np.ones((3, 3), np.uint8) 
                 self.filtered_image = cv2.dilate(self.original_image, kernel)
                 self.update_panel(self.original_image, self.filtered_image)

            elif self.all_filters['erosion']:
               # Apply erosion filter
                 kernel = np.ones((3, 3), np.uint8) 
                 self.filtered_image = cv2.erode(self.original_image, kernel)
                 self.update_panel(self.original_image, self.filtered_image)

            elif self.all_filters['hough_transform']:
                 gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
                 circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=0, maxRadius=0)
                 if circles is not None:
                    circles= np.uint16(np.around(circles))            
                    hough_image = self.original_image.copy()
                    for i in circles[0, :]:
                        cv2.circle(hough_image, (i[0], i[1]),i[2],(0,255,0),2 )  
                        cv2.circle(hough_image, (i[0], i[1]),2,(0,0,255),3 )
                 self.update_panel(self.original_image, hough_image)

            elif self.all_filters['increaseContrast']:
                alpha = random.uniform(1.0, 2.0)
                beta = random.uniform(0, 80)
                self.filtered_image = cv2.addWeighted(self.original_image, alpha,
                                                      np.zeros(self.original_image.shape, self.original_image.dtype), 0,
                                                      beta)
                self.update_panel(self.original_image, self.filtered_image)

            elif self.all_filters['decreaseContrast']:
                alpha = random.uniform(1.0, 0.8)
                beta = random.uniform(-100, 0)
                self.filtered_image = cv2.addWeighted(self.original_image, alpha,
                                                      np.zeros(self.original_image.shape, self.original_image.dtype), 0,
                                                      beta)
                self.update_panel(self.original_image, self.filtered_image)

    
            elif self.all_filters['prewitt']:
                img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
                kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
                kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
                img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
                img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
                self.filtered_image = img_prewittx + img_prewitty
                self.update_panel(self.original_image, self.filtered_image)
            
            elif self.all_filters['Robert']:
                img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
                kernelx = np.array([[-1, 0], [0, 1]])
                kernely = np.array([[0, -1], [1, 0]])
                img_Robertx = cv2.filter2D(img_gaussian, -1, kernelx)
                img_Roberty = cv2.filter2D(img_gaussian, -1, kernely)
                self.filtered_image = img_Robertx + img_Roberty
                self.update_panel(self.original_image, self.filtered_image)

            elif self.all_filters['threshold']:
                self.filtered_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
                self.update_panel(self.original_image, self.filtered_image)    

            elif self.all_filters['histogramEqualization']:
                self.filtered_image = cv2.equalizeHist(gray)
                self.update_panel(self.original_image, self.filtered_image)
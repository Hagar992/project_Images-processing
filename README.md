# project_image processing <img width="50" hieght="50" src="">
a GUI application to apply basic image processing filters built with python, openCV and tkinter 

# Features
- Applying the filters in image. 
- Ability to save new image.
- Include Increase/Decrease Contrast Filter.
- Include Gaussian filter.
- Include Laplacian filter.
- Include Sobel filter.
- Include Threshold filter.
- Include Gray filter.
- Include Median filter.
- Include Mean filter.
- Include Erosion.
- Include Dilation.
- Include Opening.
- Include Closing.
- Include Prewitt filter.
- Include Hough Transform.
- Include Histogram Equalization filter.
- Include LPF( Low Pass Filter) filter.
- Include HPF( High Pass Filter) filter.
       _______________________________________________________________________________________________________________
# simplified explanation for each of the filters:

1- 'color': Displays the original image without any modifications,
            meaning no filter is applied.

2- 'gray': Converts the image to a grayscale image by converting the
           image to the grayscale color space.

3- 'threshold': Converts the image to a binary image (black and white)
                using a specified threshold. 
                Pixels with values below the threshold become black, and pixels with values above the threshold become white.

4- Increasing contrast involves enhancing the difference in intensity between the brightest and darkest areas of an image, resulting in a more visually 
             striking appearance with sharper highlights and shadows. It's often used to make images appear more vibrant and dynamic.
  - Here's a simple explanation of how to increase contrast in an image:
       -  1- Intensity Adjustment: To increase contrast, you need to adjust the intensity values of pixels in the image. One common method is to linearly scale
             up the intensity values across the entire range of intensities. This effectively expands the intensity range, making the bright areas brighter and the dark areas darker.
       -  2- Additive and Multiplicative Factors: You can achieve contrast enhancement by applying both additive and multiplicative factors to the intensity
             values. The additive factor shifts all intensity values uniformly, while the multiplicative factor scales the intensity values. By increasing the multiplicative factor above 1, you effectively increase the contrast.

5- Decreasing contrast involves reducing the difference in intensity between the brightest and darkest areas of an image, resulting in a flatter appearance
             with less distinction between different elements. It can be useful in scenarios where the original image has very high contrast, leading to overly pronounced highlights and shadows.
  - Here's a simple explanation of how to decrease contrast in an image:
       -   1-Intensity Adjustment: To decrease contrast, you need to adjust the intensity values of pixels in the image. One common method is to linearly scale 
            down the intensity values across the entire range of intensities. This effectively compresses the intensity range, making the bright areas darker and the dark areas lighter.
       -   2-Additive and Multiplicative Factors: You can achieve contrast reduction by applying both additive and multiplicative factors to the intensity values.
            The additive factor shifts all intensity values uniformly, while the multiplicative factor scales the intensity values. By decreasing the 
             multiplicative factor below 1, you effectively reduce the contrast.


6- The Hough Transform is a popular technique in image processing used primarily for detecting geometrical shapes, such as lines, circles, and ellipses, in an
            image. The Hough Circle Transform specifically detects circular shapes within an image.
  - Here's a brief explanation of how the Hough Circle Transform works:
       -  1- Edge Detection: Typically, you perform edge detection (e.g., using Canny edge detector) to identify potential edges in the image.
       -  2-Accumulator Array: For each pixel that is identified as an edge pixel, you calculate all possible circles that could pass through that point. 
            Each circle is parameterized by its center coordinates (x, y) and its radius (r). For each potential circle, you increment a corresponding cell in an accumulator array.
       -  3-Thresholding: After processing all edge pixels, you look for peaks in the accumulator array. These peaks represent potential circles in the image.
            To reduce false positives, you may apply a threshold to filter out low-accumulated values.
       -  4-Circle Drawing: Once you have identified the centers and radii of the circles, you can draw them on the original image.
  
7- Opening is a morphological operation used in image processing to remove small objects and smooth out the boundaries of foreground objects (white regions) in
             binary images. It is the opposite of closing operation.
  - Here's how opening works:
       -   1- It involves two consecutive operations: erosion followed by dilation.
       -   2- First, erosion removes small objects and sharpens the boundaries of foreground objects by shrinking them.
       -   3- Then, dilation expands the boundaries of the eroded image, effectively smoothing out the contours of objects.
       -   4- The combination of erosion followed by dilation helps to remove noise and small objects while preserving the overall structure of larger objects.


8- Closing is a morphological operation used in image processing to fill in small holes and gaps, as well as to smooth the boundaries of foreground objects 
           (white regions) in binary images.
  - Here's how closing works:
       -  1- It involves two consecutive operations: dilation followed by erosion.
       -  2- First, dilation expands the boundaries of foreground objects, filling in small holes and gaps.
       -  3-Then, erosion shrinks the boundaries of the dilated image, smoothing out the rough edges created by dilation.
       -  4-The combination of dilation followed by erosion helps to close gaps between nearby foreground objects and to smooth the contours of objects.


9- Erosion is another fundamental morphological operation used in image processing, particularly in binary images, to reduce the size of foreground objects 
          (white regions) and to detach connected objects.
  - Here's how erosion works:
       -  1-It involves sliding a structuring element (also known as a kernel) over the image.
       -  2-At each position of the kernel, if all pixels in the input image under the kernel are white (foreground), the center pixel of the kernel in the output image remains white; otherwise, it becomes black (background).
       -  3-The size and shape of the structuring element determine the degree of erosion. A larger kernel results in more erosion of the foreground regions.


10- Dilation is a morphological operation used in image processing to enhance features like edges and boundaries in binary images. It works by expanding the 
             boundaries of regions of foreground pixels (typically represented as white) in an image.
  - Here's how dilation works:
       - 1- It involves sliding a structuring element (also known as a kernel) over the image.
       - 2- At each position of the kernel, if any pixel in the input image is white (foreground), the corresponding pixel in the output image becomes white.
       - 3- The size and shape of the structuring element determine the extent of dilation. A larger kernel results in more expansion of the foreground regions.

11- The Gaussian filter, also known as Gaussian blur, is a commonly used image processing filter for smoothing images. It works by convolving the image with a Gaussian kernel, which is a 2D matrix representing the shape of a Gaussian distribution.
  - Here's how the Gaussian filter works:
       - 1-Define the size of the Gaussian kernel. This determines how much smoothing will be applied to the image.
       - 2-Calculate the values of the Gaussian kernel based on the Gaussian distribution formula.
       - 3-Convolve the image with the Gaussian kernel. This involves sliding the kernel over the entire image and computing a weighted average of the pixel 
             values under the kernel at each position.
       - 4-Replace each pixel in the original image with the corresponding weighted average value obtained from the convolution.


12- The Sobel filter, named after its inventor Irwin Sobel, is a popular edge detection filter used in image processing. It computes the gradient of the image 
              intensity at each pixel, highlighting regions of rapid intensity change which often correspond to edges.
  - Here's how the Sobel filter works:
       -  1-Compute the gradient of the image intensity in the horizontal and vertical directions separately.
       -  2-Combine the horizontal and vertical gradient images to obtain the magnitude of the gradient at each pixel.
       -  3-Optionally, compute the direction of the gradient at each pixel.
       - The Sobel filter typically uses a 3x3 kernel for both the    horizontal and vertical gradients. The kernels are as follows:
       - Horizontal Sobel Kernel:
       - -1  0  1
       - -2  0  2
       - -1  0  1
       - Vertical Sobel Kernel:
       - -1 -2 -1
       -  0  0  0
       -  1  2  1

13- The Laplacian filter, also known as Laplacian of Gaussian (LoG), is a derivative filter used for edge detection and image sharpening in image processing. 
              It computes the second derivative of the image intensity to detect regions of rapid intensity change, which often correspond to edges.
  - Here's how the Laplacian filter works:
       -  1-Compute the second derivative of the image intensity in both the horizontal and vertical directions.
       -  2-Combine the second derivatives to obtain the Laplacian image, which highlights regions of rapid intensity change.
 

14- The median filter is a nonlinear digital filtering technique used primarily for noise reduction in images. Unlike linear filters, such as Gaussian blur or
             mean filter, the median filter replaces each pixel's value with the median value of the neighboring pixels within a specified window. This property makes it effective at preserving edges while reducing noise.
  - Here's how the median filter works:
       -  1-Define a window (typically a square or rectangular neighborhood) around each pixel in the image.
       -  2-Sort the pixel values within the window.
       -  3-Replace the pixel's value with the median value from the sorted list.
       -  4-Move the window to the next pixel and repeat the process until all pixels have been processed.

15- The mean filter, also known as the average filter, is a simple linear filter used for smoothing and noise reduction in images. It works by replacing each
              pixel's value with the average value of the neighboring pixels within a specified window.
  - Here's how the mean filter works:
       -  1-Define a window (typically a square or rectangular neighborhood) around each pixel in the image.
       -  2-Compute the average value of the pixel intensities within the window.
       -  3-Replace the pixel's value with the computed average.
       -  4-Move the window to the next pixel and repeat the process until all pixels have been processed.

16- LPF stands for Low Pass Filter. It's a type of filter used in signal processing and image processing to allow low-frequency components to pass through 
               while attenuating high-frequency components. In image processing, low-pass filtering is often used for noise reduction and smoothing.
  - Here's how a low-pass filter works:
       -  1-Define a window (typically a square or rectangular neighborhood) around each pixel in the image.
       -  2-Compute the weighted average of the pixel intensities within the window.
       -  3-Replace the pixel's value with the computed average.
       -  4-Move the window to the next pixel and repeat the process until all pixels have been processed.

17- HPF stands for High Pass Filter. It's a type of filter used in image processing to enhance high-frequency components while suppressing low-frequency 
               components. High-pass filtering is often used for edge detection and sharpening of images.
  - Here's how a high-pass filter works:
       -  1- Define a window (typically a square or rectangular neighborhood) around each pixel in the image.
       -  2- Subtract the weighted average of the pixel intensities within the window from the value of the central pixel.
       -  3- This process highlights regions of rapid intensity change (such as edges) while suppressing regions of uniform intensity.

18- The Prewitt operator is a widely used edge detection algorithm in image processing. It calculates the gradient of an image intensity function, which
                 highlights areas of rapid intensity change, typically corresponding to edges.
  - Here's how the Prewitt operator works:
       -  1-It performs convolution of the image with two 3x3 kernels (one for horizontal changes and one for vertical changes).
       -  2-The horizontal kernel detects vertical edges, while the vertical kernel detects horizontal edges.
       -  3-The magnitude of the gradient at each pixel is computed as the square root of the sum of squares of the horizontal and vertical gradients.

19- The Robert operator is a simple edge detection algorithm used to find edges in images. It is based on convolution with two small kernels.
  - Here's how the Robert operator works:
       -  1-It performs convolution of the image with two 2x2 kernels.
       -  2-The first kernel detects edges with a 45-degree orientation, while the second kernel detects edges with a 135-degree orientation.
       -  3-The magnitude of the gradient at each pixel is computed as the square root of the sum of squares of the gradients calculated using the two kernels.

20- Histogram equalization is a technique used in image processing to improve the contrast of an image by redistributing pixel intensities. It effectively 
             stretches the histogram of pixel intensities to cover a wider range of values, thus enhancing the overall contrast of the image.
  - Here's how histogram equalization works:
       -   1-Compute the histogram of the input image, which represents the frequency distribution of pixel intensities.
       -   2-Compute the cumulative distribution function (CDF) of the histogram, which represents the cumulative sum of pixel intensities.
       -   3-Map the pixel intensities of the input image to new intensity values using the CDF, effectively redistributing the pixel intensities.
       -   4-Generate the equalized image by replacing each pixel's intensity with its corresponding mapped intensity value.
  
 
 

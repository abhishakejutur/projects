> # **Face counting system using Haar Cascade** 
> > ## **Objective :**
> >     - The objective of this task to demonstrate how to detect the face and count face in the image of Opencv 
> >     - Here we will use the haar Feature- based  cascade classifier for the face detection.
> >  ## **Face detection :**
> >     - Face detection is the one of the technology in computer vision.
> >     - In face recognition/detection we locate and visualize the human face in any digital image.
> >     - It is a subdomain of object detection, object like as animals, cars , humans etc.
> >     - Face detection technology has importance in many fields like marketing and security.
> >  ![image](https://github.com/abhishakejutur/projects/assets/91953148/45f635b9-632a-47a6-8834-ffc577ea1b44)
> > ## **Introduction :**
> >     - We will implementing a face detector and counting using Haar Cascade in opencv python.
> >     - Identifying a given object in an image is know as object detection. This task can be achieved using several techniques.
> >     - Here we will us haar cascase with pretrained XML files. Its the simplest method to perform object detection.
> >     - Haar cascades have been used for object detection on low-edge devices, and it was one of the most popular object detection algorithms in OpenCV.
> > ## **Haar Cascade :**
> >     - Haar cascade is feature-based object detection algorithm to detect the object from the images.
> >     - A cascade is trained on lots of positive and negative images for detection.
> >     - Haar cascade identify only matching and shape and size.
> >     - The algorithm does not require extensive computation and can run in real-time. We can train our own cascade function for custom objects like animals, cars, bikes, etc.
> > ## **How does it work? :**
> >     - Haar cascade uses the cascade function and cascading window. It tries to calculate features for every window and classify positive and negative.
> >     - If the window could be a part of an object, then positive, else, negative. 
> >     - Haar cascade can be understood as a binary classifier. It assigns positive to those cascade windows that can be a part of our object . and negative to those windows that can’t be a part of our object.
> > ## **Pretrained haar cascade :**
> >     - There are lots of pretrained haar cascade files that make implementation super easy.
> > ![image](https://github.com/abhishakejutur/projects/assets/91953148/88562f5b-ae74-40f0-b636-65a5ca1ca270)
> >  ## **Steps :**
> >     - Importing libraries
> >     - Object creation
> >     - Load the image – input
> >     - Color conversion to gray
> >     - Face detection
> >     - Face counting process
> >  ## **Libraries :**
> >     - Opencv
> >     - Numpy
> >     - Import cv2
> >     - Import numpy as np
> >  ## **Object creation for cascade classifier :**
> >     - We are going to use the haarcascade_frontalface_default.xml.
> >     - This file can be found at location 
> >         - C:\Users\aj\AppData\Local\Programs\Python\Python310\Lib\site-packages\cv2\data
> >  ## **input :**
> >     - Load the input image with the “imread” function of the cv2 module. 
> >     - This function will receive as input the path to the image. 
> >     - We will pass as the input the image In which we want to to face detection.
> >     - Code:
> >         - image = cv2.imread('face2.jpg')
> >  ## **Color Conversion :**
> >     - We will also convert image into grayscale, by use the cvtColor function.
> >     - This will receive as input the original image and second input code for the color space conversion.
> >     - To covert from the RGB to GRAY by using COLOR_BGR2GRAY
> >     - Code: 
> >         - grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
> >  ## **Why gray :**
> >     - Many image processing algorithms use gray scale images for input rather than color spaces.
> >     - Important reason it separates the luminance plane from the chrominance plane 
> >     - Gray have one channel, The inherent complexity of grayscale images is lower than that of color images as you can obtain features relating to brightness, contrast, edges, shape, contours, textures, and perspective without color.
> >     - Gray scale is also much faster 
> >  ## **Face detection process :**
> >     - We will call detectMultiScale method on our face_cascade object,as input we will pass our converted gray image.
> >     - Here we just pass as the input image.
> >     - This will return detects objects as a rectangle[1], so we can easily mark them in the output image.
> >     - Code: 
> >         - faces = face_cascade.detectMultiScale(grayImage)
> >         - print (type(faces))
> >  ## **Face count :**
> >     - We can also know about our output by calling the shape method on our array, which will return its dimensions.
> >     - We will get a matrix of N rows and columns,  being N the number of faces detected and 4 the dimensions of the rectangle of each face.
> >  #
> >  # ![image](https://github.com/abhishakejutur/projects/assets/91953148/a1bc0dbe-baf3-46d9-b307-d88f1cf3903e) _**Thank you..**_ 
> >       Call / whatsapp : +91 7337404176
> >       Gmail : abhishake62232@gmail.com (or) abhishakejutur@gmail.com









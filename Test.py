from LatexDocumentClass import LatexDocumentClass
import os
import re
import sys
import time
import shutil
import subprocess
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z * z + c
    return max_iter



# Instantiation of the class
LatexDocument = LatexDocumentClass()

# Settings
LatexDocument.SetNameOfTheDocument("ExampleDocument")
LatexDocument.SetTitle("Example Document: How to use the LatexDocumentClass")
LatexDocument.SetAuthor("Riccardo Nicolaidis")
LatexDocument.SetEmail("riccardo.nicolaidis@unitn.it")
LatexDocument.SetOutputDirectory("./OutputDirectory/")

# Body of the document
LatexDocument.BeginSlide("Introduction")
LatexDocument.Body += r'''
This is an example of how to use the LatexDocumentClass.

The LatexDocumentClass is a Python class that allows to create a Latex document in a very easy way.

It is built on top of the Latex Beamer class, and it is designed to create slides for presentations.

I created this class because it may be useful for managing output Report data from simulations, data analysis, etc.

You only need to do the following steps:
'''

LatexDocument.BeginItemize()
LatexDocument.Item("Import the \texttt{LatexDocumentClass} class from the \texttt{LatexDocumentClass.py} file")
LatexDocument.Item("Instantiate the class")
LatexDocument.Item("Set name, author, title, email, output directory")
LatexDocument.Item("Build the body of the document by adding the desired content")
LatexDocument.Item("Compile the document")
LatexDocument.EndItemize()
LatexDocument.EndSlide()



LatexDocument.BeginSlide("Commands")
LatexDocument.Body += r'''
The following commands are available:
'''

LatexDocument.BeginItemize()
LatexDocument.Item(r"\texttt{LatexDocument.BeginSlide(<Title of the slide>)}")
LatexDocument.Item(r"\texttt{LatexDocument.EndSlide()} (to be used at the end of the slide, if not the slide will not be closed and you'll get an error)")
LatexDocument.Item(r"\texttt{LatexDocument.BeginItemize()} (to be used at the beginning of an itemize environment)")
LatexDocument.Item(r"\texttt{LatexDocument.EndItemize()} (to be used at the end of an itemize environment, if not the itemize environment will not be closed and you'll get an error)")
LatexDocument.Item(r"\texttt{LatexDocument.Item(<Text of the item>)} (to be used inside an itemize environment, if not you'll get an error)")
LatexDocument.Item(r"\texttt{LatexDocument.Body} (to be used for adding text to the body of the document)")
LatexDocument.Item(r"\texttt{LatexDocument.InsertFigure(<Path of the image>, <Caption of the image>)} (to be used for adding a figure to the body of the document)")
LatexDocument.Item(r"\texttt{LatexDocument.Compile()} (For compiling and generating the PDF file)")

LatexDocument.EndItemize()
LatexDocument.EndSlide()


LatexDocument.BeginSlide("Example of a figure")

# Creation of the desired plots
# Dimensions of the fractal
width, height = 2600, 800
xmin, xmax = -1.5, -1.4
ymin, ymax = -0.05, 0.05
max_iter = 500

# Creazione di un array di coordinate complesse
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Applicazione della funzione del frattale di Mandelbrot
fractal = np.zeros(Z.shape, dtype=int)
for i in range(width):
    for j in range(height):
        fractal[j, i] = mandelbrot(Z[j, i], max_iter)

# Creazione del plot colorato del frattale di Mandelbrot
plt.figure(figsize=(10, 5))
plt.imshow(fractal, extent=(xmin, xmax, ymin, ymax), cmap='hot', aspect = 'auto')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")

img_name = "Test.png"
# Global path 
img_dir = os.getcwd() + "/Images/"

if not os.path.exists(img_dir):
    os.makedirs(img_dir)

plt.savefig(img_dir + "Test.png")




LatexDocument.InsertFigure(img_dir + "Test.png", "A beautiful Mandelbrot Set", 1.)
LatexDocument.EndSlide()


LatexDocument.BeginSlide("End of the document")
LatexDocument.Body += r'''
This is the end of the document.
'''
LatexDocument.EndSlide()



LatexDocument.Compile()

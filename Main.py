# This is the official code section of Image Cartoonifier
# Author: Manish Sharma

import cv2            #importing computer vision library for image processing
import easygui        #importing easygui library to open the filebox
import numpy as np    #to store image
import imageio        #to read image stored at particular path
import sys
import tkinter as tk  #import tkinter module for gui
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

#Building a filebox to choose a particular image
""" fileopenbox opens the box to choose file
and help us store file path as string """
def upload() :
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)
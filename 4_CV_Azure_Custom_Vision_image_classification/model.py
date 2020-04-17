"""
Bird image classifier based on MS Azure cloud solution

This application may not work because it is determined on an active azure account.
However, should you replace the keys with an active one, it should work off the box.
"""

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
import time
# prediction endpoint
ENDPOINT = "https://tipp-birds-cv.cognitiveservices.azure.com/"

# Replace with a valid key
#training_key = "eee51c84d47247218f86585e47bcf3d7n"
prediction_key = "bd965d89ca524eff9683e3ef7746589fn"
#prediction_resource_id = "<your prediction resource id>"

publish_iteration_name = "Iteration1"

#trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)

# Create a new project

print("creating project....")
print("")
print()
print("project created.")
print()
time.sleep(3)
print()
print("~~~~~~~~~~")
print()
print("going to main menu")
print()
print("~~~~~~~~~~")
print()
print()
time.sleep(3)

import pandas as pd
import re
import time
import sys
import os
from PIL import Image,ImageOps
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

testfolder= os.walk("test_bird")

project_id ="befe8bea-f3f3-439d-a795-094032ae38d6"

# Now there is a trained endpoint that can be used to make a prediction
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

#change project.id, publish_iteration_name
#with open(base_image_url + "images/Test/test_image.jpg", "rb") as image_contents:

# print/ display selected image file
def imaging():
    print(base_image_url)
    global im
    im =Image.open(base_image_url)
    im.show()
    time.sleep(3)
    print()
    print("~~~~~~~~~~")
    print()
    print("going back to main menu")
    print()
    print("~~~~~~~~~~")
    print()
    print()
    time.sleep(3)
    menu()
    return im


# predicting the selected image
def predicting():
    
    with open(base_image_url, "rb") as image_contents:
        results = predictor.classify_image(
            #project.id, publish_iteration_name, image_contents.read())
            project_id, publish_iteration_name, image_contents.read())
        
        

    # Display the results.

        for prediction in results.predictions:
             print("\t" + prediction.tag_name +
                   ": {0:.2f}%".format(prediction.probability * 100))
             
         
         
    y = str(results.predictions[0])
    type(y)
    top = re.split(",|:|'",y)
    top = top[18]
    print()
    print("~~~~~")
    print("PREDICTION: Your image should be a %s." %top )
             
    time.sleep(3)
    print()
    print("~~~~~~~~~~")
    print()
    print("going back to main menu")
    print()
    print("~~~~~~~~~~")
    print()
    print()
    time.sleep(3)
    menu()
    return



# Main functions start here
# 1) print out all the images in the test folder

def testlist():
    print()
    testfolder= os.walk("test_bird")
    for root, dirs, files in testfolder:

        for file in files:
            if file.lower().endswith("jpg"):
                print(file)
        number= len(files)            
        print()
        print("There are %d files" % number)
    print()
    time.sleep(3)
    print("~~~~~~~~~~")
    print()
    print("going back to main menu")
    print()
    print("~~~~~~~~~~")
    print()
    print()
    time.sleep(3)
    menu()
    return
                
                

# 2) select a picture in the test folder and view it

def firstview():
    root= "test_bird"
    print("please type the picture name u want to load (eg. 1.jpg)")
    print("~~~~~")
    picture = input()
    global base_image_url
    base_image_url= os.path.join(root+"//",picture)
    print()
    print()
    print("loading complete")
    if os.path.exists(root+"//"+picture):
        print()
        print("image loading....please wait...")
        print("output maybe a popout in a different window")
        print("~~~~~~~~~~")
        print("do you know?")
        print()
        print("birds of the same colour flock together")
        print()
        print("~~~~~~~~~~")
        time.sleep(3)
        imaging()
    else:
        print("your image dont exist")
        print()
        print("my favourite bird is a fried chicken")
        print("~~~~~~~~~~")
        print()
        print("going back to main menu")
        time.sleep(3)
        menu()
    
    return


#

def firstpred():
    root= "test_bird"
    print("please type the picture name u want to load (eg. 1.jpg)")
    print("~~~~~")
    picture = input()
    global base_image_url
    base_image_url= os.path.join(root+"//",picture)
    print()
    print()
    print("loading...please wait...")
    time.sleep(3)
    print()
    if os.path.exists(root+"//"+picture):
        print()
        print("image loading....please wait...")
        print("~~~~~~~~~~")
        print()
        print("When birds sleep, do they dream of worms??")
        print()
        print("~~~~~~~~~~")
        time.sleep(3)
        predicting()
    else:
        print("your image dont exist")
        print()
        print()
        print()
        print("~~~~~~~~~~")
        print()
        print("going back to main menu")
        time.sleep(3)
        menu()
    
    return


# main menu, python application interface

def menu():
    print()
    print("Welcome:")
    print()
    print("To start: please load test file into test folder")
    print()
    print("1) To view the full list of files, press 1")
    print("2) To view a picture, press 2")
    print("3) To predict a picture, press 3")
    print("4) To quit, press 4")
    print("~~~~~~~~")
    choice = input()
    
    if choice == "1":
        testlist()
    elif choice == "2":
        firstview()
    elif choice == "3": 
        firstpred()
    elif choice == "4":
        print("K THANKS BYE")
        sys.exit()
    else:
        menu()
    return

    
def main():
    print("Welcome to Eugin's magic classifying blackbox!")
    menu()
    return
    
main()



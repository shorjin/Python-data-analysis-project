#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: XIAOJIN LI
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
#Imports classifier function for using CNN to classify images 
from classifier import classifier 
#from get_input_args import get_input_args
#from get_pet_labels import get_pet_labels

#in_arg = get_input_args()
#results = get_pet_labels(in_arg.dir)
# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(image_dir, results_dic, model):
    for i in results_dic:
        classifier_label = classifier(image_dir + i, model).lower().strip()
        #Pet image label (index 0)
        pet_label = results_dic[i][0]
        # match pet image with classifier labels 
        #prediction = 1 if pet_label in classifier_label else 0
        if pet_label in classifier_label:
            verify_label=1
        else:
            verify_label=0
        # Add the results to the results dictionary (results_dic).
        results_dic[i].append(classifier_label)
        results_dic[i].append(verify_label)
        
    #print(results_dic)
    return None

#print('finish')     
#classify_images(in_arg.dir, results, in_arg.arch)    
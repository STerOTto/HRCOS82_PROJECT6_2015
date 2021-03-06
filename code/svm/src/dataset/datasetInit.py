#!/usr/bin/env python2

'''
    File name:      datasetInit.py
	Original Author: Emotime
    Update Author:  John Eatwell (35264926)
    Date modified:   10/09/2015
    Python Version: 2.7
	Details:     CLSLIST were created to indicate the AU / Emotion to be trained. Paths are also create differently now, with valiation/data bein used to store labels to validate test data

'''
import os
import sys
import argparse
import datasetConfigParser as dcp

from os.path import join

def dataset_init(dsPath, config):
    """
        Initialize dataset
    """
    
    # If looking for AU, then there will be an extra folder NotAUX
    createList = list(config["CLSLIST"])
    if (config["RECOG_TYPE"].upper() != "EMOTION"):
        for cls in config["CLSLIST"]:
            createList.append("Not{}".format(cls))
    
    # Validation folder is now NOT created per AU / Emotion
    pth = join(dsPath, config['VALIDATION_IMAGES'])
    if not os.path.exists(pth):
        os.makedirs(pth)
    pth = join(dsPath, config['VALIDATION_FACES'])
    if not os.path.exists(pth):
        os.makedirs(pth)
    pth=join(dsPath, config['VALIDATION_FEATURES'])
    if not os.path.exists(pth):
        os.makedirs(pth)
    pth=join(dsPath, config['VALIDATION_DATA'])
    if not os.path.exists(pth):
        os.makedirs(pth)
    
    
    for cls in createList:
        print "Creating paths for image files for: {}".format(cls)
        pth = join(dsPath, join(config['TRAINING_IMAGES'], cls))
        if not os.path.exists(pth):
            os.makedirs(pth)
        pth = join(dsPath, join(config['TRAINING_FACES'], cls))
        if not os.path.exists(pth):
            os.makedirs(pth)
        pth=join(dsPath, join(config['TRAINING_FEATURES'], cls))
        if not os.path.exists(pth):
            os.makedirs(pth)

    pth=join(dsPath, config['TRAIN_FOLDER'])
    if not os.path.exists(pth):
        os.makedirs(pth)
    pth=join(dsPath, config['CLASSIFIER_FOLDER'])
    if not os.path.exists(pth):
        os.makedirs(pth)
    pth=join(dsPath, config['CLASSIFIER_SVM_FOLDER'])
    if not os.path.exists(pth):
        os.makedirs(pth)
    pth=join(dsPath, config['CLASSIFIER_ADA_FOLDER'])
    if not os.path.exists(pth):
        os.makedirs(pth)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cfg", default="dataset.cfg", help="Dataset config file name")
    parser.add_argument("dsFolder", help="Dataset folder path")
    args = parser.parse_args()

    try:
        config={}
        config=dcp.parse_ini_config(args.cfg)
        dataset_init(args.dsFolder, config)
    except Exception as e:
        print("ERR: something wrong (%s)" % str(e))
        sys.exit(1)

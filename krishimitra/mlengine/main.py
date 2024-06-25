import pickle as pkl
import numpy as np
import os

def predictYield(data):
    model = pkl.load(open(f"{os.getcwd()}/krishimitra/mlengine/CropYieldPrediction/{data[0]}.pkl", "rb"))
    data = data[1:]
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)
    return prediction[0]

def recommendCrop(data):
    model = pkl.load(open(f"{os.getcwd()}/krishimitra/mlengine/CropRecommendation/CropRecommender.pkl", "rb"))
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)
    return prediction[0]

def recommendFertilizer(data):
    model = pkl.load(open(f"{os.getcwd()}/krishimitra/mlengine/FertilizerRecommendation/FertilizerRecommender.pkl", "rb"))
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)
    return prediction[0]
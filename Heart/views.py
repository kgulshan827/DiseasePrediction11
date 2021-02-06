from django.shortcuts import render
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from joblib import load
# Create your views here.

def heart(request):
    return render (request,'heart_input.html')

def getPredictions(age,sex,cp,trestbps,chol,restecg,thalach,exang,oldpeak,slope,thal):

    model =load('Heart/Models/Heart_Model')
    X=[[age,sex,cp,np.log([trestbps]),np.log([chol]),restecg,thalach,exang,oldpeak,slope,thal]]
    sc=load('Heart/Models/scaler')
    prediction = model.predict(sc.transform(X))
    
    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'
def heart_result(request):
    age = float(request.GET['age'])
    sex = float(request.GET['sex'])
    cp = float(request.GET['cp'])
    trestbps = float(request.GET['trestbps'])
    chol = float(request.GET['chol'])
    restecg = float(request.GET['restecg'])
    thalach= float(request.GET['thalach'])
    exang = float(request.GET['exang'])
    oldpeak = float(request.GET['oldpeak'])
    slope = float(request.GET['slope'])
    thal = float(request.GET['thal'])
    
    

    result = getPredictions(age,sex,cp,trestbps,chol,restecg,thalach,exang,oldpeak,slope,thal)

    return render(request, 'heart_result.html', {'result': result})





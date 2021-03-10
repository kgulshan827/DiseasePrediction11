from django.shortcuts import render
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from joblib import load
# Create your views here.

def diabetes(request):
    return render (request,'diabetes_input.html')

def getPredictions(X):

       

    model =load('diabetes/Models/Diabetes_Model')
    sc=load('diabetes/Models/dscaler')
    prediction = model.predict(sc.transform(X))
    
    if prediction == 1:
        return 'yes'
    elif prediction == 0:
        return 'no'
    else:
        return 'error'
def diabetes_result(request):

    Z=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
    
    a=[[]]
    
    for p in Z:

        p = float(request.GET[p])
        a[0].append(p)
    

      
    
    

    result = getPredictions(a)
    return render(request, 'diabetes_result.html', {'result': result})





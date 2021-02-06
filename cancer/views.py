from django.shortcuts import render
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from joblib import load
# Create your views here.

def cancer(request):
    return render (request,'cancer_input.html')

def getPredictions(X):

       

    model =load('cancer/Models/cancer_model')
    sc=load('cancer/Models/scaler')
    prediction = model.predict(sc.transform(X))
    
    if prediction == 0:
        return 'yes'
    elif prediction == 1:
        return 'no'
    else:
        return 'error'
def cancer_result(request):

    Z=['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
       'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']
    
    a=[[]]
    
    for p in Z:

        p = float(request.GET[p])
        a[0].append(p)
    

      
    
    

    result = getPredictions(a)
    return render(request, 'cancer_result.html', {'result': result})





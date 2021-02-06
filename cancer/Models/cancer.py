import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.externals import joblib
from joblib import dump,load
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
logreg=LogisticRegression()

data=pd.read_csv("/home/gulshan/Desktop/Diseaseprediction/Datasets/cancer.csv")
data.drop(["Unnamed: 32"],axis="columns",inplace=True)
data.drop(["id"],axis="columns",inplace=True)
a=pd.get_dummies(data["diagnosis"])
cancer=pd.concat([data,a],axis="columns")
cancer.drop(["diagnosis","B"],axis="columns",inplace=True)
cancer.rename(columns={"M":"Malignant/Benign"},inplace=True)
y=cancer[["Malignant/Benign"]]
X=cancer.drop(["Malignant/Benign"],axis="columns")
ss = StandardScaler()
print(X.columns.size)
Z=['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
       'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']
for p in Z:
    print(p)
X=ss.fit_transform(X)
logreg.fit(X,y)
y_pred=logreg.predict(X)
print(y[20:21])
print(accuracy_score(y,y_pred))##98% score 
#joblib.dump(logreg,'cancer_model')
#joblib.dump(ss,'scaler')


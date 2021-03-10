import pandas as pd
import numpy as np
from sklearn.externals import joblib
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from sklearn.linear_model import LogisticRegression
#warnings.filterwarnings("ignore", category=DeprecationWarning) 
from sklearn.preprocessing import StandardScaler
import random
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_validate
import sweetviz
from sklearn.metrics import accuracy_score
data = pd.read_csv("/home/gulshan/Desktop/Diseaseprediction/Diseaseprediction/Datasets/diabetes.csv")
#print(data)
#my_report=sweetviz.analyze(data)
#my_report.show_html('report.html')
target=data['Outcome']
data=data.drop(['Outcome'],axis=1)
sc= StandardScaler()
data=sc.fit_transform(data)

lr=LogisticRegression()
lr.fit(data,target)
cv_results = cross_validate(lr, data,target, cv=10)
print(lr.predict(data))
#joblib.dump(lr,"Diabetes_Model")
#joblib.dump(sc,'dscaler')
y_pred=lr.predict(data)

#print(accuracy_score(target,y_pred))(78.38% acc.)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('heart.csv')

#print(df.tail())
#print(df.info())
#defective heart = 1
#healthy heart = 0

X=df.drop(columns='target',axis=1)
Y=df['target']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=23)
#print(X_test.shape,X_train.shape)
model = LogisticRegression()
model.fit(X_train,Y_train)
Y_pred=model.predict(X_test)
#print(Y_train)
score=accuracy_score(Y_test,Y_pred)
print("The accuracy is ",score*100)
print("Enter values")
#input_data=list(map(float,input().split()))
input_data=(62,0,1,140,268,0,0,160,0,3.6,0,2,2)
arr=np.array(input_data)
# print(arr)
prediction = model.predict(arr.reshape(1,-1))
print(prediction)
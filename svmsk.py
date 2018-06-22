import numpy as np
import pandas as pd
from sklearn import cross_validation
from sklearn.svm import SVC

dataframe = pd.read_csv('cancer.csv')
#print(dataframe.head())
dataframe.replace('?',-99999,inplace = True)
dataframe.drop(['id'],1,inplace = True)

# X = dataframe.idloc[:,:-1].values

X = dataframe.drop(['CLass'],1)
Y = dataframe['CLass']

X_train,X_test,Y_train,Y_test = cross_validation.train_test_split(X,Y,test_size = 0.25)

classifier = SVC(kernel = 'linear',random_state = 0)
classifier.fit(X_train,Y_train)

Accuracy = classifier.score(X_test,Y_test)

print'Accuracy:',Accuracy
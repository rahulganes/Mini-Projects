#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 23:15:05 2017

@author: gokul
"""



# 2.1 Decision Trees (Good)
# Fitting DT Classification
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train2_scaled, y_train)
# Predicting the Test set results
y_pred = classifier.predict(X_test2_scaled)

# 3.1 NB (worsttttttttttttttuuuuuuuuuu)
# Fitting Gaussian Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
cols = ['level_type','greedy','number theory','dp','divide and conquer','trees','submission_count','problem_solved','last_online_time_seconds','max_rating','rank']
classifier.fit(X_train3[cols], y_train)
# Predicting the Test set results
y_pred = classifier.predict(X_test3[cols])

# 4.1 Kernel-SVM
# Fitting Kernel SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train_scaled, y_train)
# Predicting the Test set results
y_pred = classifier.predict(X_test_scaled)

# 5.1 Log.Regr (Not so bad)
# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train_scaled, y_train)
# Predicting the Test set results
y_pred = classifier.predict(X_test_scaled)

# 6.1 knn - Good
# Fitting K-NN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 10, metric = 'minkowski', p = 2)
classifier.fit(X_train_scaled, y_train)
# Predicting the Test set results
y_pred = classifier.predict(X_test_scaled)


# 7.1 Gradient Boost (poor)
from sklearn.ensemble import GradientBoostingClassifier
classifier = GradientBoostingClassifier(learning_rate = 0.3, n_estimators =50 , max_depth = 5).fit(X_train_scaled, y_train)
# Predicting the Test set results
y_pred = classifier.predict(X_test_scaled)

# 8.1 MLP
from sklearn.neural_network import MLPClassifier
classifier = MLPClassifier(hidden_layer_sizes = [10], solver='lbfgs',
                         random_state = 0).fit(X_train_scaled, y_train)
# Predicting the Test set results
y_pred = classifier.predict(X_test_scaled)

# 9.1 ANN
# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense
# Initialising the ANN
classifier = Sequential()
# Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 11))
# Adding the second hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu'))
# Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))
# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 100)
# Predicting the Test set results
y_pred = classifier.predict(X_test_scaled)
#!/usr/bin/env python

from __future__ import division
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
creates random forest classifier to classify tumors from
breast cancer (wisconsin) data set as malignant or benign

input arguments:
none

return values:
none
"""
def main():
	# reading data
	data = pd.read_csv("data.csv", header=0)
	# features_mean will hold all mean columns
	features_mean =	list(data.columns[3:13])
	# binarizing diagnosis: malignant: 1, benign: 0
	data["diagnosis"] = data["diagnosis"].map({"M":1, "B":0})
	data.rename(columns={"diagnosis": "is_malignant"}, inplace=True)
	# correlation heatmap
	corr = data[features_mean].corr()
	sns.set(font_scale=0.45)
	sns.heatmap(corr, cbar=True, square=True, annot=True, fmt='.2f', xticklabels=features_mean, yticklabels=features_mean, cmap='coolwarm')
	plt.show()
	# only predict with columns with a low correlation
	prediction_columns = ["texture_mean", "perimeter_mean", "smoothness_mean", "compactness_mean", "symmetry_mean", "fractal_dimension_mean"]
	# splitting dataset
	train, test = train_test_split(data, test_size = 0.3, random_state=42)
	train_X = train[prediction_columns]
	train_y = train.is_malignant
	test_X = test[prediction_columns]
	test_y = test.is_malignant
	# prevalences
	probability_malignant = sum(train_y) / len(train_y)
	probability_benign = 1 - probability_malignant
	print "Percentage of training data that is benign:\t"+str(round(probability_benign, 2))
	print "Percentage of training data that is malignant:\t"+str(round(probability_malignant, 2))
	# fitting random forest classifier
	model = RandomForestClassifier(n_estimators=100, random_state=42)
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)
	# accuracy score
	accuracy_score = metrics.accuracy_score(prediction, test_y)
	print "\nRandom Forest Classifier Accuracy: "+str(round(accuracy_score, 2))
	# confusion matrix
	print "\nRandom Forest Classifier Confusion Matrix:"
	tn, fp, fn, tp = metrics.confusion_matrix(test_y, prediction).ravel()
	print "benign classified as benign:\t"+str(tn)
	print "malignant classified as benign:\t"+str(fp)
	print "benign classified as malignant:\t"+str(fn)
	print "malignant classified as malignant:\t"+str(tp)
	# classification report
	print "\n"+metrics.classification_report(test_y, prediction, target_names=["benign", "malignant"])

if __name__ == "__main__":
	main()

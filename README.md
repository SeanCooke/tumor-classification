# Tumor Classification
Random forest classifier achieves 96% accuracy on diagnosis from [Breast Cancer (Wisconsin) Data Set](https://www.kaggle.com/gargmanish/basic-machine-learning-with-cancer/data)

## Data
Data is taken from the [Breast Cancer (Wisconsin) Data Set](https://www.kaggle.com/gargmanish/basic-machine-learning-with-cancer/data).  and tutorial was used as a starting point

## Example
`$ python tumor-classification.py`
![Breast Cancer (Wisconsin) Correlation Heatmap](https://github.com/SeanCooke/tumor-classification/blob/master/correlation-heatmap.png?raw=true)
~~~~
Percentage of training data that is benign:	0.63
Percentage of training data that is malignant:	0.37

Random Forest Classifier Accuracy: 0.96

Random Forest Classifier Confusion Matrix:
benign classified as benign:	106
malignant classified as benign:	2
benign classified as malignant:	4
malignant classified as malignant:	59

             precision    recall  f1-score   support

     benign       0.96      0.98      0.97       108
  malignant       0.97      0.94      0.95        63

avg / total       0.96      0.96      0.96       171

Summary:
This classifier assumes the true prevalence of malignant tumors is approximately equal to the sample prevalence of malignant tumors (37%).   70% of the Breast Cancer Wisconsin (Diagnostic) data were used for training and 30% was used for testing.  A random forest classifier correctly classifies the test data 96% of the time.  In tumor classification, it is important to minimize the number of malignant tumors classified as benign tumors.  Our classifier has a false negative rate of 3%.
~~~~

## References
* [Basic Machine Learning with Cancer](https://www.kaggle.com/gargmanish/basic-machine-learning-with-cancer/notebook)

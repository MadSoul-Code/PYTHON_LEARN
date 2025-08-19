import sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix


cancer_data = load_breast_cancer()

features = cancer_data["data"]

labels = cancer_data["target"]

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state = 20,stratify=labels)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

obj_gnb = GaussianNB()

model_AI = obj_gnb.fit(X_train, y_train)

predictions = model_AI.predict(X_test)

print("Predictions:", predictions)

print("Accuracy:", accuracy_score(y_test, predictions)* 100,"%")

print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
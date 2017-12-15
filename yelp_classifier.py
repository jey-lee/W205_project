from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import pandas as pd
import sys

# features = word, count
# target = average_stars


#lr = LogisticRegression()

# Train logistic regression model
def init():
	train_data = {'word':['amazing', 'recommended', 'outstanding', 'worst', 'horrible', 'terrible']}

	train_labels = [4.90, 4.89, 4.86, 1.08, 1.09, 1.16]

	train_data = pd.DataFrame(train_data, columns=['word'])
	le = preprocessing.LabelEncoder()
	train_data['word'] = le.fit_transform(train_data['word'])
	train_labels = [int(i * 100) for i in train_labels]

	print train_data
	print train_labels

	global lr
	lr = LogisticRegression()
	lr.fit(train_data, train_labels)


# Print predicted rating based on word
def predict(w):
	le = preprocessing.LabelEncoder()
	w = le.fit_transform(w)
	print lr.predict(w)


def main():
	# split input into array
	# run prediction on each word
	# output average of predictions
	init()
	predict(sys.argv[1])

if __name__ == "__main__": main()

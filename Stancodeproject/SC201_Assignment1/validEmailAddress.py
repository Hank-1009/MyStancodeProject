"""
File: validEmailAddress.py
Name: Hank Chou
----------------------------
This file shows what a feature vector is
and what a weight vector is for valid email 
address classifier. You will use a given 
weight vector to classify what is the percentage
of correct classification.

Accuracy of this model: 0.6538461538461539
"""

WEIGHT = [                           # The weight vector selected by Jerry
	[0.4],                           # (see assignment handout for more details)
	[0.4],
	[0.2],
	[0.2],
	[0.9],
	[-0.65],
	[0.1],
	[0.1],
	[0.1],
	[-0.7]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	# create a list to record the accuracy score
	accuracy_count = []
	for maybe_email in maybe_email_list:
		# record the sum
		sum_ = []
		feature_vector = feature_extractor(maybe_email)
		for i in range(len(WEIGHT)):
			sum_.append(WEIGHT[i][0]*feature_vector[i])
		# 以下註解只是想確認格式語法正確:
		print(sum_, end=' ')
		print(sum(sum_))
		if sum(sum_) > 0:
			accuracy_count.append(True)
		else:
			accuracy_count.append(False)
	# answer是txt是否為有效email的答案，我用bool表示
	answer = [False]*13 + [True]*13
	t = 0
	for i in range(len(accuracy_count)):
		if accuracy_count[i] == answer[i]:
			t += 1
	# print(accuracy_count)
	print(t/len(accuracy_count))


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with 10 values of 0's or 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i] = 1 if '@' in maybe_email else 0
		elif i == 1:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' not in maybe_email.split('@')[0] else 0
		elif i == 2:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@')[0] != '' else 0
		elif i == 3:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@')[1] != '' else 0
		elif i == 4:
			if feature_vector[0]:
				check = maybe_email.split('@')
				for j in range(len(check)):
					if j != 0:
						if '.' in check[j]:
							feature_vector[i] = 1
		elif i == 5:
			feature_vector[i] = 1 if ' ' not in maybe_email else 0
		elif i == 6:
			feature_vector[i] = 1 if maybe_email[-4:] == '.com' else 0
		elif i == 7:
			feature_vector[i] = 1 if maybe_email[-4:] == '.edu' else 0
		elif i == 8:
			feature_vector[i] = 1 if maybe_email[-3:] == '.tw' else 0
		else:
			feature_vector[i] = 1 if len(maybe_email) > 10 else 0
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that might be valid email addresses
	"""
	# TODO: read the txt file
	email = []
	with open(DATA_FILE, "r", encoding='UTF-8') as f:
		for line in f:
			line = line.split('\n')[0]
			email.append(line)
	return email


if __name__ == '__main__':
	main()

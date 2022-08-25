"""
File: validEmailAddress_2.py
Name: Hank Chou
----------------------------
Please construct your own feature vectors
and try to surpass the accuracy achieved by
Jerry's feature vector in validEmailAddress.py.
feature1:  '@' in the string
feature2:  ends with '.com' , '.tw' or '.edu'
feature3:  There is '..' after '@'
feature4:  There is white space in the string
feature5:  @前後的字串之最後一個字元不是數字、不是英文字母也不是"類，若無'@'則直接視為1
feature6:  First letter is digit or alpha
feature7:  There are two or more  '\' in the string
feature8:  some strings before '@'
feature9:  string before '@' contains upper case letter
feature10: There are 'stancode.' or '.stancode' in the string

Accuracy of your model: 0.9615384615384616
"""
import numpy as np

WEIGHT = [                           # The weight vector selected by you
	[0.3],                              # (Please fill in your own weights)
	[0.3],
	[-1.2],
	[-0.9],
	[-1.2],
	[0.3],
	[-0.6],
	[0.1],
	[-1.2],
	[-1.2]
]

weight_vector = np.array(WEIGHT)
weight_vector = weight_vector.T

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	accuracy_count = []
	for maybe_email in maybe_email_list:
		# use sum_ to record the sum
		sum_ = []
		feature_vector = feature_extractor(maybe_email)
		array = []
		# 使用numpy module 的方式製造feature_vector的array
		for each in feature_vector:
			array.append([each])
		# create array for each feature vector of one maybe_email
		weight_vector_array = np.array(array)
		# array dot
		for i in range(len(WEIGHT)):
			sum_.append(weight_vector.dot(weight_vector_array))
		""" 這個下面是原版使用list的部分
		# for i in range(len(WEIGHT)):
			#sum_.append(WEIGHT[i][0] * feature_vector[i])
		"""
		# 以下註解只是想確認格式語法正確:
		# print(feature_vector, end=' ')
		# print(sum_, end=' ')
		# print(sum(sum_))
		if sum(sum_) > 0:
			accuracy_count.append(True)
		else:
			accuracy_count.append(False)
	# answer是txt是否為有效email的答案，我用bool表示
	answer = [False] * 13 + [True] * 13
	t = 0
	for i in range(len(accuracy_count)):
		if accuracy_count[i] == answer[i]:
			t += 1
	# print(accuracy_count) : 確認用
	print(t / len(accuracy_count))


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
			if maybe_email[-4:] == '.com':
				feature_vector[i] = 1
			elif maybe_email[-4:] == '.edu':
				feature_vector[i] = 1
			elif maybe_email[-3:] == '.tw':
				feature_vector[i] = 1
			else:
				feature_vector[i] = 0
		elif i == 2:
			if feature_vector[0]:
				check = maybe_email.split('@')
				for j in range(len(check)):
					if j != 0:
						if '..' in check[j]:
							feature_vector[i] = 1
		elif i == 3:
			feature_vector[i] = 1 if ' ' in maybe_email else 0
		elif i == 4:
			if feature_vector[0]:
				check_new = maybe_email.split('@')
				# 因為可能不只一個@符號，所以要檢查每個切割字串
				for string in check_new:
					# 先檢查有東西
					if string == '':
						feature_vector[i] = 1
						break
					elif not string[-1].isalpha() and not string[-1].isdigit() and string[-1] != '”' and string[-1] != '"' and string[-1] != '“':
						feature_vector[i] = 1
						break
			# 若沒有'@'則此項直接視為1
			else:
				feature_vector[i] = 1
		elif i == 5:
			if maybe_email[0].isalpha():
				feature_vector[i] = 1
			elif maybe_email[0].isdigit():
				feature_vector[i] = 1
			else:
				feature_vector[i] = 0
		elif i == 6:
			check_3 = maybe_email.split("\\")
			feature_vector[i] = 1 if len(check_3) > 2 else 0
		elif i == 7:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@')[0] != '' else 0
		elif i == 8:
			if feature_vector[0]:
				check_4 = maybe_email.split('@')
				for j in range(len(check_4)):
					if j != (len(check_4)-1):
						if check_4[j].lower() != check_4[j]:
							feature_vector[i] = 1
		else:
			if '.stancode' in maybe_email:
				feature_vector[i] = 1
			elif 'stancode.' in maybe_email:
				feature_vector[i] = 1
			else:
				feature_vector[i] = 0
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that might be valid email addresses
	"""
	# TODO: read the txt file
	email = []
	with open(DATA_FILE, "r", encoding='UTF-8') as f:
		for line in f:
			line = line.replace('\n', '')
			email.append(line)
	return email


if __name__ == '__main__':
	main()

def unique_char(str):
	letter_dict = {}
	for letter in str:
		if letter_dict.get(letter):
			return False
		letter_dict[letter] = 1
	return True

# print unique_char("hey")

def perm(str1,str2):
	if len(str1) == len(str2):
		str1_dict = {}
		for letter in str1:
			str1_dict[letter] = str1_dict.get(letter,0) + 1
		for letter in str2:
			if str1_dict.get(letter):
				str1_dict[letter] = str1_dict.get(letter,0) - 1
			else:
				return False
		return True
	return False

# print perm("hel  lo", " elloh")

#######################Ask about this!!!!!!!!!!!!!!!!!!!!!!!!##################
###http://www.skymind.com/~ocrow/python_string/

def spaces(str):
	str_list = []
	word_list = str.split()
	for word in word_list:
		if word != " ":
			str_list.append(word)
			str_list.append("%20")
	return ''.join(str_list)

# print spaces("Mr. John Smith     ")


#######################Ask about this!!!!!!!!!!!!!!!!!!!!!!!!##################
###############  What is the runtime?- no string concatenation?
def compressed(a_str):
	comp = []
	count  = 1
	curr_lett = a_str[0]
	print len(a_str)
	for i, letter in enumerate(a_str[1:]):
		if letter == curr_lett:
			count +=1
			if i == len(a_str)-2:
				comp.append(letter)
				comp.append(str(count))
		else:
			comp.append(curr_lett)
			comp.append(str(count))
			count = 1
			curr_lett = letter
			if i == len(a_str)-2:
				comp.append(letter)
				comp.append(str(count))
	if len(comp) == len(a_str)*2:
		return a_str
	return "".join(comp)

# print compressed("abcd")


def anagram_sets():




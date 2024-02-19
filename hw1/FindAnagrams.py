from WordCompare import word_compare
def find_anagrams(myset):
	Dict = {}
	for i in range(len(myset)):
		Dict[myset[i]] = []
		for j in range(len(myset)):
			if i != j and word_compare(myset[i],myset[j]) == "Anagram":
				Dict[myset[i]].append(myset[j])
	new = ""
	for key,value in Dict.items():
		new += key + ": " + str(value) + "\n"
	new = new.strip("\n")
	return new

#to test function
words = ["ghost", "cat", "goths", "spot", "notebook", "tac", "anagram", "desk", "email", "cheese", "tops", "looks"]

expected_results = "ghost: ['goths']\ncat: ['tac']\ngoths: ['ghost']\nspot: ['tops']\nnotebook: []\ntac: ['cat']\nanagram: []\ndesk: []\nemail: []\ncheese: []\ntops: ['spot']\nlooks: []"

assert find_anagrams(words) == expected_results
#I expect no error to run otherwise the two strings are not equivalent

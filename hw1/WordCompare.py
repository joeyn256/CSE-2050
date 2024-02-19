def word_compare(s1,s2 = "steal"):
	if isinstance(s1, str) and isinstance(s2, str):
		l_s1 = []
		l_s2 = []
		for i in s1:
			l_s1.append(i)
		for i in s2:
			l_s2.append(i)
		l_s1 = sorted(l_s1)
		l_s2 = sorted(l_s2)
		if l_s1 == l_s2:
			return("Anagram")
		else:
			return(s1, s2)
	else:
		return("Those aren't strings!")

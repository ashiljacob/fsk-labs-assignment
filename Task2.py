
s = input("Enter a Sentence : ").split()

ls = [x for x in s if x not in s[s.index(x) + 1:]]

print("No Of unique word : \n",len(ls),"\n Unique words are :",ls)
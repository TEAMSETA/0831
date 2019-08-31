str1 = "This is a "
str2 = "short string."
sentence = str1 + str2

print("{}".format(sentence))
print("{} {} {}".format("She is", "very"*4 , "beautiful." ))
m = len (sentence)
print("{}".format(m))

str1 = "My deliveralbe is due in May"
str1_list1 = str1.split()
str1_list2 = str1.split(" ",2)

print(str1_list1)
print("FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
.format(str1_list2[0], str1_list2[1], str1_list2[2]))

str2 = "Your,deliveralbe,is,due,in,June"
str2_list = str2.split(',')

print(str2_list)
print("{} {} {} {}".format(str2_list[1],str2_list[2],str2_list[5],\
str2_list[-1]))
print("{}".format(','.join(str2_list)))
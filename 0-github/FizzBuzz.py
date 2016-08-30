str = "Fizz"
str2 = "Buzz"
cnt = 0

f = open('text.txt','w')

for n in range(30):
	print >> f, n+1,
	if 0 == (n+1)%3:	
		print >> f, str,
	if 0 == (n+1)%5:
		print >> f, str2,
	print >> f, "\n",

f.close()

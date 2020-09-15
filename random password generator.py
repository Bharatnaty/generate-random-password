from random import randint
import random
def password(s7):
	temp=list(s7)
	random.shuffle(temp)
	return "".join(temp)

s1=chr(randint(65,90))
s2=chr(randint(65,90))
s3=chr(randint(97,122))
s4=chr(randint(97,122))
s5=int(randint(30,39))
s6=int(randint(30,39))
s7=s1+s2+s3+s4+str(s5)+str(s6)
str(s7)
print(password(s7))
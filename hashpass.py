#note, I suck at math, so I am not very confident in this part, and I think it can suerly be made much more optimized
import hashlib
import array
import string

# class HashableBytearray(bytearray):
# 	def __hash__(self):
# 		return hash(str(self))

def hash_my_password(password,salt,symbols,spaces):
	salt = str.encode(salt)
	password = str.encode(password)
	hashed_password = hashlib.sha256(password + salt).digest()
	# dk = hashlib.pbkdf2_hmac('sha256',passwod ,salt,100000)
	
	def testBit(int_type, offset):
		mask = 1 << offset
		return(int(bool(int_type & mask)))

	def setBit(int_type, offset):
		mask = 1 << offset
		return(int_type | mask)
	#convert the data to a string 
	barray=array.array('B', hashed_password)
	increment=0
	stringout=""
	for byte in barray:
		increment=increment+1
		for c in range(0,8):
			stringout = stringout+ str(testBit(byte,c))
	
	#put everything into groups of 8
	g=[]#list that contains the values of each byte
	bytenum=0
	while(True):
		if bytenum==256-1:
			break
		if bytenum%8==0:
			g.append(0)
		if stringout[bytenum]=="1":
			g[len(g)-1]=setBit(g[len(g)-1],bytenum%8)
		bytenum=bytenum+1
	stringout=""
	if spaces:
		symbols=" "+symbols
	chars= string.ascii_uppercase + string.ascii_lowercase + string.digits  + symbols
	for element in g:
		stringout=stringout+chars[element%len(chars)]

	return stringout
#!/usr/bin/env python3

"""
1.check hash length
2.grab salt from hash
3.remove colon from hash
4.compare hash to each value in ow (hashed with grabbed salt)
5. if hash matches produced hash (e.g. produce sha1: hashlib.sha1(salt+BytesToHash).hexdigest())
	append result to file
	jump back to beginning of ow
	move onto next hash
6. Else, move onto next value in ow.
7. If hash isnt cracked by the end of ow file, record in file (may have been wrong on hash algorithm)

function hash_crack(parameter=md5|sha256|sha512)
{
	global salt,hash
	for plaintext_val in ow:
		found=0
		plaintext_val.strip()
		ow_hash=hashlib.parameter(salt+plaintext_val).hexdigest()

		if ow_hash==hash:
			# hash cracked
			# write result to file 
			found+=1
			break
		else:
			continue
	if found==0:
		# write to file-isnt the expected hashing algorithm for that hash

}

for hash in hashes:
	hash.strip()
	if hash.length=43 or hash.length=33:
		# md5 hash
		# grab salt from hash (grab chars up until colon)
		# remove colon from hash
		# loop through ow and compared hashed ow vals to hash in loop (w/ hash_crack func)
	elif hash.length=75:
		# sha256
	elif hash.length=139:
		# sha512
	else:
		# i missed a hash algorithm, make note of it
"""

import hashlib

def gen_hashes(alg,val):
	# global keyword to specify that variables under these names should be modified under the global scope
	global hash_to_cr,salt,hashes_cr,hashes_uncr,found
	# only check hash if the found variable has not been incremented
	if found==0:
		# generate a hash to compare based on the algorithm of the hash being cracked
		if alg=="md5":	genned_hash=hashlib.md5(val.encode()+salt.encode()).hexdigest()
		elif alg=="sha256":	genned_hash=hashlib.sha256(val.encode()+salt.encode()).hexdigest()
		# useable as there are only 3 possible algorithms
		else:	genned_hash=hashlib.sha512(val.encode()+salt.encode()).hexdigest()

		
		"""if the generated hash is the same as the hash from the hash file
								increment hashes_cr and found by 1
								print results to stdout and file"""
		
		if str(genned_hash)==str(hash_to_cr):
			print(hash_to_cr,"cracked, result:",val) ; found+=1 ; hashes_cr+=1 
			results_file.write(hash_to_cr+" cracked, result: "+val+"\n")



def hash_cracker(alg):
	# reset cursor in ow_lower to beginning of file
	plaintxt_file.seek(0)
	global hash_to_cr,salt,hashes_cr,hashes_uncr,found,arra
	found=0  
	for ptxt in plaintxt_file:
		val=ptxt.strip("\n") 

		"""Adds a little more time to the execution of the program as each mangled value is produced per line in ow_lower regardless off if needed;
								for testing what mangling rules were in use this was the easiest format"""
		mangling=[
			val , val.upper() , val.capitalize() , val[::-1] , val+val[::-1] , val*2,
			val.replace("e","3") , val.replace("s","5") , val.replace("i","1") , val.replace("o","0") , val.replace('s','$') , val.replace('t','7') , val.replace('c','(') , val.replace('h','#'),
			val.replace("a","@") , val.replace("e","3").replace("s","5").replace("a","@") , val.replace('s','$').replace('a','@') , val.replace("b","8") , val.replace("b","8").replace('o','0') , val.replace('t','+'),
			val.upper().replace("E","3") , val.upper().replace("S","5") , val.upper().replace("I","1") , val.upper().replace("O","0") , val.upper().replace('S','$') , val.upper().replace('H','#'),
			val.upper().replace("A","@") , val.upper().replace('T','7') , val.upper().replace("E","3").replace("S","5").replace("A","@") , val.upper().replace('S','$').replace('A','@'),
			val.upper().replace("B","8") , val.upper().replace("B","8").replace('O','0') , val.upper().replace('T','+')
		]
			
		for r in mangling:	gen_hashes(alg,r)
								
		# execute the caesar shift cipher on the val, checks for a shift from +1 to +4
	
		shifted_chars=[] ; cae={}
		for i in range(1,5):
			shifted_chars=map(lambda ch: chr(ord(ch)+i),val)
			cae[i]="".join(shifted_chars)
			gen_hashes(alg,cae[i])
										
		# find vals beginning/ending with a special char

		for e in arra:	gen_hashes(alg,e+val) ; gen_hashes(alg,val+e) 

		# vals ending with a number- either 0 to 9 or 1950-2029
		
		for i in range(0,10):
			gen_hashes(alg,val+str(i))
			for iii in range(190,203):	gen_hashes(alg,val+str(iii)+str(i))
																																																				
	if found==0:
		print("Hash",hash_to_cr,"could not be cracked...") ; hashes_uncr+=1
		results_file.write("Hash "+hash_to_cr+" could not be cracked.\n") 


hash_file=open("./hashes.txt","r")
results_file=open("./results.txt","a+")
plaintxt_file=open("./ow_tiny_lower.lst","r")
hashes_cr=0 ; hashes_uncr=0 ;  arra=['!','@','#','$','%','^','&','*','(',')','-','_','+','<','>','?'] 

for h in hash_file:
	"""
	seperate the salt from the hash- will correctly respond to salts of variable length
	due to the use of split (slices each value upto but not including the provided param, adds 
	to an array and repeats until the end of the value is reached.)
		1 tells split that the resulting list can only hold a maximum of 2 elements
	
	Strip removes whitespace by default but will also remove specified characters- I used this 
	to rmeove the newline char after each hash	
	"""
	hash_to_cr=str(h.split(":",1)[1].strip("\n")) ; salt=str(h.split(":",1)[0].strip())

	if len(hash_to_cr)==32:
		# md5 hash
		hash_cracker("md5")
	elif len(hash_to_cr)==64:
		# sha256
		hash_cracker("sha256")
	elif len(hash_to_cr)==128:
		# sha512
		hash_cracker("sha512")
	else:
		print(h,"did not match the length of SHA512, SHA256 or MD5.")

print(str(hashes_cr)+" hashes cracked.\n"+str(hashes_uncr)+" hashes uncracked.")
results_file.write(str(hashes_cr)+" hashes cracked.\n"+str(hashes_uncr)+" hashes uncracked.")
hash_file.close() ; plaintxt_file.close() ; results_file.close()

exit(0)
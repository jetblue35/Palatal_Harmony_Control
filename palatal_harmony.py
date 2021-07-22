"""
This function checks the palatal harmony, 
It returns 1 if the word fits the rule, and 0 if it doesn't.
"""
def check_palatal_harmony(word):
	res = 0
	back_count = 0		#backness vowel's count
	front_count = 0		#frontness vowel's count
	
	w_len = len(word)
	
	for i in range(w_len):
		
		#this control block checks  the vowel letter.
		if(word[i] == 'a' or word[i] == 'ı' or word[i] == 'o' or word[i] == 'u'):
			back_count += 1
		elif(word[i] == 'e' or word[i] == 'i' or word[i] == 'ö' or word[i] == 'ü'):	
			front_count += 1
	
	if(back_count != 0 and front_count == 0):	#only backness vowel, so result is 1.
		res = 1
	elif(back_count == 0 and front_count != 0):	#only frontness vowel, so result is 1.
		res = 1
	else:										
		res = 0	

	return res	

#Driver code.
"""
if __name__ == "__main__":

	w = input("Lütfen bir kelime giriniz: ")
	res = check_palatal_harmony(w)
	if res == 1:
		print("Kelime büyük ünlü uyumuna uymaktadır.")
	else:
		print("Kelime büyük ünlü uyumuna uymamaktadır.")
"""							
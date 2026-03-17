def Names() :
	names_list = ['Ben', 'Thor', 'Zoe', 'Kate']
	Found = False
	PlayerName = str(raw_input("What Player are you looking for? "))
	for name in names_list :
		if name == PlayerName :
			Found = True
	if Found == True :
		print ("Yes, they have a top score.")
	else :
		print ("No, they do not have a top score.")


def Names() :
	names_list = ['Ben', 'Thor', 'Zoe', 'Kate']
	PlayerName = raw_input("What Player are you looking for? ")
	if PlayerName in names_list :
		print "Yes, they have a top score."
	else :
		print "No, they do not have a top score."


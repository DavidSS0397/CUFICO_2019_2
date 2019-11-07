
Fi=0
Ff=1



i=1
while i < 50:
	
	Fn=Ff+Fi

	Fi=Ff
	Ff=Fn


	if Fn % 2 == 0:
		
		print (Fn)
		i+=1
	Fn=0



	

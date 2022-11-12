while True:

	import os 
	from time import sleep


	n =5
	for i in range (1,n):
		print (' '*((n-i)*2)+'* '*i)
		
		
		
	print ('* '*(n*3-1))

	for i in range (n-1,0,-1):
		print (' '*((n-i)*2)+'* '*i)
		
		
		
		
	sleep (0.5)
	clear = lambda: os.system ('cls')
	clear ()	
		
		
		
		
	for i in range (1,n):
		print (' '*((n+4)*2) +'* '*i)
		
	print ('* '*(n*3-1))

	for i in range (n-1,0,-1):
		print (' '*((n+4)*2) +'* '*i)
		
		
		
		
	sleep (0.5)
	clear = lambda: os.system ('cls')
	clear ()	
		


	print ('          *')

	
		
	for i in range (1,n):
		print (' '*(n-i)*2 +'* '*(1+(i*2)))        #عندي سؤال هنتا المفروض ان اخر كونتر هنا هيبقا ب خمسة ف المفروض ع المعادلة كدا يطبعلى 11 نجمة فلية بقا طابعلي تسعة بس ؟!
		
		
	m= 8	
	for i in range (1,m):
		print ('          '+'*')
		
		
		
	sleep (0.5)
	clear = lambda: os.system ('cls')
	clear ()	
		
		
	m= 8	
	for i in range (1,m):
		print ('          '+'*')
		
		
	for i in range (n-1, 0, -1):
		print (' '*(n-i)*2 +'* '*(1+(i*2)))
		

	print ('          *')
	
	
	sleep (0.5)
	clear = lambda: os.system ('cls')
	clear ()
import sys
def tablin(table, i, n, h, ia):
    if(table(1,1)-table(1, n)<0):
        for(l=1, l!=n, l++):
            if(h-table(1, l)<0):
			    if(l-1<0 or l-1>0):
				    s = (table(2, l)-table(2, l-1)/(table(1,l)-table(1,l-1)))
					tablinArray = table(2, n) + (h-table(1,n))*s
					return tablinArray
				elif (l-1==0):
				    if(ia==1):
					    s=(table(2, n) – table(2, 1) ) / (table(1, n) – table(1, 1) )
						tablinArray = table(2, n) + (h-table(1,n))*s
					    return tablinArray
					elif (ia ==2):
					    if(h-table(1,1)<0 or h-table(1,1)==0):
						    s=(table(2, n) – table(2, 1) ) / (table(1, n) – table(1, 1) )
						    tablinArray = table(2, n) + (h-table(1,n))*s
					        return tablinArray
						elif(h-table(1,1)>0):
							n1=n – 1
							s=(table(2, n) – table(2, n1) ) / (table(1, n) – table(1, n1) )
							tablinArray=table(2, n) + (h – table(1, n) ) * s
							return tablinArray
			elif(h-table(1, l)==0):
			    tablinArray = table(2,l)
				return tablinArray
			elif(h-table(1, l)>0):
				if(ia==1):
					s=(table(2, n) – table(2, 1) ) / (table(1, n) – table(1, 1) )
					tablinArray = table(2, n) + (h-table(1,n))*s
					return tablinArray
				elif (ia ==2):
					if(h-table(1,1)<0 or h-table(1,1)==0):
						s=(table(2, n) – table(2, 1) ) / (table(1, n) – table(1, 1) )
						tablinArray = table(2, n) + (h-table(1,n))*s
						return tablinArray
					elif(h-table(1,1)>0):
						n1=n – 1
						s=(table(2, n) – table(2, n1) ) / (table(1, n) – table(1, n1) )
						tablinArray=table(2, n) + (h – table(1, n) ) * s
						return tablinArray
		if(ia==1):
			s=(table(2, n) – table(2, 1) ) / (table(1, n) – table(1, 1) )
			tablinArray = table(2, n) + (h-table(1,n))*s
			return tablinArray
		elif (ia ==2):
			if(h-table(1,1)<0 or h-table(1,1)==0):
				s=(table(2, n) – table(2, 1) ) / (table(1, n) – table(1, 1) )
				tablinArray = table(2, n) + (h-table(1,n))*s
				return tablinArray
			elif(h-table(1,1)>0):
				n1=n – 1
				s=(table(2, n) – table(2, n1) ) / (table(1, n) – table(1, n1) )
				tablinArray=table(2, n) + (h – table(1, n) ) * s
				return tablinArray
	elif(table(1,1)-table(1, n)==0):
	    print("23H Range of Table is Zero")
		return
	elif(table(1,1)-table(1, n)>0):
	    for(l=1, l!=n, l++):
            if(h-table(1, l)<0):
			    if(l-1<0 or l-1>0):
				    s = (table(2, l)-table(2, l-1)/(table(1,l)-table(1,l-1)))
					tablinArray = table(2, n) + (h-table(1,n))*s
					return tablinArray
				elif (l-1==0):
				    if(ia==1):
					    s=(table(2, n) – table(2, 1) ) / (table(1, n) – table(1, 1) )
						tablinArray = table(2, n) + (h-table(1,n))*s
					    return tablinArray
					elif (ia ==2):
					    if(h-table(1,1)<0 or h-table(1,1)==0):
						    s=(table(2, n) – table(2, 1) ) / (table(1, n) – table(1, 1) )
						    tablinArray = table(2, n) + (h-table(1,n))*s
					        return tablinArray
						elif(h-table(1,1)>0):
							n1=n – 1
							s=(table(2, n) – table(2, n1) ) / (table(1, n) – table(1, n1) )
							tablinArray=table(2, n) + (h – table(1, n) ) * s
							return tablinArray
			elif(h-table(1, l)==0):
                tablinArray = table(2,l)
				return tablinArray
            elif(h-table(1, l)>0):
				if(ia==1):
					s=(table(2, n) – table(2, 1) ) / (table(1, n) – table(1, 1) )
					tablinArray = table(2, n) + (h-table(1,n))*s
					return tablinArray
				elif (ia ==2):
					if(h-table(1,1)<0 or h-table(1,1)==0):
						s=(table(2, n) – table(2, 1) ) / (table(1, n) – table(1, 1) )
						tablinArray = table(2, n) + (h-table(1,n))*s
						return tablinArray
					elif(h-table(1,1)>0):
						n1=n – 1
						s=(table(2, n) – table(2, n1) ) / (table(1, n) – table(1, n1) )
						tablinArray=table(2, n) + (h – table(1, n) ) * s
						return tablinArray

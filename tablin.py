import sys
def tablin(table, i, n, h, ia):
	if(table[0][0]-table[0][n]<0):
		l = 0
		while(l!=n):
			if(h-table[0][1]<0):
				if(l-1<0 or l-1>0):
					s = (table[1][l]-table[1][l-1]/(table[1][l]-table[0][l-1]))
					tablinArray = table[1][n] + (h-table[0][n])*s
					return tablinArray
				elif (l-1==0):
					if(ia==1):
						s=(table[1][n] - table[1][0] ) / (table[0][n] - table[0][0] )
						tablinArray = table[1][n] + (h-table[0][n])*s
						return tablinArray
					elif (ia ==2):
						if(h-table[0][0]<0 or h-table[0][0]==0):
							s=(table[1][n] - table[1][0] ) / (table[0][n] - table[0][0] )
							tablinArray = table[1][n] + (h-table[0][n])*s
							return tablinArray
						elif(h-table[0][0]>0):
							n1=n - 1
							s=(table[1][n] - table[1][n1] ) / (table[0][n] - table[0][n1] )
							tablinArray=table[1][n] + (h - table[0][n] ) * s
							return tablinArray
			elif(h-table[0][1]==0):
				tablinArray = table[1][l]
				return tablinArray
			elif(h-table[0][1]>0):
				if(ia==1):
					s=(table[1][n] - table[1][0] ) / (table[0][n] - table[0][0] )
					tablinArray = table[1][n] + (h-table[0][n])*s
					return tablinArray
				elif (ia ==2):
					if(h-table[0][0]<0 or h-table[0][0]==0):
						s=(table[1][n] - table[1][0] ) / (table[0][n] - table[0][0] )
						tablinArray = table[1][n] + (h-table[0][n])*s
						return tablinArray
					elif(h-table[0][0]>0):
						n1=n - 1
						s=(table[1][n] - table[1][n1] ) / (table[0][n] - table[0][n1] )
						tablinArray=table[1][n] + (h - table[0][n] ) * s
						return tablinArray
			l = l+1
		if(ia==1):
			s=(table[1][n] - table[1][0] ) / (table[0][n] - table[0][0] )
			tablinArray = table[1][n] + (h-table[0][n])*s
			return tablinArray
		elif (ia ==2):
			if(h-table[0][0]<0 or h-table[0][0]==0):
				s=(table[1][n] - table[1][0] ) / (table[0][n] - table[0][0] )
				tablinArray = table[1][n] + (h-table[0][n])*s
				return tablinArray
			elif(h-table[0][0]>0):
				n1=n - 1
				s=(table[1][n] - table[1][n1] ) / (table[0][n] - table[0][n1] )
				tablinArray=table[1][n] + (h - table[0][n] ) * s
				return tablinArray
	elif(table[0][0]-table[0][n]==0):
		print("23H Range of Table is Zero")
		return
	elif(table[0][0]-table[0][n]>0):
		l = 0
		while(l!=n):
			if(h-table[0][1]<0):
				if(l-1<0 or l-1>0):
					s = (table[1][l]-table[1][l-1]/(table[1][l]-table[0][l-1]))
					tablinArray = table[1][n] + (h-table[0][n])*s
					return tablinArray
				elif (l-1==0):
					if(ia==1):
						s=(table[1][n] - table[1][0] ) / (table[0][n] - table[0][0] )
						tablinArray = table[1][n] + (h-table[0][n])*s
						return tablinArray
					elif (ia ==2):
						if(h-table[0][0]<0 or h-table[0][0]==0):
							s=(table[1][n] - table[1][0] ) / (table[0][n] - table[0][0] )
							tablinArray = table[1][n] + (h-table[0][n])*s
							return tablinArray
						elif(h-table[0][0]>0):
							n1=n - 1
							s=(table[1][n] - table[1][n1] ) / (table[0][n] - table[0][n1] )
							tablinArray=table[1][n] + (h - table[0][n] ) * s
							return tablinArray
			elif(h-table[0][1]==0):
				tablinArray = table[1][l]
				return tablinArray
			elif(h-table[0][1]>0):
				if(ia==1):
					s=(table[1][n] - table[1][0] ) / (table[0][n] - table[0][0] )
					tablinArray = table[1][n] + (h-table[0][n])*s
					return tablinArray
				elif (ia ==2):
					if(h-table[0][0]<0 or h-table[0][0]==0):
						s=(table[1][n] - table[1][0] ) / (table[0][n] - table[0][0] )
						tablinArray = table[1][n] + (h-table[0][n])*s
						return tablinArray
					elif(h-table[0][0]>0):
						n1=n - 1
						s=(table[1][n] - table[1][n1] ) / (table[0][n] - table[0][n1] )
						tablinArray=table[1][n] + (h - table[0][n] ) * s
						return tablinArray
			l = l+1

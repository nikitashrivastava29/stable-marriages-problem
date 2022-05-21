n= int(input("Enter number of men or women:"))
rank=[] #creates a list for inserting preferences
#The first elements till n+1 are men's preferences (including lists) and n+1 to 2n are women's preferences.

#=============================================================
for i in range(1,n+1):
  print("for man", i)
  p= (input("Enter the choice:")) #asks for each man's preferences
  m= p.split(",")
  for k in range(len(m)):
      m[k]= int(m[k])      
  rank+=[m]

for k in range(n+1, 2*n+1):
  print("For Woman", k)
  p= (input("Enter choice:")) #asks for each woman's preferences
  w=  p.split(",")
  for k in range(len(w)):
      w[k]= int(w[k])
  rank+=[w]
print(rank)

#===========================================================
#The following function checks if the woman prefers the mjth man over the man she is engaged with which is k.
def prefcheck(prefer, w, k, mj):
    for i in range(n): #checks her preferences (comprising n elements)
        if prefer[w][i]==k: #finds rank of k man
            x=i
        if prefer[w][i]==mj: #finds rank of mj man
            y=i
    if x>y: #if rank of kth man is > than rank of mj man, she prefers mj man so True
        return True
    else:
        return False
#============================================================
def Pair(prefer):
    womanPairing=[] #list wherein each element shows the man she has been paired to & index of each element refers to the 'index' of the woman being considered in the order of the input preference matrix
    menStatus=[] #each element shows the relationship status of the man (free/engaged), the index of each element refers to the order of the man in the input preference matrix.
    for i in range(n):
        womanPairing+=[False]
        menStatus+=[False]
    #Need a counter that counts the number of unpaired people. Here, no of unpaired men will always equal the number of unpaired women which is = n.
    NoOfUnpaired = n
    #initialized as n, which is the total number of men(=n) and women (=n)
    #So, when NoOfUnpaired = 0, there would be no pairing left to do and the program will terminate. n pairs would have been made.
    while (NoOfUnpaired > 0):
        for k in range(n): #for kth man
            for j in range(n):#for jth pref of kth man
                if menStatus[k] == False: #if man is unengaged
                    w = prefer[k][j] #insert his most prefered woman in the variable v
                    if womanPairing[w-n]== False:  #if woman is unpaired
                        womanPairing[w-n] = k #pair them together
                        menStatus[k]=True #change man's status to married
                        NoOfUnpaired-=1 #reduce the counter by 1 as a match has been made
                    else: #when woman is paired with someone
                        mj = womanPairing[w-n] #insert the the man she is paired with in variable mj
                        if (prefcheck(prefer,w,k,mj) == False): #if she does not prefer her current man to new one i.e she prefers the new one
                          womanPairing[w-n] = k #pair the new one with her
                          menStatus[k]=True #change kth man(new one's) status to paired
                          menStatus[mj]=False #change the old man's status to unpaired
                          #if she does not prefer to new one, so will go back to w = prefer[k][i] and so the woman will change
    print("The final pairings are:")
    print("Woman ", " Man")
    for i in range(n):
        print(i + n, "\t", womanPairing[i])

Pair(rank)

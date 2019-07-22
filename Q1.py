#get 5 numbers as string and calculate sum of tem as integer
mystr=(input('please enter 5 numbers with , for sepration:'))
list=mystr.split(',')
newlist=[int(list[0]),int(list[1]),int(list[2]),int(list[3]),int(list[4])]
print(sum(newlist))
#---------------------------

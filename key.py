dict = {'I' : 3, 'Like' : 2, 'To' : 2, 'Draw' : 1}

print("The original dictionary : " + str(dict))

x=2
res=0
for key in dict:
    if dict[key]==x:
        res = res+1

print("Frequency of K is: " + str(res))

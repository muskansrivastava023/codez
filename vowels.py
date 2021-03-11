a=input("Enter your sentence---")
vowels=['a','e','i','o','u','A','E','I','O','U']
vfound=[]

for v in a:
    if v in vowels:
        vfound.append(v.upper())

a_count=vfound.count('A')
e_count=vfound.count('E')
i_count=vfound.count('I')
o_count=vfound.count('O')
u_count=vfound.count('U')

d={'A':a_count,'E':e_count,'I':i_count,'O':o_count,'U':u_count}
set=[]
for x,y in d.items():
    if y!=0:
       set.append(x)
print("vowels in sentence---",sorted(set))

c=[]
counter=[a_count,e_count,i_count,o_count,u_count]
for i in counter:
    if i!=0:
        c.append(i)

print("each vowel repeated as---",c)




#list,tuple,dictionary
person_l = ['john','doe', 30,45.43,'mombasa',True]
print(person_l[0:5])

print(person_l.index(30))
print(len(person_l))
person_l
person_l.pop()






person_t =  ('john','doe', 30,45.43,'mombasa',True)
print(person_t[0:5])
#dictionary - structures holds aiable in key:valuenpairs
person_d = {'firstName':'john','surName': 'doe','weight' :65.54 , 'location' : 'mombasa','activeUesr': True}
print(person_d['surName'])
print(person_d['surName'] ,person_d['location'])
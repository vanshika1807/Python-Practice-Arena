f = open('../Data/write_req.txt','w')
txt = f.write('This text will be written in a newly created file')
print(txt)
f.close()
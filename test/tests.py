from clean_diskv0_1 import *

f1 = File("C:\\nauka_python\\disk_cleaner\\test1\\doc_1.txt")
f2 = File("C:\\nauka_python\\disk_cleaner\\test1\\doc_2.txt")
f3 = File("C:\\nauka_python\\disk_cleaner\\test1\\doc_3.txt")
f4 = File("C:\\nauka_python\\disk_cleaner\\test1\\doc_1.txt")

print(id(f1))
print(id(f2))
print(id(f3))
print(id(f4))
print(f1)
print(f2)
print(f3)
print(f4)
print(File._instances)
	
print(dir(f1))
print(id(f1))
print(id(f4))

print(f1)
print(f2)
print (f1 > f2)
print (f1 < f2)
print (f1 == f2)
print (f2 == f1)
print (f1 > f3)
print (f1 < f3)
print (f1 == f3)
print (f1 >= f3)
print (f1 <= f3)
print (f2 >= f1)
print (f2 <= f1)
print (f1.newerCr(f2))
print (f1.olderCr(f2))
print (f2.equalMod(f3))
print (f2.equalCr(f3))
print(f1)
print(f2)
print(f3)

print(f3.equalAll(f1))
print(f3.equalAll(f2,cr_flg=0))
print(f3.equalAll(f2))
print(f3.equalAll(f2,mod_flg=0))

f4 = File("C:\\nauka_python\\disk_cleaner\\test1\\abcd_new.txt")
print(f4)
print(f4.setName("abcd.txt"))
print(f4)
print(f4.filepath)
f4.setName("abcd.txt")
print(f4)
print(f4.filepath)



########################################################################

		
			
d1 = Dir("C:\\nauka_python\\disk_cleaner\\test1")
print(d1)
print(d1.files)
print(d1.subdirs)

for f in d1.files:
    print(f)
for d in d1.subdirs:
    print(d)
tmp = os.walk("C:\\nauka_python\\disk_cleaner\\test1")

for dir,subdirs,files in tmp:
    print("DIRECTORY %s" % dir)
    d = Dir(dir)
    print(d)
    print("FILES:")
    for ff in d.files:
        print(ff)
    print("SUBDIRS:")
    for dd in d.subdirs:
        print(dd)


print(d1.getSize())

# print(d1.setName("test1"))
print(d1.getName())

print(d1.getCreationDate())
print(d1.getModificationDate())

print([f.name for f in d1.files])
print([f.name for f in d1.subdirs])
print([f.size for f in d1.subdirs])
print([f.nFiles for f in d1.subdirs])

d2 = Dir("C:\\nauka_python\\disk_cleaner\\test1\\sub1 - kopia")

d3 = Dir("C:\\nauka_python\\disk_cleaner\\test1\\sub1 - kopia2")

print(d2)
print(d3)

# print(d2 > d3)
# print(d2 == d3)
# print(d2 <= d3)

print(d2.newerCr(d3))
print(d2.equalCr(d3))
print(d2.newerMod(d3))
print(d2.olderMod(d3))

print(d2.gtNOFiles(d3))


print(f1)
print(f2)
print(f3)
print(f2.equalAll(f3))
print(f2.equalAll(f1))
print(f2.equalAll(f1,size_flg=0))
print(f2.equalAll(f1,size_flg=0,name_flg=0))

print(d2)
print(d3)
print(d2.equalAll(d3,name_flg=0,cr_flg=0,mod_flg=0))
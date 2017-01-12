import os.path as pth
import os
import pprint
import itertools
import time
from datetime import datetime

class File(object):
	_instances = {}
	
	def __new__(self,filepath):
		if filepath not in self._instances.keys():
			self._instances[filepath] = super(File,self).__new__(self)
		return self._instances[filepath]
			
	def __init__(self,filepath):
		try:
			if not(pth.isfile(filepath)): raise NameError("FILE NOT EXISTS")
			self.filepath = filepath
			self.dir = pth.split(self.filepath)[0]
			self.name = pth.split(self.filepath)[1]
			self.stats =  os.stat(self.filepath)
			self.size = self.stats.st_size
			self.creation_dttm = int(self.stats.st_ctime)
			self.modification_dttm = int(self.stats.st_mtime)
			self.attrs = [self.filepath,self.name,self.size,datetime.fromtimestamp(self.creation_dttm),datetime.fromtimestamp(self.modification_dttm)]
		except NameError as x:
			print(x)
			
			
	def getSize(self):
		return self.size
	
	def getModificationDate(self):
		return self.modification_dttm
		
	def getCreationDate(self):
		return self.creation_dttm
		
	def __gt__(self,filepath2): # GREATER
		return self.size > filepath2.size
		
	def __eq__(self,filepath2):
		return self.size == filepath2.size
	
	def __lt__(self,filepath2): # LESS
		return self.size < filepath2.size
		
	def __ge__(self,filepath2):
		return self.size >= filepath2.size
		
	def __le__(self,filepath2):
		return self.size <= filepath2.size
	
	def newerCr(self,filepath2):
		return self.creation_dttm > filepath2.creation_dttm
		
	def olderCr(self,filepath2):
		return self.creation_dttm < filepath2.creation_dttm
		
	def equalCr(self,filepath2):
		return self.creation_dttm == filepath2.creation_dttm
	
	def newerMod(self,filepath2):
		return self.modification_dttm > filepath2.modification_dttm
		
	def olderMod(self,filepath2):
		return self.modification_dttm < filepath2.modification_dttm
		
	def equalMod(self,filepath2):
		return self.modification_dttm == filepath2.modification_dttm
		
	def equalAll(self,filepath2,size_flg=1,cr_flg=1,mod_flg=1,name_flg=1):
		eq = lambda x,y: 1 if not(x) else y
		return all([eq(size_flg,self.__eq__(filepath2)),eq(mod_flg,self.equalMod(filepath2)),eq(cr_flg,self.equalCr(filepath2))])### FIX
		
	def setName(self,newname):
		newpath = pth.join(self.dir,newname)
		os.rename(self.filepath,newpath)
		self.__init__(newpath)
		return self.filepath
	
	def getName(self):
		return self.name
		
	def move(self,tto):
		
		self.filepath = tto
		return "Moving %s ==> %s" % (self.name,newname)
		
	def __str__(self):
		return """
		File: {1}
		Directory: {0}
		size(bytes): {2}
		creation date: {3}
		modification date: {4}
		""".format(*self.attrs)
		

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
# print(len(File.indexes.items()))

# for k,v in File.indexes.items():
	# print(k,v)
	
# print(dir(f1))
# print(id(f1))
# print(id(f4))

# print(f1)
# print(f2)
# print (f1 > f2)
# print (f1 < f2)
# print (f1 == f2)
# print (f2 == f1)
# print (f1 > f3)
# print (f1 < f3)
# print (f1 == f3)
# print (f1 >= f3)
# print (f1 <= f3)
# print (f2 >= f1)
# print (f2 <= f1)
# print (f1.newerCr(f2))
# print (f1.olderCr(f2))
# print (f2.equalMod(f3))
# print (f2.equalCr(f3))
# print(f1)
# print(f2)
# print(f3)

# print(f3.equalAll(f1))
# print(f3.equalAll(f2,cr_flg=0))
# print(f3.equalAll(f2))
# print(f3.equalAll(f2,mod_flg=0))

# f4 = File("C:\\nauka_python\\disk_cleaner\\test1\\abcd_new.txt")
# print(f4)
# print(f4.setName("abcd.txt"))
# print(f4)
# print(f4.filepath)
# f4.setName("abcd.txt")
# print(f4)
# print(f4.filepath)


class Dir(File):
	
	def __init__(self,dirpath):
		try:
			if not(pth.isdir(dirpath)): raise NameError("DIRECTORY NOT EXISTS")
			self.dirpath = dirpath
			self.parent = pth.split(self.dirpath)[0]
			self.name = pth.split(self.dirpath)[1]
			self.stats =  os.stat(self.dirpath)
			self.creation_dttm = int(self.stats.st_ctime)
			self.modification_dttm = int(self.stats.st_mtime)
			self.files=[]
			self.subdirs=[]
			self.size = 0
			self.nFiles = 0
			self.nSubs = 0
			for item in os.listdir(self.dirpath):
				if pth.isfile(pth.join(self.dirpath,item)):
					f = File(pth.join(self.dirpath,item))
					self.files.append(f)
					self.size+=f.size
					self.nFiles+=1
				elif pth.isdir(pth.join(self.dirpath,item)):
					d = Dir(pth.join(self.dirpath,item))
					self.subdirs.append(d)
					self.size+=d.size
					self.nSubs+=1
					self.nFiles+=d.nFiles
			self.attrs = [self.dirpath,self.name,self.parent,self.size,datetime.fromtimestamp(self.creation_dttm),datetime.fromtimestamp(self.modification_dttm),self.nFiles,self.nSubs]
		except NameError as x:
			print(x)
			
	
	def __str__(self):
		return """
		Directory: {0}
		Name: {1}
		ParentDirectory: {2}
		size(bytes): {3}
		creation date: {4}
		modification date: {5}
		Number of files: {6}
		Number of subdirs: {7}
		""".format(*self.attrs)
		
		
			
# d1 = Dir("C:\\nauka_python\\disk_cleaner\\test1")
# print(d1)
# # print(d1.files)
# # print(d1.subdirs)

# # for f in d1.files:
	# # print(f)
# # for d in d1.subdirs:
	# # print(d)
# tmp = os.walk("C:\\nauka_python\\disk_cleaner\\test1")

# for dir,subdirs,files in tmp:
	# print("DIRECTORY %s" % dir)
	# d = Dir(dir)
	# print(d)
	# print("FILES:")
	# for ff in d.files:
		# print(ff)
	# print("SUBDIRS:")
	# for dd in d.subdirs:
		# print(dd)

# # print(os.listdir("C:\\nauka_python\\disk_cleaner\\test1"))

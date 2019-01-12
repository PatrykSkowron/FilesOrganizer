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
			self.creation_ts = int(self.stats.st_ctime)
			self.modification_ts = int(self.stats.st_mtime)
			self.attrs = [self.filepath,self.name,self.size,datetime.fromtimestamp(self.creation_ts),datetime.fromtimestamp(self.modification_ts)]
		except NameError as x:
			self.filepath,self.dir,self.name,self.stats,self.size,self.creation_ts,self.modification_ts,self.attrs = [None]*8
			print(x)
			
			
	def getSize(self):
		return self.size
	
	def getModificationDate(self):
		return self.modification_ts
		
	def getCreationDate(self):
		return self.creation_ts
		
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
		return self.creation_ts > filepath2.creation_ts
		
	def olderCr(self,filepath2):
		return self.creation_ts < filepath2.creation_ts
		
	def equalCr(self,filepath2):
		return self.creation_ts == filepath2.creation_ts
	
	def newerMod(self,filepath2):
		return self.modification_ts > filepath2.modification_ts
		
	def olderMod(self,filepath2):
		return self.modification_ts < filepath2.modification_ts
		
	def equalMod(self,filepath2):
		return self.modification_ts == filepath2.modification_ts
		
	def equalAll(self,filepath2,size_flg=1,cr_flg=1,mod_flg=1,name_flg=1):
		eq = lambda x,y: True if not(x) else y
		return all([eq(size_flg,self.__eq__(filepath2)),eq(mod_flg,self.equalMod(filepath2)),eq(cr_flg,self.equalCr(filepath2)),eq(name_flg,self.name==filepath2.name)])### FIX
		
	def setName(self,newname):
		try:
			newpath = pth.join(self.dir,newname)
			os.rename(self.filepath,newpath)
			self.__init__(newpath)
			return self.filepath
		except (AttributeError,TypeError) as x:
			return(x)
	
	def getName(self):
		return self.name
		
	def move(self,tto):
		
		self.filepath = tto
		return "Moving %s ==> %s" % (self.name,newname)
		
	def __str__(self):
		try:
			return """
			File: {1}
			Directory: {0}
			size(bytes): {2}
			creation date: {3}
			modification date: {4}
			""".format(*self.attrs)
		except TypeError as x:
			return "File doesn't exist!"
		
class Dir(File):
	
	def __init__(self,dirpath):
		try:
			if not(pth.isdir(dirpath)): raise NameError("DIRECTORY NOT EXISTS")
			self.dirpath = dirpath
			self.parent = pth.split(self.dirpath)[0]
			self.name = pth.split(self.dirpath)[1]
			self.stats =  os.stat(self.dirpath)
			self.creation_ts = int(self.stats.st_ctime)
			self.modification_ts = int(self.stats.st_mtime)
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
					if f.modification_ts > self.modification_ts: self.modification_ts = f.modification_ts
				elif pth.isdir(pth.join(self.dirpath,item)):
					d = Dir(pth.join(self.dirpath,item))
					self.subdirs.append(d)
					self.size+=d.size
					self.nSubs+=1
					self.nFiles+=d.nFiles
					if d.modification_ts > self.modification_ts: self.modification_ts = d.modification_ts
			self.attrs = [self.dirpath,self.name,self.parent,self.size,datetime.fromtimestamp(self.creation_ts),datetime.fromtimestamp(self.modification_ts),self.nFiles,self.nSubs]
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
		
	def getModificationDate(self):
		return datetime.fromtimestamp(self.stats.st_mtime)
	
	def getCreationDate(self):
		return datetime.fromtimestamp(self.stats.st_ctime)

	def setName(self,newname):
		try:
			newpath = pth.join(self.parent,newname)
			os.rename(self.dirpath,newpath)
			self.__init__(newpath)
			return self.dirpath
		except (AttributeError,TypeError) as x:
			return(x)
	
	def gtNOFiles(self,dirpath2):
		return self.nFiles > dirpath2.nFiles
		
	def eqNOFiles(self,dirpath2):
		return self.nFiles == dirpath2.nFiles
	
	def ltNOFiles(self,dirpath2):
		return self.nFiles < dirpath2.nFiles
		
	def geNOFiles(self,dirpath2):
		return self.nFiles >= dirpath2.nFiles
	
	def leNOFiles(self,dirpath2):
		return self.nFiles <= dirpath2.nFiles

	def equalAll(self,filepath2,size_flg=1,cr_flg=1,mod_flg=1,name_flg=1,noFiles_flg=1,noSubd_flg=1):
		eq = lambda x,y: True if not(x) else y
		return all([eq(size_flg,self.__eq__(filepath2)),eq(mod_flg,self.equalMod(filepath2)),eq(cr_flg,self.equalCr(filepath2)),eq(name_flg,self.name==filepath2.name),eq(noFiles_flg,self.eqNOFiles(filepath2)),eq(noSubd_flg,self.nSubs==filepath2.nSubs)])
		
	# name size cr_td md_ts NoF noSubd
	
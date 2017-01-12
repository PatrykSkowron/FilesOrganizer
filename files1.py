import os
import pprint
import itertools

def compare2_files(name,path1,path2):
	file1=os.path.join(path1,name)
	file2=os.path.join(path2,name)
	
	size1=os.path.getsize(file1)
	size2=os.path.getsize(file2)
	if size1==size2: bigger=''
	elif size1>size2: bigger=file1
	else: bigger=file2
	return([bigger])

	# return 1 if identical
	# if not: return [newer,bigger,name]
def compare_files(name,paths):
	pass
	# return 1 if identical
	# if not: return [newer,bigger,name]

def compare2_folders(path1,path2):
	pass


	pass
	

def get_foldersize(path):
	size=0
	cnt=0
	for folderName, subfolders, filenames in os.walk(path):
		for file in filenames:
			filepath=os.path.join(folderName,file)
			size+=os.path.getsize(filepath)
		cnt+=len(filenames)
			
	return((size,cnt))
	
def walk_folders(path):
	folders={}
	for folderName, subfolders, filenames in os.walk(path):
		folder=folderName.split("\\")[-1]
		folders.setdefault(folder,{"path":[],"files":[],"size":[]})
		folders[folder]["path"].append("\\".join(folderName.split("\\")[:-1]))
		folders[folder]["files"].append(filenames)
		folders[folder]["size"].append(get_foldersize(folderName))
	return folders

path="C:\\Algolytics paczka\\AM_projekty\\common_tklib\\scripts\\library"
folders=walk_folders(path)
	
pprint.pprint(folders)


# print(set([len(f) for f in tmp["files"]]))
# print(set(list(itertools.chain(*tmp["files"]))))
# print(set(tmp["size"]))

# for folder,dict in folders.items():
	
	# if len(dict["path"])>1:
		# suffix=os.path.commonprefix([f[::-1] for f in dict["path"]])[::-1]
		# prefix=os.path.commonprefix([f for f in dict["path"]])
		# print(set([len(f) for f in dict["files"]]))
		# print(set(dict["size"]))
			
		# print(""" 
# Folder:\t%s
# number of different paths: %d
	# %s
# common prefix:\t%s
# common suffix:\t%s
# """ % (folder,len(dict["path"]),"\n\t".join(dict["path"]),prefix,suffix))
					
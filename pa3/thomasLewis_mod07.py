#! python3

# import OS for file traversial and time for timestamps
import os
import time

# Setup paths
cwd = '/home/tholewi/CS4323/pa3/testdir'
# cwd = 'C:\\Users\\thoma\\PycharmProjects\\CS4323\\pa3\\testdir'

# Change dir to the cwd
os.chdir(cwd)


# Search for a file containg <filename> within a specified folder, includes partial matches
def search(sub, filename):
	files = []
	for folder, subs, file in os.walk(sub):
		for i in file:
			if filename in i:
				files.append((folder + '/' + i))

	return files


# Print out all files within all subdirectories within specified folder
def search_folder(fol):
	files = []
	for folder, subs, file in os.walk(fol):
		for i in file:
			files.append((folder + '/' + i))

	return files


# Find a specified folder within CWD. Will return first partial match
def find_folder(fol):
	for folder, subs, file in os.walk(cwd):
		if fol in folder:
			return folder


# Find a specific file (no partial matches)
def rem_file(fol, filename):
	for folder, subs, file in os.walk(fol):
		for i in file:
			if filename == i:
				os.remove(folder + '/' + i)
				print 'Removed file: ', folder, '/', i


# Print how many minute ago a file was modified based on -mmin args
def get_m_time(fol, m):
	files = []

	if '-' in m:
		mmin = int(m.replace('-', ''))
		toggle = '-'
	elif '+' in m:
		mmin = int(m.replace('+', ''))
		toggle = '+'
	else:
		mmin = int(m)
		toggle = ''

	for folder, subs, file in os.walk(fol):
		for i in file:
			mtime = int((time.time() - os.path.getmtime(folder + '/' + i)) / 60)
			if toggle == '+' and mtime > mmin:
				files.append([folder + '/' + i, '- ', mtime])
			elif toggle == '-' and mtime < mmin:
				files.append([folder + '/' + i, '- ', mtime])
			elif toggle == '' and mtime == mmin:
				files.append([folder + '/' + i, '- ', mtime])

	return files


# Find a file by inode number
def find_inode(fol, num):
	files = []
	num = int(num)
	for folder, subs, file in os.walk(fol):
		for i in file:
			inode = os.stat(folder + '/' + i)[1]
			if num == inode:
				files.append([folder + '/' + i, '- ', inode])

	return  files


def run():
	while (True):
		command = raw_input('$ ').split()

                if command[0] == 'find':
			if len(command) == 2 and 'find' == command[0]:
				search_folder(find_folder(command[1]))
			elif len(command) == 4:
				if '-name' == command[2]:
					print search(find_folder(command[1]), command[3])
				elif '-mmin' == command[2]:
					print get_m_time(find_folder(command[1]), command[3])
				elif '-inum' == command[2]:
					print find_inode(find_folder(command[1]), command[3])
			elif len(command) == 5 and command[4] == '-delete':
				if '-name' == command[2]:
                                        for i in search(find_folder(command[1]), command[3]):
						os.remove(i)
						print 'Removed file: ', i
				elif '-mmin' == command[2]:
					for i in get_m_time(find_folder(command[1]), command[3]):
						os.remove(i)
						print 'Removed file: ', i
				elif '-inum' == command[2]:
					for i in find_inode(find_folder(command[1]), command[3]):
						os.remove(i)
						print 'Removed file: ', i
		elif 'exit' in command:
			exit()


# Call my run function.
run()

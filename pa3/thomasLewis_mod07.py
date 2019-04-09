#! python3

#import OS for file traversial and time for timestamps
import os
import time

# Setup paths
cwd = '/home/tholewi/CS4323/pa3/testdir'

# Change dir to the cwd
os.chdir(cwd)


# Search for a file containg <filename> within a specified folder, includes partial matches
def search(sub, filename):
    for folder, subs, file in os.walk(sub):
	for i in file:
            if filename in i:
                print(folder + '/' + i)


# Print out all files within all subdirectories within specified folder
def search_folder(fol):
    for folder, subs, file in os.walk(fol):
        for i in file:
            print(folder + '/' + i)


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
                print folder, '/', i, ' - ', mtime
            elif toggle == '-' and mtime < mmin:
                print folder, ',', i, ' - ', mtime
            elif toggle == '' and mtime == mmin:
                print folder, ',', i, ' - ', mtime


def run():
    while(True):
        command = raw_input('$ ').split()
        
        if len(command) == 2 and 'find' == command[0]:
            search_folder(find_folder(command[1]))
        elif len(command) == 4 and 'find' == command[0]:
            if '-name' == command[2]:
                search(find_folder(command[1]), command[3])
            elif '-mmin' == command[2]:
                get_m_time(find_folder(command[1]), command[3])
            elif '-delete' == command[2]:
                rem_file(find_folder(command[1]), command[3])
        elif 'exit' in command:
            exit()


# Call my run function.
run()


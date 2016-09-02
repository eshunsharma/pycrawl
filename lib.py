import os

# for creating a new directory if does not exist

def create_dir(directory):
	if not os.path.exists(directory):
		print("create new directory")
		os.makedirs(directory)

# for making project files, crawled and queue

def create_files(project_name, base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'
	if not os.path.isfile(queue):
		print("creating queue file")
		write_file(queue, base_url)

	if not os.path.isfile(crawled):
		print("creating crawled file")
		write_file(crawled, "")

# create new file

def write_file(file, content):
	f = open(file, 'w')
	f.write(content)
	f.close()

# add data to an existing file

def append_file(file, content):
	with open(file, 'a') as file:
		file.write(content + '\n')

# delete file contents

def delete_from_file(file):
	with open(file, 'w'):
		pass

# links to set, so as they are unique

def file_to_set(filename):
	results = set()
	with open(filename, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results

# froma set, to links in file

def set_to_file(links, file):
	delete_from_file(file)
	for link in sorted(links):
		append_file(file, link)
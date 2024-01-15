myfile = open('README.md', 'w')
myfile.write('# This is a sample text I have written in this sample file.\n')
#myfile.close()

lines = ["This is line 2\n", "This is line 3\n", "This is line 4\n,", "This is line 5\n"]

#myfile = open('README.md', 'a')

myfile.writelines(lines)
myfile.close()

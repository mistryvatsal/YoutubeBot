import os
import time


# Create the directory folder History to save the log files
def create_dir():
    if not os.path.exists('History'):
        print('Creating the directory History')
        os.makedirs('History')


# Write the query log of the user into the txt file in append mode
def write_to_file(user_name, log):
    name = 'History/' + str(user_name)
    file_name = name + '.txt'
    f = open(file_name, 'a+')
    f.write(log + '\n')
    f.close()


# Computes the logs
def data(user_name, query):
    query = str(query + ' ')
    query = 'search : ' + query
    timestr = str(time.asctime())
    log = str(query + timestr)
    write_to_file(user_name, log)


# Convert the string into URL . Explicit Encoding the string to URL into UTF-8.
def urlifystring(string):
    ythomepage = 'https://www.youtube.com/results?search_query='
    string = ythomepage + string
    res = ''
    start = False
    for char in reversed(string):
        if char != ' ':
            start = True

        if char == ' ' and start is True:
            res += '+'
        else:
            res += char
    return res[::-1]












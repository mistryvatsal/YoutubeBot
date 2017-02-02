from Logs import *
from HTMLScrapping import *


# Main function that takes input of user
def user():
    user_name = str(input('ENTER YOUR NAME : '))
    query = str(input('ENTER YOUR QUERY TO BE SEARCHED ON YOUTUBE : '))
    create_dir()
    data(user_name, query)
    link = urlifystring(query)
    html_parser(link)

user()

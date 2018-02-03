from urllib import urlopen

# Python Bult-in Functions --> https://docs.python.org/2/library/functions.html

# WDYL Search Engine --> https://en.wikipedia.org/wiki/WDYL_(search_engine)

# Query String --> https://en.wikipedia.org/wiki/Query_string



movie_quotes_dir = r"/Users/brunonovo/Projects/python/Udacity/Programming-Foundations-with-Python"

def read_text():
    quotes = open(movie_quotes_dir + "/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This Document has No Curse Words!!")
    else:
        print("Could not Scan The Document Properly")

read_text()
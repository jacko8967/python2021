python_dictionary = { #modified dictionary to include email address
    'jacko8967@gmail.com' : 'jack robins',
    'john.smith@gmail.com' : 'john smith', #added first key value pair to dictionary
    'fred.jones@gmail.com' : 'fred jones', #added second key value pair to dictionary
    'bill.strong@gmail.com' : 'bill strong', #added third and final key value pair to dictionary
    'me@home.com' : "me at home"
}

emlStr = "me@home.com.au"

if (emlStr.find("@") != -1): 
    print("hello")
else:
    print("byeS")

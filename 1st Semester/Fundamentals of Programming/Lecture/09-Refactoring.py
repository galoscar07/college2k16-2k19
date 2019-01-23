'''
Created on Sep 30, 2016

@author: Arthur
'''

def add(lst, nr):
    lst.append(nr)

'''
    The startUI method below contains duplicated code.
'''

# def startUI():
#     list = []
#     print(list)
#     
#     # read user command
#     menu = """
#             Enter command:
#                 1-add element
#                 0-exit
#            """
#     print(menu)
#     cmd = input()
#     
#     while cmd != "0":
#         if cmd == "1":
#             nr = input("Give element:")
#             add(list, nr)
#             print (list)
# 
#         # read user command
#         menu = """
#                 Enter command:
#                     1-add element
#                     0-exit
#                """
#         print(menu)
#         cmd = input()        
# 
# startUI()

'''
    Below is the refactored version
'''

def getUserCommand():
    """
    Print the application menu
    Return the user's command
    """
    menu = """
            Enter command:
                1-add element
                0-exit
           """
    print(menu)
    cmd = input()
    return cmd

def startUI():
    list = []
    print(list)
    
    cmd = getUserCommand()
    
    while cmd != "0":
        if cmd == "1":
            nr = input("Give element:")
            add(list, nr)
            print (list)
        cmd = getUserCommand()        

startUI()

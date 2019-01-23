class Ui(object):

    def __init__(self,personController):
        self.__personController = personController


    def startApp(self):
        keepAlive = True
        while keepAlive:
            try:
                command = input("Enter Command")
                li = command.split(" ")
                if li[0]== "exit":
                    keepAlive = False
                elif li[0] == "list":
                    self.list()
                elif li[0] == "add":
                    self.add(li)
                elif li[0] == "vaccinate":
                    self.vaccinate(li)
            except EnvironmentError as exp:
                print(exp)

    def list(self):
        li = self.__personController.getAll()
        if len(li) == 0:
            print("No person")
        else:
            for i in li:
                print(i)

    def add(self,li):
        self.__personController.addPerson(li[1],li[2],li[3])

    def vaccinate(self,li):
        self.__personController.vaccinate(int(li[1]))
class Ui(object):
    def __init__(self,chocolateController):
        self.__chocolateController = chocolateController

    def start(self):
        keepAlive = True
        while keepAlive:
            try:
                command = int(input("Enter Command"))
                if command == 0:
                    keepAlive = False
                elif command == 1:
                    self.list()
            except:
                raise Exception

    def list(self):
        li = self.__chocolateController.getAll()
        if len(li) == 0:
            print("noyhing to be printed")
        else:
            for i in li:
                print(i)

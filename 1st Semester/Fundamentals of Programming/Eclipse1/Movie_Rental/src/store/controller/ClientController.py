'''
Created on Nov 13, 2016

@author: oscar
'''
from src.store.domain.entities import Client
from src.store.domain.validators import ClientValidatorException, ClientIdNotFound


class ClientController(object):
    """
    The class is for the clients list in the app
    """
    def __init__(self, clientRepository,undoController):
        """
        The app will initialize the clientController with a dictionary, the key will be the client id
        :param clientRepository: a class, in which are it is a set of operations visible for all controllers
        """
        self.__clientRepository = clientRepository
        self.__undoController = undoController

    def addClient(self, clientId,name):
        """
        The function will add clients into the controller
        :param clientId: is the key which will help us to save into the dictionary
        :param name: is the value fro the key clientId
        :return: The function will return the list of clients with a new client in it
        """
        client = Client(clientId,name)
        self.__clientRepository.save(client)
        self.__undoController.registerOperation(self.addClient, self.deleteClient, clientId)
         

    def deleteClient(self,clientId):
        """
        The function is designed to delete an element from the controller
        :param clientId: is the element that we will delete
        :return: the function will return the lsit with an element deleted
        """
        something = self.__clientRepository.findById(clientId)
        name = something.name
        self.__clientRepository.delete(clientId)
        self.__undoController.registerOperation(self.deleteClient,self.addClient,clientId, name)
         


    def updateClient(self,clientId, newname):
        """
        The function will update the client name
        :param clientId: is the key in which we will update the name
        :param newname: is the name which will be saved at the key clientId
        :return: the function will return the list modified
        """
        op = self.__clientRepository.findById(clientId)
        if op == None:
            raise ClientIdNotFound
        else:
            oldname = op.name
            op.name = newname
        self.__undoController.registerOperation(self.updateClient,self.updateClientUndo,clientId,oldname)
         

    def updateClientUndo(self,clientId,name):
        """
        This function does the same as the one above, but the only difference is that it is design for undo
        """
        op = self.__clientRepository.findById(clientId)
        op.name = name

    def getAll(self):
        """
        The function will return a list with all the elements in it
        """
        return self.__clientRepository.getAll()

    def searchByName(self,name):
        """
        The function will return a list will all the elements in witch the client name is the same as the variable name
        :param name: is a variable which we will compare the other elements of the list
        :return: a list with elements that have at the fields name the value of the variable name
        """
        return (list(filter(lambda client: name in client.name.lower(), self.__clientRepository.getAll())))

    def searchById(self,clientId):
        """
        The function does almost the same thing as the function from above but it search for id
        """
        return (list(filter(lambda client: clientId in str(client.entityId).lower(),self.__clientRepository.getAll())))


    def startUp(self):
        """
        The function will give 100 elements into the controller for start up
        :return: the list with 100 elements in it
        """
        self.addClient(1, "Gal Oscar")
        self.addClient(2, "Grigor Sebastian")
        self.addClient(3, "Comsa Mihai")
        self.addClient(4, "Catargiu Andreea Alexandra")
        self.addClient(5, "Constantinescu Ioana Dora")
        self.addClient(6, "Culda Catalina Maria")
        self.addClient(7, "Trifan Cristina")
        self.addClient(8, "Olar Alexandru")
        self.addClient(9, "Cerbu Valer")
        self.addClient(10,"Schiau Sorin")
        self.addClient(11, "Gal Cristina Lidia")
        self.addClient(12, "Gal Francisc Oscar")
        self.addClient(13, "Comsa Francesca")
        self.addClient(14, "Munteanu Aida")
        self.addClient(15, "Campeanu Sorin")
        self.addClient(16, "Ponta Victor")
        self.addClient(17, "Ceausescu Nicolae")
        self.addClient(18, "Iliescu Ion")
        self.addClient(19, "Constantinescu Emil")
        self.addClient(20, "Basescu Traian")
        self.addClient(21, "Klaus Iohannis")
        self.addClient(22, "Petre Florentin")
        self.addClient(23, "Schiller Daria")
        self.addClient(24, "Luta Cezar")
        self.addClient(25, "Luta Robert")
        self.addClient(26, "Luta Otto")
        self.addClient(27, "Sas Mircea")
        self.addClient(28, "Ildiko Sas")
        self.addClient(29, "Maria Tanase")
        self.addClient(30, "Sergiu Nicolaescu")
        self.addClient(31, "Badea Cartan")
        self.addClient(32, "Ciprian Porumbescu")
        self.addClient(33, "Stefan Banica")
        self.addClient(34, "Monica Anghel")
        self.addClient(35, "Loredana Groza")
        self.addClient(36, "Luta Corina")
        self.addClient(37, "Irina Anghel")
        self.addClient(38, "Adela Popescu")
        self.addClient(39, "Anda Gazon")
        self.addClient(40, "Marius Moga")
        self.addClient(41, "Vadim Tudor")
        self.addClient(42, "Tudor Gheorge")
        self.addClient(43, "Arsenie Boca")
        self.addClient(44, "Eugen Ionescu")
        self.addClient(45, "Vlad Tepes")
        self.addClient(46, "Nicolae Iorga")
        self.addClient(47, "Mirel Radoi")
        self.addClient(48, "George Enescu")
        self.addClient(49, "Gigi Becali")
        self.addClient(50, "Henri Coanda")
        self.addClient(51, "Nadia Comaneci")
        self.addClient(52, "Alexandru Ioan Cuza")
        self.addClient(53, "Ion Antonescu")
        self.addClient(54, "Mihai Eminescu")
        self.addClient(55, "Ștefan cel Mare")
        self.addClient(56, "Gregg Allman")
        self.addClient(57, "Toots Hibbertv")
        self.addClient(58, "John Fogerty")
        self.addClient(59, "Dolly Parton")
        self.addClient(60, "James Taylor")
        self.addClient(61, "Iggy Pop")
        self.addClient(62, "Steve Perry")
        self.addClient(63, "Merle Haggard")
        self.addClient(64, "Mariah Carey")
        self.addClient(65, "Frankie Valli")
        self.addClient(66, "John Lee Hooker")
        self.addClient(67, "Tom Waits")
        self.addClient(68, "Patti Smith")
        self.addClient(69, "Darlene Love")
        self.addClient(70, "Joe Cocker")
        self.addClient(71, "Stevie Nicks")
        self.addClient(72, "Steven Tyler")
        self.addClient(73, "Benazir Bhutto")
        self.addClient(74, "Eva Peron")
        self.addClient(75, "Indira Gandhi")
        self.addClient(76, "Michael Jordon")
        self.addClient(77, "Oprah Winfrey")
        self.addClient(78, "Ludwig Beethoven")
        self.addClient(79, "Lyndon Johnson")
        self.addClient(80, "Aung San Suu Kyi")
        self.addClient(81, "Rosa Parks")
        self.addClient(82, "Thomas Edison")
        self.addClient(83, "Pope John Paul II")
        self.addClient(84, "Franklin D. Roosevelt")
        self.addClient(85, "Vincent Van Gogh")
        self.addClient(86, "Pablo Picasso")
        self.addClient(87, "Leo Tolstoy")
        self.addClient(88, "Louis Pasteur")
        self.addClient(89, "Leonardo da Vinci")
        self.addClient(90, "Jawaharlal Nehru")
        self.addClient(91, "Mikhail Gorbachev")
        self.addClient(92, "John M Keynes")
        self.addClient(93, "Queen Victoria")
        self.addClient(94, "Queen Elizabeth II")
        self.addClient(95, "Plato")
        self.addClient(96, "Paul McCartney")
        self.addClient(97, "Albert Einstein")
        self.addClient(98, "Elvis Presley")
        self.addClient(99, "Charles Darwin")
        self.addClient(100, "George Orwell")


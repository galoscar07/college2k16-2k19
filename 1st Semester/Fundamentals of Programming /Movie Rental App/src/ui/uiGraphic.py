from tkinter import *
from tkinter import messagebox

import datetime


class UiGraphic():
    def __init__(self, movieController, clientController, rentalController, statisticsController,undoController):
        self.__movieController = movieController
        self.__clientController = clientController
        self.__rentalController = rentalController
        self.__statisticsController = statisticsController
        self.__undoController = undoController
        self.tk = Tk()
        self.tk.title("Movie Rental")
        self.tk.geometry("1050x650")
        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame
        self.label1 = Label(self.tk)
        self.label2 = Label(self.tk)
        self.sb = Scrollbar(self.tk, orient=VERTICAL)
        self.sb.pack(side=LEFT, fill=Y)

    def initializationMenu(self):
        self.frame.destroy()
        self.label1.pack_forget()
        self.label2.pack_forget()
        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame
        self.statisticsMBtn = Button(frame, text="Main Menu", command=self.startUI)
        self.statisticsMBtn.pack(side=LEFT)
        self.MovieMBtn = Button(frame, text="Movie Menu", command=self.movieMenu)
        self.MovieMBtn.pack(side=LEFT)
        self.label1 = Label(self.tk)
        self.label1.pack()
        self.label2 = Label(self.tk)
        self.label2.pack()

    def initializationClient(self):
        self.frame.destroy()
        self.label1.pack_forget()
        self.label2.pack_forget()
        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame
        self.statisticsMBtn = Button(frame, text="Main Menu", command=self.startUI)
        self.statisticsMBtn.pack(side=LEFT)
        self.clientMBtn = Button(frame, text="Client Menu", command=self.clientMenu)
        self.clientMBtn.pack(side=LEFT)
        self.label1 = Label(self.tk)
        self.label1.pack()
        self.label2 = Label(self.tk)
        self.label2.pack()

    def initializationRental(self):
        self.frame.destroy()
        self.label1.pack_forget()
        self.label2.pack_forget()
        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame
        self.statisticsMBtn = Button(frame, text="Main Menu", command=self.startUI)
        self.statisticsMBtn.pack(side=LEFT)
        self.clientMBtn = Button(frame, text="Rental Menu", command=self.rentMenu)
        self.clientMBtn.pack(side=LEFT)
        self.label1 = Label(self.tk)
        self.label1.pack()
        self.label2 = Label(self.tk)
        self.label2.pack()

    def initializationSearch(self):
        self.frame.destroy()
        self.label1.pack_forget()
        self.label2.pack_forget()
        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame
        self.statisticsMBtn = Button(frame, text="Main Menu", command=self.startUI)
        self.statisticsMBtn.pack(side=LEFT)
        self.clientMBtn = Button(frame, text="Search Menu", command=self.searchMenu)
        self.clientMBtn.pack(side=LEFT)
        self.label1 = Label(self.tk)
        self.label1.pack()
        self.label2 = Label(self.tk)
        self.label2.pack()

    def initializationStatistics(self):
        self.frame.destroy()
        self.label1.pack_forget()
        self.label2.pack_forget()
        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame
        self.statisticsMBtn = Button(frame, text="Main Menu", command=self.startUI)
        self.statisticsMBtn.pack(side=LEFT)
        self.clientMBtn = Button(frame, text="Statistics Menu", command=self.statisticsMenu)
        self.clientMBtn.pack(side=LEFT)
        self.label1 = Label(self.tk)
        self.label1.pack()
        self.label2 = Label(self.tk)
        self.label2.pack()



    def startUI(self):
        self.frame.destroy()
        self.label1.pack_forget()
        self.label2.pack_forget()

        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame

        self.MovieMBtn = Button(frame, text="Movie Menu", command = self.movieMenu)
        self.MovieMBtn.pack(side=LEFT)

        self.clientMBtn = Button(frame, text = "Client Menu", command = self.clientMenu)
        self.clientMBtn.pack(side=LEFT)

        self.rentMBtn = Button(frame, text="Rental Menu", command=self.rentMenu)
        self.rentMBtn.pack(side=LEFT)

        self.searchMBtn = Button(frame, text="Search Menu", command=self.searchMenu)
        self.searchMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Statistics Menu", command=self.statisticsMenu)
        self.statisticsMBtn.pack(side=LEFT)

        self.undoBtn = Button(frame, text="Undo", command=self.undo)
        self.undoBtn.pack(side=LEFT)

        self.redoBtn = Button(frame, text="Redo", command=self.redo)
        self.redoBtn.pack(side=LEFT)

        self.button = Button(frame, text="Quit", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.tk.mainloop()

    def movieMenu(self):

        self.frame.destroy()
        self.label1.pack_forget()
        self.label2.pack_forget()

        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame

        self.statisticsMBtn = Button(frame, text="Add a movie", command=self.uiaddMovie)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Remove a movie", command=self.uideleteMovie)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Update a movie", command=self.uiupdateMovie)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="List all movies", command=self.uilistMovie)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Main Menu", command = self.startUI)
        self.statisticsMBtn.pack(side=LEFT)
        self.tk.mainloop()

    def clientMenu(self):
        self.frame.destroy()
        self.label1.pack_forget()
        self.label2.pack_forget()

        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame

        self.statisticsMBtn = Button(frame, text="Add a client", command=self.uiaddClient)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Remove a client", command=self.uideleteClient)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Update a client", command=self.uiupdateClient)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="List all clients", command=self.uilistClient)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Main Menu", command=self.startUI)
        self.statisticsMBtn.pack(side=LEFT)
        self.tk.mainloop()

    def rentMenu(self):
        self.frame.destroy()
        self.label1.pack_forget()
        self.label2.pack_forget()

        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame

        self.statisticsMBtn = Button(frame, text="Rent a movie", command=self.uirentMovie)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Return a movie", command=self.uireturnMovie)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="List all rents", command=self.uilistRent)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Main Menu", command=self.startUI)
        self.statisticsMBtn.pack(side=LEFT)
        self.tk.mainloop()

    def searchMenu(self):
        self.frame.destroy()
        self.label1.pack_forget()
        self.label2.pack_forget()

        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame

        self.statisticsMBtn = Button(frame, text="After movie id", command=self.uisearchMId)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="After movie title", command=self.uisearchMTitle)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="After movie genre", command=self.uisearchMGenre)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="After movie description", command=self.uisearchMDescription)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="After client id", command=self.uisearchCId)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="After client name", command=self.uisearchCName)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Main Menu", command=self.startUI)
        self.statisticsMBtn.pack(side=LEFT)
        self.tk.mainloop()


    def statisticsMenu(self):
        self.frame.destroy()
        self.label1.pack_forget()
        self.label2.pack_forget()

        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame

        self.statisticsMBtn = Button(frame, text="Most rented movie (by nr times)", command=self.uimostRentedTimes)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Most rented movie (by nr days)", command=self.uimostRentedDays)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Most activ clients", command=self.uimostActiveClients)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="All movie currently rented", command=self.uimovieCurrentlyRented)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Late Rentals", command=self.uilateRentals)
        self.statisticsMBtn.pack(side=LEFT)

        self.statisticsMBtn = Button(frame, text="Main Menu", command=self.startUI)
        self.statisticsMBtn.pack(side=LEFT)
        self.tk.mainloop()

    def undo(self):
        try:
            self.__undoController.undo()
            messagebox.showinfo("Undo", "The undo action was done")
        except Exception as e:
            messagebox.showinfo("Error", "Error undoing - " + str(e))

    def redo(self):
        try:
            self.__undoController.redo()
            messagebox.showinfo("Redo", "The redo action was done")
        except Exception as e:
            messagebox.showinfo("Error", "Error redoing - " + str(e))

    def uiaddMovie(self):
        self.initializationMenu()

        lbl = Label(self.label1, text="Movie Id:")
        lbl.pack(side=LEFT)
        self.idtf = Entry(self.label1, {})
        self.idtf.pack(side=LEFT)

        lbl = Label(self.label1, text="Movie Title:")
        lbl.pack(side=LEFT)
        self.titletf = Entry(self.label1, {})
        self.titletf.pack(side=LEFT)

        lbl = Label(self.label2, text="Movie Genre:")
        lbl.pack(side=LEFT)
        self.genretf = Entry(self.label2, {})
        self.genretf.pack(side=LEFT)

        lbl = Label(self.label2, text="Movie Description:")
        lbl.pack(side=LEFT)
        self.descriptiontf = Entry(self.label2, {})
        self.descriptiontf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Add", command=self.addMovie)
        self.statisticsMBtn.pack(side=LEFT)

    def addMovie(self):
        try:
            self.__movieController.addMovie(int(self.idtf.get()), self.titletf.get(), self.genretf.get(),
                                            self.descriptiontf.get())
            messagebox.showinfo("Stored", "Movie %s saved.." % self.titletf.get())
        except Exception as e:
            messagebox.showinfo("Error", "Error saving movie - " + str(e))

    def uideleteMovie(self):
        self.initializationMenu()
        lbl = Label(self.label1, text="Movie Id you want to delete:")
        lbl.pack(side=LEFT)
        self.idtf = Entry(self.label1, {})
        self.idtf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Delete", command=self.deleteMovie)
        self.statisticsMBtn.pack(side=LEFT)

    def deleteMovie(self):
        try:
            self.__movieController.deleteMovie(int(self.idtf.get()))
            messagebox.showinfo("Stored", "Movie %s was deleted.." % self.idtf.get())
        except Exception as e:
            messagebox.showinfo("Error", "Error deleting movie - " + str(e))

    def uiupdateMovie(self):
        self.initializationMenu()

        lbl = Label(self.label1, text="Movie Id:")
        lbl.pack(side=LEFT)
        self.idtf = Entry(self.label1, {})
        self.idtf.pack(side=LEFT)

        lbl = Label(self.label1, text="Movie Title:")
        lbl.pack(side=LEFT)
        self.titletf = Entry(self.label1, {})
        self.titletf.pack(side=LEFT)

        lbl = Label(self.label2, text="Movie Genre:")
        lbl.pack(side=LEFT)
        self.genretf = Entry(self.label2, {})
        self.genretf.pack(side=LEFT)

        lbl = Label(self.label2, text="Movie Description:")
        lbl.pack(side=LEFT)
        self.descriptiontf = Entry(self.label2, {})
        self.descriptiontf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Update", command=self.updateMovie)
        self.statisticsMBtn.pack(side=LEFT)

    def updateMovie(self):
        try:
            if self.titletf.get() != "":
                self.__movieController.updateMovie(int(self.idtf.get()), 1, self.titletf.get())
            if self.genretf.get() != "":
                self.__movieController.updateMovie(int(self.idtf.get()), 2, self.genretf.get())
            if self.descriptiontf.get() != "":
                self.__movieController.updateMovie(int(self.idtf.get()), 3, self.descriptiontf.get())
            if self.titletf.get() == "" and self.genretf.get() == "" and self.descriptiontf.get() =="":
                raise Exception("You need to fill at least one space")
            messagebox.showinfo("Stored", "Movie was updated..")
        except Exception as e:
            messagebox.showinfo("Error", "Error updating the movie - " + str(e))


    def uilistMovie(self):
        self.initializationMenu()

        self.label1 = Listbox(self.tk, width=100, height=30)
        self.label1.pack()
        lis = self.__movieController.getAll()
        if len(lis) == 0:
            self.label1.insert(END, "Their is no movie")
        else:
            for i in lis:
                self.label1.insert(END, i)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)

    def uiaddClient(self):
        self.initializationClient()

        lbl = Label(self.label1, text="Client Id:")
        lbl.pack(side=LEFT)
        self.idtf = Entry(self.label1, {})
        self.idtf.pack(side=LEFT)

        lbl = Label(self.label1, text="Client Name:")
        lbl.pack(side=LEFT)
        self.nametf = Entry(self.label1, {})
        self.nametf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Add", command=self.addClient)
        self.statisticsMBtn.pack(side=LEFT)

    def addClient(self):
        try:
            self.__clientController.addClient(int(self.idtf.get()), self.nametf.get())
            messagebox.showinfo("Stored", "Client %s saved.." % self.nametf.get())
        except Exception as e:
            messagebox.showinfo("Error", "Error saving client - " + str(e))

    def uilistClient(self):
        self.initializationClient()
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        lis = self.__clientController.getAll()
        if len(lis) == 0:
            self.label1.insert(END,"Their is no client")
        else:
            for i in lis:
                self.label1.insert(END,i)
        self.sb.configure(command = self.label1.yview)
        self.label1.configure(yscrollcommand = self.sb.set)

    def uideleteClient(self):
        self.initializationClient()

        lbl = Label(self.label1, text="Client Id you want to delete:")
        lbl.pack(side=LEFT)
        self.idtf = Entry(self.label1, {})
        self.idtf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Delete", command=self.deleteClient)
        self.statisticsMBtn.pack(side=LEFT)

    def deleteClient(self):
        try:
            self.__clientController.deleteClient(int(self.idtf.get()))
            messagebox.showinfo("Stored", "Client %s was deleted.." % self.idtf.get())
        except Exception as e:
            messagebox.showinfo("Error", "Error deleting client - " + str(e))

    def uiupdateClient(self):
        self.initializationClient()

        lbl = Label(self.label1, text="Give an Id: ")
        lbl.pack(side=LEFT)
        self.idtf = Entry(self.label1, {})
        self.idtf.pack(side=LEFT)

        lbl = Label(self.label1, text="Give a new name: ")
        lbl.pack(side=LEFT)
        self.nametf = Entry(self.label1, {})
        self.nametf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Update", command=self.updateClient)
        self.statisticsMBtn.pack(side=LEFT)
        self.tk.mainloop()

    def updateClient(self):
        try:
            self.__clientController.updateClient(int(self.idtf.get()),self.nametf.get())
            messagebox.showinfo("Stored","Client's info %s was updated" % self.nametf.get())
        except Exception as e:
            messagebox.showinfo("Error", "Error updating client - " + str(e))

    def uireturnMovie(self):
        self.initializationRental()

        lbl = Label(self.label1, text="Rent Id:")
        lbl.pack(side=LEFT)
        self.rentidtf = Entry(self.label1, {})
        self.rentidtf.pack(side=LEFT)

        lbl = Label(self.label1, text="Renturned Date(dd.mm.yyyy):")
        lbl.pack(side=LEFT)

        self.returneddatetf = Entry(self.label1, {})
        self.returneddatetf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Return", command=self.returnMovie)
        self.statisticsMBtn.pack(side=LEFT)

    def returnMovie(self):
        try:
            self.__rentalController.returnMovie(int(self.rentidtf.get()),datetime.datetime.strptime
                                                                    (self.returneddatetf.get(),"%d.%m.%Y").date())
            messagebox.showinfo("Stored", "The movie was returned succesfully")
        except Exception as e:
            messagebox.showinfo("Error","Error returning a movie - "+str(e))


    def uirentMovie(self):
        self.initializationRental()

        lbl = Label(self.label1, text="Movie Id:")
        lbl.pack(side=LEFT)
        self.movieidtf = Entry(self.label1, {})
        self.movieidtf.pack(side=LEFT)

        lbl = Label(self.label1, text="Client Id:")
        lbl.pack(side=LEFT)
        self.clientidtf = Entry(self.label1, {})
        self.clientidtf.pack(side=LEFT)

        lbl = Label(self.label2, text="Rent Date(dd.mm.yyyy):")
        lbl.pack(side=LEFT)
        self.rentdatetf = Entry(self.label2, {})
        self.rentdatetf.pack(side=LEFT)

        lbl = Label(self.label2, text="Due Date(dd.mm.yyyy):")
        lbl.pack(side=LEFT)
        self.duedatetf = Entry(self.label2, {})
        self.duedatetf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Add", command=self.addRent)
        self.statisticsMBtn.pack(side=LEFT)

    def addRent(self):
        try:
            self.__rentalController.addRental(int(self.movieidtf.get()), int(self.clientidtf.get()),
                                              datetime.datetime.strptime(self.rentdatetf.get(),"%d.%m.%Y").date(),
                                              datetime.datetime.strptime(self.duedatetf.get(),"%d.%m.%Y").date(),None)
            messagebox.showinfo("Stored", "The rent was accomplish successfully")
        except Exception as e:
            messagebox.showinfo("Error","Error adding rental - "+str(e))

    def uilistRent(self):
        self.initializationRental()
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        lis = self.__rentalController.getAll()
        if len(lis) == 0:
            self.label1.insert(END, "Their is no rent")
        else:
            for i in lis:
                self.label1.insert(END, i)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)


    def uisearchMId(self):
        self.initializationSearch()

        lbl = Label(self.label1, text="Search using Id:")
        lbl.pack(side=LEFT)
        self.movieidtf = Entry(self.label1, {})
        self.movieidtf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Search", command=self.searchMId)
        self.statisticsMBtn.pack(side=LEFT)

    def searchMId(self):
        self.initializationSearch()

        param = self.healpingSearch(self.movieidtf.get())
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        for i in param:
            ls = self.__movieController.searchById(i)
            self.label1.insert(END, "Search by: ",i)
            for j in ls:
                self.label1.insert(END, j)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)


    def uisearchMTitle(self):
        self.initializationSearch()

        lbl = Label(self.label1, text="Search using Title:")
        lbl.pack(side=LEFT)
        self.titletf = Entry(self.label1, {})
        self.titletf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Search", command=self.searchMTitle)
        self.statisticsMBtn.pack(side=LEFT)

    def searchMTitle(self):
        self.initializationSearch()

        param = self.healpingSearch(self.titletf.get())
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        for i in param:
            ls = self.__movieController.searchByTitle(i)
            self.label1.insert(END, i)
            for j in ls:
                self.label1.insert(END, "Search by: ", j)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)

    def uisearchMGenre(self):
        self.initializationSearch()

        lbl = Label(self.label1, text="Search using Genre:")
        lbl.pack(side=LEFT)
        self.genretf = Entry(self.label1, {})
        self.genretf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Search", command=self.searchMGenre)
        self.statisticsMBtn.pack(side=LEFT)

    def searchMGenre(self):
        self.initializationSearch()
        param = self.healpingSearch(self.genretf.get())
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        for i in param:
            ls = self.__movieController.searchByGenre(i)
            self.label1.insert(END, i)
            for j in ls:
                self.label1.insert(END, "Search by: ", j)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)

    def uisearchMDescription(self):
        self.initializationSearch()

        lbl = Label(self.label1, text="Search using Description:")
        lbl.pack(side=LEFT)
        self.descriptiontf = Entry(self.label1, {})
        self.descriptiontf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Search", command=self.searchMDescription)
        self.statisticsMBtn.pack(side=LEFT)

    def searchMDescription(self):
        self.initializationSearch()

        param = self.healpingSearch(self.descriptiontf.get())
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        for i in param:
            ls = self.__movieController.searchByDescription(i)
            self.label1.insert(END, "Search by: ", i)
            for j in ls:
                self.label1.insert(END, j)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)

    def uisearchCId(self):
        self.initializationSearch()

        lbl = Label(self.label1, text="Search using Id:")
        lbl.pack(side=LEFT)
        self.clientidtf = Entry(self.label1, {})
        self.clientidtf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Search", command=self.searchCId)
        self.statisticsMBtn.pack(side=LEFT)

    def searchCId(self):
        self.initializationSearch()

        param = self.healpingSearch(self.clientidtf.get())
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        for i in param:
            ls = self.__clientController.searchById(i)
            self.label1.insert(END, "Search by: ", i)
            for j in ls:
                self.label1.insert(END, "Search by: ", j)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)


    def uisearchCName(self):
        self.initializationSearch()

        lbl = Label(self.label1, text="Search using Name:")
        lbl.pack(side=LEFT)
        self.nametf = Entry(self.label1, {})
        self.nametf.pack(side=LEFT)

        self.statisticsMBtn = Button(self.label2, text="Search", command=self.searchCName)
        self.statisticsMBtn.pack(side=LEFT)

    def searchCName(self):
        self.initializationSearch()

        param = self.healpingSearch(self.nametf.get())
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        for i in param:
            ls = self.__clientController.searchByName(i)
            self.label1.insert(END, "Search by: ", i)
            for j in ls:
                self.label1.insert(END, j)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)


    def healpingSearch(self,string):
        string = string.lower()
        string = string.split(" ")
        param = string[0:len(string)]
        newlist = [i for n, i in enumerate(param) if i not in param[:n]]
        return newlist

    def uimostRentedTimes(self):
        self.initializationStatistics()
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        self.label1.insert(END,"By the number of time: ")
        top = self.__statisticsController.topByMostRentedTimes()
        for i in top:
            self.label1.insert(END, i)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)

    def uimostRentedDays(self):
        self.initializationStatistics()
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        self.label1.insert(END, "By the number of days: ")
        top = self.__statisticsController.topByMostRentedDays()
        for i in top:
            self.label1.insert(END, i)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)

    def uimostActiveClients(self):
        self.initializationStatistics()
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        self.label1.insert(END, "Most Active Clients: ")
        top = self.__statisticsController.mostActiveClients()
        for i in top:
            self.label1.insert(END, i)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)

    def uimovieCurrentlyRented(self):
        self.initializationStatistics()
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        self.label1.insert(END, "All movies currently rented: ")
        top = self.__statisticsController.allCurrentlyRented()
        for i in top:
            self.label1.insert(END, i)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)

    def uilateRentals(self):
        self.initializationStatistics()
        self.label1 = Listbox(width=100, height=30)
        self.label1.pack()
        self.label1.insert(END, "Late Rentals: ")
        top = self.__statisticsController.lateRentals()
        for i in top:
            self.label1.insert(END, i)
        self.sb.configure(command=self.label1.yview)
        self.label1.configure(yscrollcommand=self.sb.set)
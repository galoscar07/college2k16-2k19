class ConsoleUI:
    """
      Menu-driven console-based user interface
    """
    def __init__(self, studentController, gradeController):
        self.__studentController = studentController
        self.__gradeController = gradeController

    def __readUserCommand(self):
        print("\t 1 - Add student")
        print("\t 2 - Remove student")
        print("\t 3 - Search for student")
        print("\t 4 - Update student")
        print("\t 5 - Grade student")
        print("\t 6 - View student grades")
        print("\t 7 - Top 5 at discipline")
        print("\t 0 - Exit") 
        return input("Give command:").strip()

    def __createStudent(self):
        studentId = input("Student studentId:").strip()
        studentName = input("Student studentName:").strip()
        addrCountry = input("Address - county:").strip()
        addrCity = input("Address - city:").strip()
        addrStreet = input("Address - street:").strip()

        self.__studentController.create(studentId, studentName, addrCountry, addrCity, addrStreet)

    def __removeStudent(self):
        studentId = input("Student ID:").strip()

        student = self.__studentController.remove(studentId)
        print ("Student " + student.getName() + " removed")

    def __findStudent(self):
        searchString = input("Name contains:").strip()
        students = self.__studentController.search(searchString)
        if len(students) == 0:
            print ("No matching student")
            return

        print ("Search resulted in " + str(len(students)) + " matches")
        for student in students:
            print ("\t" + str(student))

    def __top5(self):
        discipline = input("Discipline:").strip()
        sortedStudentGradeList = self.__gradeController.getTop5(discipline)
        if len(sortedStudentGradeList) == 0:
            print ("No match for given discipline")
            return

        for studentGrade in sortedStudentGradeList:
            print (str(studentGrade))

    def __updateStudent(self):
        studentId = input("Give the student's id:").strip()
        studentName = input("New student studentName:").strip()
        addrCounty = input("New address - county:").strip()
        addrCity = input("New address - addrStreet:").strip()
        addrStreet = input("New address - addrCounty:").strip()
        
        old = self.__studentController.update(studentId, studentName, addrCounty, addrCity, addrStreet)
        print ("Student " + old.getName() + " updated")

    def __assignGrade(self):
        studentId = input("Give the student's id:").strip()
        discipline = input("Discipline:").strip()
        grade = input("Grade:").strip()

        self.__gradeController.assign(studentId, discipline, int(grade))
        print ("Grade assigned")

    def __listStudentGrade(self):
        studentId = input("Give the student's id:").strip()
        gradeList = self.__gradeController.listGrades(studentId)
        if len(gradeList) == 0:
            print ("No grades for given student")
            return
        
        print ("Search resulted in " + str(len(gradeList)) + " grades")
        print ("Name".ljust(15) + "Discipline".ljust(30) + "Grade")
        for grade in gradeList:
            print (grade.getStudent().getName().ljust(15) + grade.getDiscipline().ljust(30) + str(grade.getGradeValue()))

    def startUI(self):
        commands = {"1":self.__createStudent, "2":self.__removeStudent, "3":self.__findStudent,
                    "4":self.__updateStudent, "5":self.__assignGrade, "6":self.__listStudentGrade,
                    "7":self.__top5
                    }
        
        """
            Main UI loop, handle exceptions here
        """
        while True:
#             try:
                c = self.__readUserCommand().strip()
                if c == "0":
                    print ("I'll be back!")
                    return
                
                if c not in commands.keys():
                    print("Invalid command!")
                    continue
                
                """
                    Valid commands (except exit) are in a dictionary
                    Here we run the corresponding function
                """
                commands[c]()
#             except Exception as e:
#                 print("The following error has occurred - " + str(e))


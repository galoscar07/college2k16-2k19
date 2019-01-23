from examples.studentManagement.repository.Exceptions import DuplicateIDException

class StudentRepository:
    """
      Class responsible for managing a list of students (store, retrieve , update, etc)
      GRASP - Pure Fabrication -  Repository Pattern
    """
    def __init__(self):
        self._data = {}

    def store(self, student):
        """
          Store a student
          st - student
          raise DuplicateIDException for duplicated id
        """
        if student.getId() in self._data.keys():
            raise DuplicateIDException("Duplicate student with id="+student.getId())
        
        self._data[student.getId()] = student
        

    def size(self):
        """
          return the number of students in the repository
        """
        return len(self._data)

    def __len__(self):
        return self.size()

    def __str__(self):
        result = "Student Repository:\n"
        for student in self._data.values():
            result += "\t " + str(student) + "\n"
        return result

    def remove(self, studentId):
        """
          remove a student from the repository
          studentId - string, the studentId of the student to be removed
          return student
          post: the repository not contains student with the given studentId
          raise ValueError if there is no student with the given studentId
        """
        if not studentId in self._data:
            raise ValueError("No student for studentId:" + studentId)
        
        st = self._data[studentId]
        del self._data[studentId]
        return st

    def removeAll(self):
        """
          Remove all the students from the repository
        """
        self._data.clear()

    def getAll(self):
        """
          Retrieve all the students
          return a list with students
        """
        return self._data.values()

    def update(self, studentId, student):
        """
          Update student in the repository
          studentId - string, the studentId of the student to be updated
          student - Student, the updated student
          raise ValueError if there is no student with the given studentId
        """
        self.remove(studentId)
        self.store(student)

    def find(self, studentId):
        """
          Find the student for a given studentId
          studentId - string
          return student with the given studentId or None if there is no student with the given studentId
        """
        if not studentId in self._data:
            return None

        return self._data[studentId]

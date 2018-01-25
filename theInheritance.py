class Parent():
    def __init__(self, surName, firstName):
        self.surName = surName
        self.firstName = firstName

    def showdetail(self):
        print("First name is:", self.firstName)
        print("Sur name is:", self.surName)

billyCyrus = Parent("Cyrus", "Billy")
billyCyrus.showdetail()

class child (Parent):
    def __init__(self, surName, firstName,numberOfToys):
        Parent.__init__(self, surName, firstName)
        self.numberOfToys = numberOfToys

    def showdetail(self):
        print("First name is:", self.firstName)
        print("Sur name is:", self.surName)
        print("Toys are:", self.numberOfToys)

mileCyrus = child("Cyrus","Mile", 5)
mileCyrus.showdetail()

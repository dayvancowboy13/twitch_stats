class GrabHTML:

  def __init__(self, fileName):

      try:
          self.f = open(fileName, "r+")
      except:
          print ("\nNo file by that name, creating new one...")
          self.f = open(fileName, "w+")

      n = self.f.read()
      #return to beginning of the file
      self.f.seek(0)

      #convert n, a string, to a list seperated by newline char
      self.names = n.split('\n')

      #remove the last element of the list because it is a newline char
      del self.names[len(self.names)-1]

  def __del__(self):
      """ Destructor, cleans stuff up"""

      for i in self.names:
          self.f.write(i + '\n')

      self.f.close()

  def printNames(self):
      """ Prints the contents of the list of names """
      print("\nUsernames:")
      for i in self.names:
          print(i)

  def addName(self, newName):
      """ Checks the list for the given username,
      then adds it if it's not there or spits out message
      saying it already there """
      for i in self.names:
          if newName == i:
              print ("\nAlready on the list")
              break
      else:
          self.names.append(newName)
          print("Username added!")

#needs a remove user function?

"""
#print("Hi, im here!")
myMan = UserManager("usernames.txt")
myMan.printNames()
myMan.addName("girlzy")
myMan.printNames()
"""

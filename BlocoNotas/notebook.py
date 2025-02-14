import random
class Notebook:
    def __init__(self):
        self.__notes = list()

    def storeNote(self, note):
        self.__notes.append(note)
    
    def numberOfNotes(self):
        return len(self.__notes)
    
    def showNote(self, noteNumber):
        if noteNumber < 0 :
            print("Este nao e um numero de nota valido")
        elif noteNumber < self.numberOfNotes():
            print(self.__notes[noteNumber])
        else:
            print("Esse nao e um numero de nota valido")
    
    def removeNota(self, note):
        if note in self.__notes:
            self.__notes.remove(note)
        else:
            print("Essa nao e uma nota valida")

    def listNotes(self):
        index = 0 
        while index < self.numberOfNotes() :
            print(self.__notes[index])
            index += 1

    def listNotesFor(self):
        for index in range(self.numberOfNotes()):
            print(self.__notes[index])

    def hasNotes(self): 

        if len(self.__notes) == 0:
            return False
        else: 
            return True

    def compareNote(self, note):
        if note in self.__notes:
            return True
        else:
            return False
        
    def showNoteRandom(self):
        numeroAleatorio = random.randint(1, self.numberOfNotes())
        print(self.__notes[numeroAleatorio])

    def showMultiNoteRandom(self, number):
        contador = 0
        while contador < number and self.__notes:
            random_note = random.choice(self.__notes)
            print(random_note)
            contador += 1
    
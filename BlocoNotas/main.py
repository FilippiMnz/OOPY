from notebook import Notebook

noteTeste = Notebook()

noteTeste.storeNote("Open")
noteTeste.storeNote("Professor")
noteTeste.storeNote("Rato")
print(noteTeste.numberOfNotes())
print("       ")
print("insira sua nota:")
noteTeste.storeNote(input())
print("       ")
print("numero de notas atualizadas")
print(noteTeste.numberOfNotes())
print("       ")
print("teste escolha nota")
noteTeste.showNote(int(input()))
print("       ")
print("teste removedor Notas")
noteTeste.removeNota(input())
print("       ")
print("teste Numero de notas")
print(noteTeste.numberOfNotes())
print("       ")
print("teste Listagem:")
noteTeste.listNotes()
print("       ")
print("Teste Listagem com For:")
noteTeste.listNotesFor()
print("       ")
print("Teste se há notas")
print(noteTeste.hasNotes())
print("       ")

print("Teste existencia")
print(noteTeste.compareNote(input()))
print("       ")

print("teste Aleatorio")
noteTeste.showNoteRandom()
print("       ")

print("Teste Multi")
noteTeste.showMultiNoteRandom(int(input()))
print("       ")

testeVazio = Notebook()


print("testeVazio")
print(testeVazio.hasNotes())
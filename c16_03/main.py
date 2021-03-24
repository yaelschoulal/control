note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]
print(notes)

#Question 4.A
liste = [elem[-1] for elem in notes ] 
print(liste)

somme = 0
for i in liste :
   somme = somme + i
  
moyenne = somme / len(liste) 
print(moyenne)

#Question 4.B

notes_elv1 = [note for note in notes if note[0] == 'eleve1']

print(notes_elv1)

print(sum(note[2] for note in notes_elv1)/len(notes_elv1))


notes_elv1_math = [n for n in notes_elv1 if n[1] == 'math']

print(sum(n[2] for n in notes_elv1_math)/len(notes_elv1_math))

#Question 4.c
eleve = [elem[0] for elem in notes ] 
print(eleve)

matiere = [elem[1] for elem in notes ] 
print(matiere)

class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur
 

  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)

  def __str__(self):
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeur}')"



onote = Note('eleve2', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

onote2 = Note('eleve2', 'maths', 14)
print(onote2.eleve)
print(onote2.matiere)
print(onote2.valeur)
Note.afficher(onote2)


onote3= Note('eleve1','physique',15)
print(onote3.eleve)
print(onote3.matiere)
print(onote3.valeur)
Note.afficher(onote3)

onote4= Note('eleve1','eco',12)
print(onote4.eleve)
print(onote4.matiere)
print(onote4.valeur)
Note.afficher(onote4)

onote4bis= Note('eleve1','eco',13)
print(onote4bis.eleve)
print(onote4bis.matiere)
print(onote4bis.valeur)
Note.afficher(onote4bis)

onote5= Note('eleve1','maths',13)
print(onote5.eleve)
print(onote5.matiere)
print(onote5.valeur)
Note.afficher(onote5)

onote5bis= Note('eleve1','maths',13)
print(onote5bis.eleve)
print(onote5bis.matiere)
print(onote5bis.valeur)
Note.afficher(onote5bis)

onote5bis2= Note('eleve1','maths',12)
print(onote5bis2.eleve)
print(onote5bis2.matiere)
print(onote5bis2.valeur)
Note.afficher(onote5bis2)

def moyenne_tuple(notes, eleve=None, matiere=None):
    
    notes_elv = [note for note in notes if note[0] == eleve] if eleve is not None else notes
    notes_elv_matiere = [n for n in notes_elv if n[1] == matiere] if matiere is not None else notes_elv
    return sum([n[2] for n in notes_elv_matiere])/len(notes_elv_matiere)

print(moyenne_tuple(notes, 'eleve1', 'math'))
print(moyenne_tuple(notes, 'eleve1', 'eco'))
print(moyenne_tuple(notes, 'eleve2', 'math'))
print(moyenne_tuple(notes, 'eleve1', 'physique'))

#Question 5:
liste = [elem[-1] for elem in notes ] 
print(liste)

onotes = [Note(*note) for note in notes]

#Question 6 :
def __str__ (self):
  return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeur}')"



class Node:
    def __init__(self, content: str):
        self.content = content
        self.next = None 


class LinkedList:
    SIZE = 0
    #Inicializador
    def __init__(self):
        self.first = None
     
    #Funcao para insercao de um novo elemento   
    def insert(self, content: str):
        if self.first == None:
            self.first = Node(content)
            self.SIZE += 1
            return
        copyFirst = self.first
        while(copyFirst.next != None):
           copyFirst = copyFirst.next
        copyFirst.next = Node(content)
        self.SIZE += 1

     
    #Funcao para impressao de todos os elementos da lista
    def printList(self):  
        copyFirst = self.first
        while (copyFirst != None):
            print(copyFirst.content)
            copyFirst = copyFirst.next
        
    #Funcao que retorna verdadeiro ou falso para lista vazia ou Funcao
    def isEmpty(self):
       if self.SIZE == 0 :
           return True
       else :
           return False
            
        
    
    #Funcao que retorna o numero de elementos da lista
    def size(self):
     print(self.SIZE)



list = LinkedList()
print(list.SIZE)
list.insert("Pêra")
print(list.SIZE)
list.insert("Maça")
print(list.SIZE)
list.insert("Pêssego")
print(list.SIZE)
list.insert("Goiaba")
print(list.SIZE)
list.insert("Banana")
list.printList()
print(list.isEmpty())
print(list.SIZE)

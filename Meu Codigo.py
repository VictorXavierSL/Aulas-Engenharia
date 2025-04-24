class node:
   def __init__(self , content: str):
      self.content = content 
      self.next = None


class ListLink: 
   SIZE = 0
   def __init__(self):                     #esta função indica o primeiro objeto da lista e o unico que ficara com uma variavel de referencia
        self.first = None

   def insert(self, content: str):
       if self.first == None:              #verifica se não a elementos no arrey
          self.first = node(content)       #coloca a variavel self.first para apontar para o primeiro valor da listra e adiciona o content nesse local 
          self.SIZE += 1 
          return
       
       copyfirst = self.first
       while copyfirst.next != None:
           copyfirst = copyfirst.next 
       copyfirst.next = node(content)
       self.SIZE += 1  
   
   def printlist(self): 
       copyfirst = self.first              # pegar o valor do primeiro iten
       while copyfirst.content != None :   #enquanto meu content não estiver vazio printar
           print(copyfirst.content )        #printar valor do content
           if copyfirst.next == None:      #o valor do meu .next e vaziu ?
               break                       # se for parar de printar
           copyfirst = copyfirst.next      #se  não pegar o valor do priximo objeto e continuar a printar 
   
   def isEmpyt(self): 
       if self.SIZE == 0:
        return True
       else :
           return False
   
   def size(self):
       return self.SIZE
   
   def remuvelement(self , elemet):
        copyfirst = self.first         #recebe valor do primeiro

        if elemet == 0:                # se o indici a ser removido for o primeiro self.first ira apontar pro valor de self.first.next
          self.first = self.first.next
          self.SIZE -= 1
          return  
        
    
        for itens in range(elemet -1): # anda com o copyfirt ate o indice anterior ao idice que sera removido
            copyfirst = copyfirst.next
        antelement = copyfirst         #salva a variavel do item anterior ao que sera removido

        if self.SIZE == elemet +1: #se o indice que sera removido for o ultimo (SIZE == element) antelement.netx sera None
            antelement.next = None
            self.SIZE -= 1
            return

        for itens in range(2):         #percorre ate o proximo valor depois do indice a ser removido
            copyfirst = copyfirst.next

        antelement.next = copyfirst #se o valor do copyfirst.next não for None , a variavel .next do anteriro deve apontar para o objeto seguinte do indice a ser removido
        self.SIZE -= 1

lista = ListLink()
lista.insert("casa")  
lista.insert("carro")        
lista.insert("pessoa")    
lista.insert("cachorro")        
lista.insert("drogas")    
lista.printlist()
print()
lista.remuvelement(3)
lista.printlist()
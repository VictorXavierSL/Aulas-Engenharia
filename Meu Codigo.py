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
        return

   def remuve(self):
     if self.isEmpyt() == True: 
         print("lsita esta Vazia")
         return 
     copyfirst = self.first
     for itens in range(self.size() - 2):         # O laço de repetição precisa ser menos 2 pos diferente do anterior esse se baseioa mno indice do size
            copyfirst = copyfirst.next            # então inicia do 1 e não do 0 
                                              #recebe valor do primeiro
     returnforusse = copyfirst.next 
     copyfirst.next = None
     return returnforusse

   def addinlista(self , content , Id_locate):
        copyfirst = self.first
        
        if Id_locate == 1:                
            self.first = node(content)
            self.first.next = copyfirst
            return
        
        for itens in range(Id_locate -2): # anda com o copyfirt ate o indice anterior ao idice 
            copyfirst = copyfirst.next
        
        antelement = copyfirst
        
        if Id_locate == self.size():
            
            for itens in range(1):         #percorre ate o proximo valor depois do indice 
             copyfirst = copyfirst.next
            antelement.next = node(content)
            antelement.next.next = copyfirst
            self.SIZE += 1
            return        
        
        for itens in range(2):         #percorre ate o proximo valor depois do indice 
            copyfirst = copyfirst.next
        antelement.next = node(content)
        antelement.next.next = copyfirst
        self.SIZE += 1
        return    
       


lista = ListLink()
lista.insert("casa")  
lista.insert("carro")        
lista.insert("pessoa")    
lista.insert("cachorro")        
lista.insert("drogas")    
lista.addinlista("git" , 5)
#print(lista.remuve())
#lista.remuvelement(3)
lista.printlist()

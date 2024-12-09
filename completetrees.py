# completetrees.py

class Node():
    def __init__(self, data, left = None, right = None,height = None):
        # Classe à compléter d'après les questions de la partie 1
        self.data = data
        if not (isinstance(left,Node) or left is None):
            raise ValueError("Left argument is not a node.")
        self.left=left
        if not (isinstance(right,Node) or right is None):
            raise ValueError("Right argument is not a node.")
        self.right = right
        #Partie 1 : Question 1
        if(self.left ==None and self.right==None):
            self.height = 0
        elif(self.left ==None or self.right ==None):
            raise ValueError("Subtrees should have the same height.")
        elif(self.left.height != self.right.height):
            raise ValueError("Subtrees should have the same height.")
        else:
            self.height = 1 + self.left.height


        
    #Partie 1 : Question 2
    def to_list(self):
        l1 = []
        l1.append(self.data)
        if(self.left !=None):
            l1 += self.left.to_list()
        else:
            pass
        if(self.right !=None):
            l1 += self.right.to_list()
        else:
            pass
        return l1
    
    #Partie 1 : Question 3
    def __contains__(self,item):
        if(item == self.data):
            return True
        if(self.left !=None): #Car c'est un arbre binaire donc une condi
            return self.left.__contains__(item) or self.right.__contains__(item)
        return False
       
    #Partie 1 : Question 4
    def __len__(self):
       return 2**(self.height+1) - 1
    
    #Partie 1 : Question 5
    def __getitem__(self, key):
        if(key==0):
            return self.data
        elif(key<0 or key > self.__len__()):
            raise ValueError("IndexError")
        else:
           left_len = self.left.__len__() if self.left else 0
           if key < left_len:  # If the key is in the left subtree
                if (self.left !=None):
                    return self.left.__getitem__(key - 1)
                else:
                    raise IndexError("Invalid access to left subtree")
           else:  # If the key is in the right subtree
                right_key = key - left_len - 1
                if (self.right != None):
                    return self.right.__getitem__(right_key)
                else:
                    raise IndexError("Invalid access to right subtree")
     
   
if __name__ == "__main__":
   a1 = Node(92)
   a2 = Node(34, Node(23), Node(11))
   a3 = Node(28,
              Node(40, Node(33), Node(12)),
              Node(27, Node(7), Node(55)))
   
   #---------Test-Partie1 : Question 2------------------------
   print(a1.to_list())
   print(a2.to_list())
   print(a3.to_list())
   #----------------------------------------------------------
  
  #---------Test-Partie1 : Question 3------------------------
   assert(1 not in a2)
  #----------------------------------------------------------

   #---------Test-Partie1 : Question 4------------------------
   print(a1.__len__())
   print(a2.__len__())
   print(a3.__len__())
   #----------------------------------------------------------

   #---------Test-Partie1 : Question 5------------------------
   print(a1.__getitem__(0))
   print(a3.__getitem__(1))
   #----------------------------------------------------------


   print("Tous les tests se sont bien passés")






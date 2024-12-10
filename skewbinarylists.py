# skewbinarylists.py
from completetrees import Node

class SkewBinaryList():
    def __init__(self, hd = None, tl = None):
        self.head = hd #Node
        self.next = tl #SkewBinaryList
        #Question 6:
        if not (isinstance(hd,Node) or hd is None):
            raise ValueError("Error Attribute")
        if not (isinstance(tl,SkewBinaryList) or tl is None):
            raise ValueError("Error Attribute")
    #Question 7:
    def cons(self, item):
        pass
           

          
           
     
    #Question 8:
    def to_list(self):
        l1 = []
        #-------Premier Arbre Binaire Etiqueté------
        if(self.head.data == None):
            return l1
        else:
            l1.append(self.head.data)
            if(self.head.left != None):
                l1 += self.head.left.to_list()
            if(self.head.right != None):
                l1 += self.head.right.to_list()
        #---------------------------------------------
        #-------Autres Arbres Binaire Etiqueté-------
        current = self
        while(current.next != None):
            if(current.next.head.data == None):
                return l1
            else:
                l1.append(current.next.head.data)
                if(current.next.head.left != None):
                    l1 += current.next.head.left.to_list()
                if(current.next.head.right != None):
                    l1 += current.next.head.right.to_list()
                current = current.next
        #----------------------------------------------
        return l1

    #Question 9:
    def __contains__(self,item):
        #-------Premier Arbre Binaire Etiqueté------
        if(self.head.data == item):
            return True
        if(self.head.left !=None): 
            left_tree = self.head.left.__contains__(item)
            right_tree = self.head.right.__contains__(item)
        if(left_tree or right_tree == True):
            return True
        #---------------------------------------------
        #-------Autres Arbres Binaire Etiqueté-------
        current = self
        while(current.next != None):
            if(current.next.head.data == item):
                return True
            if(current.next.head.left != None):
                tmp1 = current.next.head.left.__contains__(item)
                tmp2 = current.next.head.right.__contains__(item)
            if(tmp1 or tmp2 == True):
                return True
            else:
                current = current.next
        #----------------------------------------------
        return False
    
    #Question 10:
    def __len__(self):
        #-------Premier Arbre Binaire Etiqueté------
        left_len = len(self.head.left) if self.head.left else 0
        right_len = len(self.head.right) if self.head.right else 0
        #---------------------------------------------
        #-------Autres Arbres Binaire Etiqueté-------
        current = self
        k=1
        while(current.next != None):
            left_len +=  len(current.next.head.left) if current.next.head.left else 0
            right_len += len(current.next.head.right) if current.next.head.right else 0
            current = current.next
            k+=1
        #----------------------------------------------
        return k+left_len + right_len
    
    #Question 11:
    def __getitem__(self, key):
        #-------Premier Arbre Binaire Etiqueté------
        if key < 0 or key >= len(self):   # Step 1: Validate index bounds globally
            raise IndexError("skew binary list index out of range")
        if key == 0: # Step 2: Handle the local head
            return self.head.data  
        if self.next is None or (self.next is not None and key < len(self.head)):
            # Traverse within the current head tree
            left_len = len(self.head.left) if self.head.left else 0
            if key - 1 < left_len:  # Traverse the left subtree
                return self.head.left[key - 1]  # Adjusted key
            
            right_key = key - left_len - 1 # Traverse the right subtree
            if self.head.right and right_key >= 0:
                return self.head.right[right_key]
        #---------------------------------------------
        #-------Autres Arbres Binaire Etiqueté-------
        current = self
        while current.next is not None:
            # Adjust the key to account for the length of the current head
            key -= len(current.head)
            if key == 0:
                return current.next.head.data  # Found in the next head
            # Recalculate left subtree length
            left_len = len(current.next.head.left) if current.next.head.left else 0

            # Traverse the left subtree of next.head
            if key - 1 < left_len:
                return current.next.head.left[key - 1]

            # Traverse the right subtree of next.head
            right_key = key - left_len - 1
            if current.next.head.right and right_key >= 0:
                return current.next.head.right[right_key]
            current = current.next # Move to the next node
            #----------------------------------------------

        # If no valid index is found
        raise IndexError(f"Index {key} out of bounds in the right subtree")
     

if __name__ == "__main__":
    a1 = Node(113)
    a2 = Node(1, Node(2), Node(3))
    a3 = Node(4, Node(5), Node(6))
    a4 = Node(7, Node(8), Node(9))
    a5 = Node(10, Node(11), Node(12))
    a6 = Node(13, Node(14), Node(15))
    a7 = Node(28,
              Node(40, Node(33), Node(12)),
              Node(27, Node(7), Node(55)))
    mylist1 = SkewBinaryList(a2,SkewBinaryList(a3,None))
    mylist2 = SkewBinaryList(a2, SkewBinaryList(a3,SkewBinaryList(a4,SkewBinaryList(a5,None))))
    mylist3 = SkewBinaryList(a2, SkewBinaryList(a3,SkewBinaryList(a4,SkewBinaryList(a5,SkewBinaryList(a6,None)))))
    mylist4 = SkewBinaryList(a7,mylist3)
    print(mylist2.to_list())
    print(mylist2.__contains__(7))
    print(mylist1.__len__())
    print(mylist1.__getitem__(0))
    print(mylist1.cons(0))
    
    print("Exécution terminée")
   

#Counting of nodes starts from zero. head node is given position 0.
"""
Class Double_ll:
    1.length() - returns the length of the linkdlist
    2.printList()-prints the data in the linked list
    3.append(new_data, direction)- adds a node at the end of the list if direction is 'l' or 'L'(Equivalent to push). If direction is 'r' or 'R', adds a node at the head. Default value of direction is 'l'.
    4.reverse_ll() - returns a new doublelinkedlist with data in the reverse order of initial linked list
    5.insert_node(new_data, neighbour_node, direction)-inserts a node with new_data as data in it either before or after the node passed as neighbour_node. Directiopn decides where to insert. set directioon as 'a'/'A' to insert after the node. Set direction as 'b'/'B' to insert before the neighbour_ndoe
    6.insert(new_Data, position, direction) - direction argument is same as that mentioned  in insert_node function. Here a node with new_data as data in it is inserted after or before the 'position'th node dependiing on the direction assigned.
    7.merge_ll(ll1, ll2, new)- merges the linkedlists ll12 with ll1. If new is True returns a new merged linked list(original linked lists are unchanged.). If new is Flase, merges the linkedlists and stores the result in ll1. Default value of new is False
    8.shuffle_merge(ll1, ll2)-Creates a linkedlist by taking one element from ll1, one element from ll2 alternatively. Returns a new linkedlist. Original linkedlists remain unchaned.
    9.sorted_merge(lll1, ll2, order) - Creates a linkedlist in sorted order. Both the lists should be in either ascending order or descending order. If order is set to 'a'/'A' the resultant linked list will be in ascending gorder. If order is set to 'd'/'D', the resultant linked list will be in descending order. Default value of order is 'a'
    10.delete_node(node)- deletes the node that is passed as argument. If node is of 'int' type, the nodeth node will be deleted. If node is of type 'Node', that node will be deleted
    11.access_element(node, n)- access the node that is passed as argument and returns the data in that node if n in None. if n in int, returns the nth element in the node. If node is of thpe int, it access the nodeth node. If node is of type 'Node', it access that particular node
    12.mid_node(address)- returns the data of the middle node if address is set to False. If address is set to True returns tuple of address and data reaspectively. Default value of address is False
    13. find(key) - returns True if the the key is present in any of the Node.data
    14. search(key,element recursion)- returns node number of the first occurence of the key in the form of list if element is False and recursion is False. If recursion is True reurns a list of node positions where key is present in the node. Default value of recursion is False. element can be set to True only when recursion is False
    15.delete_key(key, recursion, element, w_n) - deletes the key. If recursion is false deletes the first occurence of key else deletes all the occurenes of key.
    16.splitList(head, ratio_list)- splits the linkedlist in the ratio passed as argument in ratio_list(it should be a list)
"""


import sys



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
        


class Double_ll:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def length(self):
        if self.head is None and self.tail is None:
            return 0
        if (self.head is not None and self.tail is None):
            temp = self.head
            count = 0
            while(temp):
                count += 1
                temp = temp.next
            return count
        if (self.head is None and self.tail is not None):
            temp = self.tail
            count = 0
            while temp:
                count += 1
                temp = temp.prev
            return count
        if self.head.next== self.tail and self.tail.prev == self.head:
            return 2
        temp = self.head
        temp1 =self.tail
        x = True
        count = 0
        while x is True:
            count += 1
            temp = temp.next
            temp1 = temp1.prev
            if temp == temp1:
                return count*2 + 1
            elif temp.next == temp1 and temp1.prev == temp:
                return (count+1)*2
            
        
    
    def printList(self):
        temp = self.head
        if self.head is None:
            print("The list is empty or has no head node.")
        while temp is not None:
            print(temp.data)
            temp = temp.next
        return
    
    def append(self,new_data, direc = 'r'):
        if self.head is None and self.tail is None:
            new_node = Node(new_data)
            self.head = new_node
            return
        if direc == 'r' or direc == 'R':
            if self.head is not None and self.tail is None:
                new_node = Node(new_data)
                self.tail = new_node
                self.head.next = self.tail
                self.tail.prev = self.head
                return
            new_node = Node(new_data)
            temp = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.prev = temp
            return
        elif direc == 'l' or direc == 'L':
            if self.head is None and self.tail is not None:
                new_node = Node(new_data)
                self.head = new_node
                self.head.next = self.tail
                self.tail.prev = self.head
                return
            elif self.head is not None and self.tail is None:
                new_node = Node(new_data)
                self.tail = self.head
                self.head = new_node
                self.tail.prev = self.head
                self.head.next = self.tail
                return
            new_node = Node(new_data)
            temp = self.head
            self.head.prev = new_node
            self.head = new_node
            self.head.next = temp
            return
        else :
            print("Select either 'l' or 'r'")
            sys.exit(0)
        
    def insert_node(self, new_data, neighbour_node, direc = 'a'):
        
        if neighbour_node == self.head and (direc == 'b' or direc == 'B'):
            self.append(new_data, 'l')
            return
        elif neighbour_node == self.tail and (direc == 'a' or direc == 'A'):
            self.append(new_data, 'r')
            return
        elif neighbour_node is None:
            print("Node not found. Node not inserted")
            sys.exit(0)
        else:
            if direc == 'a' or direc == 'A':
                new_node = Node(new_data)
                new_node.next = neighbour_node.next
                neighbour_node.next = new_node
                new_node.prev = neighbour_node
                return
            elif direc == 'b' or direc == 'B':
                new_node = Node(new_data)
                new_node.prev = neighbour_node.prev
                neighbour_node.prev.next = new_node
                neighbour_node.prev = new_node
                new_node.next = neighbour_node
               
                return
            else:
                print("Choose either 'a'/'A' for after or 'b'/'B' for before the neighbour node")
                sys.exit(0)
#The position count is srtarted from zero. head node is at position 0. tail node is at position length-1 where length is length of the linked list    
    def insert(self, new_data, position = None, direc = 'a'):
        try:
            if position >= 0:
                if position == 0 :
                    self.insert_node(new_data, self.head, direc)
                    return
                else:
                    temp = self.head
                    count = 0
                    pos = position-1
                    while count != pos:
                        temp = temp.next
                        count += 1
                        if temp.next is None:
                            print("The position do not exist. Node cannot be inserted")
                            sys.exit
                
                    self.insert_node(new_data, temp.next, direc)
                    return
            elif position < 0:
                if position == -1:
                    self.insert_node(new_data, self.tail, direc)
                    return
                else:
                    temp = self.tail
                    count = 1
                    pos = abs(position) - 1
                    while count != pos:
                        temp = temp.prev
                        count += 1
                        if temp.prev is None:
                            print("The position do not exist. Node cannot be inserted")
                            sys.exit
                    self.insert_node(new_data, temp.prev, direc)
                    return
        except TypeError:
            print("TypeError occured. Please check the argument 'position'. It should be of 'int' type")
            sys.exit(0)
                
          
    def reverse_ll(self):
        temp = self.head
        d_ll = Double_ll()
        while temp:
            d_ll.append(temp.data,'l')
            temp = temp.next
        return d_ll
    
    def merge_ll(ll1, ll2, new = False):
        try:
            if ll1.head is None and ll2.head is None:
                print("Both the lists are empty")
                sys.exit(0)
            elif ll1.head is None:
                print("ll1 is empty. returning ", ll2)
                return ll2
            elif ll2.head is None:
                print("ll2 is None.Returning ", ll1)
                return ll1
            else:
                if new is False:
                    temp = ll2.tail
                    temp1 = ll1.tail
                    ll1.tail.next = ll2.head
                    ll2.head.prev = temp1
                    ll1.tail = temp
                    return ll1
                elif new is True:
                    d_ll = Double_ll()
                    temp = ll1.head
                    
                    while temp:
                        d_ll.append(temp.data)
                        temp = temp.next
                    var = ll2.tail
                    var1 = d_ll.tail
                    d_ll.tail.next = ll2.head
                    ll2.head.prev = var1
                    d_ll.tail = var
                    return d_ll
        except AttributeError:
            print("Check the order of arguments. they should be in the following order: \n linkedlist1 linkedlist2 new")
            sys.exit(0)
        
    def shuffle_merge(ll1, ll2):
        if ll1.head is None and ll2.head is None:
            print("Both the lists are empty.")
            sys.exit(0)
        elif ll2.head is None:
            print(ll2," is empty.")
            return ll1
        elif ll1.head is None:
            print(ll1," is empty.")
            return ll2
        
        else:
            d_ll = Double_ll()
            temp1 = ll1.head
            temp2 = ll2.head
            while temp1 is not None and temp2 is not None:
                d_ll.append(temp1.data)
                d_ll.append(temp2.data)
                temp1 = temp1.next
                temp2 = temp2.next
            if temp1 is None:
                while temp2:
                    d_ll.append(temp2.data)
                    temp2 = temp2.next
                return d_ll
            if temp2 is None:
                while temp1:
                    d_ll.append(temp1.data)
                    temp1 = temp1.next
                return d_ll
            return d_ll
  
    def sorted_merge(ll1, ll2, order = 'a'):
        if ll1.head is None or ll2.head is None:
            print("Either one of the lists or both the lists are empty. Please check the linked lists")
            sys.exit(0)
        if ll1.head.data <= ll1.head.next.data and ll2.head.data <= ll2.head.next.data:
            pre_order = 'a'
        elif ll1.head.data > ll1.head.next.data and ll2.head.data > ll2.head.next.data:
            pre_order = 'd'
        else:
            print("Both the lists should either be in ascending order or descending order. Sorted_merge failed")
            sys.exit(0)
        d_ll = Double_ll()
        if pre_order == 'a' or pre_order == 'A':
            if order =='a' or order == 'A':
                temp1 = ll1.head
                temp2 = ll2.head
                while temp1 is not None and temp2 is not None:
                    if temp1.data <= temp2.data:
                        d_ll.append(temp1.data)
                        temp1 = temp1.next
                    else:
                        d_ll.append(temp2.data)
                        temp2 = temp2.next
                    if temp1 is None:
                        while temp2:
                            d_ll.append(temp2.data)
                            temp2 = temp2.next
                        return d_ll
                    elif temp2 is None:
                        while temp1:
                            d_ll.append(temp1.data)
                            temp1 = temp1.next
                        return d_ll
            elif order == 'd' or order == 'D':
                temp1 = ll1.tail
                temp2 = ll2.tail
                while temp1 is not None and temp2 is not None:
                    if temp1.data >= temp2.data:
                        d_ll.append(temp1.data)
                        temp1 = temp1.prev
                    else:
                        d_ll.append(temp2.data)
                        temp2 = temp2.prev
                    if temp1 is None:
                        while temp2:
                            d_ll.append(temp2.data)
                            temp2 = temp2.prev
                        return d_ll
                    elif temp2 is None:
                        while temp1:
                            d_ll.append(temp1.data)
                            temp1 = temp1.prev
                        return d_ll
            else:
                print("Choose either 'a'/'A' or 'd'/'D'")
                return
            
            
        else:
            if order == 'a' or order == 'A':
                temp1 = ll1.tail
                temp2 = ll2.tail
                while temp1 is not None and temp2 is not None:
                    if temp1.data <= temp2.data:
                        d_ll.append(temp1.data)
                        temp1 = temp1.prev
                    else:
                        d_ll.append(temp2.data)
                        temp2 = temp2.prev
                    if temp1 is None:
                        while temp2:
                            d_ll.append(temp2.data)
                            temp2 = temp2.prev
                        return d_ll
                    elif temp2 is None:
                        while temp1:
                            d_ll.append(temp1.data)
                            temp1 = temp1.prev
                        return d_ll
            elif order == 'd' or order == 'D':
                temp1 = ll1.head
                temp2 = ll2.head
                while temp1 is not None and temp2 is not None:
                    if temp1.data >= temp2.data:
                        d_ll.append(temp1.data)
                        temp1 = temp1.next
                    else:
                        d_ll.append(temp2.data)
                        temp2 = temp2.next
                    if temp1 is None:
                        while(temp2):
                            d_ll.append(temp2.data)
                            temp2 = temp2.next
                        return d_ll
                    elif temp2 is None:
                        while temp1:
                            d_ll.append(temp1.data)
                            temp1 = temp1.next
                        return d_ll
            else:
                print("Choose either 'a'/'A' or 'd'/'D'")
                return
            
    def delete_node(self, node):
        if type(node) == Node:
            if node == self.head:
                temp = self.head.next
                self.head = None
                temp.prev = None
                self.head = temp
                return
        
            elif node == self.tail :
                temp = self.tail.prev
                self.tail = None
                temp.next = None
                self.tail = temp
                return
            
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
                node = None
                return
        elif type(node) == int:
            if node >= 0:
                if node == 0:
                    temp = self.head.next
                    self.head = None
                    temp.prev = None
                    self.head = temp
                    return
                else:
                    count = 1
                    temp = self.head.next
                    while count != node:
                        temp = temp.next
                        if temp is None:
                            print("Cannot find the node")
                            sys.exit(0)
                        count +=1
                    if temp.next is None:
                        temp = self.tail.prev
                        self.tail = None
                        temp.next = None
                        self.tail = temp
                        return
                        
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    temp = None
                    return
            else:
                if node == -1:
                    temp = self.tail.prev
                    self.tail = None
                    temp.next = None
                    self.tail = temp
                    return
                else:
                    count = 2
                    temp = self.tail.prev
                    while count != node:
                        temp = temp.prev
                        if temp is None:
                            print("Cannot find the node")
                            sys.exit(0)
                        count -= 1
                    if temp.prev is None:
                        temp = self.head.next
                        self.head = None
                        temp.prev = None
                        self.head = temp
                        return
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    temp = None
                        
                    return
            
        else:
            print("The argument should be of 'Node' or 'int' type")
            sys.exit(0)
                
                
    
    def access_element(self,node, n= None):
        if type(node) == Node:
            if n is None:
                return node.data
            else:
                try:
                    return node.data[n]
                except TypeError:
                    print("The data is not iterable. Returning the whole data present in the node")
                    return node.data
                except IndexError:
                    print("Index out of range.")
                    sys.exit(0)
                    
        elif type(node) == int:
            if node >= 0:
                count = 0
                temp = self.head
                while count != node:
                    temp = temp.next
                    count += 1
                if n is None:
                    try:
                        return temp.data
                    except AttributeError:
                        print("Cannot find the node. Please check the arguent you have passed. Probably argument passed is greater than the no.of nodes present")
                        sys.exit(0)
                else:
                    try:
                        return temp.data[n]
                    except TypeError:
                        print("The data is not iterable. Returning the whole data present in the node")
                        return temp.data
                    except IndexError:
                        print("Index out of range")
                        sys.exit(0)
                    except AttributeError:
                        print("Cannot find the node. Please check the arguent you have passed. Probably argument passed is greater than the no.of nodes present")
                        sys.exit(0)
            else:
                count = -1
                temp = self.tail
                while count != node:
                    temp = temp.prev
                    count -= 1
                if n is None:
                    try:
                        return temp.data
                    except AttributeError:
                        print("Cannot find the node. Please check the arguent you have passed. Probably argument passed is greater than the no.of nodes present")
                        sys.exit(0)
                        
                else:
                    try:
                        return temp.data[n]
                    except TypeError:
                        print("The data is not iterable. Returning the whole data present in the node")
                        return temp.data
                    except IndexError:
                        print("Index out of range")
                        sys.exit(0)
                    except AttributeError:
                        print("Cannot find the node. Please check the arguent you have passed. Probably argument passed is greater than the no.of nodes present")
                        sys.exit(0)
        else:
            print("The argument should be of 'Node' or 'int' type")
            print(type(node))
            sys.exit(0)
            
    def mid_node(self, address = False):
        if self.head is None and self.tail is None:
            print("The list is empty. Returning None type")
            return
        if self.head is not None and self.tail is None:
            print("The list has no tail/head. Check the linked list and set a node as tail/head node")
            sys.exit(0)
        if self.head.next == self.tail and self.head ==self.tail.prev:
            print("The list has only two nodes.")
            if address is False:
                return self.head.data
            elif address is True:
                return self.head, self.head.data
            else:
                print("Address should be of bool type")
                sys.exit(0)
        
        temp = self.head
        temp1 = self.tail
       
        x = True
        count = 0            
        while x is True:
            count += 1
            temp = temp.next
            temp1 = temp1.prev
            if temp == temp1 :
                x = False
                if temp == temp1:
                    if address is False:
                        return temp.data
                    elif address is True:
                        return temp,temp.data
                    else :
                        print("Address should be of bool type")
                        sys.exit(0)
                    
            elif temp.next == temp1 and temp1.prev == temp:
                if address is False:
                    return temp.data
                elif address is True:
                    return temp, temp.data
                else:
                    print("Address should be of bool type")
                    sys.exit(0)
                
        
    def find(self, key):
        if self.head is None or self.tail is None:
            print("The has no head or tail or both. Cannot traverse through the list. Returning None" )
            return 
        
        
        if key == self.head.data or key == self.tail.data:
            return True
        
        temp = self.head.next
        temp1 = self.tail.prev
        while temp is not None and temp1 is not None:
            if key == temp.data or key == temp1.data:
                return True
            temp = temp.next
            temp1 = temp1.prev
        return False
        
    
    
    
    def search(self, key, element = False, recursion = False):
        if self.head is None or self.tail is None:
            print("The list has no tail nor head nor both. Returning None. ")
            return
        if recursion is False:
            if element is False:
                temp = self.head
           
                count = 0
                while temp :
                    if key == temp.data :
                        return [count]
                    temp = temp.next
                    count = count+1
            elif element is True:
                temp = self.head
                count = 0
                while temp:
                    try:
                        for i, ele in enumerate(temp.data):
                            if key == ele:
                                return [count , i]
                        temp = temp.next
                        count += 1
                    except TypeError:
                        count += 1
                        temp = temp.next
                print("Element cannot be found. Returning None")
                return 
            else:
                print("'element' should be of 'Bool' type")
                sys.exit(0)      
            
        elif recursion is True:
            if self.head.next == self.tail and self.tail.prev == self.head:
                print("The list has only two nodes")
                if element is False:
                    if key == self.head.data and key == self.tail.data:
                    
                        return [0, 1]
                    elif key == self.head.data and key != self.tail.data:
                        return [0]
                    elif  key == self.tail.data:
                        return [1]
                    else:
                        return []
                elif element is True:
                       
                    element_pos = []
                    try:
                        for i, ele in enumerate(self.head.data):
                            if key == ele:
                                element_pos.append((0, i))
                    except TypeError:
                        if key == self.head.data:
                            element_pos.append((0, 'NA'))
                                    
                    try:
                        for i,ele in enumerate(self.tail.data):
                            if key == ele:
                                element_pos.append((1, i))
                    except TypeError:
                        if key == ele:
                            element_pos.append((1, 'NA'))
                    return element_pos
                        
                        
                
            if element is False:
                
                temp = self.head
                temp1 = self.tail
                count_list = []
                count_list_rev = []
                count = 0
                count1 = -1
                x = True
                while x is True and temp is not None and temp1 is not None:
                    if key == temp.data:
                        count_list.append(count)
                    if key == temp1.data:
                        count_list_rev.append(count1)
                    count += 1
                    count1 -= 1
                    temp = temp.next
                    temp1 = temp1.prev
                    if temp == temp1 :
                        x = False
                        if temp.data == key:
                            count_list.append(count)
                        return count_list+sorted([count*2+1+x for x in count_list_rev])
                    elif temp.next == temp1 and temp1.prev == temp:
                        x = False
                        if temp1.data == key:
                            count_list.append(count+1)
                        return count_list+sorted([(count+1)*2+x for x in count_list_rev])
            elif element is True:
                    print("This operation is currently unsupported. Please set elemetn to True when recursion is set to True")
                    sys.exit(0)
            else :
                print("element should be of 'Bool' type")
                sys.exit(0)
                    
        else :
            print("'Recursion should be of 'Bool' type")
            sys.exit(0)
                    
    def delete_key(self,key, recursion = False, element = False, w_n = False):
        if self.head is None and self.tail is None:
            print("The list is empty.")
            return
        if self.head is None or self.tail is None:
            print("The lnked list is missing either head node or tail node or both. Please check")
            sys.exit(0)
        if recursion is False:
            if element is False:
                temp = self.head
                while temp:
                    if key== temp.data:
                        self.delete_node(temp)
                        return
                    temp = temp.next
            elif element is True:
                temp = self.head
                while temp:
                    try:
                        for i, elem in enumerate(temp.data):
                            if key == elem:
                                if w_n is True:
                                    self.delete_node(temp)
                                    return
                                elif w_n is False:
                                    #del temp.data[i]
                                    print("This function is not supported. 'w_n' must be True")
                                    return
                                else:
                                    print("'w_n' should be of 'Bool' type")
                                    sys.exit(0)
                                
                    except TypeError:
                        if temp.data == key:
                            self.delete_node(temp)
                            return
                    
                    temp = temp.next
                
            else :
                print("'element' should be of type 'Bool'")
                sys.exit(0)
            
    def splitList(self,head, ratio_list):
        if self.head is None or self.tail is None:
            print("The linked list has either no head or no tail or both")
            return
        if self.head.next.next is None:
            print("The list has only two nodes.")
            return [self.head, self.tail]
        length_of_list = self.length()
        if len(ratio_list) != 2:
            print("The length of the ratio list should be equal to 2")
            sys.exit(0)
        total = sum(ratio_list)
        sub_ll_a = Double_ll()
        sub_ll_b = Double_ll()
        a = round(length_of_list/total*ratio_list[0])
        temp = self.head
        for i in range(a):
            sub_ll_a.append(temp.data)
            temp = temp.next
        #b = length_of_list - a
        while temp is not None:
            sub_ll_b.append(temp.data)
            temp = temp.next
        return [sub_ll_a, sub_ll_b]
    
    
    
            
            
        
        
        
                   
                
            
            
                    
                    
        
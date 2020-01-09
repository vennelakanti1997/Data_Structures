# -*- coding: utf-8 -*-
#source : http://cslibrary.stanford.edu/105/LinkedListProblems.pdf
#source : https://www.geeksforgeeks.org/merge-sort-for-linked-list/
#source : https://www.geeksforgeeks.org/merge-sort-for-linked-list/



#The numbering of nodes starts from Zero
""""
List of fucntions-

class LinkedList()-

1.length() - to get the length of the linked list
2.printList() - To print the list of the linked list
3.push(new_data) - adds a node with data 'new_data' at the starting of the linked list
4.append(new_data) - adds a node at the end of the linked list with 'new_data' as data in it
5.insert(new_data, position = None, neighbour_node = None) - inserts a node with 'new_data' as data after the positionth node or 
                                                             after the neighbour_node. Both position and 
                                                             neighbour_node should not be mentioned
6.accessing_elements_in_a_node(node_number, n)-  if only node_number is passed it returns the data in that particular node
                                               if n is also mentioned, it returns the nth element of the data present in the
                                                node_numberth node(if the data is iterable else returns the whole data present at the node).

7.search_all(key, recursion = False)- it searches for the first occurence of the key in the data in the linkedlist and returns the nide number
                                    if recursion is set to True it returns the list of node numbers where the data is present

8.search_element(element, length = None) - searches for a particular element in the iterable data in a a node.

9.find(key) - returns True if the element is present in the list. else return False
10.mid_Node(head)- gives the mid node when the head node of the linked list is passed as argument
11.merge_ll(ll1, ll2)- merges two linked lists ll1, ll2 and stores the result in ll1. Changes the original ll1.
12.merge_new_ll(ll1, ll2)- merges the linkedlists ll1, ll2 and stores the result in a new linkedlist. Takes more time than merge_ll() but ll1, ll2 remain uncghanged.
13.sortedMerge(head1, head2, pre_order, order) - head1, head2 are the head nodes of the linked lists that are already sorted.
     (iterative method)                                               pre_order - order of linked lists. if ll1, ll2 are in ascending order-'a' / 'A'
                                                                                       if ll1, ll2 are in descending order- 'd' / 'D'
                                                    order - the order of the return type linkedlist. 'a'/ 'A' for ascending order. 'd' / 'D' for descending order
                                                    The default values for pre_order and order are 'a'
                                Note: both ll1, ll2 musth either be in ascending order or desccenting order. i.e., they must be in same kind of order
            
14.pop()- deletes the head node and returns the data of the present in the head node
15.deleteAfter(neighbour_node)- deletes the node that is present after the node passed in the argument
16.delete(key, recursion)- If recursion is set to false deletes the first occurence of the key. 
                           If recursion is set to True, deletes all the occurences of the key in the linked list.
                           Default value of recursion is False.

17.splitListRatio(head, ratioList)- splits the linkedlist into two lists of ratio specified in the argument ratioList(List datatype with only two elements in it)
                                    Note: For now it can only divide the linkedlist into two parts of given ratio
                           
18.shufflemerge(ll1, ll2)- Creates a linkedlist by taking one element from ll1, one element from ll2 alternatively.
 returns a new linkedlist. Original linkedlists remain unchaned.
 
 
 class LinkedList_sorting :
     mergeSort(head) - sorts the linkedlist data in ascending order.
Note : Recursion is used. may eatup the stack.                      
"""

import numpy
import cmath

class Node:

    def __init__(self, data):
       # for position in data:
        self.data = data
       #pointer to next node
        self.next = None


class LinkedList:

    def __init__(self):
       #Root node
        self.head = None


#length of linked list(No.of nodes) We iterate through every node and count the number of nodes
    def length(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count


#print the whole linked list. iterate through every node and print data at every node
    def printList(self):
        temp = self.head
        if self.head is None:
            print("The list is empty")
            return
        while(temp):
            print(temp.data)
            temp = temp.next

#Add node at the starting of linkedlist
    def push(self, new_data):
        #Assigning data into a new node
        new_node = Node(new_data)
        
        #pointer in the new node is pointing to the existing root node
        new_node.next = self.head
        #new_node is assigned to head. Hence new_node has become the root node
        self.head = new_node

#Add node at the end of linked list
    def append(self, new_data):
        #Assigning data into a new node
        new_node = Node(new_data)
 
        #if list is empty return the new_node
        if self.head is None:
            self.head = new_node
            return 

        
        last  = self.head
        #Travel to the last node
        while(last.next):
            last = last.next
        #Assign the new node to the pointer of the last node
        last.next = new_node

  
#Insert a node after the node you want
    def insertAfter(self, neighbour_node, new_data):
        if neighbour_node is None:
            print("The given previous node does not exist")
            return

        #Assigning data into a new node
        new_node = Node(new_data)
        
        #As the new node is being inserted after the neighbour_node, the pointer in the neighbour_node is transferred into the pointer of the new_node. and the negihbour_node points to the new node
        new_node.next = neighbour_node.next
        neighbour_node.next = new_node
    

    #The node are numbered from zero. The following function creates a node after the (position)th node. If position = -1, the below function is equivalent to push. if position is equal to length of linkekdlist, the below function is equivalent to append
    def insert(self, new_data, position = None, neighbour_node = None):
        if (self.head is None):
            self.head = Node(new_data)
            print("The list is empty and the element is added to it. The length of list is 1")
            return
        if position is not None and neighbour_node is not None:
            print("Both Position and neighbour_node are mentioned. Make either of them as None")
            return 
        
        if position == None and neighbour_node != None:
            self.insertAfter(neighbour_node, new_data)
        if ( position is not None and position < 0):
            self.insert(new_data, self.length())
        #count = 0
        temp = self.head
        self.new_data= new_data
        
        if position == -1:
            self.push(self.new_data)
            return
       
        if position is not None:
            for i in range(0, position):
            #count += 1
            #print(count, temp.data)
                temp = temp.next
                if temp is None:
                    print("Index out of range.")
                    return
            self.insertAfter(temp, self.new_data)
                    


#This only works if the data at a node is a list or a string. where n is the element you want to access. it access (n-1)th position. Default value of n is i1(imaginary number). If no value is assigned to n while calling the function, the function returns the whole data present at the node.
    def accessing_elements_in_a_node(self, node_number, n = complex(1)):
        temp = self.head
        if self.head is None:
            print("The list is empty")
            return
        try:
            if n == complex(1):
                for i in range (node_number):
                    temp = temp.next
                return temp.data
        
            for i in range(0, node_number):
                temp = temp.next
            return temp.data[n]
 
        except TypeError:
            print("The data is not iterable. Returning the whole data present in the node")
            return temp.data

        except AttributeError:
            print("Index out of range. The length of the linked list is:")
            return self.length()

        except IndexError:
            print("IndexError:", type(temp.data), "Index out of range")
            return 


    def search(self, key):
        if self.head is None:
            print("The list is empty. Cannot find element")
            return
        count = 0
        temp = self.head
        while(temp):
            if(temp.data == key):
                #print("Key found at", count,"th node")
                return (count)
            count += 1
            temp = temp.next
        print("Element not found")
        return
        
 #Nodes are numbered from zero. By default this function gives the first occurence of the key. If recursion is set to True it returns the list of positions of the key
    def search_all(self, key, recursion = False):
        if self.head is None:
            print("The list is empty. Cannot find element")
            return
        if recursion == False:
            element = self.search(key)
            return element
        count_list = []
        count = 0
        temp = self.head
        #temp1 = self.tail
        while(temp):
            if(temp.data == key):
                count_list.append(count)
            count +=1
            temp = temp.next
                
        if (numpy.array(count_list)).size:
            return count_list
        else:
            print("Element not found")
            return 
        
#This returns the bool type and prints the first occurence of the key
    def find(self, key, return_type = False):
        if self.head is None:
            print("The list is empty.")
            return False
        count = 0
        temp = self.head
        while(temp):
            if (temp.data == key):
                if return_type == False:
                    return True
                return True, count
            count += 1
            temp = temp.next
        return False
    
#Searches a particular element in the data of each node and gives a list of tuples whose format is [(node_number, position_of_element_in_the data_At_the_node)]. If the data at a node is not iterable it checks if the data is equal to the elemment and position_of_element_in_the data_At_the_node will be 'NA'
    def search_element(self, element, length = None):
        if self.head is None:
            print("The list is empty. Cannot find element")
            return 
        if length is None:
            length = self.length()
        mapped_list = []
        node_number = []
        element_pos = []
        temp = self.head
        while(temp):
            for i in range(length):
                try:
                    for j in range(len(temp.data)):
                        if (temp.data[j] == element):
                            node_number.append(i)
                            element_pos.append(j)
                            
                    temp = temp.next
                except TypeError:
                    if (temp.data == element):
                        node_number.append(i)
                        element_pos.append('NA')
                    temp = temp.next
        mapped_list = list(zip(node_number, element_pos))
        return mapped_list

#Gives (n/2) if no. of nodes is even else gives (n+1/2)th node. Should give the head node as argument. returns a list of address of node and data respectively
    def mid_Node(self, head): 
        if (head == None): 
            return head 
  
        slow = head 
        fast = head 
        count = 0
        while (fast.next != None and 
               fast.next.next != None): 
            slow = slow.next
            fast = fast.next.next
            count += 1
        #print(count*2, self.length())
        return slow

#merges ll1, ll2 and the result will be stored in ll1. Approx.Time taken is O(length(ll2)). This changes the original linkedlist. 
    def merge_ll(self, ll1, ll2):
        if ll1.head is None:
            return ll2

        elif ll2.head is None:
            return ll1

        else:
            temp = ll2.head
            while(temp):
                ll1.append(temp.data)
                temp = temp.next
            return ll1, ll1.length()

#Merges ll1 and ll2 and the result will be stored in a new linkedlist. Approx.Time taken is O(length(ll1)+length(ll2))
    def merge_new_ll(self, ll1, ll2):
        
        if ll1.head is None:
            return ll2

        elif ll2.head is None:
            return ll1

        else:
            ll = LinkedList()
            temp = ll2.head
            temp1 = ll1.head
            while(temp1):
                ll.append(temp.data)
                temp1 = temp1.next
            while(temp):
                ll.append(temp.data)
                temp = temp.next
            return ll, ll.length()
           
    def sortedMerge(self, head1, head2, pre_order = 'a', order = 'a'):
        ll = LinkedList()
        if head1 is None :
            return head2
        elif head2 is None :
            return head1
        else :
            temp1 = head1
            temp2 = head2
            
            if pre_order == 'a' or pre_order == 'A':
           
                if order == 'a' or order == 'A':
                    while temp1 is not None and temp2 is not None:
                
                        if temp1.data <= temp2.data:
                            ll.append(temp1.data)
                            temp1 = temp1.next
                        else :
                            ll.append(temp2.data)
                            temp2 = temp2.next

                    if temp1 is None:
                        while temp2 is not None:
                            ll.append(temp2.data)
                            temp2 = temp2.next
                    elif temp2 is None:
                        while temp1 is not None:
                            ll.append(temp1.data)
                            temp1 = temp1.next
                    return ll
                elif order == 'd' or order =='D':
                    while temp1 is not None and temp2 is not None:
                
                        if temp1.data <= temp2.data:
                            ll.push(temp1.data)
                            temp1 = temp1.next
                        else :
                            ll.push(temp2.data)
                            temp2 = temp2.next

                    if temp1 is None:
                        while temp2 is not None:
                            ll.push(temp2.data)
                            temp2 = temp2.next
                    elif temp2 is None:
                        while temp1 is not None:
                            ll.push(temp1.data)
                            temp1 = temp1.next
                    return ll
           
                else:
                    print("Choose either ascending 'a' or descending 'd' order")
                    return
            elif pre_order == 'd' or pre_order == 'D':
                if order == 'd' or order == 'D':
                    while temp1 is not None and temp2 is not None:
                        if temp1.data >= temp2.data:
                            ll.append(temp1.data)
                            temp1 = temp1.next
                        else:
                            ll.append(temp2.data)
                            temp2 = temp2.next
                            
                    if temp1 is None:
                        while temp2 is not None:
                            ll.append(temp2.data)
                            temp2 = temp2.next
                    elif temp2 is None:
                        while temp1 is not None:
                            ll.append(temp1.data)
                            temp1 = temp1.next
                    return ll
                elif order == 'a' or order == 'A':
                    while temp1 is not None and temp2 is not None:
                        if temp1.data >= temp2.data:
                            ll.push(temp1.data)
                            temp1 = temp1.next
                        else:
                            ll.push(temp2.data)
                            temp2 = temp2.next
                            
                    if temp1 is None:
                        while temp2 is not None:
                            ll.push(temp2.data)
                            temp2 = temp2.next
                    if temp2 is None:
                        while temp1 is not None:
                            ll.push(temp1.data)
                            temp1 = temp1.next
                    return ll
                else:
                    print("Choose either ascending 'a' or descending 'd' order")
                    return
            else:
                print("Mention the sorted order of the linked lists i.e., Either ascending order ('a'/ 'A') or descending order ('d'/ 'D')")
                return
                
    def delete_Node(self, position):
        if self.head is None:
            print("The linked list is empty.")
            return
         
        temp = self.head
        try :
            if position == 0:
                self.head = temp.next
                temp = None
                return
            
            for i in range(position-1):
                temp = temp.next
                if temp is None:
                    print("Index out of range. check the number of nodes present in the list. Count starts from zero")
                    return
           
            temp_next = temp.next.next
            temp.next = None
            temp.next = temp_next

        except AttributeError:
            print("AttributeError: 'NoneType' object has no attribute 'next' Check if the position given lies in the range 0 - (length of linkedlist - 1)")
            return

        except TypeError :
            print("Positions should be of 'int' type")
            return

    
    
    def deleteAfter(self, neighbour_node):
        if self.head is None:
            print("The list is empty")
            return 
        if neighbour_node.next is None:
            print("The node doesnot exist")
            return
        temp = neighbour_node.next
        neighbour_node.next = neighbour_node.next.next
        temp = None
        return
        
        
        
        
    def delete_key(self, key):
        if self.head is None:
            print("The list is empty.")
            return
        temp = self.head
        if key == self.head.data:
            self.head = temp.next
            temp = None
            return
            
        if self.head.next is  None:
            return
        else :
            temp1 = self.head.next
            
        while temp1 is not None:
            if temp1.data == key:
                temp.next = temp1.next
                temp1 = None
                return
            temp = temp1
            temp1 = temp1.next
                    
        return
        
    
   
    
    def pop(self):
         if self.head is None:
             print("The list is empty. Cannot pop")
             return
         temp = self.head
         temp_Data = temp.data
         self.head = temp.next
         temp = None
         return temp_Data
     
        
    def delete(self, key, recursion = False):
        if self.head is None:
            print("The list is empty")
            return
        temp = self.head
        if recursion is False:
            self.delete_key(key)
            return
        #print("line386:",type(temp))
        
        #print("line 391:",type(temp))
        if  recursion is True :
            if self.head.data == key:
                a = self.pop()
            temp = self.head
            if self.head.next is None:
                if self.head.data == key:
                    b = self.pop()
                    return
            temp1 = self.head.next
            while temp1 is not None:
                if temp1.data == key:
                    self.deleteAfter(temp) 
                    temp1 = temp.next
                else:
                    temp = temp1
                    temp1 = temp1.next
            return
                
    
    def splitListRatio(self, head, ratio_list):
        if self.head is None:
            print("The list is empty.")
            return
        if self.head.next.next is None:
            print("The ist contains only two nodes")
            return [self.head, self.head.next]
        temp = self.head
        length_of_ratio_list = len(ratio_list)
        total = sum(ratio_list)
        length_ll = self.length()
        if length_of_ratio_list == 2:
            sub_ll_a = LinkedList()
            sub_ll_b = LinkedList()
            a = round((length_ll/total)*ratio_list[0])
            print(a)
            for i in range(length_ll):
                if i < a:
                    sub_ll_a.append(temp.data)
                    temp = temp.next
                else :
                    sub_ll_b.append(temp.data)
                    temp = temp.next
            return [sub_ll_a, sub_ll_b]
                
        else:
            print("Sorry, This function supports only splitting linkedlist into two parts.")
            return []
        
    
    
        
        
    def shufflemerge(self, ll1, ll2):
        ll = LinkedList()
        
        temp1 = ll1.head
        temp2 = ll2.head
        
        while( temp1 is not None and temp2 is not None):
            ll.append(temp1.data)
            ll.append(temp2.data)
            temp1 = temp1.next
            temp2 = temp2.next
        if temp1 is None:
            while(temp2 is not None):
                ll.append(temp2.data)
            return ll
        elif temp2 is None:
            while(temp1 is not None):
                ll.append(temp1.data)
            return ll
        
    
        
          

    
   
#IF you want to sort a linkedlist use this method. # This code is contributed by Vikas Chitturi in geeks for geeks

class LinkedList_sorting(LinkedList): 

    #def __init__(self):
	
	
		
    def sortedMerge(self, a, b): 
        result = None
		
        # Base cases 
        if a == None: 
            return b 
        if b == None: 
            return a 
			
	# pick either a or b and recur.. 
        if a.data <= b.data: 
            result = a 
            result.next = self.sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = self.sortedMerge(a, b.next) 
        return result
	

    def mergeSort(self, h): 
		
		# Base case if head is None 
        if h == None or h.next == None: 
            return h 

		# get the middle of the list 
        middle = self.mid_Node(h) 
        nexttomiddle = middle.next

		# set the next of middle node to None 
        middle.next = None

		# Apply mergeSort on left list 
        left = self.mergeSort(h) 
		
		# Apply mergeSort on right list 
        right = self.mergeSort(nexttomiddle) 

		# Merge the left and right lists 
        sortedlist = self.sortedMerge(left, right) 
        return sortedlist 
	


    
          

    
            

       

	
		


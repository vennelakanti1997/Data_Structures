import linked_list
import random
import cmath

if __name__ == '__main__':
    data1 = [1, 2, 3]

#create a linked list and assigning data to nodes
    llist = linked_list.LinkedList()
    llist.head = linked_list.Node(data1)
    second = linked_list.Node([2, 4, 5])
    third = linked_list.Node([3, 5, 7])

#Linking the nnodes
    llist.head.next = second
    second.next = third

    print("Original linked list:")
    llist.printList()
    

    data1.append(4)
    print("Original linked list after appending an element to a node:")
    llist.printList()

    llist.append([6,7,8])
    print("After appending :")
    llist.printList()

    print("After inserting :")
    llist.insertAfter(llist.head.next, [11,12,13]) 
    llist.printList()

    print("Length of linked list is :", llist.length(), "\n")

    llist.push(['a', 'b' ,'c'])
    print("After pushing the linked list is:")
    llist.printList()

    print("After inserting :")
    llist.insert([111,12,13],None, llist.head ) 
    llist.printList()
   
    print("After inserting at position 0:")
    llist.insert(['b','c','d'], llist.length()-1)
    llist.printList()

    llist.insert("bhargava", -2)
    print("After inserting at position 2:")
    llist.printList()

    print("Acessing an element at node 2:")
    print(llist.accessing_elements_in_a_node(3, -2))

    llist.search('bhargava')
    
    llist.append(data1)
    llist.insert(data1, 5)
    print("After appending same data i.e.,data1 for sake of search_All:")
    llist.printList()
    print("The list is :")
    print(llist.search_all(['a', 'b', 'c']), llist.search_all(data1, True))
    
    llist.append(1)
    llist.insert(['bhargava', 7, 'narendra', 7], 3)
    print("After pushing and inserting an element to list:")
    llist.printList()
    print("Search element:")
    print( llist.search_element(7, llist.length()))
    llist.append('AI')
    print("Middle node is:", llist.mid_Node(llist.head), llist.mid_Node(llist.head).data)
    print("Original list is:")
    llist.printList()
    print("Deleting a node:")
    llist.delete_key(llist.head.data)
    llist.printList()
    print("Doing pop operation:")
    print(llist.pop())
    print("Printing list after pop:")
    llist.printList()
    
    llist.push([1,2,3,4,5])
    llist.push([1,2,3,4,5])
    llist.append([1,2,3,4,5])
    llist.append([1,2,3,4,5])
    llist.insert([1,2,3,4,5], 3)
   
    #llist.insert(3, [1,2,3,4,5])
    print("Original List:")
    llist.append('bhargava')
    llist.push([6,7,8])
    llist.push([1,2,3,4,5])
    llist.append([1,2,3,4,5])
    llist.printList()
    #llist.delete_duplicates(llist.head)
    print("To check 'Delete Nodes' method:")
    llist.delete([1,2,3,4,5], True)
    llist.printList()
    
    """print("Finding an element:")
    print(llist.find(data1))
    llist1 = linked_list.LinkedList()
    #llist1.insert_at_position(0, ['b','c','d'], llist1.length_of_ll())
    llist1.printList()
    print(llist1.search_all(['a', 'b', 'c']), llist1.search(data1), llist1.search_element('a', llist1.length()))  
    print("The list is:")
    llist1.printList()
    print("Middle element is:",llist.mid_Node(llist1.head))"""


#Testing sortedMerge
    """llist1 = linked_list.LinkedList()
    for i in range(10,0,-1):
        llist1.append(i)
    print("LL1:")
    llist1.printList()
    llist2 = linked_list.LinkedList()
    for i in range(10,0,-1):
        llist2.append(i+2)
    print("LL2:")
    llist2.printList()
    print("Merged linked list is:")
    linked_list.LinkedList().sortedMerge(llist1.head, llist2.head, 'd' ,'a').printList()"""
    

    """print("Sorted List is:")
    sortedList = linked_list.LinkedList()
    sortedList.head = linked_list.LinkedList_sorting().mergeSort(llist1.head)"""

    #sortedList.printList()


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

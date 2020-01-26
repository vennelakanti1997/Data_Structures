import double_linked_lists

d_ll = double_linked_lists.Double_ll()
count = 0
data = [1,2,3,4,5]

for i in range(10):
    d_ll.append(data)
for i in range(10):
    d_ll.append(2)
print("List is :" ,d_ll.length())
d_ll.printList()
d_ll.delete_key(2, False, True)
print("SpliList:")
a = d_ll.splitList(d_ll.head, (5,4))
a[0].printList()
print("--------------------------")
a[1].printList()
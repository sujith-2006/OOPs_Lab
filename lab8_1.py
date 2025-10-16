# Lab 8:- Write a program to implement singly linked list and its operations
# Insertion (at beginning, end, middle), deletion, displaying

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def count(self):
        count = 0
        temp = self.head
        while (temp.next != None):
            temp = temp.next
            count += 1
        return count
    
    def insertStart(self, value):
        if (self.head == None):
            self.head = Node(value)
            return
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        
    def insertEnd(self, value):
        if (self.head == None):
            self.head = Node(value)
        temp = self.head
        newNode = Node(value)
        while (temp.next != None):
            temp = temp.next
        temp.next = newNode
    
    def deleteNode(self, position):
        if (self.head == None):
            print("Empty Linked List")
            return
        if (position == 1):
            temp = self.head.next
            self.head.next = None
            self.head = temp
            return
        prev = None
        temp = self.head
        for i in range(position-1):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp.next = None
    def insertMid(self, data):
        length = self.count()
        
        insert_position = length // 2
        
        if insert_position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            print(f"Inserted '{data}' at the beginning (list was empty or 1 node).")
            return

        new_node = Node(data)
        current_index = 0
        current = self.head
        
        while current and current_index < insert_position - 1:
            current = current.next
            current_index += 1
            
        if current:
            new_node.next = current.next
            current.next = new_node
            print(f"Inserted '{data}' at middle (Position {insert_position}).")
        else:
            print("Error: Insertion point not found.")
            
            
    def display(self):
        if (self.count() == 0):
            print("Empty Linked List!")
            return
        temp = self.head
        while (temp != None):
            print(f"{temp.value} -> ", end = '')
            temp = temp.next
        print("NULL")

linkedList = LinkedList()
linkedList.insertStart(2)
linkedList.insertStart(5)
linkedList.insertStart(10)
linkedList.insertEnd(20)
linkedList.display()
linkedList.insertMid()
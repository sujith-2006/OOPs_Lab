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
    
    def display(self):
        if (self.count == 0):
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
linkedList.deleteNode(2)
linkedList.deleteNode(1)
linkedList.deleteNode(1)
linkedList.deleteNode(1)
linkedList.display()

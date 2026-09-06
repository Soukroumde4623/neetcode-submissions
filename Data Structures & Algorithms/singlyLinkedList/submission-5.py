class ListNode:
    def __init__(self, val:int):
        self.element = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None 
     
    def get(self, index: int) -> int:
       current = self.head

       while current is not None and index>0:
             current = current.next
             index-=1
       if current is None:
            return -1
       return current.element

    def insertHead(self, val: int) -> None:
         New = ListNode(val)
         New.next = self.head
         self.head = New
             
    def insertTail(self, val: int) -> None:
        new = ListNode(val)
        if self.head is None :
            self.head = new
            return 

        current = self.head
        while current.next is not None:
              current = current.next
        current.next = new
        
    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index ==0:
            self.head = self.head.next
            return True

        current = self.head

        for _ in range(index-1):
             if current.next is None:
                return False
             current= current.next

        if current.next is None:
            return False

        current.next = current.next.next
        return True
        
    def getValues(self) -> List[int]:
        tab =[]
        current = self.head

        while current is not None:
               tab.append(current.element)
               current =current.next 
        return tab

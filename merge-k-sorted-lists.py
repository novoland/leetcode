class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if not lists:
            return        
        head = ListNode(0)
        cur = head
        heap = []
        for x in lists:
            if x:
                heap.append(x)
        if not heap:
            return head.next
        self.build(heap)
        while heap:
            cur.next = heap[0]
            cur = cur.next
            if heap[0].next:
                heap[0] = heap[0].next
            else:
                if len(heap) > 1:
                    heap[0] = heap.pop()
                else:
                    break
            self.sink(0,heap)
        return head.next

    def build(self,heap):
        size = len(heap)
        pos = size/2 -1
        for x in xrange(pos,-1,-1):
            self.sink(x,heap)
        
    def sink(self,pos,heap):
        size = len(heap)
        if pos >= size/2:
            return
        left,right=2*pos+1,2*pos+2
        if right < size:
            if heap[right].val < heap[left].val:
                if heap[pos].val > heap[right].val:
                    heap[pos],heap[right]=heap[right],heap[pos]
                    self.sink(right,heap)
            else:
                if heap[pos].val > heap[left].val:
                    heap[pos],heap[left]=heap[left],heap[pos] 
                    self.sink(left,heap)
        else:
            if heap[pos].val > heap[left].val:
                heap[pos],heap[left]=heap[left],heap[pos] 
                self.sink(left,heap)

                

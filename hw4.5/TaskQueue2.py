class Task:
    def __init__(self, id, cycles_left, prev = None, link = None):
        self.id = id
        self.cycles_left = cycles_left
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self
    def reduce_cycles(self, x):
        x1 = self.cycles_left - x
        self.cycles_left = x1
        return

class TaskQueue:
    def __init__(self, cycles_per_task = 1):
        self._head = None
        self._tail = None
        self._cycles_per_task = cycles_per_task
        self._current = None
        self._length = 0
        self._length2 = 0
    
    def __len__(self):
        return self._length2
    
    def is_empty(self):
        return self._length == 0

    def add_task(self, item, time):
        if self._length == 0:
            self._current = self._head = self._tail = Task(id = item, cycles_left = time, prev = None, link = None)
            self._head.prev = self._tail
            self._head.prev = self._current
            self._current.link = self._head
            self._tail.link = self._head
            self._length += 1
            self._length2 += time
        elif self._length == 1:
            newnode = Task(id = item, cycles_left = time, prev = None, link = self._current)
            self._current.prev = newnode
            self._head = newnode
            self._length += 1
            self._length2 += time
            #These functions complete the loop
            self._head.prev = self._tail
            self._head.prev = self._current
            self._current.link = self._head
            self._tail.link = self._head
        elif self._length == 2:
            newnode = Task(id = item, cycles_left = time, prev = self._head, link = self._current)
            self._head.link = newnode
            self._current.prev = newnode
            self._length += 1
            self._length2 += time
        else:
            newnode = Task(id = item, cycles_left = time, prev = self._current.prev, link = self._current)
            self._length += 1
            self._length2 += time
    
    def remove_task(self, item):
        current = self._head
        while current.id != item:
            current = current.link
        before = current.prev
        after = current.link
        before.link = after
        after.prev = before
        self._length -= 1
        self._length2 -= current.cycles_left
        return item

    def execute_tasks(self):
        total_cycles = 0
        currentnode = self._current
        L_tasks = []
        while self._length != 0:
            if currentnode.cycles_left > self._cycles_per_task:
                currentnode.cycles_left -= self._cycles_per_task
                total_cycles += self._cycles_per_task
                currentnode = currentnode.link
            
            elif currentnode.cycles_left == self._cycles_per_task:
                currentnode.cycles_left == 0
                total_cycles += self._cycles_per_task

                currentnode2 = currentnode
                self.remove_task(currentnode2.id)
                currentnode = currentnode.link
                L_tasks += ['Finished task ' + str(currentnode2.id) + ' after ' + str(total_cycles) + ' clock cycles']
            
            else:
                total_cycles += currentnode.cycles_left
                currentnode.cycles_left == 0
                currentnode2 = currentnode
                self.remove_task(currentnode2.id)
                currentnode = currentnode.link
                L_tasks += ['Finished task ' + str(currentnode2.id) + ' after ' + str(total_cycles) + ' clock cycles']
        s1 = ""
        for i in range(len(L_tasks) - 1):
            s1 += L_tasks[i] + '\n'
        s1 += L_tasks[len(L_tasks) - 1]
        return s1




if __name__== '__main__':
    
    t1 = Task(id=1, cycles_left=3)
    t2 = Task(id=2, cycles_left=1)
    t3 = Task(id=3, cycles_left=5)
    tasks = [t1, t2, t3]
    TQ = TaskQueue(cycles_per_task = 1)
    TQ.add_task(1,3)
    assert TQ._head.id == 1
    assert TQ._tail.id == 1
    assert TQ._current.id == 1
    TQ.add_task(2,1)
    assert TQ._head.id == 2
    assert TQ._tail.id == 1
    assert TQ._current.id == 1
    TQ.add_task(3,5)
    assert TQ._head.id == 2
    assert TQ._current.id == 1
    assert TQ._current.prev.id == 3
    assert TQ._head.link.id == 3
    TQ.add_task(4,1)
    assert TQ._head.id == 2
    assert TQ._current.id == 1
    assert TQ._head.link.id == 3
    assert TQ._current.prev.id == 4
    assert TQ._current.prev.prev.id == 3
    TQ.add_task(5,1)
    assert TQ._head.id == 2
    assert TQ._head.link.id == 3
    assert TQ._head.link.link.id == 4
    assert TQ._head.link.link.link.id == 5
    assert TQ._head.link.link.link.link.id == 1
    assert TQ._current.prev.id == 5
    assert TQ._current.prev.prev.id == 4
    assert TQ._current.prev.prev.prev.id == 3
    assert TQ._current.prev.prev.prev.prev.id == 2
    assert TQ._tail.prev.id == 5
    assert TQ._tail.prev.prev.id == 4
    assert TQ._tail.prev.prev.prev.id == 3
    assert TQ._tail.prev.prev.prev.prev.id == 2
    # Tests to see if links work 2 --> 3 --> 4 --> 5 --> 1
    # Tests to see if prev works 2 <-- 3 <-- 4 <-- 5 <-- 1
    
    assert len(TQ) == 11

    # Test to see if list keeps going 2 --> 3 --> 4 --> 5 --> 1 --> 2
    # Test to see if list keeps going other way 1 <-- 2 <-- 3 <-- 4 <-- 5 <-- 1
    assert TQ._current.prev.prev.prev.prev.prev.id == 1
    assert TQ._tail.prev.prev.prev.prev.prev.id == 1
    assert TQ._head.link.link.link.link.link.id == 2

    TQ.remove_task(4)
    TQ.remove_task(5)
    TQ.add_task(t1)

    print(TQ.execute_tasks())

"""
    assert TQ.remove_task(4) == 4
    # Tests to see if links work 2 --> 3 --> 5 --> 1
    # Tests to see if prev works 2 <-- 3 <-- 5 <-- 1
    assert TQ._head.id == 2
    assert TQ._current.id == 1
    assert TQ._tail.id == 1
    assert TQ._head.link.id == 3
    assert TQ._head.link.link.id == 5
    assert TQ._head.link.link.link.id == 1
    assert TQ._current.prev.id == 5
    assert TQ._current.prev.prev.id == 3
    assert TQ._current.prev.prev.prev.id == 2
    assert TQ._tail.prev.id == 5
    assert TQ._tail.prev.prev.id == 3
    assert TQ._tail.prev.prev.prev.id == 2

    assert len(TQ) == """

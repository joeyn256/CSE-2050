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
        self.cycles_per_task = cycles_per_task
        self.current = None
        self._length = 0
        self._length2 = 0
        self.set1 = set()
    
    def __len__(self):
        return self._length
    
    def is_empty(self):
        return self._length == 0

    def add_task(self, task):
        if self._length == 0:
            self.current = self._head = Task(task.id, task.cycles_left, prev = None, link = None)
            self._head.prev = self.current
            self.current.link = self._head
        elif self._length == 1:
            newnode = Task(task.id, task.cycles_left, prev = None, link = self.current)
            self.current.prev = newnode
            self._head = newnode
            #These functions complete the loop
            self._head.prev = self.current
            self.current.link = self._head
        elif self._length == 2:
            newnode = Task(task.id, task.cycles_left, prev = self._head, link = self.current)
            self._head.link = newnode
            self.current.prev = newnode
        else:
            newnode = Task(task.id, task.cycles_left, prev = self.current.prev, link = self.current)
        self.set1.add(task.id)
        self._length += 1
        self._length2 += task.cycles_left
    
    def remove_task(self, item):
        current = self._head
        if item in self.set1:
            while current.id is not item:
                current = current.link  
            current.prev.link = current.link
            current.link.prev = current.prev
            if current.id is self.current.id and len(self) > 1:
                self.current = self.current.link
            if current.id is self.current.id and len(self) == 1:
                self.current.prev = None
                self.current.link = None
                self.current = None
            self._length -= 1
            self.set1.remove(item)
            self._length2 -= current.cycles_left
            return item
        else:
            raise RuntimeError("Not in LL")

    def execute_tasks(self):
        total_cycles = 0
        currentnode = self.current
        L_tasks = []
        while self._length != 0:
            if currentnode.cycles_left > self.cycles_per_task:
                currentnode.cycles_left -= self.cycles_per_task
                total_cycles += self.cycles_per_task
            elif currentnode.cycles_left <= self.cycles_per_task:
                total_cycles += currentnode.cycles_left
                currentnode.cycles_left == 0
                currentnode2 = currentnode
                self.remove_task(currentnode2.id)
                L_tasks += ['Finished task ' + str(currentnode2.id) + ' after ' + str(total_cycles) + ' clock cycles']
            currentnode = currentnode.link
        s1 = ""
        for i in range(len(L_tasks) - 1):
            s1 += L_tasks[i] + '\n'
        s1 += L_tasks[len(L_tasks) - 1]
        print (s1)
        return total_cycles

if __name__== '__main__':
    t1 = Task(id=1, cycles_left=3)
    t2 = Task(id=2, cycles_left=1)
    t3 = Task(id=3, cycles_left=5)
    tasks = [t1, t2, t3]
    TQ = TaskQueue()
    for task in tasks:
        TQ.add_task(task)

    TQ.execute_tasks()
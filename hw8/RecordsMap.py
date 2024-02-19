class LocalRecord:
    """Represents a given instance of max and min temperature at a given position"""
    def __init__(self, pos, max=None, min=None, precision = 0): 
        """Initializes a local record, and handles initial rounding."""
        self.max=max
        self.min=min
        self.pos=(round(pos[0],precision),round(pos[1],precision))  #rounds to precision decimal

    def add_report(self, new): 
            """Adds local record, handles adjusting max and min"""
            if self.max==None and self.min==None: #initialize if values are none
                self.max=new
                self.min=new
            if new>self.max:                   #update temp if it is greater than max
                self.max = new
            if new<self.min:                   #update tempt if it is less than min
                self.min=new
     
    def __eq__(self, other): 
        """Returns if two positions are equal"""
        if (self.pos==other.pos):     
            return True
        else:
            return False
    def __hash__(self): 
        """Gives initial hashing of a local record"""
        return hash(self.pos)

    def __repr__(self):
        """"""
        return f"Record(pos={self.pos}, max={self.max}, min={self.min}"
    #store local records in records maps



class RecordsMap:
    def __init__(self): 
        self.n_buckets=8
        self._L = [[] for i in range(self.n_buckets)]   #Using a loop to create 8 buckets
        self._len = 0

    def __len__(self): 
        return(self._len)

    def add_report(self, pos, temp):

        bucket = hash(pos) % self.n_buckets
        i1 = LocalRecord(pos)
        if self._len >= (self.n_buckets)/2: self._rehash((2*self.n_buckets))
        for i in self._L[bucket]:
            if i.pos == i1.pos:
                return i.add_report(temp)
        else: 
            self._L[bucket].append(LocalRecord(pos,temp,temp))
            self._len += 1

    def __getitem__(self, pos): 
        i1 = LocalRecord(pos)
        bucket = hash(pos) % self.n_buckets
        for i in self._L[bucket]:
            if i.pos == i1.pos:
                return (i.min, i.max)
            #return min and max
        else:
            raise KeyError('not in mapping')


    def __contains__(self, pos): 
        i=LocalRecord(pos)
        h=(hash(pos)%self.n_buckets)
        for item in self._L[h]:
            if i.pos==item.pos:
                return True
            else: 
                return False

    def _rehash(self, new_L): 
        new_L = [[] for i in range(int(new_L))]
        self.n_buckets = len(new_L)

        for bucket in self._L:
            for item in bucket:
                h=hash(item)%self.n_buckets
                new_L[h].append(item)
        self._L = new_L

RM= RecordsMap()
p1=(-500,-32.2456)
RM.add_report(p1,34)
RM.add_report(p1,35)
p2 = (1,2)
RM.add_report(p2,1)
p3 = (3,4)
RM.add_report(p3,2)
p4 = (5,6)
RM.add_report(p4,3)
p5 = (7,8)
RM.add_report(p5,4)
# Should rehash around here since i'm using length 8 for my buckets
p6 = (9,10)
print(RM._L)
print(hash((46,-32)) % 16)
print(hash((1,2)) % 16)
print(hash((3,4)) % 16)
print(hash((5,6)) % 16)
print(hash((7,8)) % 16)
print(hash((9,10)) % 16)
print(hash((11,12)) % 16)
print(hash((13,14)) % 16)

 # did some testing with hashes and I expect p2 to be in 3, p3 in 5, p4 in 5, p5 in 14, p6 in 0, p7 in 0, and p8 in 1 which they are!



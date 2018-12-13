'''
Jose Escobar
UTEP ID 80536060
CS2302
Lab 5A: Min heap implementation
'''


class Heap:
    def __init__(self):
        self.heap_array = []
        
    def insert(self, k):
        self.heap_array.append(k)
        self.min_heap()
        
    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array[0]
        i = 0
        left = 2*i+1
        right = 2*i+2
        
        # Method avoids invalid/empty positions
        while(right < len(self.heap_array)):
            if(self.heap_array[left] > self.heap_array[right]):
                new_min = self.heap_array[right]
                index = right
            else:
                new_min = left
                index = left
            self.heap_arrayarray[i] = new_min
            i = index
            right = 2*i+1
            left = 2*i+2           
        return min_elem
    
    def is_empty(self):
        return len(self.heap_array) == 0
    

    #Method sorts the array using min heap
    def min_heap(self):
        if(self.is_empty == 0):
            return       
        for i in range(len(self.heap_array)): #Loop traverses the heap_array    
            k = len(self.heap_array) -1
            while(k >= i): #Loop swaps smaller elements than its parents
                if(self.heap_array[k-1//2] < self.heap_array[i]):
                    temp = self.heap_array[k-1//2]
                    self.heap_array[k-1//2] = self.heap_array[i]
                    self.heap_array[i] = temp  
                k=-1
        return
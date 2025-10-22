class FlatIterator():
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.list_cursor = 0
        self.sub_list_cursor = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if self.list_cursor >= len(self.list_of_lists):
                raise StopIteration
            
            current_list = self.list_of_lists[self.list_cursor]
                
            if self.sub_list_cursor < len(current_list):
                    element = current_list[self.sub_list_cursor]
                    self.sub_list_cursor +=1
                    return element
            else:
                    self.list_cursor += 1
                    self.sub_list_cursor = 0
                    continue
               

def flat_generator(list_of_lists):
    for current_list in list_of_lists:
        for element in current_list:
            yield element


def flat_generator2(list_of_lists):
    for element in list_of_lists:
        if isinstance(element, list):
            yield from flat_generator2(element)
        else:
            yield element
            

class FlatIterator2():
    def __init__(self, main_list):
        self.main_list = main_list
        self.coords = [0]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            current_element = self.main_list
            
            try:
                for num in self.coords:
                    current_element = current_element[num]
            except IndexError:
                self.coords.pop()
                if not self.coords:
                    raise StopIteration
                self.coords[-1] += 1
                continue
           
            if isinstance(current_element, list):
                self.coords.append(0)
                continue
            else:
                self.coords[-1] += 1
                return current_element
            
        
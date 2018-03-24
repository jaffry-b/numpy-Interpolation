## @file SeqADT.py
#  @title SeqADT
#  @author Bilal Jaffry
#  @date 1/22/2018

## @brief This class represents sequences.
#  @details This class represents a sequence as a list, being able to remove, add, get, or set values to the list.
#  It also has the ability to see if a value lies in the given sequence.
class SeqT:
    ## @brief Constructor for SeqADT
    #  @details Accepts no parameters, constructs an empty list of self type.
    def __init__(self):
        ## @brief Initializes empty sequence.
        self.initList = []

    ## @brief Add's or replaces an element to the list.
    #  @param i index in list to be appended.
    #  @param v element being appended at index i, in list.
    #  @return v is inserted in i, if i is currently in list. If not, it is appended to end of the list.
    def add(self, i, v):
        if i < len(self.initList):
            return self.initList.insert(i, v)
        else:
            return self.initList.append(v)

    ## @brief Removes element in list.
    #  @param i index in list being accessed.
    #  @return list after removing element at given index
    def rm(self, i):
        self.initList.pop(i)
        return self.initList

    ## @brief Replaces an element in list.
    #  @param i index of list being accessed.
    #  @param v element being set to at index i.
    #  @return returns the list after value has been replaced at i.
    def set(self, i, v):
        if i < len(self.initList):
            self.initList[i] = v
            return self.initList
        else:
            raise IndexError("Index is not in list.")

    ## @brief Gets value at index.
    #  @param i index of list being accessed.
    #  @return returns the value at the given index.
    def get(self, i):
        if i < len(self.initList):
            y = self.initList[i]
            return y
        else:
            raise IndexError("Index is not in list.")

    ## @brief Obtains the size of the list.
    #  @return returns the length of the list.
    def size(self):
        return len(self.initList)

    ## @brief Checks to see if the element is in sequence.
    #  @param v the element being inputed to see if in sequence.
    #  @return returns the index at which the value is bounded by.
    def indexInSeq(self, v):
        for index in range(len(self.initList)-1):
            if self.get(index) <= v and v <= self.get(index + 1):
                return index

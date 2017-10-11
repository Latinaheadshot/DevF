my_set = {1,3}
def add_element_to_set():
    #add an element
    #my_set.add(2)
    #print ("Elemente added", my_set)

    #add multiple elements
    #my_set.update({2,3,4})
    #print("Set updated with several element a once", my_set)

    # add list and set
    my_set.update([4,5]), {1,6,8}
    print("Set updated using a list", my_set)

def delete_set_elements():
    # initialize my_set
    my_set = {1,3,4,5,6}
    print (my_set)

    # discard an element
    my_set.discard(4)
    print(my_set)

    # remove an element
    my_set.remove(16)
    print(my_set)

def pop_element_from_set()
    # initialize my_set
    # output: set of unique elements
    my_set = set("Hello World")
    print(my_set)

    #pop and element
    # Output: random element
    print(my_set.pop())

    # clear my_set
    # output: set()
    my_set.clear()
    print(my_set)
pop_element_from_set()





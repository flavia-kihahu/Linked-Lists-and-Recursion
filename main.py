from linked_list import LinkedList

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_front(5)
    print("Original list:")
    linked_list.display()
    print("Sum:", linked_list.recursive_sum())
    print("Search for 20:", linked_list.recursive_search(20))
    print("Search for 99:", linked_list.recursive_search(99))
    linked_list.recursive_reverse()
    print("Reversed list:")
    linked_list.display()
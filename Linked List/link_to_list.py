def link2list(linked_list):
    my_list = []
    while linked_list:
        node = linked_list.val
        my_list.append(node)
        linked_list = linked_list.next
    return my_list

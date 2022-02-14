def length(head):
    count = 0
    while head != None:
        count += 1
        head = head.next
    return count
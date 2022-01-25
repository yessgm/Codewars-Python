def move_ten(st):
    return ''.join(chr(ord(i)+10) if i<'q' else chr(ord(i)-16) for i in st)

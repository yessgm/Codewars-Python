def remove(s):
    return s.replace('!', '')+ '!'*(len(s)- len(s.rstrip('!')))

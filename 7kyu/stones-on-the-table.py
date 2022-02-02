def solution(stones):
    changes = [i for i in range(len(stones)-1) if stones[i] == stones[i+1]]
    return len(changes)
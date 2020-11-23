from pico2d import *
import gobj
import gfw 

def hands(indexs,shape):
    pair = 0#페어
    index = indexs.copy()
    index.sort()
    print(index)
    global si
    si = index.sort()
    flcont = 0
    stcont = 0
    for i in range(1,5):
        if index[i] == index[i-1]-1:
            stcont+=1
        if shape[i] == shape[i-1]:
            flcont+=1
    if stcont==4 and flcont ==3:
        return 'stfl'
    else:
        if stcont == 4:
            return 'st' 
        elif flcont ==3:
            return 'fl'
    samenum = []        
    for c1 in range(0,5):
        for c2 in range(c1,5):
            if index[c1] == index[c2]:
                samenum.append(index[c1])
                pair +=1
    if pair == 1:
        return 'op'
    if pair == 2:
        return 'tp'
    if pair == 3:
        if samenum[0]== samenum[1] and samenum[0] == samenum[2]:
            return 'tk'
    if pair == 4:
        if samenum[0]== samenum[1] and samenum[0] == samenum[2] and samenum[0] == samenum[3]:
            return 'fk'
        else:
            return 'hs'

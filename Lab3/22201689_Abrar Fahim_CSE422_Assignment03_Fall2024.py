import random

def minimax(startingplayer,depth,maxdepth,maximizingplayer):
    if depth==maxdepth:
        return random.choice([-1, 1])
    if maximizingplayer:
        bestvalue=float('-inf')
        for i in range(2):
            value=minimax(startingplayer,depth+1,maxdepth,False)
            bestvalue=max(bestvalue,value)
        return bestvalue
    else:
        bestvalue=float('inf')
        for i in range(2):
            value=minimax(startingplayer,depth+1,maxdepth,True)
            bestvalue=min(bestvalue,value)
        return bestvalue

def mortal_kombat(startingplayer):
    maxdepth=5
    mustwin=(maxdepth+1)//2
    scorpion=0
    subzero=0
    roundwinners=[]
    count=0
    while scorpion<mustwin and subzero<mustwin:
        count+=1
        result=minimax(startingplayer,0,maxdepth,startingplayer==1,)
        if result==-1:
            scorpion+=1
            roundwinners.append("Scorpion")
        else:
            subzero+=1
            roundwinners.append("Sub-Zero")
        if startingplayer==0:
            startingplayer=1
        else:
            startingplayer=0

    if scorpion>subzero:
        game="Scorpion"
    else:
        game="Sub-Zero"
    return game,count,roundwinners

with open('input.txt') as fin:
    startingplayer=int(fin.readline().strip())

winner,played,roundwinner=mortal_kombat(startingplayer)

print('-'*10 + 'Minimax' + '-'*10)
print(f"Game Winner: {winner}\nRounds Played: {played}\nRound Winners:")
for i in range(len(roundwinner)):
    print(f"Round {i+1}: {roundwinner[i]}")

print('\n')

def alphabetapruning(startingplayer,depth,maxdepth,maximizingplayer,alpha=float('-inf'),beta=float('inf')):
    if depth==maxdepth:
        return random.choice([-1,1])
    if maximizingplayer:
        bestvalue=float('-inf')
        for i in range(2):
            value=alphabetapruning(startingplayer,depth+1,maxdepth,False,alpha,beta)
            bestvalue=max(bestvalue,value)
            alpha=max(alpha,bestvalue)
            if beta<=alpha:
                break
        return bestvalue
    else:
        bestvalue=float('inf')
        for i in range(2):
            value=alphabetapruning(startingplayer,depth+1,maxdepth,True,alpha,beta)
            bestvalue=min(bestvalue,value)
            beta=min(beta,bestvalue)
            if beta<=alpha:
                break
        return bestvalue
    
def mortal_kombat_alphabetapruning(startingplayer):
    maxdepth=5
    mustwin=(maxdepth+1)//2
    scorpion=0
    subzero=0
    roundwinners=[]
    count=0
    while scorpion<mustwin and subzero<mustwin:
        count+=1
        result=alphabetapruning(startingplayer,0,maxdepth,startingplayer==1)
        if result==-1:
            scorpion+=1
            roundwinners.append("Scorpion")
        else:
            subzero+=1
            roundwinners.append("Sub-Zero")
        if startingplayer==0:
            startingplayer=1
        else:
            startingplayer=0

    if scorpion>subzero:
        game="Scorpion"
    else:
        game="Sub-Zero"
    return game,count,roundwinners

with open('input.txt') as fin:
    startingplayer=int(fin.readline().strip())

winner,played,roundwinner=mortal_kombat(startingplayer)

print('-'*10 + 'Alpha Beta Pruning' + '-'*10)
print(f"Game Winner: {winner}\nRounds Played: {played}\nRound Winners:")
for i in range(len(roundwinner)):
    print(f"Round {i+1}: {roundwinner[i]}")


# Task 2

print('\n')

def alpha_beta_pruning(depth,is_maximizing,alpha,beta,index,values,max_depth):
    if depth==max_depth:
        return values[index]
    if is_maximizing:
        max_eval=float('-inf')
        for i in range(2):
            eval=alpha_beta_pruning(depth+1,False,alpha,beta,index*2+i,values,max_depth)
            max_eval=max(max_eval,eval)
            alpha=max(alpha,eval)
            if beta<=alpha:
                break
        return max_eval
    else:
        min_eval=float('inf')
        for i in range(2):
            eval=alpha_beta_pruning(depth+1,True,alpha,beta,index*2+i,values,max_depth)
            min_eval=min(min_eval,eval)
            beta=min(beta,eval)
            if beta<=alpha:
                break
        return min_eval

def minimax_max(depth,alpha,beta,index,values,max_depth):
    if depth==max_depth:
        return values[index],None,None
    max_eval=float('-inf')
    left_subtree=None
    right_subtree=None
    for i in range(2):
        eval,left,right=minimax_max(depth+1,alpha,beta,index*2+i,values,max_depth)
        if i==0:
            left_subtree=eval
        else:
            right_subtree=eval
        max_eval=max(max_eval,eval)
        alpha=max(alpha,eval)
        if beta<=alpha:
            break
    return max_eval,left_subtree,right_subtree

def pacman_game(cost):
    values = [3, 6, 2, 3, 7, 1, 2, 0]
    max_depth=3
    cost_without_magic=alpha_beta_pruning(0,True,float('-inf'),float('inf'),0,values,max_depth)
    cost_with_magic,left,right=minimax_max(0,float('-inf'),float('inf'),0,values,max_depth)
    left=left-cost
    right=right-cost
    if left>right:
        cost_with_magic=left
        val='left'
    else:
        cost_with_magic=right
        val='right'
    if cost_with_magic>cost_without_magic:
        print(f"The new minimax value is {cost_with_magic}. Pacman goes {val} and uses dark magic")
    else:
        print(f"The minimax value is {cost_without_magic}. Pacman does not use dark magic")

print('-'*10 + 'Pacman Game' + '-'*10)
pacman_game(2)

pacman_game(5)
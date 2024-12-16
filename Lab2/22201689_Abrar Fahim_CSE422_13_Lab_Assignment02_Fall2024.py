import random
from collections import defaultdict

def fitness(genome,course,timeslot):
    fitness_dict = defaultdict(int)
    s=0;e=course;totalfit=0
    for i in range(course):
        fitness_dict[i]=0
    for i in range(t):
        fit=0
        st=genome[s:e]
        for j in range(timeslot):
            if st[j]=='1':
                fitness_dict[j]+=1
                fit+=1
        fit-=1
        totalfit+=abs(fit)
        s+=course;e+=course
    for i in range(t):
        fitness_dict[i]=abs(fitness_dict[i]-1)
        totalfit+=abs(fitness_dict[i])
    return totalfit*-1

def populator(n,t):
        genpop=[]
        for j in range(20):
            genome=''
            for i in range(n*t):
                genome+=random.choice('01')
            genpop.append(genome)
        return genpop

def parentpair(genpop):
    parentpairs=[]
    for i in range(10):
        parentpairs.append(random.sample(genpop,2))
    return parentpairs

def crossover(parent1,parent2,n,t):
    crosspoint=random.randint(1,n*t-1)
    offspring1=parent1[:crosspoint]+parent2[crosspoint:]
    offspring2=parent2[:crosspoint]+parent1[crosspoint:]
    return offspring1,offspring2

def mutation(genome):
    point1=random.randint(0,len(genome)-1)
    point2=random.randint(0,len(genome)-1)
    if genome[point1]=='0':
        genome=genome[:point1]+'1'+genome[point1+1:]
    else:
        genome=genome[:point1]+'0'+genome[point1+1:]
    if genome[point2]=='0':
        genome=genome[:point2]+'1'+genome[point2+1:]
    else:
        genome=genome[:point2]+'0'+genome[point2+1:]
    return genome
    

with open('input.txt','r') as file:
    n,t=map(int,file.readline().split())
    bestgenome=''
    bestfitness=float('-inf')
    initial_population=populator(n,t)
    for i in range(20):
        parents=parentpair(initial_population)
        offsprings=[]
        for parent1,parent2 in parents:
            offspring1,offspring2=crossover(parent1,parent2,n,t)
            offsprings.append(offspring1)
            offsprings.append(offspring2)
        offsprings2=[]
        for i in offsprings:
            offsprings2.append(mutation(i))
        initial_population=offsprings2
        genwithfitness=[]
        for i in initial_population:
            genwithfitness.append((i,fitness(i,n,t)))
        genwithfitness.sort(key=lambda x:x[1], reverse=True)
        
        if genwithfitness[0][1]>bestfitness:
            bestfitness=genwithfitness[0][1]
            bestgenome=genwithfitness[0][0]
    print(bestgenome)
    print(bestfitness)


# Task 2: multi point cross over

def multipointcrossover(parent1,parent2,n,t):
    crosspoint1=random.randint(1,n*t-1)
    crosspoint2=random.randint(crosspoint1,n*t-1)
    offspring1=parent1[:crosspoint1]+parent2[crosspoint1:crosspoint2]+parent1[crosspoint2:]
    offspring2=parent2[:crosspoint1]+parent1[crosspoint1:crosspoint2]+parent2[crosspoint2:]
    return offspring1,offspring2

# All other functions remain the same

with open('input.txt','r') as file:
    n,t=map(int,file.readline().split())
    bestgenome=''
    bestfitness=float('-inf')
    initial_population=populator(n,t)
    for i in range(20):
        parents=parentpair(initial_population)
        offsprings=[]
        for parent1,parent2 in parents:
            offspring1,offspring2=multipointcrossover(parent1,parent2,n,t)
            offsprings.append(offspring1)
            offsprings.append(offspring2)
        offsprings2=[]
        for i in offsprings:
            offsprings2.append(mutation(i))
        initial_population=offsprings2
        genwithfitness=[]
        for i in initial_population:
            genwithfitness.append((i,fitness(i,n,t)))
        genwithfitness.sort(key=lambda x:x[1], reverse=True)
        
        if genwithfitness[0][1]>bestfitness:
            bestfitness=genwithfitness[0][1]
            bestgenome=genwithfitness[0][0]
    print(bestgenome)
    print(bestfitness)
    

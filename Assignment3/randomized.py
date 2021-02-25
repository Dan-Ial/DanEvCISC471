"""
Homework 3
By: Evelyn Yach (20071956) & Daniel Oh (20063998)
2021.02.09
"""

"""
RANDOMIZEDMOTIFSEARCH(Dna, k, t)
    randomly select k-mers Motifs = (Motif1, …, Motift) in each string
        from Dna
    BestMotifs ← Motifs
    while forever
        Profile ← Profile(Motifs)
        Motifs ← Motifs(Profile, Dna)
        if Score(Motifs) < Score(BestMotifs)
            BestMotifs ← Motifs
        else
            return BestMotifs
"""

import random
import math
import operator

def Profile(best_motifs):
    profile = []
    for i in range(len(best_motifs[0])):
        A, T, G, C = 1, 1, 1, 1
        for motif in best_motifs:
            if motif[i] == 'A':
                A += 1
            elif motif[i] == 'T':
                T += 1
            elif motif[i] == 'G':
                G += 1
            elif motif[i] == 'C':
                C += 1

        #add to the current profile
        profile.append([A/(len(best_motifs)+4),
                        T/(len(best_motifs)+4),
                        G/(len(best_motifs)+4),
                        C/(len(best_motifs)+4)])
    return profile

def Motifs(profile, Dna):
    motifs = []
    
    for dna_str in Dna:
        
        #set stuff up
        k = len(profile)
        best_pattern = dna_str[0:0 + k]
        best_probability = 0

        #begin calculating the most probable pattern
        for i in range(len(dna_str) - k + 1):
            
            s = dna_str[i:i + k]
            
            #calculate probability
            probability = 1
            for i in range(0,len(s)):
                if s[i] == 'A':
                    probability = probability * profile[i][0]
                elif s[i] == 'T':
                    probability = probability * profile[i][1]
                elif s[i] == 'G':
                    probability = probability * profile[i][2]
                elif s[i] == 'C':
                    probability = probability * profile[i][3]

            #determine if the new probability is better then the old one  
            if probability > best_probability:
                best_pattern = s
                best_probability = probability

        motifs.append(best_pattern)

    return motifs
    

def HammingDistance(s1, s2):
    count = 0
    for i, j in zip(s1, s2):
        if i != j:
            count += 1
    return count

def Score(motifs):
    #beginning similar to the Profile function
    #find a consensus
    consensus = ''
    for i in range(len(motifs[0])):
        A, T, G, C = 0, 0, 0, 0
        for motif in motifs:
            #count em up
            if motif[i] == 'A':
                A += 1
            elif motif[i] == 'T':
                T += 1
            elif motif[i] == 'G':
                G += 1
            elif motif[i] == 'C':
                C += 1

        #find max
        if A >= max(C, G, T):
            consensus += "A"
        elif T >= max(C, G, A):
            consensus += "T"
        elif G >= max(C, A, T):
            consensus += "G"
        elif C >= max(A, G, T):
            consensus += "C"

    #calculate the score based on the Hamming Distance
    score = 0
    for motif in motifs:
        score += HammingDistance(consensus, motif)

    return score
            

def RandomizedMotifSearch(Dna, k, t):
    #randomly select the best k-mers motifs
    best_motifs = []
    for i in Dna:
        position = random.randint(0, len(i) - k)
        best_motifs.append(i[position:position + k])

    #whilest forever
    while True:
        
        #Profile ← Profile(Motifs)
        profile = Profile(best_motifs)

        #Motifs ← Motifs(Profile, Dna)
        motifs = Motifs(profile, Dna)

        #want the one with the  lower score
        #if Score(Motifs) < Score(BestMotifs)
        if Score(motifs) < Score(best_motifs):
            #BestMotifs ← Motifs
            best_motifs = motifs
        #else
        else:
            #return BestMotifs
            return best_motifs

def IterativeRandomizedMotifSearch(rosalind_Dna, k, t):
    #iterate thru
    #find all the best motifs from the data
    best_motifs = []
    for i in range(t):
        best_motifs.append(rosalind_Dna[i][:k])

    #Because we want a collection BestMotifs resulting from running
    #RandomizedMotifSearch(Dna, k, t) 1000 times. we iterate
    iterator = 0
    while iterator < 1000:
        #bread and butter right there
        motifs = RandomizedMotifSearch(rosalind_Dna, k, t)
        
        if Score(motifs) < Score(best_motifs):
            best_motifs = motifs
            
        iterator += 1

    #our final result will be stored in best_motifs
    return best_motifs
            
"""   
if __name__ == '__main__':
    rosalind_Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
                    "TAGTACCGAGACCGAAAGAAGTATACAGGCGT","TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
                    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
    k = 8
    t = 5   #len(rosalind_Dna)

    best_motifs = IterativeRandomizedMotifSearch(rosalind_Dna, k, t)

    #print
    for motif in best_motifs:
        print(motif)
""" 

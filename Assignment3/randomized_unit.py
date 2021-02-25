"""
Homework 3
By: Evelyn Yach (20071956) & Daniel Oh (20063998)
2021.02.09
"""

"""
Unit Tests
        For
         RandomMotifSearch
"""

import random
import math
import operator
from randomized import Profile, Motifs, HammingDistance, Score, RandomizedMotifSearch, IterativeRandomizedMotifSearch

#Unit Tests
#sample dataset
def testcase1():
    rosalind_Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
                    "TAGTACCGAGACCGAAAGAAGTATACAGGCGT","TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
                    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
    k = 8
    t = 5   #len(rosalind_Dna)

    best_motifs = IterativeRandomizedMotifSearch(rosalind_Dna, k, t)

    answer = ["TCTCGGGG", "CCAAGGTG", "TACAGGCG",
              "TTCAGGTG", "TCCACGTG"]

    return best_motifs, answer

#test dataset1
def testcase2():
    rosalind_Dna = ["AATTGGCACATCATTATCGATAACGATTCGCCGCATTGCC",
                    "GGTTAACATCGAATAACTGACACCTGCTCTGGCACCGCTC",
                    "AATTGGCGGCGGTATAGCCAGATAGTGCCAATAATTTCCT",
                    "GGTTAATGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG",
                    "AATTGGACGGCAACTACGGTTACAACGCAGCAAGAATATT",
                    "GGTTAACTGTTGTTGCTAACACCGTTAAGCGACGGCAACT",
                    "AATTGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG",
                    "GGTTAAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA",]
    k = 6
    t = 8   #len(rosalind_Dna)

    best_motifs = IterativeRandomizedMotifSearch(rosalind_Dna, k, t)

    answer = ["CGATAA", "GGTTAA", "GGTATA",
              "GGTTAA", "GGTTAC", "GGTTAA",
              "GGCCAA", "GGTTAA"]

    return best_motifs, answer

#test dataset2
def testcase3():
    rosalind_Dna = ["GCACATCATTAAACGATTCGCCGCATTGCCTCGATTAACC",
                    "TCATAACTGACACCTGCTCTGGCACCGCTCATCCAAGGCC",
                    "AAGCGGGTATAGCCAGATAGTGCCAATAATTTCCTTAACC",
                    "AGTCGGTGGTGAAGTGTGGGTTATGGGGAAAGGCAAGGCC",
                    "AACCGGACGGCAACTACGGTTACAACGCAGCAAGTTAACC",
                    "AGGCGTCTGTTGTTGCTAACACCGTTAAGCGACGAAGGCC",
                    "AAGCTTCCAACATCGTCTTGGCATCTCGGTGTGTTTAACC",
                    "AATTGAACATCTTACTCTTTTCGCTTTCAAAAAAAAGGCC"]
    k = 6
    t = 8   #len(rosalind_Dna)

    best_motifs = IterativeRandomizedMotifSearch(rosalind_Dna, k, t)

    answer = ["TTAACC", "ATAACT", "TTAACC",
              "TGAAGT", "TTAACC", "TTAAGC",
              "TTAACC", "TGAACA"]

    return best_motifs, answer

#Extra Functions
def display(best_motifs):
    #print
    for motif in best_motifs:
        print(motif)

def check(best_motifs, correct_motifs):
    #check for each line
    for i in range(len(correct_motifs)):
        if best_motifs[i] != correct_motifs[i]:
            return False
    return True
            

if __name__ == '__main__':

    #Unit Test 1
    print("Unit Test 1:")
    test1, answer1 = testcase1()    #run the first test
    pass1 = check(test1, answer1)   #check to see if its right
    print(pass1)
    #if the test failed, show the output
    if pass1 == False:
        print("Output:")
        display(test1)

    #Unit Test 2
    print("\nUnit Test 2:")
    test2, answer2 = testcase2()    #run the second test
    pass2 = check(test2, answer2)   #check to see if its right
    print(pass2)
    #if the test failed, show the output
    if pass2 == False:
        print("Output:")
        display(test2)

    #Unit Test 3
    print("\nUnit Test 3:")
    test3, answer3 = testcase3()    #run the third test
    pass3 = check(test3, answer3)   #check to see if its right
    print(pass3)
    #if the test failed, show the output
    if pass3 == False:
        print("Output:")
        display(test3)

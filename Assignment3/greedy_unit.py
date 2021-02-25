"""
Homework 3
By: Evelyn Yach (20071956) & Daniel Oh (20063998)
2021.02.25
"""
from greedy import greedy_motif_search


# Extra Functions
def display(best_motifs):
    # print
    for motif in best_motifs:
        print(motif)


def check(best_motifs, correct_motifs):
    # check for each line
    for i in range(len(correct_motifs)):
        if best_motifs[i] != correct_motifs[i]:
            return False
    return True


def test_greedy_motif_search_pos():
    # positive test case
    rosalind_dna_data = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    k = 3
    t = 5  # len(rosalind_dna_data)

    best_motifs = greedy_motif_search(rosalind_dna_data, k, t)

    answer = ['CAG', 'CAG', 'CAA', 'CAA', 'CAA']

    return best_motifs, answer


def test_greedy_motif_search_neg_1():
    # test when k is larger than allowed
    rosalind_dna_data = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    k = 15
    t = 5  # len(rosalind_dna_data)

    best_motifs = greedy_motif_search(rosalind_dna_data, k, t)

    answer = []

    return best_motifs, answer


def test_greedy_motif_search_neg_2():
    # test when an empty list is passed in
    rosalind_dna_data = []
    k = 3
    t = 5  # len(rosalind_dna_data)

    best_motifs = greedy_motif_search(rosalind_dna_data, k, t)

    answer = []

    return best_motifs, answer


def run_greedy_test_cases():
    # Unit Test 1
    print("Unit Test 1:")
    test1, answer1 = test_greedy_motif_search_pos()  # run the first test
    pass1 = check(test1, answer1)  # check to see if its right
    print(pass1)
    # if the test failed, show the output
    if pass1 == False:
        print("Output:")
        display(test1)

    # Unit Test 2
    print("\nUnit Test 2:")
    test2, answer2 = test_greedy_motif_search_neg_1()  # run the second test
    pass2 = check(test2, answer2)  # check to see if its right
    print(pass2)
    # if the test failed, show the output
    if pass2 == False:
        print("Output:")
        display(test2)

    # Unit Test 3
    print("\nUnit Test 3:")
    test3, answer3 = test_greedy_motif_search_neg_2()  # run the third test
    pass3 = check(test3, answer3)  # check to see if its right
    print(pass3)
    # if the test failed, show the output
    if pass3 == False:
        print("Output:")
        display(test3)


if __name__ == '__main__':
    run_greedy_test_cases()

"""
Homework 3
By: Evelyn Yach (20071956) & Daniel Oh (20063998)
2021.02.25
"""
from gibbs import gibbs_sampler

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


def test_gibbs_sampler_pos():
    # positive test case
    rosalind_dna_data = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
                         'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
                         'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
                         'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
                         'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
    k = 8
    t = 5  # len(rosalind_dna_data)
    N = 100

    best_motifs = gibbs_sampler(rosalind_dna_data, k, t, N)

    return best_motifs


def test_gibbs_sampler_neg_1():
    # negative test case
    rosalind_dna_data = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
                         'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
                         'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
                         'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
                         'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
    k = 40
    t = 5  # len(rosalind_dna_data)
    N = 100

    best_motifs = gibbs_sampler(rosalind_dna_data, k, t, N)

    answer = []

    return best_motifs, answer


def test_gibbs_sampler_neg_2():
    # test when an empty list is passed in
    rosalind_dna_data = []
    k = 8
    t = 5  # len(rosalind_dna_data)
    N = 100

    best_motifs = gibbs_sampler(rosalind_dna_data, k, t, N)

    answer = []

    return best_motifs, answer


def run_gibbs_test_cases():
    # Unit Test 1
    print("Unit Test 1:")
    test1 = test_gibbs_sampler_pos()  # run the first test
    # check to see if its right
    # due to the randomness of this algorithm, we check that a valid output is returned
    pass1 = True
    for motif in test1:
        # check for motif length
        if len(motif) != 8:
            pass1 = False
        # check for motif content (must only contain A's, C's, T's, or G's)
        for char in motif:
            if char not in 'ACTG':
                pass1 = False
        # break if we have failed any checks
        if not pass1:
            break
    print(pass1)
    # if the test failed, show the output
    if pass1 == False:
        print("Output:")
        display(test1)

    # Unit Test 2
    print("\nUnit Test 2:")
    test2, answer2 = test_gibbs_sampler_neg_1()  # run the second test
    pass2 = check(test2, answer2)  # check to see if its right
    print(pass2)
    # if the test failed, show the output
    if pass2 == False:
        print("Output:")
        display(test2)

    # Unit Test 3
    print("\nUnit Test 3:")
    test3, answer3 = test_gibbs_sampler_neg_2()  # run the third test
    pass3 = check(test3, answer3)  # check to see if its right
    print(pass3)
    # if the test failed, show the output
    if pass3 == False:
        print("Output:")
        display(test3)

if __name__ == '__main__':
    run_gibbs_test_cases()

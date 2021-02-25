"""
Homework 3
By: Evelyn Yach (20071956) & Daniel Oh (20063998)
2021.02.25
"""
import random
from HelperFunctions import create_profile, score, find_most_probable_profile

def gibbs_sampler(dna, k, t, N):
    """
    conducts gibbs sampling on a list of DNA strings
    :param dna: list of DNA strings
    :param k: length of kmers
    :param t: length of the dna parameter
    :param N: number of loop iterations
    :return: list of best motifs
    """
    # invalid input checking
    if (len(dna) == 0) or (len(dna) != t) or (k > len(dna[0]) or (N < 1)):
        return []
    # check if we have any invalid characters and differing dna lengths
    for dna_string in dna:
        if len(dna_string) != len(dna[0]):
            return []
        for char in dna_string:
            if char not in 'ACTG':
                return []

    # randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    motifs = []
    for i in dna:
        position = random.randint(0, len(i) - k)
        motifs.append(i[position:position + k])

    best_motifs = motifs
    best_motif_score = score(best_motifs)

    for j in range(N):
        i = random.randrange(t)

        # check if i+1 is out of bounds
        if len(motifs) == i:  # if out of bounds, account for it
            profile = create_profile(motifs[:i])
        else:
            profile = create_profile(motifs[:i] + motifs[i + 1:])

        motifs[i] = profile_randomly_generated(dna[i], profile, k)

        current_motif_score = score(motifs)
        if current_motif_score < best_motif_score:
            best_motif_score = current_motif_score
            best_motifs = motifs

    return best_motifs


def profile_randomly_generated(dna_string, profile, k):
    """
    generates profile based on random generation
    :param dna_string: a string of dna
    :param profile: a profile
    :param k: the k parameter
    :return: the selected profile
    """
    # useful variable to determine how much our loops need to iterate
    iteration_range = len(dna_string) - k + 1
    # calculate the probabilities of each kmer
    kmer_probabilities = [1 for x in range(iteration_range)]

    for i in range(iteration_range):
        for j in range(k):
            # in the following nested if statements, we dont include 0's into our calculations
            if dna_string[i+j] == 'A' and profile['A'][j] != 0:
                kmer_probabilities[i] *= profile['A'][j]
            elif dna_string[i+j] == 'C' and profile['C'][j] != 0:
                kmer_probabilities[i] *= profile['C'][j]
            elif dna_string[i+j] == 'G' and profile['G'][j] != 0:
                kmer_probabilities[i] *= profile['G'][j]
            elif dna_string[i+j] == 'T' and profile['T'][j] != 0:
                kmer_probabilities[i] *= profile['T'][j]

    # normalize the probabilities
    total = sum(kmer_probabilities)
    for i in range(iteration_range):
        kmer_probabilities[i] = kmer_probabilities[i] / total

    # convert list to a running total progression so that we can select a kmer using a random value between 0 and 1
    last_element = 0
    for i in range(iteration_range):
        kmer_probabilities[i] += last_element
        last_element = kmer_probabilities[i]  # save the last element

    # generate a random value between 0 and 1 to select the kmer
    rand_kmer_selector = random.random()
    for i in range(iteration_range):
        # if this is the kmer our random number generator has selected
        if rand_kmer_selector < kmer_probabilities[i]:
            break

    return dna_string[i:i+k]


if __name__ == '__main__':
    rosalind_dna_data = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
                         'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
                         'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
                         'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
                         'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
    print(gibbs_sampler(rosalind_dna_data, 8, 5, 1000))

# ['TCTCGGGG', 'GAGGTATG', 'AAAGAAGT', 'CAAGTTTC', 'AATGTTGG']
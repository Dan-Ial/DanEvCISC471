"""
Homework 2
By: Evelyn Yach (20071956) & Daniel Oh (20063998)
2021.02.02
"""
import math
from HelperFunctions import create_profile, score, find_most_probable_profile


def greedy_motif_search(dna, k, t):
    '''
    conducts greedy motif search
    :param dna: a list of DNA sequences
    :param k: the length of kmers
    :param t: t parameter
    :return: list of best motifs
    '''
    best_motifs = [dna_string[:k] for dna_string in dna]
    best_score = math.inf

    # construct a list of all kmer motifs in the first string of dna
    kmer_motifs, dna_index = [], 0
    while dna_index + k < len(dna[0]) + 1:
        kmer_motifs.append(dna[0][dna_index:dna_index+k])
        dna_index += 1

    for motif in kmer_motifs:
        motifs = [motif]
        for i in range(1, t):
            # form Profile from motifs Motif[1], …, Motif[i - 1]
            profile = create_profile(motifs)
            # find and add the most probable profile
            motifs.append(find_most_probable_profile(dna[i], profile, k))

        current_score = score(motifs)
        if current_score < best_score:
            best_score = score(best_motifs)
            best_motifs = motifs

    return best_motifs


if __name__ == '__main__':
    rosalind_dna_data = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    print(greedy_motif_search(rosalind_dna_data, 3, 5))
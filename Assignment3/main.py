"""
Homework 2
By: Evelyn Yach (20071956) & Daniel Oh (20063998)
2021.02.02
"""

def greedy_motif_search(dna, k, t):
    best_motifs = [dna_string[:k] for dna_string in dna]

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

        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    return best_motifs


def create_profile(motifs):
    '''
    creates a profile from a list of motifs
    :param motifs: a list of motifs
    :return: the profile
    '''
    profile = {'A': [], 'G': [], 'T': [], 'C': []}
    # we iterate through columns so that each element of profile is the same len as motifs[0]
    for i in range(len(motifs[0])):

        a, g, t, c = 0, 0, 0, 0
        for motif in motifs:
            if motif[i] == "A":
                a += 1
            elif motif[i] == "G":
                g += 1
            elif motif[i] == "T":
                t += 1
            elif motif[i] == "C":
                c += 1

        profile["A"].append(a)
        profile["G"].append(g)
        profile["T"].append(t)
        profile["C"].append(c)

    return profile



def find_most_probable_profile(dna_string, profile, k):
    pass # LEFT OFF HERE


def score(motifs):
    pass


if __name__ == '__main__':
    rosalind_dna_data = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    greedy_motif_search(rosalind_dna_data, 3, 5)
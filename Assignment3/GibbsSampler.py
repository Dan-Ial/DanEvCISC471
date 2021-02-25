'''pseudo code
    GIBBSSAMPLER(Dna, k, t, N)
        randomly select k-mers Motifs = (Motif1, …, Motift) in each string
            from Dna
        BestMotifs ← Motifs
        for j ← 1 to N
            i ← Random(t)
            Profile ← profile matrix constructed from all strings in Motifs
                       except for Motifi
            Motifi ← Profile-randomly generated k-mer in the i-th sequence
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        return BestMotifs
'''
import random
import math
from HelperFunctions import create_profile, score, find_most_probable_profile
import operator


def gibbs_sampler(dna, k, t, N):
    # randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    # BestMotifs ← Motifs
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

        motifs[i] = find_most_probable_profile(dna[i], profile, k)

        current_motif_score = score(motifs)
        print(str(current_motif_score) + " " + str(best_motif_score))
        if current_motif_score < best_motif_score:
            best_motif_score = current_motif_score
            best_motifs = motifs

    return best_motifs


if __name__ == '__main__':
    rosalind_dna_data = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
                         'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
                         'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
                         'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
                         'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
    print(gibbs_sampler(rosalind_dna_data, 8, 5, 100))

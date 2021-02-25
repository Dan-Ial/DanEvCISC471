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
    '''
    returns the most probable profile
    :param dna_string: a string of dna
    :param profile: a profile
    :param k: the k parameter
    :return: most probable profile
    '''
    letter = [[] for i in range(k)]
    hamm_dict = {}

    # construct a list of all kmer motifs in the first string of dna
    kmer_motifs, dna_index = [], 0
    while dna_index + k < len(dna_string) + 1:
        kmer_motifs.append(dna_string[dna_index:dna_index+k])
        dna_index += 1

    for a in range(k):
        for j in "ACGT":
            letter[a].append(profile[j][a])

    to_index_helper_dict = {"A": 0, "C": 1, "G": 2, "T": 3}
    index = 1
    for c in kmer_motifs:
        for x in range(len(c)):
            index *= float(letter[x][to_index_helper_dict[c[x]]])
        hamm_dict[c] = index
        index = 1

    final_profile = 0
    for pat, hamm in hamm_dict.items():
        if hamm == max(hamm_dict.values()):
            final_profile = pat
            break

    return final_profile


def score(motifs):
    '''
    calculates the score for motifs
    :param motifs: the motifs we will be scoring
    :return: the score as a float
    '''
    consensus = generate_consensus(motifs)
    score = 0.0
    for motif in motifs:
        consensus_motif_zip = zip(consensus, motif)  # creates a list of tuples (consensus[n], motif[n])
        score += sum(con != mot for con, mot in consensus_motif_zip)
    return round(score, 2)


def generate_consensus(motifs):
    '''
    generates a sister string of consensus for a motif
    note: this is only used in the score() function
    :param motif: the motifs to generate a consensus on
    '''
    consensus = ""
    for i in range(len(motifs[0])):
        a, g, t, c = 0, 0, 0, 0

        for kmer in motifs:
            if kmer[i] == 'A':
                a += 1
            elif kmer[i] == 'G':
                g += 1
            elif kmer[i] == 'T':
                t += 1
            elif kmer[i] == 'C':
                c += 1

        if a >= max(g, t, c):
            consensus += 'A'
        elif g >= max(a, t, c):
            consensus += 'G'
        elif t >= max(a, g, c):
            consensus += 'T'
        elif c >= max(a, g, t):
            consensus += 'C'

    return consensus
"""
Homework 4
By: Evelyn Yach (20071956) & Daniel Oh (20063998)
2021.03.11
"""

def rna_translate(pattern):
    """
    takes in an RNA string and translates it into a string of amino acids
    :param pattern: a string of RNA to translate into amino acid string
    :return peptide: amino acid string translated from the RNA string
    """
    peptide = ""
    stop_codon_reached = False
    for i in range(0, len(pattern), 3):
        codon = pattern[i:i+3]
        if len(codon) == 3:  # make sure this is a valid codon. if codon is not valid, ignore it.
            if codon == 'CAU' or codon == 'CAC':
                # histidine
                peptide += 'H'
            elif codon == 'CAA' or codon == 'CAG':
                # glutamine
                peptide += 'Q'
            elif codon[:-1] == 'CC':
                # proline
                peptide += 'P'
            elif codon[:-1] == 'CG' or codon == 'AGA' or codon == 'AGG':
                # arginine
                peptide += 'R'
            elif codon[:-1] == 'CU' or codon == 'UUG' or codon == 'UUA':
                # leucine
                peptide += 'L'
            elif codon == 'GAU' or codon == 'GAC':
                # aspartic acid
                peptide += 'D'
            elif codon == 'GAA' or codon == 'GAG':
                # glutamic acid
                peptide += 'E'
            elif codon[:-1] == 'GC':
                # alanine
                peptide += 'A'
            elif codon[:-1] == 'GG':
                # glycine
                peptide += 'G'
            elif codon[:-1] == 'GU':
                # valine
                peptide += 'V'
            elif codon == 'UAC' or codon == 'UAU':
                # tyrosine
                peptide += 'Y'
            elif codon[:-1] == 'UC' or codon == 'AGC' or codon == 'AGU':
                # serine
                peptide += 'S'
            elif codon == 'UGC' or codon == 'UGU':
                # cysteine
                peptide += 'C'
            elif codon == 'UGG':
                # tryptophan
                peptide += 'W'
            elif codon == 'UUC' or codon == 'UUU':
                # phenylalanine
                peptide += 'F'
            elif codon == 'AAC' or codon == 'AAU':
                # asparagine
                peptide += 'N'
            elif codon == 'AAA' or codon == 'AAG':
                # lysine
                peptide += 'K'
            elif codon[:-1] == 'AC':
                # threonine
                peptide += 'T'
            elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
                # isoleucine
                peptide += 'I'
            elif codon == 'AUG':
                # methionine
                peptide += 'M'
            elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
                # stop codon
                stop_codon_reached = True
                break
            else:
                print("WARNING: Invalid codon! Codon: " + '"' + codon + '"' + "\n Skipping...")

    if stop_codon_reached:
        return peptide
    else:
        return "No valid stop codon found"

if __name__ == "__main__":
    print(rna_translate("UUUGGGAFVUAG"))
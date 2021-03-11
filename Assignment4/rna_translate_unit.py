"""
Homework 4
By: Evelyn Yach (20071956) & Daniel Oh (20063998)
2021.03.11
"""
from rna_translate import rna_translate

#######################
# POSITIVE TEST CASES #
#######################
def test_rna_translate_rosalind_data():
    print("Positive Test case #1: Rosalind Sample Data")

    rosalind_data_file = open("rosalind_data.txt", "r")
    rosalind_data_list = rosalind_data_file.readlines()
    rosalind_data_file.close()
    rosalind_data_list[0] = rosalind_data_list[0][:-1]  # trim off the new line char

    print("Result: " + str(rna_translate(rosalind_data_list[0]) == rosalind_data_list[1]))
    print()


def test_rna_translate_rosalind_extra_data():
    print("Positive Test case #2: Rosalind Sample Extra Data")

    rosalind_data_extra_file = open("rosalind_data_extra.txt", "r")
    rosalind_data_extra_list = rosalind_data_extra_file.readlines()
    rosalind_data_extra_file.close()
    rosalind_data_extra_list[0] = rosalind_data_extra_list[0][:-1]  # trim off the new line char

    print("Result: " + str(rna_translate(rosalind_data_extra_list[0]) == rosalind_data_extra_list[1]))
    print()


#######################
# NEGATIVE TEST CASES #
#######################
def test_rna_translate_no_stop():
    print("Negative Test case #1: No stop codon")

    rosalind_data_file = open("rosalind_data.txt", "r")
    rosalind_data_list = rosalind_data_file.readlines()
    rosalind_data_file.close()
    rosalind_data_list[0] = rosalind_data_list[0][:-1]  # trim off the new line char

    rosalind_data_list[0] = rosalind_data_list[0][:-3]  # remove the stop codon from the end
    expected_output = "No valid stop codon found"  # returns this error return

    print("Result: " + str(rna_translate(rosalind_data_list[0]) == expected_output))
    print()


def test_rna_translate_invalid_codon():
    print("Negative Test case #2: Invalid Codon")
    print("Note: Should see a warning about an invalid codon")

    rosalind_data_file = open("rosalind_data.txt", "r")
    rosalind_data_list = rosalind_data_file.readlines()
    rosalind_data_file.close()
    rosalind_data_list[0] = rosalind_data_list[0][:-1]  # trim off the new line char

    rosalind_data_list[0] = "ABC" + rosalind_data_list[0]  # add a nonsense codon to the beginning

    # should ignore the invalid codon
    output = rna_translate(rosalind_data_list[0])
    print("Result: " + str(output == rosalind_data_list[1]))
    print()


def run_unit_tests():
    test_rna_translate_rosalind_data()
    test_rna_translate_rosalind_extra_data()
    test_rna_translate_no_stop()
    test_rna_translate_invalid_codon()

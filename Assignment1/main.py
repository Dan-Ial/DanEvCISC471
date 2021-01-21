#Homework 1
#By: Evelyn Yach (20071956)& Daniel Oh (20063998)
#2021.01.19

### 1.1 Frequent k-mer ###
def frequent_k_mer(text, k):
    # error checking
    if text == "":
        return []

    #update frequentPatterns to an empty set
    frequentPatterns = []

    #update count to an array of length |text|-k+1
    count = []
    for i in range(0,len(text)-k+1):
        count.append(0)

    end = k
    #for i <- 0 to |text|-k
    for i in range(0,len(text)-k):
        #update pattern to text(i,k)
        pattern = text[i:end]
        
        #update count(i) to PatternCount helper function
        #PatternCount takes text and pattern as arguments
        count[i] = PatternCount(text, pattern)

        i = i + 1
        end = end + 1
        
    #update maxCount to maximum value in the array count
    maxCount = max(count)

    #for i <- 0 to |text|-k
    end = k
    for j in range(0,len(text)-k):
        #if count(i) = maxCount
        if count[j] == maxCount:
            #add text(i,k) to frequentPatterns
            frequentPatterns.append(text[j:end])

        j = j + 1
        end = end + 1

    #remove duplicates from frequentPatterns
    fp = [] 
    [fp.append(x) for x in frequentPatterns if x not in fp]

    #return frequentPatterns
    return fp

### 1.1 Helper Functions ###
def PatternCount(text, pattern):
    #set num = 0
    num = 0

    #for i <- 0 to |text|-|pattern|
    end = len(pattern)
    for i in range(0,len(text)-len(pattern)):
        #if text(i, |pattern|) = pattern
        if (text[i:end] == pattern):
            #num = num + 1
            num = num + 1

        i = i + 1
        end = end + 1

    #return num
    return num



### 1.2 Frequent k-mer with mismatches ###
def frequent_k_mer_mismatch(text, k, d):
    # error checking
    if text == "":
        return []

    # first, make a dictionary of all possible k length strings
    possible_substrings = []
    for i in range(len(text)-k+1):
        possible_substrings.append(text[i:i+k])

    freq_map = {}
    for p in possible_substrings:
        freq_map[p] = 0

    # iterate through each possible string
    for substring in possible_substrings:
        possible_alt_substring = Neighbors(substring, d)  # generate a set of all possible polymorphed strings
        for alt_substring in possible_alt_substring:  # iterate through all the polymorphed strings
            if alt_substring in text:  # check that the polymorphed substring exists
                freq_map[alt_substring] += 1

    # find the most frequent occurrences
    m = max(freq_map.values())
    return_list = []
    for key in freq_map:
        if freq_map[key] == m:
            return_list.append(key)

    return return_list


### 1.2 Helper Functions ###
def Neighbors(pattern, d):
    # acceptable bases
    bases = "ATCG"

    # check if d is 0
    if d == 0:
        return {pattern}

    # recursion step
    r2 = Neighbors(pattern[1:], d - 1)

    r = [b + r3 for r3 in r2 for b in bases]

    if d < len(pattern):
        # another recursion step
        r2 = Neighbors(pattern[1:], d)

        r = r + [pattern[0] + r3 for r3 in r2]

    return set(r)


'''
Unit Tests
'''
def test_k_mer_positive():
    """
    testing frequent_k_mer multiple results
    """
    fkmer = frequent_k_mer("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
    print("test_k_mer_positive passed: " + str(fkmer == ['GCAT', 'CATG']))


def test_k_mer_negative():
    """
    testing frequent_k_mer no results
    """
    fkmer = frequent_k_mer("", 4)
    print("test_k_mer_negative passed: " + str(fkmer == []))

def test_k_mer_mismatch_positive():
    """
    testing frequent_k_mer_mismatch multiple results
    """
    fkmer = frequent_k_mer_mismatch("ACTATGCATACTATCGGGAACT", 5, 1)
    print("test_k_mer_mismatch_positive passed: " + str(fkmer == ['ACTAT', 'CTATG', 'CTATC']))

def test_k_mer_mismatch_negative():
    """
    testing frequent_k_mer_mismatch no results
    """
    fkmer = frequent_k_mer_mismatch("", 5, 1)
    print("test_k_mer_mismatch_negative passed: " + str(fkmer == []))

### Running Test Cases ###
if __name__ == '__main__':
    test_k_mer_positive()
    test_k_mer_negative()
    test_k_mer_mismatch_positive()
    test_k_mer_mismatch_negative()

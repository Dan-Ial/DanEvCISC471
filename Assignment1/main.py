#Homework 1
#By: Evelyn Yach (20071956)
#2021.01.19

### 1.1 Frequent k-mer ###
def frequent_k_mer(text, k):
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
    #set pattern to an array of strings length 0

    #set freqMap to an empty map

    #set n to the length of text

    #for i from 0 to n-k

        #upate pattern to text(i,k)

        #update neighborhood to the output of function Neighboors
        #Neighboors accepts pattern and d as arguments

        #for j from 0 to size of neighborhood - 1

            #update neighbor to neighborhood[j]

            #if freqMap[neighbor] DNE
                #update freqMap[neighbor] to 1
            #else
                #update freqMap[neighbor] to freqMap[neighbor] + 1

    #set m to MaxMap(freqMap)

    #for every key pattern in freqMap

        #if freqMap[pattern] = m
            #append pattern to patterns

    #return patterns
    return patterns


#main driver function
def main():
    fkmer = frequent_k_mer("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
    print(fkmer)

    fmismmatch = frequent_k_mer_mismatch("ACTATGCATACTATCGGGAACT", 5, 1)
    print(fmismatch)

main()

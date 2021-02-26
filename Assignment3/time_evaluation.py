from greedy import greedy_motif_search
from randomized import IterativeRandomizedMotifSearch
from gibbs import gibbs_sampler
import time

def time_greedy(iterations):
    rosalind_dna_data = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    total_time = 0
    for i in range(iterations):
        start = time.time()
        greedy_motif_search(rosalind_dna_data, 3, 5)
        end = time.time()
        total_time += end - start
    print("Time for greedy: " + str(total_time/iterations))


def time_random(iterations):
    rosalind_dna_data = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    total_time = 0
    for i in range(iterations):
        start = time.time()
        IterativeRandomizedMotifSearch(rosalind_dna_data, 8, 5)
        end = time.time()
        total_time += end - start
    print("Time for random: " + str(total_time/iterations))


def time_gibbs(iterations):
    rosalind_dna_data = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    total_time = 0
    for i in range(iterations):
        start = time.time()
        gibbs_sampler(rosalind_dna_data, 8, 5, 1000)
        end = time.time()
        total_time += end - start
    print("Time for gibbs: " + str(total_time/iterations))


if __name__ == '__main__':
    time_greedy(20)
    time_random(20)
    time_gibbs(20)

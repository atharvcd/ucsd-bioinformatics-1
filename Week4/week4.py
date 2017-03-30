from Week4.week4_utility import *

def randomized_motif_search_problem():
    with open('Datasets/RandomizedMotifSearch/quiz.txt', 'r') as datafile:
        args = datafile.readline().strip().split(" ")
        k = int(args[0])
        t = int(args[1])
        dnas = []
        for i in range(t):
            dnas.append(datafile.readline().strip())

    motifs = randomized_motif_search(dnas, k, t)
    print(str('\n'.join(motifs)))


def gibbs_sampler_problem():
    with open('Datasets/GibbsSampler/quiz.txt', 'r') as datafile:
        args = datafile.readline().strip().split(" ")
        k = int(args[0])
        t = int(args[1])
        dnas = []
        for i in range(t):
            dnas.append(datafile.readline().strip())

    motifs = gibbs_sampler(dnas, k, t, 1000)
    print(str('\n'.join(motifs)))


#randomized_motif_search_problem()
gibbs_sampler_problem()
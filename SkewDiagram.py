from matplotlib import pyplot as plt


def MinimumSkew(Genome):
    positions = []
    skwarry = SkewArray(Genome)
    #Given that there can be many points at which the minimum is reached, it is import to identify all canditates for ori
    minimum = min(skwarry)
    for i in range(len(skwarry)):
        if skwarry[i] == minimum:
            positions.append(i)
    return positions

#The skew of a Genome is particularly important because of the asymmetrical nature of DNA. Because there is more
# Cytosine present on the lagging strand and more Guanine on the leading strand, the point at which Guanine minus
# Cytosine reaches a minimum signifies a potenial origin of replication.

def SkewArray(Genome):
    #The below definition of Skew allows for recursive definition of new list items
    Skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'G':
            Skew.append(Skew[i] + 1)
        elif Genome [i] == 'C':
            Skew.append(Skew[i] - 1)
        else:
            Skew.append(Skew[i])
    return Skew

#An example of application of the above functions lies below

dna_section = 'AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT'

section_skew_array = SkewArray(dna_section)
print(section_skew_array)

section_skew_minimums = MinimumSkew(dna_section)
print(section_skew_minimums)

plt.plot(range(len(section_skew_array)), section_skew_array)
plt.show()

import random

# Markov Factors
d_a = [["d0", "a0", 100],
       ["d0", "a1", 1],
       ["d1", "a0", 1],
       ["d1", "a1", 100]]

a_b = [["a0", "b0", 30],
       ["a0", "b1", 5],
       ["a1", "b0", 1],
       ["a1", "b1", 10]]

b_c = [["b0", "c0", 100],
       ["b0", "c1", 1],
       ["b1", "c0", 1],
       ["b1", "c1", 100]]

c_d = [["c0", "d0", 1],
       ["c0", "d1", 100],
       ["c1", "d0", 100],
       ["c1", "d1", 1]]

# Generate a sample for each of the 4 variables
def samplea(lastsample):
    if lastsample[3] == 0:
        a0 = d_a[0][2] * a_b[1][2]
        a1 = d_a[1][2] * a_b[3][2]
        a1Percent = a1 / (a1 + a0)
        randomVar = random.uniform(0, 1)
        if randomVar <= a1Percent:
            lastsample[0] = 1
        else:
            lastsample[0] = 0
    else:
        a0 = d_a[2][2] * a_b[1][2]
        a1 = d_a[3][2] * a_b[3][2]
        a1Percent = a1 / (a1 + a0)
        randomVar = random.uniform(0, 1)
        if randomVar <= a1Percent:
            lastsample[0] = 1
        else:
            lastsample[0] = 0
    return lastsample


def samplec(lastsample):
    if lastsample[3] == 0:
        c0 = c_d[0][2] * b_c[2][2]
        c1 = c_d[2][2] * b_c[3][2]
        c1Percent = c1 / (c1 + c0)
        randomVar = random.uniform(0, 1)
        if randomVar <= c1Percent:
            lastsample[2] = 1
        else:
            lastsample[2] = 0
    else:
        c0 = c_d[1][2] * b_c[2][2]
        c1 = c_d[3][2] * b_c[3][2]
        c1Percent = c1 / (c1 + c0)
        randomVar = random.uniform(0, 1)
        if randomVar <= c1Percent:
            lastsample[2] = 1
        else:
            lastsample[2] = 0
    return lastsample


def sampled(lastsample):
    # A=0, C=0
    if lastsample[0] == 0 and lastsample[2] == 0:
        d0 = d_a[0][2] * c_d[0][2]
        d1 = d_a[2][2] * c_d[1][2]
        d1Percent = d1 / (d1 + d0)
        randomVar = random.uniform(0, 1)
        if randomVar <= d1Percent:
            lastsample[3] = 1
        else:
            lastsample[3] = 0
    elif lastsample[0] == 1 and lastsample[2] == 0:
        # A=1, C=0
        d0 = d_a[1][2] * c_d[0][2]
        d1 = d_a[3][2] * c_d[1][2]
        d1Percent = d1 / (d1 + d0)
        randomVar = random.uniform(0, 1)
        if randomVar <= d1Percent:
            lastsample[3] = 1
        else:
            lastsample[3] = 0
    elif lastsample[0] == 0 and lastsample[2] == 1:
        # A=0, C=1
        d0 = d_a[0][2] * c_d[2][2]
        d1 = d_a[2][2] * c_d[3][2]
        d1Percent = d1 / (d1 + d0)
        randomVar = random.uniform(0, 1)
        if randomVar <= d1Percent:
            lastsample[3] = 1
        else:
            lastsample[3] = 0
    else:
        # A=1, C=1
        d0 = d_a[1][2] * c_d[2][2]
        d1 = d_a[3][2] * c_d[3][2]
        d1Percent = d1 / (d1 + d0)
        randomVar = random.uniform(0, 1)
        if randomVar <= d1Percent:
            lastsample[3] = 1
        else:
            lastsample[3] = 0
    return lastsample


# Initialize 1st sample  (values can be changed)
lastSample = [1,1,0,0]
print(lastSample)
varToSample = "C"

# Generate Samples
for i in range(1, 20000):
    if varToSample == "A":
        ls = samplea(lastSample)
        print(*ls, sep='')
        lastSample = ls
        varToSample = "C"
    elif varToSample == "C":
        ls = samplec(lastSample)
        print(*ls, sep='')
        lastSample = ls
        varToSample = "D"
    else:
        ls = sampled(lastSample)
        print(*ls, sep='')
        lastSample = ls
        varToSample = "A"


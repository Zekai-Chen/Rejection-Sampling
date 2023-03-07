import pomegranate

from collections import Counter

from model import model

def generate_sample():

    # Mapping of random variable name to sample generated
    sample = {}

    # Mapping of distribution to sample generated
    parents = {}

    # Loop over all states, assuming topological order
    for state in model.states:

        # If we have a non-root node, sample conditional on parents
        if isinstance(state.distribution, pomegranate.ConditionalProbabilityTable):
            sample[state.name] = state.distribution.sample(parent_values=parents)

        # Otherwise, just sample from the distribution alone
        else:
            sample[state.name] = state.distribution.sample()

        # Keep track of the sampled value in the parents mapping
        parents[state.distribution] = sample[state.name]

    # Return generated sample
    return sample

# Rejection sampling
# Compute distribution of Node_D 
N = 10000

data1 = []
data2 = []

for i in range(N):
    sample = generate_sample()
    if sample["Node_C"] == "+c":
        data1.append(sample["Node_D"])
    if (sample["Node_A"] == "-a" and sample["Node_B"] == "+b"):
        data2.append(sample["Node_D"])

print("Observation: c")
print(Counter(data1))

print("Observation: (-a, b)")
print(Counter(data2))


from pomegranate import *

# Node_A node has no parents
Node_A = Node(DiscreteDistribution({
    "+a": 0.0,
    "-a": 1.0
}), name="Node_A")

# Node_B node has no parents
Node_B = Node(DiscreteDistribution({
    "+b": 0.9,
    "-b": 0.1
}), name="Node_B")

# Train Node_C is conditional on Node_A and Node_B
Node_C = Node(ConditionalProbabilityTable([
    ["+a", "+b", "+c", 0.2],
    ["+a", "+b", "-c", 0.8],
    ["+a", "-b", "+c", 0.6],
    ["+a", "-b", "-c", 0.4],
    ["-a", "+b", "+c", 0.5],
    ["-a", "+b", "-c", 0.5],
    ["-a", "-b", "+c", 0.0],
    ["-a", "-b", "-c", 1.0]
], [Node_A.distribution, Node_B.distribution]), name="Node_C")

# Train Node_D is conditional on Node_B and Node_C
Node_D = Node(ConditionalProbabilityTable([
    ["+b", "+c", "+d", 0.75],
    ["+b", "+c", "-d", 0.25],
    ["+b", "-c", "+d", 0.1],
    ["+b", "-c", "-d", 0.9],
    ["-b", "+c", "+d", 0.5],
    ["-b", "+c", "-d", 0.5],
    ["-b", "-c", "+d", 0.2],
    ["-b", "-c", "-d", 0.8]
], [Node_B.distribution, Node_C.distribution]), name="Node_D")

# Create a Bayesian Network and add states
model = BayesianNetwork()
model.add_states(Node_A, Node_B, Node_C, Node_D)

# Add edges connecting nodes
model.add_edge(Node_A, Node_C)
model.add_edge(Node_B, Node_C)
model.add_edge(Node_C, Node_D)
model.add_edge(Node_B, Node_D)

# Finalize model
model.bake()

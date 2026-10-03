'''
Question 1
Take the sample network from our lectures:

3 inputs, two hidden layers of 4 neurons each, one output, 41 parameters. Now remove every activation, so each neuron outputs only its raw weighted sum plus bias.

Prove this 41 parameter network can compute nothing that a simple 3 input to 1 output network (4 parameters, no hidden layers) cannot. 

Do it with matrices: write each layer as a weight matrix times a vector plus a bias, compose the three layers, and show precisely what you are left with.

Handle the biases carefully, they do not simply vanish.

Then show that infinitely many different weight settings across the three layers produce the exact same overall function.

State what this says about using parameter count to measure a model's real power, and in one sentence,

what the activation_function must therefore be doing.
'''

import numpy as np


'''
If we remove activation function it will just dissolve into an simple matrix multiplication (linear regression)

- activation function helps in learning complex patterns 
'''

'''
Does Models Parameters justify the it's relevance

Parameter count is headcount. It tells you how big the crew is, not how good they are. And activation function is close to the least important lever, which is the counterintuitive part.

  Why activation barely matters. Once a nonlinearity is any reasonable shape, the network can route around its quirks by adjusting weights. ReLU, GELU, SwiGLU differ by a few percent at most. Essentially every
  frontier model uses some SwiGLU variant, so it's a constant across the comparison, not a differentiator. The activation was a big deal in 2012 when ReLU replaced sigmoid and made deep training possible. Since
  then it's plumbing.

  What actually moves the needle:

  - Training data volume.
  - Compute spent. Roughly parameters times tokens. This is the real scaling axis.
  - Architecture.
  - Post-training. Instruction tuning and RLHF change behavior enormously with almost no new parameters.
  - Inference-time compute (when an new data is provided model tries to map it with)

'''



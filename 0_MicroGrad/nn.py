from engine import Value
import random

class Neuron:
  def __init__(self, ninput):
    self.w = [Value(random.uniform(-1, 1)) for _ in range(ninput)]
    self.b = Value(random.uniform(-1, 1))

  def __call__(self, x):
    # w * x + b
    act = sum((xi*wi for xi, wi in zip(x, self.w)), self.b)
    out = act.tanh()
    return out
  
  def parameters(self):
    return self.w + [self.b]

class Layer:
  def __init__(self, ninput, noutput):
    self.neurons = [Neuron(ninput) for _ in range(noutput)]
 
  def __call__(self, x):
    outs = [neuron(x) for neuron in self.neurons]
    return outs[0] if len(outs) == 1 else outs
  
  def parameters(self):
    return [param for neuron in self.neurons for param in neuron.parameters()]

class MLP:
  def __init__(self, ninput, noutputs): 
    size = [ninput] + noutputs
    self.layers = [Layer(size[i], size[i+1]) for i in range(len(noutputs))]

  def __call__(self, x):
    for layer in self.layers:
      x = layer(x)
    return x
  
  def parameters(self):
    return [param for layer in self.layers for param in layer.parameters()]
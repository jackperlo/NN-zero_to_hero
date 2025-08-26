# 🌱 Micrograd

**Micrograd** is a lightweight **auto-grad engine**.  
The term *autograd* stands for **automatic differentiation**, which enables **backpropagation**.

---

## 🔄 What is Backpropagation?

Backpropagation is an algorithm that efficiently computes the **gradient of a loss function** with respect to the **weights of a neural network**.  

This allows us to **iteratively update the weights** in order to **minimize the loss function**, which in turn **improves the accuracy of the model**.  

In simple terms:  
👉 Backpropagation is the **recursive application of the chain rule** *backwards* through the computational graph.

---

## 📚 Topics Covered

- 🧮 **Local Derivative Computation** – Finding gradients of simple operations  
- 🔗 **Chain Rule for Derivative Computation** – Combining local gradients across a graph  
- 🔄 **Manual Backward Propagation** – Explicitly applying derivatives step by step  
- 📊 **Loss Function (MSE)** – Measuring prediction error with *Mean Squared Error*  
- 📉 **Gradient Descent Step** – Updating parameters to reduce loss  
- 📦 **Training Batch Size Parameter** – Controlling how much data is processed per step  
- 🧠 **Multi-Layer Perceptron (MLP)** – The simplest neural network built from Micrograd  

---

✨ With these building blocks, we can construct and train **simple neural networks from scratch**!

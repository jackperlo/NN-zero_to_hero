# ✨ Makemore

**Makemore** is a simple yet powerful project that demonstrates how language models can be built **from scratch**.  
It starts with a **bigram model**, where the **next token** is predicted based **only on the previous token**.  

While simple, this model lays the groundwork for understanding more advanced architectures like **n-grams, RNNs, and Transformers**.

---

## 🔎 What is a Bigram Model?

A **bigram model** predicts the next symbol (character or token) based solely on the **current one**.  
For example:  

- "H" → predicts "e"  
- "e" → predicts "l"  
- "l" → predicts "l"  
- "l" → predicts "o"  

This step-by-step process lets us **generate sequences** and understand the **probabilistic structure** of language.

---

## 📚 Topics Covered

- 🔄 **Broadcasting Rule in PyTorch** – Leveraging tensor shapes efficiently  
- 📊 **Log-Likelihood** – Measuring how well the model fits the data  
- 🧹 **Model Smoothing** – Handling unseen tokens in training data  
- 🎭 **One-Hot Encoding** – Representing categorical tokens as vectors  
- 🔥 **Softmax** – Converting logits into probability distributions  
- 🛡 **L2 Regularization** – Preventing overfitting by penalizing large weights  

---

## 🚀 Why It Matters

✨ With Makemore, you gain a **hands-on understanding** of how models like GPT are built from the ground up!

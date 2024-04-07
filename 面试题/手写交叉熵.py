"""手动实现Softmax和CrossEntropyLoss函数"""
import numpy as np


class CrossEntropyLoss:
    def softmax(self, input):
        exp_input = np.exp(input - np.max(input, axis=1, keepdims=True))
        sum_exp_input = np.sum(exp_input, axis=1, keepdims=True)
        output_probs = exp_input / sum_exp_input
        return output_probs

    def cross_entropy_loss(self, input, labels):
        output_probs = self.softmax(input)
        batch_size = output_probs.shape[0]
        loss = -np.sum(labels * np.log(output_probs + 1e-9)) / batch_size
        return loss


logits = np.array([[2.0, 1.0, 0.1],
                   [0.1, 3.0, 0.2],
                   [0.2, 0.2, 2.8]])
labels = np.array([[0, 0, 1],
                   [0, 1, 0],
                   [1, 0, 0]])
g = CrossEntropyLoss()
softmax_output = g.softmax(logits)
print("Softmax is :", "\n", softmax_output)

loss = g.cross_entropy_loss(logits, labels)
print("Cross Entropy Loss is :", loss)




















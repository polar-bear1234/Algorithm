"""Encoder-Decoder"""

import torch
import torch.nn as nn
import torch.nn.functional as F

class EncoderLayer(nn.Module):
    def __init__(self, d_model, heads, dropout=0.1):
        super.__init__()
        self.norm_1 = Norm(d_model)
        self.norm_2 = Norm(d_model)
        self.att =

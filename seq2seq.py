#imports
import torch
import torch.nn as nn
import torch.optim as optim

#encoder
class Encoder(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(Encoder, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)

    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)  # Initialize hidden state
        c0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)  # Initialize cell state
        out, _ = self.lstm(x, (h0, c0))  # Forward propagate LSTM
        return out[:, -1, :]  # Return last hidden state

class Decoder(nn.Module):
    def __init__(self, hidden_size, output_size):
        super(Decoder, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(hidden_size, hidden_size, batch_first=True)
        self.out = nn.Linear(hidden_size, output_size)

    def forward(self, x, hidden):
        out, _ = self.lstm(x.unsqueeze(1), hidden)  # Pass decoder input through LSTM
        out = self.out(out)  # Pass LSTM output through linear layer
        return out

class Seq2Seq(nn.Module):
    def __init__(self, encoder, decoder):
        super(Seq2Seq, self).__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, src, trg):
        batch_size = trg.shape[0]
        trg_len = trg.shape[1]
        trg_vocab_size = trg.max().item() + 1
        outputs = torch.zeros(batch_size, trg_len, trg_vocab_size).to(src.device)
        
        # Encode
        encoder_hidden = self.encoder(src)
        
        # Decode
        for t in range(1, trg_len):
            output, hidden = self.decoder(trg[:, t-1], encoder_hidden)
            outputs[:, t, :] = output
        
        return outputs

input_size = 10  # Size of input features
hidden_size = 20  # Hidden size of LSTM
output_size = 10  # Size of output features

encoder = Encoder(input_size, hidden_size)
decoder = Decoder(hidden_size, output_size)
model = Seq2Seq(encoder, decoder)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Dummy input and target tensors for demonstration
src = torch.randn(64, 10)  # Source sequence of length 10
trg = torch.randint(0, 10, (64, 10))  # Target sequence of length 10, each element is a random integer between 0 and 9

# Forward pass
outputs = model(src, trg)

# Compute loss
loss = criterion(outputs.view(-1, output_size), trg.view(-1))

# Backward pass and optimization
loss.backward()
optimizer.step()

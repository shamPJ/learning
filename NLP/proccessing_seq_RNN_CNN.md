# Notes to "Hands-on ML" A.Geron

## Recurrent neurons and layers

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1*mHimR6ok4bAEYhKESwhdrg.png&f=1&nofb=1&ipt=2d1648050764fec491c45e88ea9ab456624b46046ce370ba0b07caecd92ec2dc&ipo=images">

Simple case - hidden state == output:

We feed in vector $\mathbf{x}_{t}$ at time $t$ to a reccurent neuron and getting output scalar ${y}_{t}$.
For one layer and one datapoint (output is also a vector now $\mathbf{y}_{t}$):

$\mathbf{y}_{t} = \phi( \mathbf{W}_{x}^{T}\mathbf{x}_{t} + \mathbf{W}_{y}^{T}\mathbf{y}_{t-1} + \mathbf{b})$

- $\mathbf{y}_{t} - ({n}_{neurons},1)$ and $\mathbf{x}_{t} - ({n}_{in},1)$
- $\mathbf{W}_{x} - ({n}_{in}, {n}_{neurons})$ --> $\mathbf{W}_{x}^{T}\mathbf{x}_{t} - ({n}_{neurons},1)$
- $\mathbf{W}_{y} - ({n}_{neurons}, {n}_{neurons})$ --> $\mathbf{W}_{y}^{T}\mathbf{y}_{t-1}- ({n}_{neurons},1)$

Activation function - usually tanh.

For one layer and all datapoints ($m$ n.o. samples in a batch):

$\mathbf{Y}_{t} = \phi( \mathbf{X}_{t} \mathbf{W}_{x}+ \mathbf{Y}_{t-1}\mathbf{W}_{y} + \mathbf{b}) = $ 
$                 \phi( (\mathbf{X}_{t} + \mathbf{Y}_{t-1}) \mathbf{W} + \mathbf{b}) $ 

- $\mathbf{Y}_{t} - (m, {n}_{neurons})$ and $\mathbf{X}_{t} - (m, {n}_{in})$
- $\mathbf{W}_{x} - ({n}_{in}, {n}_{neurons})$ --> $\mathbf{X}_{t}\mathbf{W}_{x} - (m, {n}_{neurons})$
- $\mathbf{W}_{y} - ({n}_{neurons}, {n}_{neurons})$ --> $\mathbf{Y}_{t-1}\mathbf{W}_{y} - (m, {n}_{neurons})$

Output at time $t$ - depends on all inputs from prev. time steps --> memory. Vanilla RNN - can "memorize" about 10 last steps.
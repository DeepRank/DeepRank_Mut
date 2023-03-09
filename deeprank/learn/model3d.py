import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

######################################################################
#
# Model automatically generated by modelGenerator
#
######################################################################

# ----------------------------------------------------------------------
# Network Structure
# ----------------------------------------------------------------------
# conv layer   0: conv | input -1  output  4  kernel  2  post relu
# conv layer   1: pool | kernel  2  post None
# conv layer   2: conv | input  4  output  5  kernel  2  post relu
# conv layer   3: pool | kernel  2  post None
# fc   layer   0: fc   | input -1  output  84  post relu
# fc   layer   1: fc   | input  84  output  1  post None
# ----------------------------------------------------------------------


class cnn_reg(nn.Module):

    def __init__(self, input_shape):
        super(cnn_reg, self).__init__()

        self.convlayer_000 = nn.Conv3d(input_shape[0], 4, kernel_size=2)
        self.convlayer_001 = nn.MaxPool3d((2, 2, 2))
        self.convlayer_002 = nn.Conv3d(4, 5, kernel_size=2)
        self.convlayer_003 = nn.MaxPool3d((2, 2, 2))

        size = self._get_conv_output(input_shape)

        self.fclayer_000 = nn.Linear(size, 84)
        self.fclayer_001 = nn.Linear(84, 1)

    def _get_conv_output(self, shape):
        num_data_points = 2
        inp = Variable(torch.rand(num_data_points, *shape))
        out = self._forward_features(inp)
        return out.data.view(num_data_points, -1).size(1)

    def _forward_features(self, x):
        x = F.relu(self.convlayer_000(x))
        x = self.convlayer_001(x)
        x = F.relu(self.convlayer_002(x))
        x = self.convlayer_003(x)
        return x

    def forward(self, x):
        x = self._forward_features(x)
        x = x.view(x.size(0), -1)
        x = F.relu(self.fclayer_000(x))
        x = self.fclayer_001(x)
        return x


######################################################################
#
# Model automatically generated by modelGenerator
#
######################################################################

# ----------------------------------------------------------------------
# Network Structure
# ----------------------------------------------------------------------
# conv layer   0: conv | input -1  output  4  kernel  2  post relu
# conv layer   1: conv | input  4  output  4  kernel  2
# conv layer   2: pool | kernel  2  post None
# conv layer   3: conv | input  4  output  5  kernel  2  post relu
# conv layer   4: pool | kernel  2  post None
# fc   layer   0: fc   | input -1  output  84  post relu
# fc   layer   1: fc   | input  84  output  1  post None
# ----------------------------------------------------------------------

class cnn_class(nn.Module):

    def __init__(self, input_shape):
        super(cnn_class, self).__init__()

        self.convlayer_000 = nn.BatchNorm3d(input_shape[0])
        self.convlayer_001 = nn.Conv3d(input_shape[0], int(input_shape[0]//2), kernel_size=2)
        self.convlayer_002 = nn.BatchNorm3d(input_shape[0])
        self.convlayer_003 = nn.Conv3d(int(input_shape[0]//2), int(input_shape[0]//2), kernel_size=2)
        self.convlayer_004 = nn.MaxPool3d((2, 2, 2))
        self.convlayer_005 = nn.Conv3d(int(input_shape[0]//2), int(input_shape[0]//2), kernel_size=2)

        size = self._get_conv_output(input_shape)

        self.fclayer_000 = nn.Linear(size, 84)
        self.fclayer_001 = nn.Linear(84, 2)
        
        self.dropout= nn.Dropout(p=0.5)

    def _get_conv_output(self, shape):
        inp = Variable(torch.rand(1, *shape))
        out = self._forward_features(inp)
        return out.data.view(1, -1).size(1)

    def _forward_features(self, x):
        x = F.relu(self.convlayer_001(x))
        x = F.relu(self.convlayer_003(x))
        x = self.convlayer_004(x)
        x = F.relu(self.convlayer_005(x))
        return x

    def forward(self, x):
        x = self._forward_features(x)
        x = x.view(x.size(0), -1)
        x = self.dropout(x)
        x = F.relu(self.fclayer_000(x))
        x = self.dropout(x)
        x = self.fclayer_001(x)
        return x

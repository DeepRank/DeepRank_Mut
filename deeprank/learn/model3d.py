import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F


######################################################################
#
# Model automatically generated by modelGenerator
#
######################################################################

#----------------------------------------------------------------------
# Network Structure
#----------------------------------------------------------------------
#conv layer   0: conv | input -1  output  4  kernel  2  post relu
#conv layer   1: pool | kernel  2  post None
#conv layer   2: conv | input  4  output  5  kernel  2  post relu
#conv layer   3: pool | kernel  2  post None
#fc   layer   0: fc   | input -1  output  84  post relu
#fc   layer   1: fc   | input  84  output  1  post None
#----------------------------------------------------------------------

class cnn(nn.Module):

    def __init__(self,input_shape):
        super(cnn,self).__init__()

        self.convlayer_000 = nn.Conv3d(input_shape[0],4,kernel_size=2)
        self.convlayer_001 = nn.MaxPool3d((2,2,2))
        self.convlayer_002 = nn.Conv3d(4,5,kernel_size=2)
        self.convlayer_003 = nn.MaxPool3d((2,2,2))

        size = self._get_conv_output(input_shape)

        self.fclayer_000 = nn.Linear(size,84)
        self.fclayer_001 = nn.Linear(84,1)


    def _get_conv_output(self,shape):
        inp = Variable(torch.rand(1,*shape))
        out = self._forward_features(inp)
        return out.data.view(1,-1).size(1)

    def _forward_features(self,x):
        x = F.relu(self.convlayer_000(x))
        x = self.convlayer_001(x)
        x = F.relu(self.convlayer_002(x))
        x = self.convlayer_003(x)
        return x

    def forward(self,x):
        x = self._forward_features(x)
        x = x.view(x.size(0),-1)
        x = F.relu(self.fclayer_000(x))
        x = self.fclayer_001(x)
        return x



######################################################################
#
# Model automatically generated by modelGenerator
#
######################################################################

#----------------------------------------------------------------------
# Network Structure
#----------------------------------------------------------------------
#conv layer   0: conv | input -1  output  4  kernel  2  post relu
#conv layer   1: pool | kernel  2  post None
#conv layer   2: conv | input  4  output  5  kernel  2  post relu
#conv layer   3: pool | kernel  2  post None
#fc   layer   0: fc   | input -1  output  84  post relu
#fc   layer   1: fc   | input  84  output  1  post None
#----------------------------------------------------------------------

class cnn_class(nn.Module):

    def __init__(self,input_shape):
        super(cnn_class,self).__init__()

        self.convlayer_000 = nn.Conv3d(input_shape[0],4,kernel_size=2)
        self.convlayer_001 = nn.MaxPool3d((2,2,2))
        self.convlayer_002 = nn.Conv3d(4,5,kernel_size=2)
        self.convlayer_003 = nn.MaxPool3d((2,2,2))

        size = self._get_conv_output(input_shape)

        self.fclayer_000 = nn.Linear(size,84)
        self.fclayer_001 = nn.Linear(84,2)


    def _get_conv_output(self,shape):
        inp = Variable(torch.rand(1,*shape))
        out = self._forward_features(inp)
        return out.data.view(1,-1).size(1)

    def _forward_features(self,x):
        x = F.relu(self.convlayer_000(x))
        x = self.convlayer_001(x)
        x = F.relu(self.convlayer_002(x))
        x = self.convlayer_003(x)
        return x

    def forward(self,x):
        x = self._forward_features(x)
        x = x.view(x.size(0),-1)
        x = F.relu(self.fclayer_000(x))
        x = self.fclayer_001(x)
        return x

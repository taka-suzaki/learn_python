class ImageSize:
    def __init__(self, width, height, channel):
        self.width = width
        self.height = height
        self.channel = channel
        
    def __str__(self):
        return f"ImSize(w:{self.width}, h:{self.height}, c:{self.channel})"

    def __repr__(self):
        return self.__str__()
        
        
class Layer:
    def __init__(self, out_channel, kernel_size, stride=1, padding=0, deliation=1):
        if type(kernel_size) is int:
            kernel_size = (kernel_size, kernel_size)
        if type(stride) is int:
            stride = (stride, stride)
        if type(padding) is int:
            padding = (padding, padding)
        if type(deliation) is int:
            deliation = (deliation, deliation)
        self.out_channel = out_channel
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.deliation = deliation
        
    def next_size(self, image_size: ImageSize):
        w_out = int((image_size.height + 2 * self.padding[0] - self.deliation[0] * (self.kernel_size[0] - 1) - 1)/ self.stride[0] + 1)
        h_out = int((image_size.height + 2 * self.padding[1] - self.deliation[1] * (self.kernel_size[1] - 1) - 1)/ self.stride[1] + 1)
        return ImageSize(w_out, h_out, self.out_channel)
    

if __name__ == "__main__":
    input_size = ImageSize(160, 160, 1)
    print(input_size)
    conv1 = Layer(out_channel=16, kernel_size=6, stride=2,)
    h1 = conv1.next_size(input_size)
    conv2 = Layer(out_channel=32, kernel_size=3,)
    h2 = conv2.next_size(h1)
    print(h1)
    print(h2)
    


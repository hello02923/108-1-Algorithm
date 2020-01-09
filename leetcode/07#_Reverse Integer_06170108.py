    def reverse(self, x):
        x_max=2**31-1
        x_min=-2**31
        if x<0:
            x=-1*int(str(0-x)[::-1])
        else:
            x=int(str(x)[::-1])
        if x>x_max or x<x_min:
            return 0
        return x
        
        
        ####

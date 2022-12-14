import numpy as np

class TinyStatistician:

    def mean(self, x):
        if isinstance(x, np.ndarray) or isinstance(x,list):
            length = len(x)
            if length:
                try:
                    return(sum(x) / length)
                except:
                    return None

    def median(self, x):
        if isinstance(x, np.ndarray) or isinstance(x,list):
            length = len(x)
            mid = length // 2
            ordered = sorted(x)
            try:
                if length % 2:
                    return ordered[mid] / 1
                elif length:
                    return (ordered[mid] + ordered[mid - 1]) / 2
            except:
                return None
    
    def quartile(self, x):
        if isinstance(x, np.ndarray) or isinstance(x,list):
            length = len(x)
            ordered = sorted(x)
            if length:
                try:
                    quotient = (length - 1) / 4
                    first = ordered[int(quotient)] + (quotient - int(quotient)) * (ordered[int(quotient) + 1] - ordered[int(quotient)])
                    quotient*=3    
                    third = ordered[int(quotient)] + (quotient - int(quotient)) * (ordered[int(quotient) + 1] - ordered[int(quotient)])
                    return ([first, third])
                except:
                    return None
            
    def var(self, x):
        if isinstance(x, np.ndarray) or isinstance(x,list):
            length = len(x)
            if length:
                try:
                    mean = self.mean(x)
                    return (sum((i - mean)**2 for i in x) / length)
                except:
                    return None
    
    def std(self, x):
        if isinstance(x, np.ndarray) or isinstance(x,list):
            if len(x):
                try:
                    return (self.var(x)**0.5)
                except:
                    return None
# defuzz.py
# Eduardo Avelar
# October 2018

import numpy as np

def defuzz(x, y, w, defuzz_method):
    
    if defuzz_method is 'centroid':
        if w ==0:
            total_area = sum(y)
            return sum(y * x) / total_area
        else:
            area = np.zeros(len(x))
            for i in range(len(x)):
                area[i] = w[i]/2*(2*y[i]-y[i]*y[i])
            return sum(x * area)    
    elif defuzz_method is 'bisector':
        total_area = sum(y)
        data_n = len(x)
        tmp = y[0]
        for k in range(1, data_n):
            tmp = tmp + y[k]
            if tmp >= total_area/2:
                break
        return x[k]
    elif defuzz_method is 'mom':
        return np.mean(x[y == max(y)])
    elif defuzz_method is 'som':
        tmp = x[y == max(y)]
        which = np.argmin(abs(tmp))
        return tmp[which]
    elif defuzz_method is 'lom':
        tmp = x[y == max(y)]
        which = np.argmax(abs(tmp))
        return tmp[which]
    elif defuzz_method is 'wtaver':
        return sum(x * y) / sum (y)
    else:
        raise ValueError('The input for `type`, %s, was incorrect.' % (type))
    
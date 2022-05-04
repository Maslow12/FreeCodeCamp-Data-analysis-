import numpy as np

def calculate(list1):
    if len(list1) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        a = np.array(list1).reshape(3,3)
        calculations = {
            'mean':list([a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), a.mean().tolist()]),
            'variance':list([a.var(axis=0).tolist(), a.var(axis=1).tolist(), a.var().tolist()]),
            'standard deviation':list([a.std(axis=0).tolist(), a.std(axis=1).tolist(), a.std().tolist()]),
            'max':list([a.max(axis=0).tolist(), a.max(axis=1).tolist(), a.max().tolist()]),
            'min':list([a.min(axis=0).tolist(), a.min(axis=1).tolist(), a.min().tolist()]),
            'sum':list([a.sum(axis=0).tolist(), a.sum(axis=1).tolist(), a.sum().tolist()])
        }            
        retu2,3,4,5,6,7,8]))
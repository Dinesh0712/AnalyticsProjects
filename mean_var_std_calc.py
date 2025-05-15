import numpy as np
np.set_printoptions(legacy='1.25')

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    lst = np.array(list)    
    
    mean1 = [lst[0:2].mean(), lst[3:5].mean() , lst[6:8].mean()]
    mean2 = [lst[0: :3].mean(), lst[1: :3].mean() , lst[2: :3].mean()]

    var2 = [lst[0: :3].var(), lst[1: :3].var() , lst[2: :3].var()]
    var1 = [lst[0:2].var(), lst[3:5].var() , lst[6:8].var()]
    
    std2 = [lst[0: :3].std(), lst[1: :3].std() , lst[2: :3].std()]
    std1 = [lst[0:2].std(), lst[3:5].std() , lst[6:8].std()]

    max2 = [lst[0: :3].max(), lst[1: :3].max() , lst[2: :3].max()]
    max1 = [lst[0:2].max(), lst[3:5].max() , lst[6:8].max()]

    min2 = [lst[0: :3].min(), lst[1: :3].min() , lst[2: :3].min()]
    min1 = [lst[0:2].min(), lst[3:5].min() , lst[6:8].min()]

    sum2 = [lst[0: :3].sum(), lst[1: :3].sum() , lst[2: :3].sum()]
    sum1 = [lst[0:2].sum(), lst[3:5].sum() , lst[6:8].sum()]


    
    return {
        'mean': [mean1, mean2, lst.mean()],
        'variance': [var1, var2, lst.var()],
        'standard deviation': [std1, std2, lst.std()],
        'max': [max1, max2, lst.max()],
        'min': [min1, min2, lst.min()],
        'sum': [sum1, sum2, lst.sum()]

         }
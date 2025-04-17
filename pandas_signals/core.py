
import pandas as pd

def exrem(primary: pd.Series, secondary: pd.Series) -> pd.Series:
    result = pd.Series(False, index=primary.index)
    active = False
    for i in range(len(primary)):
        if not active and primary.iloc[i]:
            result.iloc[i] = True
            active = True
        elif secondary.iloc[i]:
            active = False
    return result

def flip(primary: pd.Series, secondary: pd.Series) -> pd.Series:
    result = pd.Series(False, index=primary.index)
    active = False
    for i in range(len(primary)):
        if primary.iloc[i]:
            active = True
        elif secondary.iloc[i]:
            active = False
        result.iloc[i] = active
    return result

def valuewhen(expr: pd.Series, array: pd.Series, n: int = 1) -> pd.Series:
    result = pd.Series(index=array.index, dtype=array.dtype)
    true_indices = expr[expr].index.tolist()
    for i in range(len(array)):
        recent_trues = [t for t in true_indices if t <= array.index[i]]
        if len(recent_trues) >= n:
            target_index = recent_trues[-n]
            result.iloc[i] = array.loc[target_index]
        else:
            result.iloc[i] = pd.NA
    return result

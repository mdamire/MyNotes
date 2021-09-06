import pandas as pd
import math

class Node():
    def __init__(self, att, ntype, node_dict):
        self.att = att
        self.type = ntype
        self.ndict = node_dict



def percentage(val, vlist) -> float:
    return (vlist.count(val)) / len(vlist)

def entropy(vlist) -> float:
    uset = set(vlist)
    res = 0.0
    for i in uset:
        per = percentage(i, vlist)
        log = math.log2(per)
        res += (per * log)

    res = -(res)

    return res

def entropy_respestive(df: pd.DataFrame, target_col, decision_col) -> float:
    ulist = list(df.iloc[:, target_col])
    uset = set(ulist)
    
    res = 0.0
    for i in uset:
        px = percentage(i, ulist)
        dfc = df[df.iloc[:, target_col] == i]
        en = entropy(list(dfc.iloc[:, decision_col]))
        res += (px * en)

    return res

def trainer(df: pd.DataFrame, decision_col):
    col_len = len(df.columns)
    des_entropy = entropy(list(df.iloc[:,decision_col]))
    if des_entropy == 0:
        return Node(df.iloc[0,decision_col], 'l', {})

    max_gain = 0.0
    rcol = -1

    for i in range(col_len):
        if i == decision_col:
            continue

        res_entropy = entropy_respestive(df, i, decision_col)
        gain = des_entropy - res_entropy

        if gain > max_gain:
            max_gain = gain
            rcol = i

    d = {}
    for col_val in set(df.iloc[:, rcol]):
        dfc = df[df.iloc[:, rcol] == col_val]
        del dfc[dfc.columns[rcol]]
        d[col_val] = trainer(dfc, (decision_col - 1))

    return Node(df.columns[rcol], 'd', d)

def print_tree(n: Node, depth):
    print(" " * depth, "#", n.att)
    for i in n.ndict:
        print(" " * (depth+1), "-", str(i), ":")
        print_tree(n.ndict[i], depth + 4)

def predict(node: Node, df: pd.DataFrame):
    if node.type == 'l':
        return node.att

    v = df.loc[0, node.att]
    if v not in node.ndict:
        return ""
        
    n2 = node.ndict[v]

    return predict(n2, df)

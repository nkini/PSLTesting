import sys
import pandas as pd
import matplotlib
import re

def get_consensus_values(logfile):
    cols_pattern = re.compile('(SAME\([^\)]*\))')
    vals_pattern = re.compile('([\d\.]+)')
    vals = []
    with open(logfile) as f:
        linenum = 1
        for line in f:            
            if linenum == 1:
                colnames = cols_pattern.findall(line.strip())
                print(colnames)
            else:
                vals.append(list(map(float, vals_pattern.findall(line.strip()))))
            linenum += 1
    return pd.DataFrame(vals, columns=colnames)
                

logfile = sys.argv[1]
dfconsensus = get_consensus_values(logfile)
print(dfconsensus)

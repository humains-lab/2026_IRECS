# J. de la Torre-López, A. Ramírez, J.R. Romero.
# "Automatic selection of primary studies in systematic reviews with evolutionary rule-based classification".
# 2025.

from datetime import datetime

startTime = datetime.now()

"""Message for the log"""
def log(msg, omitNewLine = False):
    outputFile = "log.txt"
    f = open(outputFile, 'a+')
    
    if not omitNewLine:
        f.write(str(datetime.now()) + ' | ' +  msg +'\n')
    else:         
        f.write(msg)
    f.flush()
    f.close()

"""Logs a complete new line of results in the results file."""
def logResult(resultLine, omitTime = False):
    outputFile = "results.txt"
    f = open(outputFile, 'a+')   
    executionTime = (datetime.now() - startTime).total_seconds() / 60.0 
    if not omitTime:
        f.write(f'{resultLine};{executionTime}\n')
    else:
        f.write(f'{resultLine}\n')
    f.flush()
    f.close()

"""Logs a complete new line of results in the results file."""
def logStatistics(resultLine, omitTime = False):
    outputFile = "resultsStatistics.txt"
    f = open(outputFile, 'a+')   
    executionTime = (datetime.now() - startTime).total_seconds() / 60.0 
    if not omitTime:
        f.write(f'{resultLine};{executionTime}\n')
    else:
        f.write(f'{resultLine}\n')
    f.flush()
    f.close()

def setExecutionTimer():
    global startTime
    startTime = datetime.now()
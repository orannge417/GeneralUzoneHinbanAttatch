
import pandas as pd
from tqdm import tqdm

from . import method

def attachUzone(mainDF, uZoneDF, editCol):

    if(editCol != "純正品番"):
        uZoneDF = uZoneDF.rename(columns={"純正品番":editCol})
    uZoneDF = uZoneDF.rename(columns={"Uzone品番":"Uzone品番_" + editCol})
    
    mainDF = method.hifenReplace(mainDF, editCol)
    uZoneDF = method.hifenReplace(uZoneDF, editCol)
    colNum = mainDF.columns.get_loc(editCol)

    print(mainDF)
    mainDF.insert(colNum+1, "Uzone品番_" + editCol, "")
    print(mainDF)

    mainDF[editCol] = mainDF[editCol].astype(str) 
    uZoneDF[editCol] = uZoneDF[editCol].astype(str) 
    mainDF["Uzone品番_" + editCol] = mainDF["Uzone品番_" + editCol].astype(str) 
    uZoneDF["Uzone品番_" + editCol] = uZoneDF["Uzone品番_" + editCol].astype(str) 

    mainDF = pd.merge(mainDF, uZoneDF, on=editCol, how="left")
    mainDF = method.mergeRowNameFix(mainDF, "Uzone品番_" + editCol)

    return mainDF   
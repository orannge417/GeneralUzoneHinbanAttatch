import pandas as pd
import numpy as np

def readCSV(fileName):  
    try: 
        df = pd.read_csv("GeneralUzoneHinbanAttach//inputdata//" + fileName, encoding="cp932")
    except:
        df = pd.read_csv("GeneralUzoneHinbanAttach//inputdata//" + fileName, encoding="utf-8")

    return(df)

def hifenReplace(df, colName):
    df.loc[:, colName] = df.loc[:, colName].str.replace("-", "")
    return df

def renameDrop(df, colName):
    df = df.rename(columns={colName+"_x":colName})
    df = df.drop(columns=colName+"_y")
    return df

def mergeRowNameFix(mainDF, colName):
    
    if(mainDF.loc[:, colName+"_x"].empty):
        print("元々の情報なし")
        mainDF.loc[:, colName+"_x"] = mainDF.loc[:, colName+"_y"] 
        mainDF = renameDrop(mainDF, colName)
        return mainDF

    elif(mainDF.loc[:, colName+"_y"].empty):
        print("追加する情報なし")
        mainDF = renameDrop(mainDF, colName)
        return mainDF

    else:
        for i, cell in enumerate(mainDF.loc[:, colName+"_x"]):
            try:
                if(np.isnan(cell) or cell == ""):
                    mainDF.loc[i, colName+"_x"] = mainDF.loc[i, colName+"_y"] 
            except:
                if cell == "":
                    mainDF.loc[i, colName+"_x"] = mainDF.loc[i, colName+"_y"] 

        mainDF = renameDrop(mainDF, colName)
        return mainDF

def dropCol(df, colName):
    try:
        df = df.drop(columns=[colName])
    except:
        pass
    return df


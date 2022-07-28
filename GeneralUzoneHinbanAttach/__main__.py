# アクセラ用　アーネストデータ整理プログラム

import datetime
from time import strftime
import os

from GeneralUzoneHinbanAttach.basicInfo import *

def main():
    today = datetime.datetime.today()
    todaystr = "{0:%Y%m%d}".format(today)

    inputFileName = input("読み込むファイルの名前を指定してください\n")
    mainDF = method.readCSV(inputFileName + ".csv")
    
    editCol = input("比較する列の名前を指定してください\n")
    uZoneDF = method.readCSV("UZone品番リスト.csv")

    print(mainDF, uZoneDF)

    mainDF = attachUzone(mainDF, uZoneDF, editCol)

    
    try:
        mainDF.to_csv(todaystr + "_"+ inputFileName + "出力.csv", encoding="cp932", index=False)
    except PermissionError:
        print(todaystr + "_"+ inputFileName + "出力.csvを閉じてください")

        while(True):
            y = input("yを押したら再開します\n")

            if(y == "y"):
                break
        mainDF.to_csv(todaystr + "_"+ inputFileName + "出力.csv", encoding="cp932", index=False)


if __name__ == "__main__":
    main()
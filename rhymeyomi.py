import tkinter as tk
import tkextrafont as tkfont
import jaconv as jv
import pandas as pd
import xlrd
from pathlib import Path

arhyme = ["ア", "カ", "ガ", "カ゚", "ラ゚", "サ", "ザ", "ハ", "バ", "パ", "ラ", "ラ゚", "ワ", "マ", "ナ", "タ", "ダ", "ヤ", "チャ", "ファ", "ヴァ"]
irhyme = ["イ", "キ", "ギ", "キ゚", "シ", "ジ", "チ", "ヂ", "ニ", "ヒ", "ビ", "ピ", "ミ", "リ", "ヰ", "ヸ", "フィ", "ディ", "ウィ", "ティ", "ヴぃ"]
urhyme = ["ウ", "ク", "グ", "ク゚","ス", "ズ", "ツ", "ヅ", "ツ゚", "ヌ", "フ", "ブ", "プ", "ム", "ル", "ユ", "キュ", "チュ", "ヴ", "シュ", "リュ"]
erhyme = ["エ", "ケ", "ゲ","セ", "ゼ", "テ", "デ", "ネ", "ヘ", "ベ", "ペ", "メ", "レ", "イェ", "フェ", "シェ", "チェ", "シュ", "ヱ", "ヹ", "ウェ", "ヴェ"]
orhyme = ["オ", "コ", "ゴ","ソ", "ゾ", "ト", "ド", "ノ", "ホ", "ボ", "ポ", "モ", "ロ", "ヨ", "ヲ", "ヺ", "ショ", "チョ", "フォ", "ヴォ"]
n = ["ン"]

sheet = Path(__file__).parent / "jawl.xls"
wb = xlrd.open_workbook(sheet, encoding_override='utf-8')
df = pd.read_excel(sheet, sheet_name="list", usecols="Q", dtype = object)
wordlist = df.values.tolist()


window = tk.Tk()
window.title("ライム読み ALPHA")
font = tkfont.Font(file="font\digi.ttf", family="UD Digi Kyokasho N-R")
results = ()
wordnums = []

def err1():     #Error that displays if user enters invalid characters
    error1 = tk.Toplevel(window)
    error1.geometry("350x75")
    error1.title("Error!")
    hermes1 = tk.Label(error1, text = "エラーが発生した！\n検索に一つ以上の文字は無効だ！", font=font)
    hermes1.pack()

def kensakustart():     #Displays search onscreen and adds results field
    origsearch = kanahara.get()
    searchtoiu = tk.Label(font=font,text=f"検索は：{origsearch}")
    searchtoiu.grid(row=3, column=2, sticky="ew", padx=1, pady=1)
    search = jv.hira2kata(origsearch)
    winlist = henkan(search)
    print(winlist)
    kekkahara = tk.Label(text=f"{winlist}")
    kekkahara.grid(row=4, column=2, sticky="ew", padx=1, pady=1)
    

def jisho(word: str):        #Converts dictionary words to numbers
    searchlist = word[::1]
    rhymelist = []
    for x in searchlist:
        if x == "ア":
            if len(rhymelist) == 0:
                rhymelist.append(1)
            elif rhymelist[-1] == 1:
                rhymelist.pop()
                rhymelist.append("11")
            elif rhymelist[-1] == 4:
                rhymelist.pop()
                rhymelist.append("41")
            else:
                rhymelist.append(1)
        elif x == "イ":
            if len(rhymelist) == 0:
                rhymelist.append(2)
            elif rhymelist[-1] == 1:
                rhymelist.pop()
                rhymelist.append("12")
            elif rhymelist[-1] == 4:
                rhymelist.pop()
                rhymelist.append("42")
            elif rhymelist[-1] == 5:
                rhymelist.pop()
                rhymelist.append("52")
            else:
                rhymelist.append(2)
        elif x == "ウ":
            if len(rhymelist) == 0:
                rhymelist.append(3)
            elif rhymelist[-1] == 1:
                rhymelist.pop()
                rhymelist.append("13")
            elif rhymelist[-1] == 2:
                rhymelist.pop()
                rhymelist.append("23")
            elif rhymelist[-1] == 3:
                rhymelist.pop()
                rhymelist.append("33")
            elif rhymelist[-1] == 5:
                rhymelist.pop()
                rhymelist.append("55")
            else:
                rhymelist.append(3)
        elif x == "エ":
            if len(rhymelist) == 0:
                rhymelist.append(4)
            elif rhymelist[-1] == 1:
                rhymelist.pop()
                rhymelist.append("14")
            elif rhymelist[-1] == 4:
                rhymelist.pop()
                rhymelist.append("44")
            else:
                rhymelist.append(4)
        elif x == "オ":
            if len(rhymelist) == 0:
                rhymelist.append(5)
            elif rhymelist[-1] == 1:
                rhymelist.pop()
                rhymelist.append("15")
            elif rhymelist[-1] == 5:
                rhymelist.pop()
                rhymelist.append("55")
            else:
                rhymelist.append(5)
        else:
            if x in arhyme: 
                rhymelist.append(1)
            if x in irhyme:
                rhymelist.append(2)
            if x in urhyme:
                rhymelist.append(3)
            if x in erhyme:
                rhymelist.append(4)
            if x in orhyme:
                rhymelist.append(5)
            if x in n:
                rhymelist.append(6)
            if x == "ャ" or x == "ァ":
                rhymelist.pop()
                rhymelist.append(1)
            if x == "ィ":
                rhymelist.pop()
                rhymelist.append(2)
            if x == "ュ" or x == "ゥ" or x == "ㇷ゚" or x == "ㇷ":
                rhymelist.pop()
                rhymelist.append(3)
            if x == "ェ":
                rhymelist.pop()
                rhymelist.append(4)
            if x == "ョ" or x == "ォ":
                rhymelist.pop()
                rhymelist.append(5)
            if x == "ー":
                if rhymelist[-1] == 1:
                    rhymelist.pop()
                    rhymelist.append("11")
                if rhymelist[-1] == 2:
                    rhymelist.pop()
                    rhymelist.append("22")
                if rhymelist[-1] == 3:
                    rhymelist.pop()
                    rhymelist.append("33")
                if rhymelist[-1] == 4:
                    rhymelist.pop()
                    rhymelist.append("44")
                if rhymelist[-1] == 5:
                    rhymelist.pop()
                    rhymelist.append("55")
            if x == "ッ":
                rhymelist.pop()
    return(rhymelist)

def henkan(search: str):        #Converts search query to numbers
    searchlist = search[::1]
    rhymelist = []
    for x in searchlist:
        if x == "ア":
            if len(rhymelist) == 0:
                rhymelist.append(1)
            elif rhymelist[-1] == 1:
                rhymelist.pop()
                rhymelist.append("11")
            elif rhymelist[-1] == 4:
                rhymelist.pop()
                rhymelist.append("41")
            else:
                rhymelist.append(1)
        elif x == "イ":
            if len(rhymelist) == 0:
                rhymelist.append(2)
            elif rhymelist[-1] == 1:
                rhymelist.pop()
                rhymelist.append("12")
            elif rhymelist[-1] == 4:
                rhymelist.pop()
                rhymelist.append("42")
            elif rhymelist[-1] == 5:
                rhymelist.pop()
                rhymelist.append("52")
            else:
                rhymelist.append(2)
        elif x == "ウ":
            if len(rhymelist) == 0:
                rhymelist.append(3)
            elif rhymelist[-1] == 1:
                rhymelist.pop()
                rhymelist.append("13")
            elif rhymelist[-1] == 2:
                rhymelist.pop()
                rhymelist.append("23")
            elif rhymelist[-1] == 3:
                rhymelist.pop()
                rhymelist.append("33")
            elif rhymelist[-1] == 5:
                rhymelist.pop()
                rhymelist.append("55")
            else:
                rhymelist.append(3)
        elif x == "エ":
            if len(rhymelist) == 0:
                rhymelist.append(4)
            elif rhymelist[-1] == 1:
                rhymelist.pop()
                rhymelist.append("14")
            elif rhymelist[-1] == 4:
                rhymelist.pop()
                rhymelist.append("44")
            else:
                rhymelist.append(4)
        elif x == "オ":
            if len(rhymelist) == 0:
                rhymelist.append(5)
            elif rhymelist[-1] == 1:
                rhymelist.pop()
                rhymelist.append("15")
            elif rhymelist[-1] == 5:
                rhymelist.pop()
                rhymelist.append("55")
            else:
                rhymelist.append(5)
        else:
            if x in arhyme: 
                rhymelist.append(1)
            if x in irhyme:
                rhymelist.append(2)
            if x in urhyme:
                rhymelist.append(3)
            if x in erhyme:
                rhymelist.append(4)
            if x in orhyme:
                rhymelist.append(5)
            if x in n:
                rhymelist.append(6)
            if x == "ャ" or x == "ァ":
                rhymelist.pop()
                rhymelist.append(1)
            if x == "ィ":
                rhymelist.pop()
                rhymelist.append(2)
            if x == "ュ" or x == "ゥ" or x == "ㇷ゚" or x == "ㇷ":
                rhymelist.pop()
                rhymelist.append(3)
            if x == "ェ":
                rhymelist.pop()
                rhymelist.append(4)
            if x == "ョ" or x == "ォ":
                rhymelist.pop()
                rhymelist.append(5)
            if x == "ー":
                if rhymelist[-1] == 1:
                    rhymelist.pop()
                    rhymelist.append("11")
                if rhymelist[-1] == 2:
                    rhymelist.pop()
                    rhymelist.append("22")
                if rhymelist[-1] == 3:
                    rhymelist.pop()
                    rhymelist.append("33")
                if rhymelist[-1] == 4:
                    rhymelist.pop()
                    rhymelist.append("44")
                if rhymelist[-1] == 5:
                    rhymelist.pop()
                    rhymelist.append("55")
            if x == "ッ":
                rhymelist.pop()
    if  0 in rhymelist:
        err1()
        return
    print(rhymelist)
    for z in range(len(wordnums)):
        winlist = ("")
        compare = wordnums[z]
        if len(rhymelist) <= len(compare):
            if rhymelist == compare[0-(len(rhymelist)):]:
                goodword = wordlist[z]
                print(goodword[0])
    return winlist




for y in wordlist:
    for x in y:
        rhymelist = jisho(x)
        wordnums.append(rhymelist)
        

window.geometry("800x600")
writekana = tk.Label(font=font,text="カナ文字で言葉を書いてください！")
kanahara = tk.Entry(window)
botan = tk.Button(text="検索", command=kensakustart)

writekana.grid(row=1, column=1, sticky="e", padx=5, pady=5)
kanahara.grid(row=2, column=1, sticky="e", padx=5, pady=5)
botan.grid(row=2, column=2, sticky="e", padx=5, pady=5)
window.mainloop()

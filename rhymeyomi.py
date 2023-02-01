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
    kekkahara = tk.Text()
    kekkahara.grid(row=4, column=2, sticky="ew", padx=1, pady=1)
    search = jv.hira2kata(origsearch)
    henkan(search)

def henkan(search):        #Converts query to numbers
    searchlist = search[::1]
    rhymelist = []
    for x in searchlist:
        rhymelist.append(0)
        if x in arhyme: 
            rhymelist.pop()
            rhymelist.append(1)
        if x in irhyme:
            rhymelist.pop()
            rhymelist.append(2)
        if x in urhyme:
            rhymelist.pop()
            rhymelist.append(3)
        if x in erhyme:
            rhymelist.pop()
            rhymelist.append(4)
        if x in orhyme:
            rhymelist.pop()
            rhymelist.append(5)
        if x in n:
            rhymelist.pop()
            rhymelist.append(6)
        if x == "ャ" or x == "ァ":
            rhymelist.pop()
            rhymelist.pop()
            rhymelist.append(1)
        if x == "ィ":
            rhymelist.pop()
            rhymelist.pop()
            rhymelist.append(2)
        if x == "ュ" or x == "ゥ" or x == "ㇷ゚" or x == "ㇷ":
            rhymelist.pop()
            rhymelist.pop()
            rhymelist.append(3)
        if x == "ェ":
            rhymelist.pop()
            rhymelist.pop()
            rhymelist.append(4)
        if x == "ョ" or x == "ォ":
            rhymelist.pop()
            rhymelist.pop()
            rhymelist.append(5)
        if x == "ー":
            rhymelist.pop()
            rhymelist += rhymelist[-1:]
        if x == "ッ":
            rhymelist.pop()
        if  0 in rhymelist:
            err1()
            return
    print(rhymelist)



window.geometry("800x600")
writekana = tk.Label(font=font,text="カナ文字で言葉を書いてください！")
kanahara = tk.Entry(window)
botan = tk.Button(text="検索", command=kensakustart)

writekana.grid(row=1, column=1, sticky="e", padx=5, pady=5)
kanahara.grid(row=2, column=1, sticky="e", padx=5, pady=5)
botan.grid(row=2, column=2, sticky="e", padx=5, pady=5)
window.mainloop()

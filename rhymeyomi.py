import tkinter as tk
import tkextrafont as tkfont
import jaconv as jv

arhyme = ["ア", "カ", "ガ","サ", "ザ", "ハ", "バ", "パ", "ラ", "ワ", "マ", "ナ", "タ", "ダ", "ヤ", "チャ", "ファ", "ヴァ"]
irhyme = ["イ", "キ", "ギ","シ", "ジ", "チ", "ヂ", "ニ", "ヒ", "ビ", "ピ", "ミ", "リ", "フィ", "ディ", "ウィ", "ティ", "ヴぃ"]
urhyme = ["ウ", "ク", "グ","ス", "ズ", "ツ", "ヅ", "ヌ", "フ", "ブ", "プ", "ム", "ル", "ユ", "キュ", "チュ", "ヴ", "シュ", "リュ"]
erhyme = ["エ", "ケ", "ゲ","セ", "ゼ", "テ", "デ", "ネ", "ヘ", "ベ", "ペ", "メ", "レ", "イェ", "フェ", "シェ", "チェ", "シュ", "ウェ", "ヴェ"]
orhyme = ["オ", "コ", "ゴ","ソ", "ゾ", "ト", "ド", "ノ", "ホ", "ボ", "ポ", "モ", "ロ", "ヨ", "ヲ", "ショ", "チョ", "フォ", "ヴォ"]


window = tk.Tk()
window.title("ライム読み ALPHA")


def kensakustart():     #Displays search onscreen and adds results field
    origsearch = kanahara.get()
    searchtoiu = tk.Label(font=font,text=f"検索は：{origsearch}")
    searchtoiu.grid(row=3, column=2, sticky="ew", padx=1, pady=1)
    kekkahara = tk.Text()
    kekkahara.grid(row=4, column=2, sticky="ew", padx=1, pady=1)
    search = jv.hira2kata(origsearch)
    kensaku(search)

def kensaku(search):        #Searches for rhymes in dictionary
    searchlist = search[::1]
    rhymelist = []
    for x in range(len(searchlist)):
        if searchlist[x] in arhyme:
            rhymelist.append(0)
        else:
            if searchlist[x] in irhyme:
                rhymelist.append(1)
            else:
                if searchlist[x] in urhyme:
                    rhymelist.append(2)
                else:
                    if searchlist[x] in erhyme:
                        rhymelist.append(3)
                    else:
                        if searchlist[x] in orhyme:
                            rhymelist.append(4)



window.geometry("800x600")
font = tkfont.Font(file="font\digi.ttf", family="UD Digi Kyokasho N-R")
writekana = tk.Label(font=font,text="カナ文字で言葉を書いてください！")
kanahara = tk.Entry(window)
botan = tk.Button(text="検索", command=kensakustart)

writekana.grid(row=1, column=1, sticky="e", padx=5, pady=5)
kanahara.grid(row=2, column=1, sticky="e", padx=5, pady=5)
botan.grid(row=2, column=2, sticky="e", padx=5, pady=5)

window.mainloop()

import tkinter as tk
import tkextrafont as tkfont
import jaconv as jv
import pandas as pd
import xlrd
from pathlib import Path
from PIL import ImageTk,Image 
import tkinter.ttk as ttk

arhyme = ["ア", "カ", "ガ", "カ゚", "ラ゚", "サ", "ザ", "ハ", "バ", "パ", "ラ", "ラ゚", "ワ", "マ", "ナ", "タ", "ダ", "ヤ", "チャ", "ファ", "ヴァ"]
irhyme = ["イ", "キ", "ギ", "キ゚", "シ", "ジ", "チ", "ヂ", "ニ", "ヒ", "ビ", "ピ", "ミ", "リ", "ヰ", "ヸ", "フィ", "ディ", "ウィ", "ティ", "ヴぃ"]
urhyme = ["ウ", "ク", "グ", "ク゚","ス", "ズ", "ツ", "ヅ", "ツ゚", "ヌ", "フ", "ブ", "プ", "ム", "ル", "ユ", "キュ", "チュ", "ヴ", "シュ", "リュ"]
erhyme = ["エ", "ケ", "ゲ","セ", "ゼ", "テ", "デ", "ネ", "ヘ", "ベ", "ペ", "メ", "レ", "イェ", "フェ", "シェ", "チェ", "シュ", "ヱ", "ヹ", "ウェ", "ヴェ"]
orhyme = ["オ", "コ", "ゴ","ソ", "ゾ", "ト", "ド", "ノ", "ホ", "ボ", "ポ", "モ", "ロ", "ヨ", "ヲ", "ヺ", "ショ", "チョ", "フォ", "ヴォ"]
n = ["ン"]
other = ["ャ","ァ","ィ","ュ","ゥ","ㇷ゚","ㇷ","ェ","ョ","ォ","ー","ッ"]
allvalid = arhyme + irhyme + urhyme + erhyme + orhyme + n + other
errlist = {
"001":"エラーが発生した！\n検索に一つ以上の文字は無効だ！(001)"
}



def updatelabel(label, message):
    label.config(text=message)
    window.update()

def err(code):     #Error that displays if user enters invalid characters
    error = tk.Toplevel(window)
    error.geometry("350x75")
    error.title("Error!")
    hermes1 = tk.Label(error, text = errlist[code], font=font)
    hermes1.pack()

def kensakustart():     #Displays search onscreen and adds results field
    origsearch = kanahara.get()
    searchtoiu = tk.Label(font=font,text=f"検索は：{origsearch}", anchor="center")
    searchtoiu.grid(row=4, column=1, sticky="ew", padx=1, pady=1)
    search = jv.hira2kata(origsearch)
    winlist, winfuri = henkan(search)
    kekkahara.delete(*kekkahara.get_children())
    for x, y in zip(winlist, winfuri):
            kekkahara.insert('', 'end', values=(x, y))

def albyfunction(rhymelist):
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


    
def rhymeprocess(word: str):    #Converts given string to numbers for comparison
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
            elif rhymelist[-1] == 2:
                rhymelist.pop()
                rhymelist.append("22")
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
                pass
        if x not in allvalid:
            err("001")
            print(f"Error! {x} is invalid!")
            return(["Error"])
    return(rhymelist)

def henkan(word: str):        #Compares search to dictionary
    ping=0
    rhymelist = rhymeprocess(word)
    if  0 in rhymelist:
        err("001")
        return
    print(rhymelist)
    winlist = []
    winfuri = []
    for z in range(len(wordnums)):
        compare = wordnums[z]
        if len(rhymelist) <= len(compare):
            if rhymelist == compare[0-(len(rhymelist)):]:
                goodword = kanlist[z]
                winlist.append(goodword[0])
                goodfuri = wordlist[z]
                winfuri.append(goodfuri[0])
                #print(goodfuri[0])
                #print(goodword[0])
    if not dictionaries:
        print(f"{len(winlist)} results found!")
    return winlist, winfuri
    




if __name__ == "__main__":
    window = tk.Tk()
    window.title("ライム読み ALPHA")
    font = tkfont.Font(file="font\digi.ttf", family="UD Digi Kyokasho N-R")
    results = ()
    print("Opening dictionary...")
    sheet = Path(__file__).parent / "assets" / "vdrj.xls"
    wb = xlrd.open_workbook(sheet, encoding_override='utf-8')
    print("Reading dictionary...")
    df = pd.read_excel(sheet, sheet_name="list", usecols="C", dtype = object)
    df2 = pd.read_excel(sheet, sheet_name="list", usecols="A", dtype = object)
    wordlist = df.values.tolist()
    kanlist = df2.values.tolist()
    wordnums = []
    wordwords = []
    print("Processing dictionary...")
    dictionaries = True
    for y in wordlist:
        for x in y:
            dictionary = rhymeprocess(x)
            if x == "Error":
                err("001")
            wordnums.append(dictionary)
    print("Adding kanji...")
    for y in kanlist:
        for x in y:
            wordwords.append(x)
        
dictionaries = False
window.geometry("800x600")
writekana = tk.Label(font=font,text="カナ文字で言葉を書いてください！")
kanahara = tk.Entry(window)
botan = tk.Button(text="検索", command=kensakustart)
style = ttk.Style()
style.configure('Treeview', font=font)
headerstyle = ttk.Style()
headerstyle.configure('Treeview.Heading', font=('TkDefaultFont', 13))
please = tk.Label(font=('TkDefaultFont', 10), text="Please open an issue on the GitHub page if there's any problems!")
logopic = Image.open(Path(__file__).parent / "assets" / "logo" / "logocrop.png")
resizelogo = logopic.resize((logopic.size[0] // 10, logopic.size[1] // 10))
resizephoto = ImageTk.PhotoImage(resizelogo)
logo = tk.Label(window, image=resizephoto)
creds = tk.Label(font=('TkDefaultFont', 10), text="RhymeYomi created by Ana-Luisa Aikman. RY ALPHA 0.0.3 - 2023.03.08")
kekkahara = ttk.Treeview(window, columns=('kanji', 'furigana'), height=4)
kekkahara.column('#1', width=150, minwidth=150, stretch=tk.YES)
kekkahara.column('#2', width=150, minwidth=150, stretch=tk.YES)
kekkahara.config(show='headings')
kekkahara.heading('#1', text='漢字')
kekkahara.heading('#2', text='フリガナ')
please.grid(row=1, column=1, sticky="nesw", padx=5, pady=5)
writekana.grid(row=2, column=1, sticky="nesw", padx=5, pady=5)
kanahara.grid(row=3, column=1, sticky="nesw", padx=5, pady=5)
botan.grid(row=3, column=2, sticky="nesw", padx=5, pady=5)
kekkahara.grid(row=5, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)
creds.grid(row=6, column=1, sticky="nesw", padx=5, pady=5)
logo.grid(row=7, column=1, sticky="nesw", padx=5, pady=5)
window.columnconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=0)
window.rowconfigure(5, weight=5)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=0)
window.mainloop()

﻿import tkinter as tk
import tkextrafont as tkfont
import jaconv as jv
import pandas as pd
import xlrd
from pathlib import Path
from PIL import ImageTk,Image 
import tkinter.ttk as ttk

#Note to self: ALWAYS UPDATE THE VERSION NUMBER

class RhymeYomi:
    def __init__(self):
        #Lists of all katakana sorted by vowel
        self.arhyme = ["ア", "カ", "ガ", "カ゚", "ラ゚", "サ", "ザ", "ハ", "バ", "パ", "ラ", "ラ゚", "ワ", "マ", "ナ", "タ", "ダ", "ヤ", "チャ", "ファ", "ヴァ"]
        self.irhyme = ["イ", "キ", "ギ", "キ゚", "シ", "ジ", "チ", "ヂ", "ニ", "ヒ", "ビ", "ピ", "ミ", "リ", "ヰ", "ヸ", "フィ", "ディ", "ウィ", "ティ", "ヴぃ"]
        self.urhyme = ["ウ", "ク", "グ", "ク゚","ス", "ズ", "ツ", "ヅ", "ツ゚", "ヌ", "フ", "ブ", "プ", "ム", "ル", "ユ", "キュ", "チュ", "ヴ", "シュ", "リュ"]
        self.erhyme = ["エ", "ケ", "ゲ","セ", "ゼ", "テ", "デ", "ネ", "ヘ", "ベ", "ペ", "メ", "レ", "イェ", "フェ", "シェ", "チェ", "シュ", "ヱ", "ヹ", "ウェ", "ヴェ"]
        self.orhyme = ["オ", "コ", "ゴ","ソ", "ゾ", "ト", "ド", "ノ", "ホ", "ボ", "ポ", "モ", "ロ", "ヨ", "ヲ", "ヺ", "ショ", "チョ", "フォ", "ヴォ"]
        self.n = ["ン"]
        self.other = ["ャ","ァ","ィ","ュ","ゥ","ㇷ゚","ㇷ","ェ","ョ","ォ","ー","ッ"]
        self.allvalid = self.arhyme + self.irhyme + self.urhyme + self.erhyme + self.orhyme + self.n + self.other
        self.dictlist = ["dict1.xls", "dict2.xls", "dict3.xls"]
        self.wordlist = [] 
        self.kanlist = [] 

        #List of errors
        self.errlist = {
        "001":"エラーが発生した！\n検索で一つ以上の文字は無効だ！(001)", #Invalid characters in search
        "002":"エラーが発生した！\n辞書で一つ以上の文字は無効だ！GitHubでIssueを作ってください！(002)" #Invalid characters in dictonary (very problematic)
        }
        
        self.window = tk.Tk()
        self.window.title("ライム読み ALPHA")
        self.font = tkfont.Font(file="font\digi.ttf", family="UD Digi Kyokasho N-R")
        self.results = ()
        self.processdict()
        self.create_ui()
        self.window.mainloop()
        

    def processdict(self):          #Converts dictionary to number format
        self.dictionaries = True
        for x in self.dictlist:
            print("Opening dictionary...")
            self.sheet = Path(__file__).parent / "assets" / x
            self.wb = xlrd.open_workbook(self.sheet, encoding_override='utf-8')
            print("Reading dictionary...")
            self.df = pd.read_excel(self.sheet, sheet_name="list", usecols="C", dtype = object)
            self.df2 = pd.read_excel(self.sheet, sheet_name="list", usecols="A", dtype = object)
            self.wordlist.extend(self.df.values.tolist())
            self.kanlist.extend(self.df2.values.tolist())
        self.wordnums = []
        self.wordwords = []
        print("Processing dictionary...")
        self.dictionaries = True
        for y in self.wordlist:
            for x in y:
                self.dictionary = self.rhyme_process(x)
                if x == "Error":
                    self.err("002")
                self.wordnums.append(self.dictionary)
        print("Adding kanji...")
        for y in self.kanlist:
            for x in y:
                self.wordwords.append(x)
        self.dictionaries = False
        print(len(self.wordnums))
        print(len(self.wordwords))

    def poppend(self,thelist,thenum):     #Pops and appends something to a given list
        thelist.pop()
        thelist.append(thenum)

    def create_ui(self):
        self.window.geometry("800x600")

        #Label that tells the user to enter kana only
        self.writekana = tk.Label(font=self.font,text="カナ文字で言葉を書いてください！")
        self.syllablenum = tk.Label(font=self.font,text="音節数（オプション）")

        #Kana entry field
        self.kanahara = tk.Entry(self.window)
        self.numberhara = tk.Entry(self.window)

        #Search button
        self.botan = tk.Button(text="検索", command=self.search_start)

        #Style of results treeview
        self.style = ttk.Style()
        self.style.configure('Treeview', font=self.font)
        self.headerstyle = ttk.Style()
        self.headerstyle.configure('Treeview.Heading', font=('TkDefaultFont', 13))

        #Addt'l text and logos
        self.please = tk.Label(font=('TkDefaultFont', 10), text="Please open an issue on the GitHub page if there's any problems!")
        self.logopic = Image.open(Path(__file__).parent / "assets" / "logo" / "logocrop.png")
        self.resizelogo = self.logopic.resize((self.logopic.size[0] // 10, self.logopic.size[1] // 10))
        self.resizephoto = ImageTk.PhotoImage(self.resizelogo)
        self.logo = tk.Label(self.window, image=self.resizephoto)
        #Version number
        self.creds = tk.Label(font=('TkDefaultFont', 10), text="RhymeYomi created by Ana Aikman. RY ALPHA 0.0.8 - 2023.05.19")

        #Results treeview
        self.kekkahara = ttk.Treeview(self.window, columns=('kanji', 'furigana'), height=4)
        self.kekkahara.column('#1', width=150, minwidth=150, stretch=tk.YES)
        self.kekkahara.column('#2', width=150, minwidth=150, stretch=tk.YES)
        self.kekkahara.config(show='headings')
        self.kekkahara.heading('#1', text='漢字')
        self.kekkahara.heading('#2', text='フリガナ')

        #UI grid placement
        self.please.grid(row=1, column=1, sticky="nesw", padx=5, pady=5)
        self.writekana.grid(row=2, column=1, sticky="nesw", padx=5, pady=5)
        self.syllablenum.grid(row=2, column=2, sticky="nesw", padx=5, pady=5)
        self.kanahara.grid(row=3, column=1, sticky="nesw", padx=5, pady=5)
        self.numberhara.grid(row=3, column=2, sticky="nesw", padx=5, pady=5)
        self.botan.grid(row=3, column=3, sticky="nesw", padx=5, pady=5)
        self.kekkahara.grid(row=5, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.creds.grid(row=6, column=1, sticky="nesw", padx=5, pady=5)
        self.logo.grid(row=7, column=1, sticky="nesw", padx=5, pady=5)
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=0)
        self.window.rowconfigure(5, weight=5)
        self.window.rowconfigure(6, weight=1)
        self.window.rowconfigure(7, weight=0)

    def update_label(self, label, message): #Function to change label text
        label.config(text=message)
        self.window.update()

    def err(self, code):     #Error that displays if user enters invalid characters
        error = tk.Toplevel(self.window)
        error.geometry("350x75")
        error.title("Error!")
        hermes1 = tk.Label(error, text = self.errlist[code], font=self.font)
        hermes1.pack()

    def search_start(self):    #Displays search onscreen and adds results field
        origsearch = self.kanahara.get()
        try:
            sylnum = int(self.numberhara.get())
        except ValueError:
            sylnum = 0
        searchtoiu = tk.Label(font=self.font,text=f"検索は：{origsearch}", anchor="center")
        searchtoiu.grid(row=4, column=1, sticky="ew", padx=1, pady=1)
        search = jv.hira2kata(origsearch)
        winlist, winfuri = self.search_compare(search, sylnum)
        self.kekkahara.delete(*self.kekkahara.get_children())
        for x, y in zip(winlist, winfuri):
                self.kekkahara.insert('', 'end', values=(x, y))


    def rhyme_process(self, word: str):    #Converts given string to numbers based on vowels for comparison
        searchlist = word[::1]
        rhymelist = []
        for x in searchlist:
            if x == "ア":
                if len(rhymelist) == 0:
                    rhymelist.append(1)
                elif rhymelist[-1] == 1:
                    self.poppend(rhymelist,"11")
                elif rhymelist[-1] == 4:
                    self.poppend(rhymelist,"41")
                else:
                    rhymelist.append(1)
            elif x == "イ":
                if len(rhymelist) == 0:
                    rhymelist.append(2)
                elif rhymelist[-1] == 1:
                    self.poppend(rhymelist,"12")
                elif rhymelist[-1] == 2:
                    self.poppend(rhymelist,"22")
                elif rhymelist[-1] == 4:
                    self.poppend(rhymelist,"42")
                elif rhymelist[-1] == 5:
                    self.poppend(rhymelist,"52")
                else:
                    rhymelist.append(2)
            elif x == "ウ":
                if len(rhymelist) == 0:
                    rhymelist.append(3)
                elif rhymelist[-1] == 1:
                    self.poppend(rhymelist,"13")
                elif rhymelist[-1] == 2:
                    self.poppend(rhymelist,"23")
                elif rhymelist[-1] == 3:
                    self.poppend(rhymelist,"33")
                elif rhymelist[-1] == 5:
                    self.poppend(rhymelist,"55")
                else:
                    rhymelist.append(3)
            elif x == "エ":
                if len(rhymelist) == 0:
                    rhymelist.append(4)
                elif rhymelist[-1] == 1:
                    self.poppend(rhymelist,"14")
                elif rhymelist[-1] == 4:
                    self.poppend(rhymelist,"44")
                else:
                    rhymelist.append(4)
            elif x == "オ":
                if len(rhymelist) == 0:
                    rhymelist.append(5)
                elif rhymelist[-1] == 1:
                    self.poppend(rhymelist,"15")
                elif rhymelist[-1] == 5:
                    self.poppend(rhymelist,"55")
                else:
                    rhymelist.append(5)
            else:
                if x in self.arhyme: 
                    rhymelist.append(1)
                if x in self.irhyme:
                    rhymelist.append(2)
                if x in self.urhyme:
                    rhymelist.append(3)
                if x in self.erhyme:
                    rhymelist.append(4)
                if x in self.orhyme:
                    rhymelist.append(5)
                if x in self.n:
                    rhymelist.append(6)
                if x == "ャ" or x == "ァ":
                    self.poppend(rhymelist,1)
                if x == "ィ":
                    self.poppend(rhymelist,2)
                if x == "ュ" or x == "ゥ" or x == "ㇷ゚" or x == "ㇷ":
                    self.poppend(rhymelist,3)
                if x == "ェ":
                    self.poppend(rhymelist,4)
                if x == "ョ" or x == "ォ":
                    self.poppend(rhymelist,5)
                if x == "ー":
                    if rhymelist[-1] == 1:
                        self.poppend(rhymelist,"11")
                    if rhymelist[-1] == 2:
                        self.poppend(rhymelist,"22")
                    if rhymelist[-1] == 3:
                        self.poppend(rhymelist,"33")
                    if rhymelist[-1] == 4:
                        self.poppend(rhymelist,"44")
                    if rhymelist[-1] == 5:
                        self.poppend(rhymelist,"55")
                if x == "ッ":
                    pass
            if x not in self.allvalid:
                self.err("001")
                print(f"Error! {x} is invalid!")
                return(["Error"])
        return(rhymelist)

    def search_compare(self, word: str, syllables: int):        #Compares search to dictionary
        rhymelist = self.rhyme_process(word)
        if  0 in rhymelist:
            self.err("001")
            return
        print(rhymelist)
        winlist = []
        winfuri = []
        for z in range(len(self.wordnums)): #wordnums = dictionary words as numbers
            compare = self.wordnums[z] #loads up word from dictionary to compare
            if len(rhymelist) <= len(compare): #if the length of the query is less than or equal to the length of the word
                if syllables != 0: #if a value is given for syllable length
                    if len(compare) == (syllables-1):
                        if rhymelist == compare[0-(len(rhymelist)):]: #if the last ___ syllables of the query match the word
                            goodword = self.kanlist[z]
                            winlist.append(goodword[0])
                            goodfuri = self.wordlist[z]
                            winfuri.append(goodfuri[0])
                            #print(goodfuri[0])
                            #print(goodword[0])
                else:
                    if rhymelist == compare[0-(len(rhymelist)):]: #if the last ___ syllables of the query match the word
                            goodword = self.kanlist[z]
                            winlist.append(goodword[0])
                            goodfuri = self.wordlist[z]
                            winfuri.append(goodfuri[0])
                            #print(goodfuri[0])
                            #print(goodword[0])
        if not self.dictionaries:
            print(f"{len(winlist)} results found!")
        return winlist, winfuri



if __name__ == "__main__":
    app = RhymeYomi()



    


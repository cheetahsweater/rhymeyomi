import tkinter as tk
import tkextrafont as tkfont

window = tk.Tk()
window.title("RhymeYomi ALPHA")

def kensaku():
    search = kanahara.get()
    searchtoiu = tk.Label(font=font,text=f"検索は：{search}")
    searchtoiu.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
    kekkahara = tk.Text()
    kekkahara.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

window.geometry("600x600")
font = tkfont.Font(file="font\digi.ttf", family="UD Digi Kyokasho N-R")
writekana = tk.Label(font=font,text="カナ文字で言葉を書いてください！")
kanahara = tk.Entry(window)
botan = tk.Button(text="検索", command=kensaku)

writekana.grid(row=1, column=1, sticky="e", padx=5, pady=5)
kanahara.grid(row=2, column=1, sticky="e", padx=5, pady=5)
botan.grid(row=2, column=2, sticky="e", padx=5, pady=5)

window.mainloop()

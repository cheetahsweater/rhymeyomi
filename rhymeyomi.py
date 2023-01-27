import tkinter as tk
import tkextrafont as tkfont

window = tk.Tk()
window.title("RhymeYomi ALPHA")

window.geometry("600x600")
font = tkfont.Font(file="font\digi.ttf", family="UD Digi Kyokasho N-R")
writekana = tk.Label(font=font,text="カナ文字で言葉を書いてください！")
kanahara = tk.Entry()

writekana.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
kanahara.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
window.mainloop()

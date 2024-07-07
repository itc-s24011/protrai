# 24011 entry_kadai.py
# エントリーウィジェット標準入力で受け付けた金額を税込み(10%)価格として出力するプログラム

import tkinter as tk #  tkinterをtkと略して使用する

def dispLael():
    a = entry.get()
    print(F"aは{type(a)}") # ログの出力
    lbl.

root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200") # 画面の大きさを決める


lbl = tk.Label(text="ラベル", font=("Helvetica", 20))
entry = tk.Entry(font("Helvetica", 20))
btn = tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mineloop()

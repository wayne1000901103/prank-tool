import tkinter as tk
import os

def run_blue_screen():
    os.system("start CMD-blue-screen.exe")

def run_crash():
    os.system("start CMD-Crash.exe")

def run_popups():
    os.system("start CMD-unlimited-pop-ups.exe")

def run_vbs():
    os.system("start that-can’t-be-turned-off.vbs")

root = tk.Tk()
root.title("惡搞工具")

# 創建按鈕
btn_blue_screen = tk.Button(root, text="藍屏", command=run_blue_screen)
btn_blue_screen.pack(pady=10)

btn_crash = tk.Button(root, text="崩潰系統", command=run_crash)
btn_crash.pack(pady=10)

btn_popups = tk.Button(root, text="無限彈窗", command=run_popups)
btn_popups.pack(pady=10)

btn_vbs = tk.Button(root, text="無法關閉的VBS", command=run_vbs)
btn_vbs.pack(pady=10)

# 啟動 GUI
root.mainloop()

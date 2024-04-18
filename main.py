import tkinter as tk
from tkinter import messagebox
import pyautogui
import cv2
import numpy as np
import threading


class huy:
    def __init__(self, master):
        self.master = master
        master.title("Screen recorder")
        master.geometry("300x300")
        self.recording= False
        self.record_button = tk.Button(master, text="Start recording", command= self.toggle_recording, height= 2, width= 20)
        self.record_button.pack(pady=20)
        
    def toggle_recording(self):
        if not self.recording:
            self.recording=  True
            threading.Thread(target=self._record_screen).start()
            self.record_button.config(text="End recording")
        else:
            self.recording=False
            self.record_button.config(text="Start recording")
        
    def _record_screen(self):
        SCREEN_SIZE = pyautogui.size()
        FPS = 24.0
        self.fourcc = cv2.VideoWriter_fourcc(*"XVID")
        self.out = cv2.VideoWriter("screen_recorder/output.avi", self.fourcc, FPS, (SCREEN_SIZE))
        while self.recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)
        self.out.release()
        messagebox.showinfo("Recording ended.", "Recording saved output.avi")
        
if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap('screen_recorder/skuf.ico')
    app = huy(root)
    root.mainloop()
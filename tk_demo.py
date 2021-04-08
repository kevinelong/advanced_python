import tkinter as tk
from tkinter import simpledialog, messagebox
import re
ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What's your Name?:")

# n = f"{USER_INP} should get to work!!!"

n = USER_INP + " should get to work!!!"

# n =  (USER_INP,('should get to work'))
# m = re.search('.*', n)
# m.group(0)
# print(m)

answer = messagebox.showinfo(title="True Fact", message= n)
print(answer)
# check it out
# print("Hello", USER_INP)
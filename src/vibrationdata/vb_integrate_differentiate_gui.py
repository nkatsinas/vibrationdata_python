###########################################################################
# program: vb_integrate_differentiate_gui.py
# author: Tom Irvine
# version: 1.0
# date: January 17, 2015
#
###############################################################################

from __future__ import print_function

import sys

if sys.version_info[0] == 2:
    print("Python 2.x")
    import Tkinter as tk
    from tkFileDialog import asksaveasfilename
    import tkMessageBox

if sys.version_info[0] == 3:
    print("Python 3.x")
    import tkinter as tk
    from tkinter.filedialog import asksaveasfilename
    import tkinter.messagebox as tkMessageBox

###############################################################################


class vb_integrate_differentiate:
    def __init__(self, parent):
        self.master = parent        # store the parent
        top = tk.Frame(parent)    # frame for all class widgets
        top.pack(side='top')      # pack frame in parent's window

        self.master.minsize(350, 350)
        self.master.geometry("450x300")

        self.master.title(
            "vb_integrate_differentiate_gui.py  ver 1.0  by Tom Irvine")

        crow = 0

        self.hwtext3 = tk.Label(top, text='Select Analysis')
        self.hwtext3.grid(row=crow, column=1, pady=7)

        crow = crow+1

        self.Lb3 = tk.Listbox(top, height=3, width=45, exportselection=0)
        self.Lb3.insert(1, "Integrate")
        self.Lb3.insert(2, "Double Integrate to Velocity & Displacement")
        self.Lb3.insert(3, "Differentiate")
        self.Lb3.grid(row=crow, column=1, columnspan=1,
                      padx=10, pady=4, sticky=tk.N)
        self.Lb3.select_set(0)

        crow = crow+1

        self.button_go = tk.Button(
            top, text="Perform Analysis", command=self.analysis_go)
        self.button_go.config(height=2, width=15)
        self.button_go.grid(row=crow, column=1, columnspan=1, padx=10, pady=10)

        crow = crow+1

        root = self.master

        self.button_quit = tk.Button(
            top, text="Quit", command=lambda root=root: quit(root))
        self.button_quit.config(height=2, width=15)
        self.button_quit.grid(row=crow, column=1, padx=6, pady=10)


###############################################################################

    def analysis_go(self):

        win = tk.Toplevel()

        n = int(self.Lb3.curselection()[0])

        m = 0

        if (n == m):
            from vibrationdata.vb_integrate_gui import vb_integrate
            vb_integrate(win)
        m = m+1

        if (n == m):
            from vibrationdata.vb_double_integrate_gui import vb_double_integrate
            vb_double_integrate(win)
        m = m+1

        if (n == m):
            from vibrationdata.vb_differentiate_gui import vb_differentiate
            vb_differentiate(win)
        m = m+1


def quit(root):
    root.destroy()

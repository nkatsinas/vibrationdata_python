################################################################################
# program: vb_srs_plot_gui.py
# author: Tom Irvine
# version: 1.1
# date: May 16, 2014
# description:
################################################################################

from __future__ import print_function

import sys

if sys.version_info[0] == 2:
    print("Python 2.x")
    import Tkinter as tk

if sys.version_info[0] == 3:
    print("Python 3.x")
    import tkinter as tk


import matplotlib.pyplot as plt

import numpy as np


from vibrationdata.vb_utilities import read_two_columns_from_dialog, read_three_columns_from_dialog


class vb_srs_plot:

    def __init__(self, parent):
        self.master = parent        # store the parent
        top = tk.Frame(parent)    # frame for all class widgets
        top.pack(side='top')      # pack frame in parent's window

        w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        w = int(2.*(w*0.22))
        h = int(2.*(h*0.24))
        self.master.geometry("%dx%d+0+0" % (w, h))

        self.master.title("vb_srs_plot_gui.py ver 1.1  by Tom Irvine")

################################################################################

        crow = 0

        self.hwtext1 = tk.Label(top, text='Plot Shock Response Spectrum')
        self.hwtext1.grid(row=crow, column=0, columnspan=6,
                          pady=7, sticky=tk.W)

        crow = crow+1

        self.hwtext2 = tk.Label(top, text='Select Input Format')
        self.hwtext2.grid(row=crow, column=0, columnspan=6,
                          pady=7, sticky=tk.W)

################################################################################

        crow = crow+1

        self.Lb1 = tk.Listbox(top, height=3, width=40, exportselection=0)
        self.Lb1.insert(1, "Naural Freq & Absolute Peak ")
        self.Lb1.insert(2, "Naural Freq & Peak Pos & Peak Neg")
        self.Lb1.grid(row=crow, column=0, columnspan=2, padx=2, sticky=tk.NE)
        self.Lb1.select_set(0)

        crow = crow+1

        self.hwtext4 = tk.Label(top, text='Enter Plot Title ')
        self.hwtext4.grid(row=crow, column=0, columnspan=2,
                          pady=7, sticky=tk.W)

        crow = crow+1

        self.t_string = tk.StringVar()
        self.t_string.set('Shock Response Spectrum  Q=10')
        self.t_string_entry = tk.Entry(
            top, width=40, textvariable=self.t_string)
        self.t_string_entry.grid(
            row=crow, column=0, columnspan=3, padx=5, pady=3, sticky=tk.W)

################################################################################

        crow = crow+1

        self.hwtext3 = tk.Label(top, text='Enter X-axis Label ')
        self.hwtext3.grid(row=crow, column=0, columnspan=2,
                          pady=7, sticky=tk.W)

        crow = crow+1

        self.x_string = tk.StringVar()
        self.x_string.set('Natural Frequency (Hz)')
        self.x_string_entry = tk.Entry(
            top, width=26, textvariable=self.x_string)
        self.x_string_entry.grid(
            row=crow, column=0, columnspan=3, padx=5, pady=3, sticky=tk.W)

################################################################################

        crow = crow+1

        self.hwtext3 = tk.Label(top, text='Enter Y-axis Label ')
        self.hwtext3.grid(row=crow, column=0, columnspan=3,
                          pady=7, sticky=tk.W)

        crow = crow+1

        self.y_string = tk.StringVar()
        self.y_string.set('Peak Accel (G)')
        self.y_string_entry = tk.Entry(
            top, width=26, textvariable=self.y_string)
        self.y_string_entry.grid(
            row=crow, column=0, columnspan=3, padx=5, pady=3, sticky=tk.W)


################################################################################

        crow = crow+1

        self.button_read = tk.Button(
            top, text="Read Input File", command=self.read_data)
        self.button_read.config(height=2, width=15)
        self.button_read.grid(row=crow, column=1,
                              columnspan=1, pady=10, sticky=tk.W)

        root = self.master

        self.button_quit = tk.Button(
            top, text="Quit", command=lambda root=root: quit(root))
        self.button_quit.config(height=2, width=15)
        self.button_quit.grid(row=crow, column=3,
                              columnspan=1, padx=10, pady=20)

################################################################################

    def read_data(self):

        n = 1+int(self.Lb1.curselection()[0])

        if (n == 1):
            self.a, self.b, self.num = read_two_columns_from_dialog(
                'Select Input File', self.master)

        else:
            self.a, self.b, self.c, self.num = read_three_columns_from_dialog(
                'Select Input File', self.master)

        plt.ion()
        plt.close(1)
        plt.figure(1)

        if (n == 1):
            plt.plot(self.a, self.b, linewidth=1.0,
                     color='b')        # disregard error
        else:
            plt.plot(self.a, self.b, label="positive")
            plt.plot(self.a, self.c, label="negative")
            plt.legend(loc="upper right")

        plt.grid(True)
        plt.xlabel(self.x_string.get())
        plt.ylabel(self.y_string.get())
        plt.title(self.t_string.get())
        plt.xscale('log')
        plt.yscale('log')
        plt.draw()

################################################################################


def quit(root):
    root.destroy()

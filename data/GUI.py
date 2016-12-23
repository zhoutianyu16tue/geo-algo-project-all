#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a hello world GUI example.'
import Star
import polygon
import widePolygon
from tkinter import Frame, Label, Button, Entry


'a hello world GUI example.'


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Star', command=self.Star)
        self.alertButton.pack()
        self.alertButton = Button(self, text='Polygon', command=self.Polygon)
        self.alertButton.pack()
        self.alertButton = Button(self, text='WidePolygon', command=self.WidePolygon)
        self.alertButton.pack()

    def Star(self):
        name = self.nameInput.get()
        Star.do(int(name))

    def Polygon(self):
        name = self.nameInput.get()
        polygon.do(int(name))

    def WidePolygon(self):
        name = self.nameInput.get()
        widePolygon.do(int(name))

app = Application()
app.master.title('DataSet')
# 主消息循环:
app.mainloop()
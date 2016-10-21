# -*- coding: utf-8 -*-

import wx

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(400,200))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")
button_1 = wx.Button(panel, wx.ID_ANY, u"ボタン１")
button_2 = wx.Button(panel, wx.ID_ANY, u"ボタン２")
button_3 = wx.Button(panel, wx.ID_ANY, u"ボタン３")

layout = wx.BoxSizer(wx.HORIZONTAL)
layout.Add(button_1)
layout.Add(button_2)
layout.Add(button_3)

panel.SetSizer(layout)
frame.Show()

application.MainLoop()

#_*_coding:utf-8_*_
import wx
import threading
from imageGrasp import ImageGrasp
class Content:
    TITLE_WINDOW_EN='Images Downloader'
    TITLE_WINDOW='图片下载器'
    TEXT_NOTHING=''
    TEXT_PROMOT_EN='Write down anything you want to search...'
    TEXT_PROMOT='写下你想下载图片的关键字......'
    TEXT_PROMOT2_EN='Write down something...'
    TEXT_PROMOT2='你还没有写关键字......'
    TEXT_SEARCHING_EN='Searching...'
    TEXT_SEARCHING='正在搜索'
    TEXT_SEARCH_EN='Searching'
    TEXT_SEARCH='搜索'
class Frame0(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title=Content.TITLE_WINDOW,pos=(100,100),size=(600,200))
        self.panel=wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(100, 100, 100))

        self.label1=wx.StaticText(self.panel,-1,Content.TEXT_PROMOT,pos=(100,10))
        self.label1.SetForegroundColour(wx.Colour(200, 200, 200))

        self.listBox=wx.ListBox(choices=[],parent=self.panel,id=-1,pos=(100,100),size=(200,100))
        self.listBox.SetBackgroundColour(wx.Colour(100, 100, 100))

        self.textSearch=wx.TextCtrl(self.panel,-1,pos=(100,50),size=(200,20))
        self.buttonOK=wx.Button(self.panel,-1,Content.TEXT_SEARCH,pos=(300,45))
        self.Bind(wx.EVT_BUTTON,self.OnButtonOK,self.buttonOK)
    def OnButtonOK(self,event):
        finalStr=self.textSearch.GetValue()
        if finalStr=='':
            self.listBox.Append(Content.TEXT_PROMOT2)
        else:
            self.listBox.Append(Content.TEXT_SEARCHING+finalStr.encode('utf-8')+'......')
            t=threading.Thread(target=self.searching)
            t.start()
            
        self.listBox.SetSelection(self.listBox.GetCount()-1)
    def searching(self):
        imageGrasp=ImageGrasp(self.textSearch.GetValue())
        imageGrasp.openURL()
app=wx.App()
frame=Frame0()
frame.Show(True)
app.MainLoop()

import sys,u1,jieba,wordcloud
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from PyQt5.QtCore import pyqtSlot
from scipy.misc import imread
class MyWindow(QMainWindow,u1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bm='utf-8'
        self.background='white'
        self.progressBar.hide()
    @pyqtSlot()
    def on_bcloud_clicked(self):
        self.progressBar.show()
        self.progressBar.setValue(10)
        txt=open(self.lineEdit.text(),encoding=self.bm).read()
        for i in '，。；：‘’“”【】？、（）！…… \n':
            txt=txt.replace(i,' ')
        self.progressBar.setValue(15)
        lt=jieba.lcut(txt)
        self.progressBar.setValue(30)
        txt2=' '.join(lt)
        widths=eval(self.lewidth.text())
        heights=eval(self.leheight.text())
        font=self.lefont.text()
        if font=='':
            font='C:\\Windows\\Fonts\\simfang.ttf'
        self.progressBar.setValue(40)
        if self.lemask.text()!='':
            mk=imread(self.lemask.text())
            word=wordcloud.WordCloud(background_color=self.background,\
                stopwords=None,width=widths,height=heights,\
                    font_path=font,\
                        max_words=self.sbnum.value(),\
                            max_font_size=self.sbmax.value(),\
                                min_font_size=self.sbmin.value(),\
                                    font_step=self.sbrange.value(),\
                                        mask=mk)
        else:#默认没有mask
            word=wordcloud.WordCloud(background_color=self.background,\
                stopwords=None,width=widths,height=heights,\
                    font_path=font,\
                        max_words=self.sbnum.value(),\
                            max_font_size=self.sbmax.value(),\
                                min_font_size=self.sbmin.value(),\
                                    font_step=self.sbrange.value(),\
                                        )
        self.progressBar.setValue(60)
        pathsave=self.lesave.text()
        if pathsave=='':
            pathsave='词云.png'
        self.progressBar.setValue(65)
        word.generate(txt2)
        self.progressBar.setValue(70)
        word.to_file(pathsave)
        self.progressBar.setValue(100)
        self.progressBar.hide()
    @pyqtSlot()
    def on_tbfont_clicked(self):
        path=QFileDialog.getOpenFileName(self,'选择TTF字体','./','TTF(*.ttf)')[0]
        self.lefont.setText(path)
    @pyqtSlot()
    def on_tbmask_clicked(self):
        path=QFileDialog.getOpenFileName(self,'选择PNG文件','./','PNG文件(*.png)')[0]
        self.lemask.setText(path)
    @pyqtSlot()
    def on_tbsave_clicked(self):
        path=QFileDialog.getSaveFileName(self,'保存','./','PNG(*.png);;JPG(*.jpg)')[0]
        self.lesave.setText(path)
    @pyqtSlot(int)
    def on_checkBox_stateChanged(self,state):
        if state==2:
            self.background='black'
            print('black')
        else:
            self.background='white'
            print('white')
    @pyqtSlot(int)
    def on_checkBox_2_stateChanged(self,state):
        if state==2:
            self.bm='gbk'
        else:
            self.bm='utf-8'
    @pyqtSlot()
    def on_tbopen_clicked(self):
        path=QFileDialog.getOpenFileName(self,'打开','./','文本文件(*.txt)')[0]
        self.lineEdit.setText(path)
    
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())

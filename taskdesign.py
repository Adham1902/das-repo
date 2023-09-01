import PyQt5.QtWidgets as qtw
import task14 as window

#from PyQt5.QtWidgets import QLineEdit

class mainwindow(qtw.QMainWindow,window.Ui_ToDoList):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tasks = []
        self.addtask.clicked.connect(self.add_task)
        self.sortname.clicked.connect(self.sort_n)
        self.sortdeadline.clicked.connect(self.sort_date)
        self.deletetask.clicked.connect(self.delete_task)
        self.deleteall.clicked.connect(self.delete_all)
        self.exit.clicked.connect(self.Exit)        
    def add_task(self):
        task = self.addedtask.toPlainText()
        due_data=self.duetask.toPlainText()
        self.tasks.append({"task": task, "due_date": due_data, "done": False})
        self.listoftasks.addItem(task)
        if due_data!="":
            
            self.listoftasks.addItem(due_data)
        self.addedtask.clear()
        self.duetask.clear()
    
    def sort_date(self):
        swapped=True
        while True:
            if swapped==False:
                break
            swapped=False 
            for i in range(0,len(self.tasks)-1):
                dates1=self.tasks[i]["due_date"].split("/")
                dates2=self.tasks[i+1]["due_date"].split("/")
                date_m=int(dates1[1])
                date2_m=int(dates2[1])
                day1=int(dates1[0])
                day2=int(dates2[0])
                if date2_m<date_m:
                    swapped=True
                    swap=self.tasks[i]["task"]
                    self.tasks[i]["task"]=self.tasks[i+1]["task"]
                    self.tasks[i+1]["task"]=swap
                    
                    
                    swap_d=self.tasks[i]["due_date"]
                    
                    self.tasks[i]["due_date"]=self.tasks[i+1]["due_date"]
                    self.tasks[i+1]["due_date"]=swap_d
                elif  date_m==date2_m:
                     
                     if day2< day1:
                        swapped=True
                        swap=self.tasks[i]["task"]
                        self.tasks[i]["task"]=self.tasks[i+1]["task"]
                        self.tasks[i+1]["task"]=swap
                        
                        swap_d=self.tasks[i]["due_date"]
                        self.tasks[i]["due_date"]=self.tasks[i+1]["due_date"]
                        self.tasks[i+1]["due_date"]=swap_d     
        self.listoftasks.clear()        
        for i in range(0,len(self.tasks)):
            self.listoftasks.addItem(self.tasks[i]["task"])
            self.listoftasks.addItem(self.tasks[i]["due_date"])    
    def sort_n(self):
        swapped=True
        while True:
            if swapped==False:
                break
            swapped=False 
            for i in range(0,len(self.tasks)-1):
                if self.tasks[i+1]["task"]<self.tasks[i]["task"]:
                    swapped=True
                    swap=self.tasks[i]["task"]
                    self.tasks[i]["task"]=self.tasks[i+1]["task"]
                    self.tasks[i+1]["task"]=swap
        self.listoftasks.clear()        
        for i in range(0,len(self.tasks)):
            self.listoftasks.addItem(self.tasks[i]["task"])                         
    def delete_task(self):
        selecteditems=self.listoftasks.selectedItems()
        if selecteditems:
            selectetask=selecteditems[0].text()
            self.listoftasks.takeItem(self.listoftasks.row(selecteditems[0]))
            for taskitem in self.tasks:
                if taskitem["task"] == selecteditems:
                    self.tasks.remove(taskitem)
    def delete_all(self):
        self.listoftasks.clear()
        self.tasks=[]

    def Exit(self):
        win.close()
        
app = qtw.QApplication([])
win=mainwindow()
win.show()
app.exec()
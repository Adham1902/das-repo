import PyQt5.QtWidgets as qtw
import task14 as window

class mainwindow(qtw.QMainWindow,window.Ui_ToDoList):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tasks = []
        self.addtask.clicked.connect(self.add_task)
        self.search.clicked.connect(self.search_task)
        self.deletetask.clicked.connect(self.delete_task)
        self.deleteall.clicked.connect(self.delete_all)
        self.exit.clicked.connect(self.Exit)        
    def add_task(self):
        task = self.addedtask.toPlainText()
        due_data=self.duetask.toPlainText()
        self.tasks.append({"task": task, "due_date": due_data, "done": False})
        self.listoftasks.addItem(task)
        self.addedtask.clear()
        self.duetask.clear()

    def search_task(self):  
        text = self.searchtask.toPlainText()
        for task_item in self.tasks:
            if text in (task_item["task"]):
                self.searching.clear()
                self.searching.addItem(text)
                self.searchtask.clear()
                
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
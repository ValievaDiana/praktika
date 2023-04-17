if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ChatMainWindow = QtWidgets.QMainWindow()
    ui = Ui_ChatMainWindow()
    ui.setupUi(ChatMainWindow)
    ChatMainWindow.show()
    sys.exit(app.exec_())
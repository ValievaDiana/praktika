if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ContactsWindow = QtWidgets.QMainWindow()
    ui = Ui_ContactsWindow()
    ui.setupUi(ContactsWindow)
    ContactsWindow.show()
    sys.exit(app.exec_())
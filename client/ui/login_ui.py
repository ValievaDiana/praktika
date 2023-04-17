if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login_Dialog = QtWidgets.QDialog()
    ui = Ui_Login_Dialog()
    ui.setupUi(Login_Dialog)
    Login_Dialog.show()
    sys.exit(app.exec_())
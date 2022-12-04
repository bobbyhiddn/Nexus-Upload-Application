import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QCoreApplication

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Uploader'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a button for uploading the file
        uploadButton = QPushButton('Upload', self)
        uploadButton.setToolTip('Click to upload the file')
        uploadButton.move(250, 220)
        uploadButton.clicked.connect(self.uploadFile)

        # Create a text box for the user to enter the file path
        self.filePath = QLineEdit(self)
        self.filePath.move(250, 180)
        self.filePath.resize(280, 20)

        # Create a label for the file path text box
        filePathLabel = QLabel(self)
        filePathLabel.setText("File path:")
        filePathLabel.move(150, 180)

        # Create a text box for the user to enter the authentication key
        self.authKey = QLineEdit(self)
        self.authKey.move(250, 140)
        self.authKey.resize(280, 20)

        # Create a label for the authentication key text box
        authKeyLabel = QLabel(self)
        authKeyLabel.setText("Authentication key:")
        authKeyLabel.move(150, 140)

        # Create a text box for the user to enter the Nexus URL
        self.nexusURL = QLineEdit(self)
        self.nexusURL.move(250, 100)
        self.nexusURL.resize(280, 20)

        # Create a label for the Nexus URL text box
        nexusURLLabel = QLabel(self)
        nexusURLLabel.setText("Nexus URL:")
        nexusURLLabel.move(150, 100)

        # Create a label for displaying the uploaded file
        self.uploadedFile = QLabel(self)
        self.uploadedFile.move(250, 250)

        self.show()

    def uploadFile(self):
        # Get the file path, authentication key, and Nexus URL from the text boxes
        file_path = self.filePath.text()
        auth_key = self.authKey.text()
        nexus_url = self.nexusURL.text()


        # Use the curl command to upload the file to Nexus, using the authentication key and Nexus URL
        
        curl_command = f"curl -X PUT -u {auth_key}: {nexus_url} -F file=@{file_path}"
        try:
            result = subprocess.check_output(curl_command, shell=True)
            # If the file was uploaded successfully, display a success message
            self.uploadedFile.setText("Upload successful!")
        except:
            # If the file upload failed, display a failure message
            self.uploadedFile.setText("Upload failed!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
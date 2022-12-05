import sys
import subprocess

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QLabel, QLineEdit, QProgressBar
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QCoreApplication, QFile


class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Nexus Uploader'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Calculate the x and y coordinates for the center of the screen
        rect = self.frameGeometry()
        x = int((app.desktop().width() - rect.width()) / 2)
        y = int((app.desktop().height() - rect.height()) / 2)

        # Set the background color of the app to white (#FFFFFF)
        self.setStyleSheet("font-family: Arial;background-color: #767685;")


        # Move the application to the center of the screen
        self.move(480, 150)


        # Create a button for uploading the file
        uploadButton = QPushButton('Upload', self)
        uploadButton.setToolTip('Click to upload the file')
        uploadButton.move(250, 220)
        uploadButton.clicked.connect(self.uploadFile)

        # Create a progress bar for displaying the upload status
        progressBar = QProgressBar(self)

        # Set the minimum and maximum values of the progress bar
        progressBar.setMinimum(1)
        progressBar.setMaximum(100)

        # Set the initial value of the progress bar
        progressBar.setValue(0)

        # Set the position and size of the progress bar
        progressBar.setGeometry(250, 260, 280, 20)

        # Set the label to be displayed under the upload button
        progressBar.stackUnder(uploadButton)

        # Create a text box for displaying the text from "Explain.txt"
        self.explainText = QTextEdit(self)

        # Set the position and size of the text box
        self.explainText.setGeometry(250, 290, 350, 200)

        # Read the contents of "Explain.txt" and set it as the text of the text box
        with open("Explain.txt") as file:
            text = file.read()
            self.explainText.setText(text)


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

        # Create a text box for the user to enter the Nexus repository
        self.repository = QLineEdit(self)
        self.repository.move(250, 60)
        self.repository.resize(280, 20)

        # Create a label for the Nexus repository text box
        repositoryLabel = QLabel(self)
        repositoryLabel.setText("Nexus repository:")
        repositoryLabel.move(150, 60)

        # Create a text box for the user to enter the Nexus directory
        self.directory = QLineEdit(self)
        self.directory.move(250, 20)
        self.directory.resize(280, 20)

        # Create a label for the Nexus directory text box
        directoryLabel = QLabel(self)
        directoryLabel.setText("Nexus directory:")
        directoryLabel.move(150, 20)

        # Create a variable that contains all of the fields in the application
        fields = (self.filePath, self.authKey, self.nexusURL, self.repository, self.directory)


       # Create a label for displaying the image
        imageLabel = QLabel(self)

        # Set the pixmap property of the label to the image you want to display
        imageLabel.setPixmap(QPixmap("Nexus_Logo.png"))

        # Move the label to the top right corner of the application
        #imageLabel.move(self.width - imageLabel.width(), 0)
        imageLabel.setGeometry(0, 100, 640, 480)

        # Set the label to be displayed under the fields variable
        imageLabel.lower()

        # Create a label for displaying the uploaded file
        self.uploadedFile = QLabel(self)
        self.uploadedFile.move(800, 600)

        #Show the application
        self.show()

    def uploadFile(self):
        # Get the file path, authentication key, Nexus URL, repository, and directory from the text boxes
        file_path = self.filePath.text()
        auth_key = self.authKey.text()
        nexus_url = self.nexusURL.text()
        repository = self.repository.text()
        directory = self.directory.text()
        

        
        # Use the curl command to upload the file to Nexus, using the authentication key, Nexus URL, repository, and directory
        curl_command = f"curl -X PUT -u {auth_key}: {nexus_url}/{repository}/{directory} -F file=@{file_path} -k"

        # Update the progress bar to show the progress of the upload
        progressBar.setValue(currentProgress)

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



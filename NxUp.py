
import PyQt5

import sys

import subprocess

import logging

import os


 

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QLabel, QLineEdit, QProgressBar, QFileDialog

from PyQt5.QtGui import QPixmap

 

class App(QWidget):

   

 

    def openFileDialog(self):

        # Open the file browse dialog

        file = QFileDialog.getOpenFileName(self, 'Select a file')

 

        # Store the full file path in a separate variable

        self.filePath = file[0]

       

        # Use the os.path.basename() function to extract the file name from the file path

        file_name = os.path.basename(file[0])

 

       

        # Update the text of the file name label

        self.fileNameLabel.setText(file_name)

 

        # Log a debug message

        self.logger.debug('Opening file dialog')

 

    def initUI(self):

 

        # Log an info message

        self.logger.info('Initializing UI')

 

        self.setWindowTitle(self.title)

        self.setGeometry(self.left, self.top, self.width, self.height)

 

        # Calculate the x and y coordinates for the center of the screen

        rect = self.frameGeometry()

        x = int((app.desktop().width() - rect.width()) / 2)

        y = int((app.desktop().height() - rect.height()) / 2)

 

        # Set the background color of the app to white (#FFFFFF)

        self.setStyleSheet("font-family: Arial;background-color: #767685;")

 

        # Move the application to the center of the screen

        self.move(240, 90)





        # Create a button for uploading the file

        uploadButton = QPushButton('Upload', self)

        uploadButton.setToolTip('Click to upload the file')

        uploadButton.move(300, 220)

        uploadButton.clicked.connect(self.upload_to_nexus)

 

        # Create a progress bar for displaying the upload status

        self.progressBar = QProgressBar(self)

 

        # Set the minimum and maximum values of the progress bar

        self.progressBar.setMinimum(1)

        self.progressBar.setMaximum(100)

 

        # Set the initial value of the progress bar

        self.progressBar.setValue(0)

 

        # Set the position and size of the progress bar

        self.progressBar.setGeometry(300, 260, 280, 20)

 

        # Set the label to be displayed under the upload button

        self.progressBar.stackUnder(uploadButton)

 

       

 

        # Create a text box for displaying the text from "Explain.txt"

        self.explainText = QTextEdit(self)

 

        # Set the position and size of the text box

        self.explainText.setGeometry(250, 290, 650, 650)

 

        # Read the contents of "Explain.txt" and set it as the text of the text box

        with open("Explain.txt") as file:

            text = file.read()

            self.explainText.setText(text)

 

        #Create a button for opening the file browse dialog

        browseButton = QPushButton('Browse', self)

        browseButton.setToolTip('Click to browse for a file')

        browseButton.move(300, 140)

        browseButton.clicked.connect(self.openFileDialog)

 

        # Create a label for displaying the selected file name

        self.fileNameLabel = QLabel(self)

        self.fileNameLabel.move(420, 140)

        self.fileNameLabel.resize(280, 20)

        #file_name = os.path.basename(self.filePath)

   

 

        # Create a text box for displaying the selected file path

        self.filePathform = QLabel(self)

        self.filePathform.setText("File path:")

        self.filePathform.move(150, 140)

 

        # Create a text box for the user to enter the authentication key

        self.authKey = QLineEdit(self)

        self.authKey.move(300, 180)

        self.authKey.resize(280, 20)

 

        # Create a label for the authentication key text box

        authKeyLabel = QLabel(self)

        authKeyLabel.setText("Authentication key:")

        authKeyLabel.move(150, 180)

 

        # Create a text box for the user to enter the Nexus URL

        self.nexusURL = QLineEdit(self)

        self.nexusURL.move(300, 20)

        self.nexusURL.resize(280, 20)

 

        # Create a label for the Nexus URL text box

        nexusURLLabel = QLabel(self)

        nexusURLLabel.setText("Nexus URL:")

        nexusURLLabel.move(150, 20)

 

        # Create a text box for the user to enter the Nexus repository

        self.repository = QLineEdit(self)

        self.repository.move(300, 60)

        self.repository.resize(280, 20)

 

        # Create a label for the Nexus repository text box

        repositoryLabel = QLabel(self)

        repositoryLabel.setText("Nexus repository:")

        repositoryLabel.move(150, 60)

 

        # Create a text box for the user to enter the Nexus directory

        self.directory = QLineEdit(self)

        self.directory.move(300, 100)

        self.directory.resize(280, 20)

 

        # Create a label for the Nexus directory text box

        directoryLabel = QLabel(self)

        directoryLabel.setText("Nexus directory:")

        directoryLabel.move(150, 100)

 

        # Create a variable that contains all of the fields in the application

        #fields = (self.filePath, self.authKey, self.nexusURL, self.repository, self.directory)

 

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

 

    def upload_to_nexus(self):

        # Log an info message

        self.logger.info('Uploading to Nexus')

 

        # Set the value of the progress bar to 10

        self.progressBar.setValue(2)

 

        # Get the values entered by the user in the input fields  

        nexus_url = self.nexusURL.text()

        repository = self.repository.text()

        auth_key = self.authKey.text()

        directory = self.directory.text()

        file_Path = self.filePath

        # Use the os.path.basename() function to extract the file name from the file path

        #file_name = os.path.basename(self.filePath)

        file_name = self.fileNameLabel.text()

        #file_path = self.filePath()

 

        # Check if the authentication key has been entered

        if self.authKey.text() == '':

            # Log an error message

            self.logger.error('No authentication key entered')

            return

 

        # Open the file in binary mode

        with open(file_Path, "rb") as file:

            # Set the form fields for the request

 

            # Check if the nexus_url value starts with https:// or http://

            if not nexus_url.startswith('https://') and not nexus_url.startswith('http://'):

                # If not, add the https:// prefix to the nexus_url value

                # You can also use the http:// prefix if your Nexus server is accessible using HTTP

                nexus_url = 'https://' + nexus_url

 

            # Set the URL for the Nexus REST API endpoint for uploading components

            url = '{}/service/rest/v1/components?repository={}'.format(nexus_url, repository)

 

            # Create a string containing the `curl` command and its options

            curl_command = 'curl -v -k -X POST "{}" -H "accept: application/json" -H "Content-Type: multipart/form-data" -H "Authorization: Basic {}" -F "raw.directory={}" -F raw.asset1=@{} -F "raw.asset1.filename={}" '.format(url, auth_key, directory, file_Path, file_name)

 

            # Run the `curl` command using the `subprocess` module

            response = subprocess.run(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

 

            # Write the curl command to a text file

            with open('curl_command.txt', 'w') as file:

                file.write(curl_command)

 

            # Check if the upload process has completed successfully

            if response.returncode == 0:

                # Log a success message

                self.logger.info('File uploaded successfully')

 

                # Update the progress bar

                self.progressBar.setValue(100)

            else:

                # Log an error message with the response details

                self.logger.error('Failed to upload file to Nexus server: status_code=%s, body=%s', response.returncode, response.stdout)

 

           

    def __init__(self):

 

        # Initialize the logger object

        self.logger = logging.getLogger('NxUp')

        self.logger.setLevel(logging.DEBUG)

 

        # Create a file handler for the logger

        file_handler = logging.FileHandler('log_NxUp.log')

 

        # Create a formatter for the logger

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

 

        # Attach the formatter to the file handler

        file_handler.setFormatter(formatter)

 

        # Attach the file handler to the logger

        self.logger.addHandler(file_handler)

 

        try:

            super().__init__()

            self.title = 'Nexus Uploader'

            self.left = 10

            self.top = 10

            self.width = 650

            self.height = 800

            self.initUI()

        except Exception as e:

            self.logger.exception('Error initializing application: {}'.format(str(e)))

 

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = App()

    sys.exit(app.exec_())
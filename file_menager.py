class FileManager():
    def __init__(self, fileName):
        self.fileName=fileName
    def read_file(self):
        pliczek=open(self.fileName)
        dane = pliczek.read()
        print(dane)
        pliczek.close()
    def update_file(self, text_data):
        pliczek = open(self.fileName, 'a', encoding='utf-8')
        pliczek.write(text_data)
        pliczek.close()
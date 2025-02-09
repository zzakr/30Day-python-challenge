class Document:
    def write(self):
        return "Writing document..."

class Pen:
    def write(self):
        return "Writing with pen..."

def start_writing(obj):
    print(obj.write())

start_writing(Document())  # Writing document...
start_writing(Pen())       # Writing with pen...

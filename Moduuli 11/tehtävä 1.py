class Publication:
    def __init__(self,type_p,name):
        self.type_p = type_p
        self.name = name

class Book(Publication):
    def __init__(self,type_p,name,author,page_count):
        super().__init__(type_p,name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"{self.author} wrote the {self.type_p} {self.name}, and it is {self.page_count} pages long.")



class Magazine(Publication):
    def __init__(self,type_p,name,chief_editor):
        super().__init__(type_p,name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"{self.chief_editor} is the chief editor of the {self.type_p} {self.name}.")


publications = []
publications.append(Magazine("magazine","Donald Duck","Aki Hyyppä"))
publications.append(Book("book","Compartment no.6","Rosa Liksom","192"))
print(" ")
for i in publications:
    i.print_information()
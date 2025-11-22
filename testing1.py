book=[]
class Library:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        book.append(self.title)  # اضافه کردن عنوان کتاب به لیست     
    def remov_book(remov):
        if remov in book:
            book.remove(remov)
        else:
             print(f"'{remov}' is not found in the book list.")

    def show_boook(self):
        print(book) 
    def search_book(sisi):
        if sisi in book :
            print(sisi)
        else :
            print(f"{sisi} ra mojod nadarim")    

                

        
                
rosh=Library("tarikh","garaloo")
martob=Library("hava","karimi")
ziba=martob.show_boook()
#Library.search_book("havab")




#                    ------------------------------------------------------- Library Management System -----------------------------------------------------------------------

class Library:

     # constructer method 
     # __init__ methodu, sınıfın kurucu methodudur. Bu method, sınıfın bir nesnesi oluşturulduğunda otomatik olarak çağrılır.Bu nedenden dosya açma işlemini burada yapmalıyız.
    
    def __init__(self, file_name):    
        self.file_name = file_name  #Sınıfın dosya adını sakladık.
        self.file =open (self.file_name, 'a+',encoding="utf-8") # open methodu verilen parametrelerle dosya açmaya yarar.
                                                                # open methodunun 'a+' modu ile dosyaya hem yazma hemde okuma amacıyla açabiliriz.Bu sebepten 'a+' modu kullancağız. Dosayı 'a+' modu ile açtığımızda
                                                                # dosya mevcut ise dosya pointeri otomatikmen dosya sonuna konumlanır yazma işlemi dosya sonuna yapılır.Eğer dosya mevcut değilse oluşturulur.
    
     # destructor method
     # __del__ methodu sınıf nesnesi yok edildiğinde otomatik olarak çağrılır. Bu metod, dosyayı kapatmak için kullanmalıyız.
     # Dosya işlemi tamamlandığında dosyanın kapatılması önemlidir çünkü dosyaların işlem sırasında açık kalması beklenmedik hatalara neden olabilir.
        
    def __del__(self):
        self.file.close() # Bu method dosyayı kapatır.


     #-------- a. List Books ---------
     # books.txt dosyasındaki tüm kitapları listelemek amacıyla bir method yazmalıyız.
     # Öncelikle dosyanın içeriğini okuyup bu dosyada bulunan her bir satırı bir listeye eklemeliyiz. Ardından bu listeyi kullanarak kitap adlarını ve yazarlarını terminale bastırmalıyız.  
         
    def list_books(self):
        # 'a+' modunda dosyayı açtığımız için dosya pointeri otomatik olarak dosya sonuna işaret eder. Okuma yapabilmek için öncelikle dosya pointerini dosyanın başlangıcına point ettirmeliyiz.

        self.file.seek(0) # Dosya pointerını dosya başlangıcına konumlandırdık baştan kitapları listelemek için
        book_list = self.file.read().splitlines() # Dosyanın tamamını read() methodu ile okur ve splitlines() methoduyla string'i satırlara bölüp her bir satırı içeren bir liste oluşturulur.
        
        # Dosyada kitap var mı yok mu onun kontrolünü sağlamalıyız.

        if not book_list:
            print("\nIn the books.txt file is empty. No books have been added yet.")
            return
        else:    
           for book in book_list:
             book_details = book.strip().split(",") # strip() methodu her kitap için baştaki ve sondaki boşlukları temizler ve split() methoduyla kitap adını,yazarı,yayımlanma tarihini ve sayfa sayısını ayırırız.
                                               
             # Her satırın gerekli bilgileri içerdiğinden emin olmak amacıyla kontrol sağlamamıza gerek yok çünkü add_book() methodunda kontrolleri sağlıyoruz.
            
             book_name, author = book_details[0:2]  # Kitap adını ve yazarını terminale bastırmak için bir değişkene atarız.
             print(f"\nBook Name: {book_name}, Author: {author}") # Kitap adını ve yazarını formatlı string biçiminde terminale bastırırız.
    
     #-------- b. Add Book ---------
     # books.txt dosyasına kitap başlığı,kitap yazarı,yayımlanma tarihi ve sayfa sayısı bilgilerini içeren bir kitap ekleyecek method yazmalıyız.
     # Kitap bilgilerini kullanıcıdan isteyip değişkenlere atamalıyız.Ardından kitap bilgileri ile aralarında virgül olacak şekilde bir string oluşturup bu stringi dosyaya eklemeliyiz.          

    def add_book(self):
        book_title = input("\nEnter the book title: ")
        book_author = input("Enter the book author: ")
        release_year = input("Enter the release year: ")
        num_pages = input("Enter the number of pages: ")    

         # Girişlerin boş olup olmadığını kontrol etmek için basit bir hata kontrolü yapmalıyız.
        
        if not book_title or not book_author or not release_year or not num_pages:
           print("The book could not be added to the books.txt file. Please enter all book information.")
           print("For unknown book information, 'unknown' should be written.")
           return

         # Sayfa sayısının sayısal bir değer olup olmadığını kontrol etmeliyiz.
         
        if not num_pages.isdigit():
          print("The book could not be added to the books.txt file. Number of pages must be a valid integer.")
          return

         # Yayımlanma yılının sayısal bir değer olup olmadığını kontrol etmeliyiz.
        
        if not release_year.isdigit():
          print("The book could not be added to the books.txt file. Release year must be a valid integer.")
          return
   


        book = f"{book_title},{book_author},{release_year},{num_pages}\n" # Kitap bilgilerini içeren ve virgül ile bilgilerin birbirinden ayrıldığı bir string oluşturduk.

        self.file.write(book)# Kitap bilgilerini içeren string'i write() methoduyla books.txt dosyasının sonuna ekleriz (a+ modunda açtığımız için file pointer otomatik olarak dosya sonuna konumlanır.)
        print("Book successfully added to books.txt file.")


     #-------- c. Remove Book --------
     # Bu method'da kullanıcıdan bir kitap başlığı alınıp o kitap başlığına sahip kitap silinecektir.
     # Öncelikle kullanıcıdan silinecek kitap başlığı alınmalı sonra books.txt dosyasındaki tüm kitaplar bir listeye alınıp silinecek kitap başlığı hangi indexte ise bulunmalı ve 
     # birden fazla aynı isme sahip kitap olabileceği için bu indexler bir listede tutulmalıdır.
     # Tüm kitapların olduğu listede for ile dönüp silinecek kitapların index listesi ve kontrol yapıları yardımı ile ilgili başlığa sahip kitap bilgileri listeden silinmelidir.
     # Sonra books.txt dosyası boşaltılıp kullanıcıdan alınan kitabın silinmesiyle oluşan yeni listeyi tekrar books.txt dosyasına yazılmalıdır.
        
    def remove_book(self):
        book_title = input("\nEnter the title of the book to be removed:" )

        # Dosyanın başından içeriğini okuyup kitapların bilgilerini bir listeye ekleyelim.İlk önce dosya pointerini dosyanın başlangıcına konumlandırmalıyız.
        # Ardından tüm satırları okuyup bir listeye eklemeliyiz.

        self.file.seek(0) # Dosya pointerini dosyanın başlangıcına konumlandırdık.
        book_list= self.file.readlines() # Dosyanın tüm satırlarının bir listesini aldık.

       # print(book_list)  # Kontrol sağlamak amacıyla kullanıldı.

        # Bu adımdan sonra 2 yol izleyebiliriz. 
          # 1.yol-- Listede gezerek silinecek kitabın başlığını içermeyen sütunları yeni bir listeye ekleyip books.txt yazarız.
          # 2.yol-- Listede gezerek silinecek kitabın başlığını içeren sütünların indexleri bulup onları listeden silip books.txt listeyi yazarız.
        
        # Bizden 2.yol istenmektedir.

        # Yukarıda oluşturduğumuz kitap listesi içerisinde gezerek silinecek kitabın hangi indexte olduğunu bulmalıyız.
        # Aynı başlığa sahip birden fazla kitap olabilir bu yüzden yine bir liste oluşturacağız bu liste silinecek kitapların bulunduğu indexleri tutacak.

        indexes_to_remove = [] # Silinecek kitapların indexlerini tutacak liste 
        for index,book in enumerate(book_list): # enumerate methoduyla hem elemanın indexini hemde kendisini elde ediyoruz.
            removed_book=book.strip().split(",") # Kullanıcının girdiği başlıkla listedeki kitapları karşılaştırmak için her kitabın bilgilerini ayırıp listeye atmalıyız.

           # print(removed_book) # Kontrol sağlamak amacıyla kullanıldı.

            if removed_book[0]==book_title:  # removed_book listesinin ilk elemanı kitabın başlığını içerdiği için kontrolü böyle sağlamalıyız.
                                             # Burada if book.startswith(book_title): kullanılırsa yanlış bir kullanım olur nedenini bir örnek ile açıklayalım.
                                             # Kış ve Kış Güzeli adında 2 kitabımız olsun Kış adlı kitabı silmek istediğimizde 2 kitapta kış ile başladığı için 2 kitabıda silecektir.
             indexes_to_remove.append(index) # Kontrol doğru ise silenecek kitabın indexini listeye ekleriz.

     # print(indexes_to_remove) # Kontrol sağlamak amacıyla kullanıldı. 
             
        # Eğer silinecek kitap başlığına sahip kitap dosyada mevcut ise silme işlemi gerçekleştireceğiz mevcut değil ise kullanıcıya geri dönüt sağlayacağız.
             
        if indexes_to_remove :

          # Listedeki indexler silime işlemi sırasında değiştiğinden dolayı yanlış kitapları silebiliriz bunu önlemek için indexlerin bulunduğu listedeki elemanları tersten silmeliyiz.
            
            for index in reversed(indexes_to_remove):
              del book_list[index]
              
              # print(book_list) # Kontrol sağlamak amacıyla kullanıldı.  

         # Bundan sonra books.txt dosyasının içeriğini temizleyip yeni listeyi books.txt yazmalıyız.    
                 
            self.file.seek(0) # Dosya ponterini dosya başına aldık dosyanın içeriğini temizleyeceğimiz için.
            self.file.truncate() # truncate() methoduyla dosyanın içeriğini tamamen temizleriz.

         # Güncellenmiş liste ile dosyayı tekrar yazıyoruz.
            
            for book in book_list:
                self.file.write(book)

            print(f"\nBook with title '{book_title}' removed successfully.")

         #Eğer kullanıcın girdiği kitap başlığına sahip bir kitap listesimizde yok ise   
             
        else:
            print(f"\nNo book found with title '{book_title}'.")

    


lib = Library("books.txt") # Library sınıfından bir nesne oluşturduk. # Kod ile dosya aynı dizinde oldukları için direk dosya adı yazılmıştır dosyanın tam path'i de yazılabilir.

# lib nesnesi ile etkileşim için menüyü tasarlayalım.
while True:
    print("\n---------------------------------------")
    print("\n***MENU***")
    print("1) List Books")  # Terminalde 1'e basıldığında books.txt dosyasındaki kitapların başlığı ve yazarı listelenmesini istiyoruz.
    print("2) Add Book")    # Terminalde 2'ye basıldığında books.txt dosyasına kullanıcıdan alınan bilgileri içeren kitabın eklenmesini istiyoruz.
    print("3) Remove Book") # Terminalde 3'e basıldığında kullanıcıdan alınan kitap başlığına sahip kitap bilgileri books.txt dosyasından silinmesini istiyoruz.
    print("4) Quit")        # Terminalde 4'e basıldığında uygulamadan çıkış yapılmasını istiyoruz.
    

    choice = input("Enter your choice (1-4): ") # Kullanıcıdan menüye göre seçimi istenir.
    print("\n---------------------------------------")

     # Kullanıcı seçimine göre gerekli methodlar çalıştırılır.
    if choice == "1":
        lib.list_books()  # Terminalde 1'e basıldığında books.txt dosyasındaki kitapların başlığı ve yazarı list_books() method'u yardımıyla listelenir.
    elif choice == "2":
        lib.add_book()    # Terminalde 2'ye basıldığında books.txt dosyasına kullanıcıdan alınan bilgileri içeren kitap add_book() method'u yardımıyla eklenir.
    elif choice == "3":
        lib.remove_book() # Terminalde 3'e basıldığında kullanıcıdan alınan kitap başlığına sahip kitap bilgileri books.txt dosyasından remove_book() method'u yardımıyla silinir.
    elif choice == "4":
        exit()            # Terminalde 4'e basıldığında uygulamadan çıkış yapılır.
    else:
        print("\nInvalid choice. Please enter a number between 1 and 4.")  # Diğer durumlarda hata mesajı verilir.


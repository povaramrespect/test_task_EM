from .data_manager import Data

class Data_Operator(Data):
    """Class with all operations with data"""
    def __init__(self, data: Data) -> None:
        self.data = data
        self.books = data.books
        self.current_id = data.current_id
        self.logger = data.logger
        self.file_path = data.file_path

    def print_books(self):
        """Prints all books from database"""
        print("ID |    TITLE    |    AUTHOR    |   YEAR   |  STATUS  ")
        for book in self.books:
            for value in book.items():
                print(value[1], end=' | ')
            print()

    def print_book(self, book):
        """Prints all found books by search condition"""
        print("ID |    TITLE    |    AUTHOR    |   YEAR   |  STATUS  ")
        for i in book:
            for value in i.items():
                print(value[1], end=' | ')
            print()

    def find_book_by_title(self, key):
        """Returns list of all found books by title. 
        key -> output(list)"""
        output = []
        for book in self.books:
            if book['title'] == key:
                output.append(book)
        return(output)

    def find_books_by_author(self, key):
        """Returns list of all found books by author. 
        key -> output(list)"""
        output = []
        for book in self.books:
            if book['author'] == key:
                output.append(book)

        return(output)
            
    def find_books_by_year(self, key):
        """Returns list of all found books by year. 
        key -> output(list)"""
        output = []
        for book in self.books:
            if book['year'] == key:
                output.append(book)

        return(output)
            
    def add_book(self, title, author, year):
        """Stores new book into list: books, then saves it in database file."""
        new_book = {
            'id': self.current_id,
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии'
        }
        self.books.append(new_book)
        self.save_to_file()
        self.logger.info(f"Книга '{title}' добавлена с ID {self.current_id}")
        self.current_id += 1

    def delete_book(self, id):
        """Deletes book by id."""
        original_length = len(self.books)
        self.books = [book for book in self.books if book['id'] != id]
        if len(self.books) < original_length:
            self.logger.info(f"Книга с ID {id} удалена")
            self.save_to_file()
        else:
            self.logger.error(f'Книга с ID: {id} не найдена.')

    def update_status(self, id, status):
        """Updates book status.
        id, status -> new status on id"""
        if status == 1:
            status = 'в наличии'
        elif status == 2:
            status = 'выдана'
        updated = False
        for book in self.books:
            if book['id'] == id:
                book['status'] = status
                updated = True
                break
        if not updated:
            return self.logger.error(f'Книга с ID: {id} не найдена.')
        self.logger.info(f'Статус книги с ID {id} обновлен на: {status}')
        self.save_to_file()
        

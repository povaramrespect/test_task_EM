import json

class Data:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.books = self.read_file()
        self.current_id = self.autoincrement()

    def read_file(self):
        with open(self.file_path, encoding='utf-8') as f:
            books = json.load(f)
        return books

    def print_books(self):
        for book in self.books:
            for key, value in book.items():
                print(f'{key} : {value}')
            print()

    def find_book_by_title(self, key):
        output = []
        for book in self.books:
            if book['title'] == key:
                output.append(book)
        return(output)

    def find_books_by_author(self, key):
        output = []
        for book in self.books:
            if book['author'] == key:
                output.append(book)

        return(output)
            
    def find_books_by_year(self, key):
        output = []
        for book in self.books:
            if book['year'] == key:
                output.append(book)

        return(output)
            
    def add_book(self, title, author, year):
        new_book = {
            'id': self.current_id,
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии'
        }
        self.books.append(new_book)
        self.save_to_file()
        self.read_file()
        print(f"Книга '{title}' добавлена с ID {self.current_id}")
        self.current_id += 1

    def save_to_file(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.books, f, ensure_ascii=False, indent=4)

    def autoincrement(self):
        if self.books:
            return max(book['id'] for book in self.books) + 1
        return 1
    
    def delete_book(self, id):
        original_length = len(self.books)
        self.books = [book for book in self.books if book['id'] != id]
        if len(self.books) < original_length:
            self.save_to_file()
            print(f"Книга с ID {id} удалена")
        else:
            raise ValueError(f'Книга с ID: {id} не найдена.')

    def update_status(self, id, status):
        if status not in ['в наличии', 'выдана']:
            raise ValueError(f'Некорректный статус: {status}')
        updated = False
        for book in self.books:
            if book['id'] == id:
                book['status'] = status
                updated = True
                print(f'Статус книги с ID {id} обновлен на: {status}')
                break
        if not updated:
            raise ValueError(f'Книга с ID: {id} не найдена.')
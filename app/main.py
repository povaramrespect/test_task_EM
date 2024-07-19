if __name__ == '__main__':
    from data_manager import Data
    file_path = 'library.json'
    data_manager = Data(file_path)
    books = data_manager.read_file()
    data_manager.print_books()
    data_manager.update_status(5, 'sdf')

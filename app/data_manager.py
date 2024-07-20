import json

class Data:
    """Base dataclass that includes reading, saving, autoincrement."""
    def __init__(self, file_path: str, logger) -> None:
        self.logger = logger
        self.file_path = file_path
        self.books = self.read_file()
        self.current_id = self.autoincrement()

    def read_file(self):
        """Reading file on path to return data in python object"""
        self.logger.debug(f'Reading file: {self.file_path}')
        try:    
            with open(self.file_path, encoding='utf-8') as f:
                books = json.load(f)
            self.logger.debug("База данных успешно открыта.")
            return books
        except: 
            self.logger.error("Ошибка чтения базы данных.")

    def save_to_file(self):
        """Saves python object data to json file"""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.books, f, ensure_ascii=False, indent=4)
            self.logger.debug("Данные успешно сохранены.")
        except Exception as e:
            self.logger.error(f"Ошибка сохранения данных: {e}")

    def autoincrement(self):
        """Autoincrements id value by current max id in books + 1."""
        if self.books:
            return max(book['id'] for book in self.books) + 1
        return 1
    
    
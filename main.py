from json.decoder import JSONDecodeError

if __name__ == '__main__':
    # Запуск приложения
    from app.data_manager import Data
    from app.operations import Data_Operator
    import app.app_config
    # Инициализация настроек
    logger = app.app_config.setup_logger()
    file_path = app.app_config.PATH

    try:
        data_manager = Data(file_path, logger)
        operations = Data_Operator(data_manager)

    except FileNotFoundError as e:
        logger.error(f"JSON файл с данными не обнаружен или поврежден. Проверьте корректность указанного пути. Подробнее:\n{e}")
        quit()


    except JSONDecodeError as e:
        logger.error(f"Указан путь к файлу с неверным форматом или файл поврежден. Программа поддерживает формат .json для файла с данными. Подробнее:\n{e}")
        quit()

    # Бесконечный цикл для отрисовки интерфейса
    while True:
        try:
            action = int(input("Выберите действие:\n1 - показать все книги\n2 - найти книгу\n3 - удалить книгу\n4 - обновить статус книги\n5 - добавить новую книгу\n6 - выйти\n"))
        except ValueError as e:
            logger.error(e)
            print("Ошибка: Введите число от 1 до 5.")
            continue

        if action == 1:
            try:
                print("Полный список книг: ")
                operations.print_books()
            except Exception as e:
                logger.error(e)
                print("Данные не обнаружены")

        elif action == 2:
            try:
                action = int(input("Найти книги по:\n1 - названию\n2 - автору\n3 - году\n4 - назад\n"))
                if action == 1:
                    title = input("Введите название книги(с учетом регистра): ")
                    book = operations.find_book_by_title(title)
                    if book:
                        operations.print_book(book)
                    else:
                        print(f"Книга с названием {title} не найдена")

                elif action == 2:
                    author = input("Введите имя автора(с учетом регистра): ")
                    book = operations.find_books_by_author(author)
                    if book:
                        operations.print_book(book)
                    else:
                        print(f"Книга с автором {author} не найдена")

                elif action == 3:
                    year = input("Введите год книги: ")
                    book = operations.find_books_by_year(year)
                    if book:
                        operations.print_book(book)
                    else:
                        print(f"Книга с годом {year} не найдена")

                elif action == 4:
                    continue

            except ValueError as e:
                logger.error(e)
                print("Ошибка: Введите число от 1 до 4.")
                continue

        elif action == 3:
            try:
                book_id = int(input("Введите id книги для удаления: "))
            except ValueError as e:
                logger.error(e)
                print("Ошибка: Введите id в числовом формате.")
                continue

            operations.delete_book(book_id)

        elif action == 4:
            try:
                book_id = int(input("Введите id книги для обновления статуса: "))

            except ValueError as e:
                logger.error(e)
                print("Ошибка: Введите id в числовом формате.")
                continue

            new_status = int(input("Введите новый статус книги (1 - в наличии, 2 - выдана): "))
            operations.update_status(book_id, new_status)

        elif action == 5:
            title = input("Введите название: ")
            author = input("Введите имя автора: ")
            year = input("Введите год книги: ")
            operations.add_book(title, author, year)

        elif action == 6:
            quit()

        else:
            logger.error("Неверно введено действие")


 
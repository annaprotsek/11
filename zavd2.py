import json

def save_books_to_json():
    books = []
    print("Введіть дані про книги (для завершення введіть порожній рядок):")
    
    while True:
        title = input("Назва книги: ").strip()
        if not title:
            break
        author = input("Автор книги: ").strip()
        books.append({"Назва": title, "Автор": author})
    
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
    print("Файл books.json створено.")

def main_task_2():
    save_books_to_json() 

if __name__ == "__main__":
    main_task_2()

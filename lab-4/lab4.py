# Composite: Файлова система (файли + папки)
from abc import ABC, abstractmethod

# Абстрактний компонент
class FileSystemComponent(ABC):
  @abstractmethod
  def show(self, indent=0):
    pass

# Лист — Файл
class File(FileSystemComponent):
  def __init__(self, name):
    self.name = name

  def show(self, indent=0):
    print("  " * indent + f"- File: {self.name}")

# Композит — Папка
class Folder(FileSystemComponent):
  def __init__(self, name):
    self.name = name
    self.children = []

  def add(self, component: FileSystemComponent):
    self.children.append(component)

  def show(self, indent=0):
    print("  " * indent + f"+ Folder: {self.name}")
    for child in self.children:
      child.show(indent + 1)

# Facade: Простий інтерфейс для взаємодії
class FileSystemFacade:
  def __init__(self):
    self.root = Folder("Root")

  def create_sample_structure(self):
    docs = Folder("Documents")
    pics = Folder("Pictures")

    file1 = File("resume.docx")
    file2 = File("photo.jpg")
    file3 = File("notes.txt")

    docs.add(file1)
    docs.add(file3)
    pics.add(file2)

    self.root.add(docs)
    self.root.add(pics)

  def display_file_system(self):
    self.root.show()

# Основна функція
def main():
  fs = FileSystemFacade()
  fs.create_sample_structure()
  print("Файлова структура:")
  fs.display_file_system()

if __name__ == "__main__":
  main()

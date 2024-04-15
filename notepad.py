import time

notepad = []

def add_note(notepad):
    note = input("Eklemek istediğiniz notu giriniz:\n")
    notepad.append(note)
    print("\nNot başarıyla eklendi.\n")

def delete_note(notepad):
    note = input("Silmek istediğiniz notu girin:\n")
    if note in notepad:
        notepad.remove(note)
        print("\nNot başarıyla silindi.\n")
    else:
        print("\nBöyle bir not bulunmuyor.\n")

def show_note(notepad):
    print("Notlar:\n")
    for note in notepad:
        print("- " + note + "\n")

def clear_notepad(notepad):
    notepad.clear()
    print("\nNotepad başarıyla temizlendi.\n")

while True:
    print("Yapmak istediğin işlemi seç:\n1- Not ekle\n2- Not sil\n3- Notları göster\n4- Not defterini temizle")
    choice = int(input("Seçim: "))

    if choice == 1:
        add_note(notepad)

    elif choice == 2:
        delete_note(notepad)

    elif choice == 3:
        show_note(notepad)

    elif choice == 4:
        clear_notepad(notepad)

    else:
        print("\nBöyle bir işlem yok.")




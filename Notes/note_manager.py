from note import Note
import datetime
import json


class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                notes_data = json.load(file)
                notes = [Note(note["id"], note["title"], note["body"], datetime.datetime.strptime(note["created_at"], "%d.%m.%y %H:%M:%S")
                ) for note in notes_data]
                return notes
        except FileNotFoundError:
            return []
        
    def save_notes(self):
        notes_data = [note.as_dict() for note in self.notes]
        with open(self.file_path, "w") as file:
            json.dump(notes_data, file)
        
    def get_notes_list(self):
        return self.notes
    
    def search_notes_by_data(self, search_date):
        try:
            search_date = datetime.datetime.strptime(search_date, "%d.%m.%y").date()
        except ValueError:
            print("неверный формат даты надо дд.мм.гг")
            return []
        matching_notes = [note for note in self.notes if note.created_at.date() == search_date]
        return matching_notes
    
    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None
        
    def add_note(self, title, body):
        new_note_id = 1 if not self.notes else max(note.note_id for note in self.notes) + 1
        created_at = datetime.datetime.now()
        new_note = Note(new_note_id, title, body, created_at)
        self.notes.append(new_note)
        self.save_notes()

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.note_id == note_id:
                if new_title:
                    note.title = new_title
                if new_body:
                    note.body = new_body
                note.created_at = datetime.datetime.now()
                self.save_notes()
                return
        print(f"не нашли id {note_id}")

    def delete_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                self.save_notes()
                return
        print(f"не нашли id {note_id}")

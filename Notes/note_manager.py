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
                notes = [Note(note["note_id"], note["title"], note["body"], datetime.strptime(note["created_at"], "%d.%m.%y %H:%M:%S")
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
            search_date = datetime.strptime(search_date, "%d.%m.%y").date()
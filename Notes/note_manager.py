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

class Note:
    def __init__(self, note_id, title, body, created_at):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at

    def as_dict(self):
        return {
            "id": self.note_id,
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at.strftime("%d.%m.%y %H:%M:%S")
        }
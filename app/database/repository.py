from app.database.loader import load_database


class DatabaseRepository:

    def __init__(self, uploaded_file):

        self.bets, self.selections = load_database(
            uploaded_file
        )

    def get_bets(self):
        return self.bets

    def get_selections(self):
        return self.selections
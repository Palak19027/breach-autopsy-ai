class LogStore:
    """
    Azure Monitor–style in-memory log store
    """

    def __init__(self):
        self.logs = []

    def store(self, logs):
        self.logs = logs

    def get_all(self):
        return self.logs


log_store = LogStore()

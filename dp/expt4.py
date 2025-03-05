# Protection Proxy example
class SensitiveDocument:
    def view(self, user: str) -> None:
        print(f"Showing confidential document to {user}")


class DocumentProxy:
    def __init__(self):
        self._real_doc = SensitiveDocument()
        self._allowed_users = ["admin", "auditor"]

    def view(self, user: str) -> None:
        if user in self._allowed_users:
            self._real_doc.view(user)
        else:
            print(f"Access denied for {user}")


# Usage
doc = DocumentProxy()
doc.view("admin")  # Shows document
doc.view("hacker")  # Access denied

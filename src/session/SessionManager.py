class SessionManager:
    sessions = []

    def add_session(self, token, is_admin):
        self.sessions.append(
            {
                "token": token,
                "is_admin": is_admin
            }
        )

    def check_auth(self, token, is_admin):
        return self.sessions.__contains__(
            {
                "token": token,
                "is_admin": is_admin
            }
        )

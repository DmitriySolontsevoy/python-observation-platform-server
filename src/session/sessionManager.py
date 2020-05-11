from dto.session import Session


class SessionManager:

    __sessions = []

    def add_session(self, token, is_admin):
        self.__sessions.append(Session(token, is_admin))

    def remove_session(self, token):
        for session in self.__sessions:
            if session.token == token:
                self.__sessions.remove(session)

    def check_session(self, request, is_admin):
        header = request.headers.get("Authorization")

        for session in self.__sessions:
            if session.token == header:
                if session.is_admin == is_admin:
                    return True, True
                else:
                    return True, False

        if is_admin is True:
            return False, False
        else:
            return False

    def check_auth_regular_user(self, request):
        if self.check_session(request, False):
            return None, None
        else:
            return {"success": "false", "reason": "Unauthorized"}, 401

    def check_auth_admin(self, request):
        is_authorized, is_admin = self.check_session(request, True)

        if is_authorized:
            if is_admin:
                return None, None
            else:
                return {"success": "false", "reason": "Requires admin rights"}, 403
        else:
            return {"success": "false", "reason": "Unauthorized"}, 401

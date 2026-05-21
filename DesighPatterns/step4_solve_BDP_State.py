from enum import Enum


class UserRoles(Enum):
    READER = 1
    EDITOR = 2
    ADMIN = 3


from abc import ABC, abstractmethod
class State(ABC):
    @abstractmethod
    def publish(self):
        pass


class DraftState(State):
    def __init__(self, document):
        self._document = document

    def publish(self):
        self._document.state = ModerationState(self._document)


class ModerationState(State):
    def __init__(self, document):
        self._document = document

    def publish(self):
        if self._document.current_user_role == UserRoles.ADMIN:
            self._document.state = PublishState(self._document)


class PublishState(State):
    def __init__(self, document):
        self._document = document

    def publish(self):
        if self._document.current_user_role == UserRoles.ADMIN:
            pass


class Document:
    def __init__(self, curreent_user_role: UserRoles):
        self.state = DraftState(self)
        self.current_user_role = curreent_user_role

    def publish(self):
        self.state.publish()


doc = Document(UserRoles.EDITOR)
print(doc.state.__class__.__name__)
doc.publish()
print(doc.state.__class__.__name__)
doc.publish()
print(doc.state.__class__.__name__)

doc = Document(UserRoles.ADMIN)
print(doc.state.__class__.__name__)

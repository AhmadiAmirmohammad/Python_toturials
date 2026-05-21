# The state pattern allows an object to behave defferently depending on the state that it is in.
# the object have different behavioral dependign on current state that is in.

#ex1. when use wordpress and want to writing a blog post using the content managment system,
# the document or post can be have 3 state:
#     1. Draft
#     2. Moderation (under review by an admin)
#     3. Published

# There are three types of user roles:
# 1. Reader
# 2. Edittor
# 3. Admin (only admin can publish posts.)

from enum import Enum

class DocumentState(Enum):
    DRAFT = 1
    MODERATION = 2
    PUBLISHED = 3
class UserRoles (Enum):
    READER = 1
    EDITOR = 2
    ADMIN = 3

class Document:
    def __init__(self, state:DocumentState, curreent_user_role:UserRoles ):
        self.state = state
        self.current_user_role = curreent_user_role

    def publish (self):
        if self.state == DocumentState.DRAFT:
            self.state = DocumentState.MODERATION
        elif self.state == DocumentState.MODERATION and self.current_user_role == UserRoles.ADMIN:
            self.state = DocumentState.PUBLISHED
        elif self.state == DocumentState.PUBLISHED:
            # Don nothing
            pass

doc = Document(DocumentState.DRAFT, UserRoles.ADMIN)
print(f"initial state: {doc.state.name}")

doc.publish()
print(f"Initial state: {doc.state.name}")

doc.publish()
print(f"Initial state: {doc.state.name}")


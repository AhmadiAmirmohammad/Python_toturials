#Client → GUIFactory (abstract factory) → Concrete Factory → Products


# You're building a cross-platform application that must work on Windows and macOS.
# Each platform has different-looking Buttons and Checkboxes.

from abc import ABC, abstractmethod
# -----  Button -----
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self, action):
        pass


# -----  Checkbox -----
class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_check(self, checked):
        pass

# for windows
class WindowsButton(Button):
    def render(self):
        return "Rendering Windows-style button [ OK ]"

    def on_click(self, action):
        return f"Windows button clicked: executing {action}"


class WindowsCheckbox(Checkbox):
    def render(self):
        return "Rendering Windows-style checkbox [X] Selected"

    def on_check(self, checked):
        status = "checked" if checked else "unchecked"
        return f"Windows checkbox is now {status}"


#for mac
class MacButton(Button):
    def render(self):
        return "Rendering macOS-style button ● OK ●"

    def on_click(self, action):
        return f"Mac button clicked: executing {action}"

class MacCheckbox(Checkbox):
    def render(self):
        return "Rendering macOS-style checkbox ✓ Selected"

    def on_check(self, checked):
        status = "checked" if checked else "unchecked"
        return f"Mac checkbox is now {status}"


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def render_ui(self):
        print("\n--- Rendering UI ---")
        print(self.button.render())
        print(self.checkbox.render())

    def simulate_clicks(self):
        print("\n--- Simulating User Interaction ---")
        print(self.button.on_click("save_data"))
        print(self.checkbox.on_check(True))


def configure_application(os_type: str) -> Application:
    """config base OS system"""
    if os_type == "Windows":
        factory = WindowsFactory()
        print("🪟 Configuring for Windows...")
    elif os_type == "Mac":
        factory = MacFactory()
        print("🍎 Configuring for macOS...")
    else:
        raise ValueError(f"Unknown OS: {os_type}")

    app = Application(factory)
    app.create_ui()
    return app

# ========== Run on Windows ==========
windows_app = configure_application("Windows")
windows_app.render_ui()
windows_app.simulate_clicks()

from textual.screen import Screen
from textual.widgets import Button, Static
from textual.app import ComposeResult
from textual.containers import Center, Horizontal
from enums.enums import ConformationDialogTypes

# TODO: Create a new Conformation dialog that handles yes/no answers
# TODO: Styling and more information servers
#     yield Center(Static("Are you sure?"))
#     yield Center(Button("Yes", id=ConformationDialogTypes.Yes.name))
#     yield Center(Button("No", id=ConformationDialogTypes.No.name))

class ServerActionsDialog(Screen):
    CSS_PATH = "dialog.tcss"

    def __init__(self, container):
         super().__init__()
         self.container = container

    def compose(self) -> ComposeResult:
        yield Center(Static(f"Name {self.container.name}"))
        yield Center(Static(f"Status {self.container.status}"))
        yield Horizontal(
            Button("Start", id=ConformationDialogTypes.Start.name),
            Button("Stop", id=ConformationDialogTypes.Stop.name),
            Button("Delete", id=ConformationDialogTypes.Delete.name),
            Button("Restart", id=ConformationDialogTypes.Restart.name),
            Button("Pause", id=ConformationDialogTypes.Pause.name),
            Button("Back", id=ConformationDialogTypes.Back.name),
            classes='action-btn'
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case ConformationDialogTypes.Start.name:
                if self.container.status in ['created', 'exited']:
                    self.container.start()
                    self.notify(f"Server {self.container.name} is running")
                    self.dismiss()
                elif self.container.status in ['paused']:
                    self.container.unpause()
                    self.notify(f"Server {self.container.name} is running")
                    self.dismiss()
                else:
                    self.notify(f"Server {self.container.name} is already running")
            case ConformationDialogTypes.Stop.name:
                if self.container.status in ['running']:
                    self.container.stop()
                    self.notify(f"Server {self.container.name} is stopped")
                    self.dismiss()
                else:
                    self.notify(f"Server {self.container.name} is already stopped")
            case ConformationDialogTypes.Delete.name:
                # TODO: Auto ready the server for deletion.
                # TODO: Add extra confirmation here to stop the server if running, paused or restarting.
                if self.container.status in ['created', 'exited', 'dead']:
                    self.container.remove()
                    self.notify(f"Server {self.container.name} is deleted")
                    self.dismiss()
                else:
                    self.notify(f"Server {self.container.name} can't be deleted")
            case ConformationDialogTypes.Restart.name:
                if self.container.status in ['created', 'exited', 'paused', 'running']:
                    self.container.restart()
                    self.notify(f"Server {self.container.name} is restating")
                    self.dismiss()
                else:
                    self.notify(f"Server {self.container.name} can't be restarted")
            case ConformationDialogTypes.Pause.name:
                if self.container.status in ['running']:
                    self.container.pause()
                    self.notify(f"Server {self.container.name} is paused")
                    self.dismiss()
                else:
                    self.notify(f"Server {self.container.name} can't be paused")
            case ConformationDialogTypes.Back.name:
                self.dismiss()


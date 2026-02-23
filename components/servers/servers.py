from serverEngine.serverEngine import ServerEngine
from components.serverActionsDialog.serverActionsDialog import ServerActionsDialog

from textual.widgets import OptionList
from textual.widgets.option_list import Option
from textual.app import ComposeResult
from textual.screen import Screen

# TODO: Create a server basic version. 1

# TODO: Save server/container settings in db.
# TODO: backup server manager settings whole db to api.
# TODO: backup server in json to api.

class Servers(Screen):

    def compose(self) -> ComposeResult:
        self.serverEngine = ServerEngine()
        optionList = OptionList()
        self.containers = self.serverEngine.Get_Servers(True)

        for container in self.containers:
            optionList.call_after_refresh(optionList.add_option, Option(container.name, id=container.id))

        yield optionList
    
    async def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        self.containers = self.serverEngine.Get_Servers(True)
        containers = [container for container in self.containers if container.id == event.option.id]
        await self.app.push_screen(ServerActionsDialog(containers[0]))
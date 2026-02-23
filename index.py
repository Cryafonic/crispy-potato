from textual.app import App
from components.servers.servers import Servers

class ServerManagerApp(App):
        SCREENS = {
              "servers": Servers,
        }

        def on_mount(self) -> None:
              self.push_screen("servers")
            
if __name__ == "__main__":
    ServerManagerApp().run()
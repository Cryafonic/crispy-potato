import docker

class ServerEngine():

    def __init__(self):
        self.client = docker.from_env()

    def Get_Servers(self, viewAll) -> list[any]:
        return self.client.containers.list(all=viewAll)
import docker
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

client = docker.from_env()

container_list = client.containers.list(filters={'status':'running','ancestor':'python:alpine'})
for container in container_list:
    print('Terminating :',container)
    container.kill()

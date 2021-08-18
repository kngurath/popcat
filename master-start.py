import docker
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

client = docker.from_env()

container_list =  []


test_num = 100
for i in range(test_num):

    container = client.containers.run('a23956491z/popcat',
                                          detach=True,
                                          network='br1',
                                          volumes={dir_path : {'bind': '/data', 'mode': 'rw'}},
                                          working_dir='/data',
                                          command='main.py',
                                          stdout=True,
                                          remove=True
    )

    container_list.append(container)
    print(container)

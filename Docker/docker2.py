import docker

client = docker.DockerClient(base_url='unix://var/run/docker.sock')

client.images.list()  # docker images  显示image的信息列表
print(client.images.list() )
print('_____________________________')

client.containers.list()  # docker ps
print(client.containers.list() )
print('_____________________________')

client.containers.list(all=True)  # docker ps -a
print(client.containers.list(all=True))
print('_____________________________')



container = client.containers.run('hello-world', detach=True)
# container = client.containers.get( container_id)  # 获取daodocker容器

container.start()  # docker start container_id   开启容器
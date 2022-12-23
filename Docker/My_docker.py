import docker
from docker import DockerClient

# print(docker.api())
# docker.APIClient()
# docker.client()
# docker.DockerClient() #其实也是docker.client()的一个子集
# docker.from_env() # 其实就是docker.client()的一个子集

'''docker相关的方法使用'''
# 使用DockerClient对象，会有以下方法：
# C.api
# C.containers
# C.events
# C.from_env
# C.images
# C.info
# C.login
# C.networks
# C.nodes
# C.ping
# C.services
# C.swarm
# C.version
# C.volumes

# 输出docker的相关信息，相当于docker info
# C.info()


# C = docker.DockerClient(base_url='unix://var/run/docker.sock', version='auto', timeout=10)
# C = docker.DockerClient(base_url='unix://var/run/docker.sock', version='1.41', timeout=5)
client = docker.APIClient(base_url='unix://var/run/docker.sock', version='1.41', timeout=5)

client.version()
print(client.version())
print('_____________________________')
client.info()
print(client.info())
print('_____________________________')
# client.containers.run('<image>', '<command>')         运行容器

# client.containers.run('alpine', 'echo hello world')


C = docker.DockerClient(base_url='unix://var/run/docker.sock', version='auto', timeout=10)
print(C.info())
print('_____________________________')

# 列出当前存活的容器：
print(C.images.list())
print('_____________________________')

# 列出指定容器：
# C.containers.get('Image: ')
# print('_____________________________')

# 创建client
# 从environment里面拿
client = docker.from_env()
client.version()
print(client.version())
print('_____________________________')
client.info()
print(client.info())

C.containers.run('alpine', 'echo hello world')


print('_____________________________')
# 如果detach是True，会运行container并立即返回Container对象，类似docker run -d.
container = client.containers.run('hello-world', detach=True)

# 得到byte类型log
container.logs()
# 得到可遍历log
logs = container.logs(stream=True)
for line in logs:
    print(line)
# 查看返回转态码
exit_code = container.wait()
print(exit_code)


# print(container.swapcase())
# # 如果detach是True，会运行container并立即返回Container对象，类似docker run -d.
# container = C.containers.run('<image>', detach=True)
# container.logs()

# print(C.version())

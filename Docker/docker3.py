# python 运行 docker 容器实例

# Docker selenium 自动化 - 使用python操作docker，python运行、启用、停用和查询容器实例演示


import docker

client = docker.from_env()


def create_docker1(docker_name):
    '''
     作用：运行一个(selenium/hub)容器实例，可选参数detach=True为后台运行
     参数：docker_name为容器的名称
     返回：容器对象
    '''
    client.containers.run("selenium/hub", name=docker_name, ports={"4444/tcp": None}, detach=True, shm_size="500M")
    container = client.containers.get(docker_name)

    return container


def create_docker2(docker_name):
    '''
     作用：运行一个(selenium/node-chrome)容器实例，可选参数detach=True为后台运行
     参数：docker_name为容器的名称
     返回：容器对象
    '''
    client.containers.run("selenium/node-chrome", name=docker_name, detach=True, links={"hub": "hub"})
    container = client.containers.get(docker_name)

    return container


# python 查询、展示容器实例列表
def list_docker():
    '''
     作用：展示容器相关列表
     参数：无
     返回：无
    '''
    # 显示所有的容器对象
    results = client.containers.list()
    k = 0
    for i in results:
        k = k + 1;
        print("序号：" + str(k))
        print("容器短id:" + i.short_id)
        print("容器名:" + i.name)
        print("容器状态:" + i.status)
        print("容器端口:" + str(i.ports))
        print("")


# python 启用、停用容器实例
def stop_docker(container_name):
    '''
     作用：停用容器
     参数：需要停用的容器名称
     返回：无
    '''
    container = client.containers.get(container_name)
    container.stop()
    print("容器已停用")


def start_docker(container_name):
    '''
     作用：启用容器
     参数：需要启用的容器名称
     返回：无
    '''
    container = client.containers.get(container_name)
    container.start()
    print("容器已启用")


container = create_docker1("hub")
container = create_docker2("elastic_tharp")

start_docker("hub")
start_docker("elastic_tharp")

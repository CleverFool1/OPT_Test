
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

start_docker("hub")
start_docker("elastic_tharp")
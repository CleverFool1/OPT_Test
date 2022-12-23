

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
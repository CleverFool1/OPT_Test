# -*- coding: UTF8 -*-
# 2021.12.13
# 小蓝枣
# docker selenium 自动化
import selenium
from selenium import webdriver
from time import sleep

help(selenium)

print('进程正确1')

# driver = webdriver.Remote(
#     command_executor='http://127.0.0.1:32791/wd/hub',
#     # command_executor='http://localhost:32791/wd/hub',
#
#     # command_executor='http://127.0.0.1:32791/wd/hub',
#     # desired_capabilities={'browserName': 'chrome'},
#     options=webdriver.ChromeOptions()
# )

driver = webdriver.Remote(
    command_executor='http://localhost:32791/wd/hub',
    options=webdriver.ChromeOptions()
)

size = driver.get_window_size()  # 获取手机屏幕大小,分辨率
print(size)



print('进程正确2')

try:
    # 登录中国气象网查看北京天气
    driver.get('http://www.weather.com.cn/weather1d/101010100.shtml')
    sleep(3)
    # 读取天气信息
    print('进程正确')
    bj_temperature = driver.find_element_by_xpath('//*[@class="sk mySkyNull"]//*[@class="tem"]/*').text
    bj_wind_direction = driver.find_element_by_xpath('//*[@class="sk mySkyNull"]//*[@class="zs w"]/span').text
    bj_wind_class = driver.find_element_by_xpath('//*[@class="sk mySkyNull"]//*[@class="zs w"]/em').text
    bj_air_quality = driver.find_element_by_xpath('//*[@class="sk mySkyNull"]//*[@class="zs pol"]//a').text

    bj_weather = '''
    城市：北京
    当前温度：%s
    风向：%s
    风力：%s
    空气质量：%s
    ''' % (bj_temperature, bj_wind_direction, bj_wind_class, bj_air_quality)

    # 打印抓取的天气信息
    print(bj_weather)

    # 保存截图
    driver.get_screenshot_as_file("docker_selenium_run_001.png")

# 保证出错后进程正常释放
finally:
    driver.quit()
    print('进程错误')

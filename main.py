from source import Settings
from source import XHS


def example():
    """代码示例"""
    # 测试链接
    error_demo = "https://www.xiaohongshu.com/explore/"
    image_demo = "https://www.xiaohongshu.com/explore/64d1b406000000000103ee8d"
    video_demo = "https://www.xiaohongshu.com/explore/64c05652000000000c0378e7"
    # 实例对象
    path = "./"  # 作品下载储存根路径，默认值：当前路径
    folder = "Download"  # 作品下载文件夹名称（自动创建），默认值：Download
    proxies = None  # 代理
    timeout = 5  # 网络请求超时限制，默认值：10
    chunk = 1024 * 1024  # 下载文件时，每次从服务器获取的数据块大小，单位字节
    xhs = XHS(
        path=path,
        folder=folder,
        proxies=proxies,
        timeout=timeout,
        chunk=chunk, )  # 使用自定义参数
    # xhs = XHS()  # 使用默认参数
    # 无需区分图文和视频作品
    # 返回作品详细数据，包括下载地址
    download = True  # 启用自动下载作品文件
    print(xhs.extract(error_demo))  # 获取数据失败时返回空字典
    print(xhs.extract(image_demo, download=download))
    print(xhs.extract(video_demo, download=download))


def main():
    xhs = XHS(**Settings().run())  # 配置文件生效
    while True:
        if url := input("请输入小红书作品链接："):
            xhs.extract(url, download=True)
        else:
            break


if __name__ == '__main__':
    # example()
    main()

from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client
from django.conf import settings
class FDFSStorage(Storage):
    '''fastdfs文件存储类'''

    def __init__(self, client_conf=None, basic_url=None):
        '''初始化'''
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf

        if basic_url is None:
            basic_url = settings.FDFS_URL
        self.basic_url = basic_url


    def _open(self, name, model='rb'):
        '''打开文件时使用'''
        pass

    def _save(self, name, content):
        '''保存文件时使用'''
        # name:你选择的上传的文件的名字
        # content:file类对象，包含你上传文件内容的File对象

        # 创建一个Fdfs_client对象
        client = Fdfs_client(self.client_conf)
        """
        {'Group name': 'group1', 
        'Remote file_id': 'group1\\M00/00/00/ejM0bF3j0EWAEuAHAAAdOajwgxQ0638.md', 
        'Status': 'Upload successed.', 
        'Local file name': 'python_github库.md', 
        'Uploaded size': '7.00KB', 
        'Storage IP': '122.51.52.108\x00l'}
        """
        # 上传文件到fast_dfs系统
        res = client.upload_by_buffer(content.read())

        if res.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传文件到fast_dfs失败！')

        # 获取返回的文件ID
        filename = res.get('Remote file_id')
        return filename

    def exists(self, name):
        '''django判断文件名是否可用'''
        return False

    def url(self, name):
        '''django会传递这个name参数，传递的就是你保存的url'''
        return self.basic_url + name





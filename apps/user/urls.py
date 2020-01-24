from django.conf.urls import url
from user.views import RegisterView, LoginView, ActiveView, UserInfoView, UserOrderView, AddressView, LogutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^register$', RegisterView.as_view(), name='register'),    # 注册页面显示与注册处理
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),  # 用户激活
    url(r'^login$',  LoginView.as_view(), name='login'),            # 用户登录
    # url(r'^$', login_required(UserInfoView.as_view()), name='user'),    # 用户中心信息页
    # url(r'^order$', login_required(UserOrderView.as_view()), name='order'), # 用户中心订单页面
    # url(r'^address$', login_required(AddressView.as_view()), name='address')
    url(r'^$', UserInfoView.as_view(), name='user'),
    url(r'^order/(?P<page>\d+)$', UserOrderView.as_view(), name='order'),
    url(r'^address$', AddressView.as_view(), name='address'),
    url(r'^logout$', LogutView.as_view(), name='logout'),   # 注销登录
]

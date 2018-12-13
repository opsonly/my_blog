# my_blog
![](https://img.shields.io/badge/python-3.7-brightgreen.svg) ![](https://img.shields.io/badge/django-2.1-ff69b4.svg) ![](https://img.shields.io/badge/Powered%20by-%40%20opsonly-blue.svg)
 > 基于```python3.7```和```django2.1```的多人博客系统
---

## 简介
> 该博客前段框架使用了Bootstrap 4，在其基础上添加了一些自己需要用的css样式，后端使用django2.1。
> 由于自己也在摸索中，会继续完善此项目的功能。觉得有用的欢迎给个star！~

## 主要功能:
---
- 用户注册，登录,删除，以及使用第三方库password_reset来重置用户密码
- 文章的发布，修改以及删除，支持markdown以及代码高亮
- 留言板系统
- 支持文章的多人互动评论
- 文章标签功能，通过标签搜索相关文章

## 环境
```python
python3.7
```

## 下载
```
git clone https://github.com/opsonly/my_blog.git
```

## 安装
```python
pip install -r requirements.txt  #安装所有依赖
python manage.py makemigrations #数据库修改
python mange.py migrate
```
## 使用
```python
python manage.py createsuperuser # 初始化用户名密码
python manage.py runserver #启动Django服务

http://ip:port/admin #访问后台管理员后台

```
> 浏览器中打开http://127.0.0.1:8000/ 即可访问
---
## 部分演示
- 用户注册及登录页
![](https://note.youdao.com/yws/public/resource/93da14c62d82be64f4b77e58d4d0db42/xmlnote/482E6000B7894FBE9D5885435843BB7B/6697)

- 所有文章列表及文章所属的标签
![](https://note.youdao.com/yws/public/resource/93da14c62d82be64f4b77e58d4d0db42/xmlnote/60F996916BF54BD3AC09162A83C85E21/6699)

- 根据标签搜索
![](https://note.youdao.com/yws/public/resource/93da14c62d82be64f4b77e58d4d0db42/xmlnote/52B31F7961594111B0D8B25DF43AA578/6711)

- 文章详情页及其评论
![](https://note.youdao.com/yws/public/resource/93da14c62d82be64f4b77e58d4d0db42/xmlnote/5743BF64688F4178ABF965148FE949B4/6703)

- 我的博客页面
![](https://note.youdao.com/yws/public/resource/93da14c62d82be64f4b77e58d4d0db42/xmlnote/48079CE8505F4B908817ADCF9C191BBA/6707)


- 删除文章选项
![](https://note.youdao.com/yws/public/resource/93da14c62d82be64f4b77e58d4d0db42/xmlnote/1B4C14DADB344DDBBDACFE6D1B658D60/6709)

- 网站留言板
![](https://note.youdao.com/yws/public/resource/93da14c62d82be64f4b77e58d4d0db42/xmlnote/964E4D1746D64C77A44A7BEBE619F7A3/6701)

---

## 问题相关
联系邮箱```opsonly.com@gmail.com```
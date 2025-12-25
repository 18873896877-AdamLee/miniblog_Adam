from app import create_app, db
from app.models import User, Menu, ArticleTypeSetting, ArticleType, Source, BlogInfo, Plugin, BlogView

app = create_app()

with app.app_context():
    # 创建数据库表
    db.create_all()
    
    # 检查是否已经初始化数据
    if User.query.count() == 0:
        # 插入管理员账号
        User.insert_admin(email='blog_mini@163.com', username='blog_mini', password='blog_mini')
        print("已插入管理员账号")
    
    if Menu.query.count() == 0:
        # 插入菜单
        Menu.insert_menus()
        print("已插入菜单")
    
    if ArticleTypeSetting.query.count() == 0:
        # 插入分类设置
        ArticleTypeSetting.insert_default_settings()
        print("已插入分类设置")
    
    if ArticleType.query.count() == 0:
        # 插入系统默认分类
        ArticleType.insert_system_articleType()
        print("已插入系统默认分类")
    
    if Source.query.count() == 0:
        # 插入文章来源
        Source.insert_sources()
        print("已插入文章来源")
    
    if BlogInfo.query.count() == 0:
        # 插入博客信息
        BlogInfo.insert_blog_info()
        print("已插入博客信息")
    
    if Plugin.query.count() == 0:
        # 插入系统插件
        Plugin.insert_system_plugin()
        print("已插入系统插件")
    
    if BlogView.query.count() == 0:
        # 插入博客访问统计
        BlogView.insert_view()
        print("已插入博客访问统计")

if __name__ == '__main__':
    app.run(debug=True, port=5001)

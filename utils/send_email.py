import zmail
from config.conf import cm 

def send_report():
    """发送报告"""
    with open(cm.REPORT_FILE,encoding='utf-8') as f:
        content_html = f.read()

    try:
        mail = {
            'from': '1361794254@qq.com',
            'subject':'最新的测试报告邮件',
            'content_html': content_html,
            'attachment': [cm.REPORT_FILE]
        }
        server = zmail.server(*cm.EMAIL_INFO.values())
        server.send_mail(cm.ADDRESS,mail)
        print("测试邮件发送成功！")
    except Exception as e:
        print("Error:无法发送邮件，{}".format(e))


if __name__ == "__main__":
    """请现在config/conf.py文件中设置QQ邮箱的账号和密码"""
    send_report()
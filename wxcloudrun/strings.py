
商务合作 = """
感谢您对《原来是这样》的支持，请将以下信息发送至电子邮箱
Dscience2014@126.com

邮件标题为：【商务合作】
邮件内容包括以下信息：
昵称/姓名：
微信号：
QQ号：
商务合作的具体内容形式：

感谢您的参与，邮件发送后，我们会尽快联系您。
"""

撰稿人 = """
感谢您对《原来是这样》的支持，请将以下信息发送至电子邮箱
Dscience2014@126.com

邮件标题为：【撰稿人】+文案选题（拟）

邮件内容包括以下信息：
1、昵称/姓名：
2、微信号：
3、最高学历及专业：
4、工作领域及经历：
5、（简述文案内容及大致提纲）

感谢您的参与，邮件发送后，我们会尽快和您取得联系！
"""

默认回复 = """
在回复中标上【留言】，可以提高被看到的几率~

如果您想成为【撰稿人】或寻求【商业合作】，回复相应关键词试试？！

如果你正在新春闯关，请回复"提示"
"""

提示 = """
这是操作提示
"""

def simple_reply(content):
    if(content == "商务合作"):  
        return 商务合作
    if(content == "撰稿人"):  
        return 撰稿人
    if(content == "提示"):  
        return 提示
    
    return 默认回复
    

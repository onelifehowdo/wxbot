import Config
import Message
import init
import re


def cleanMsg(m_text):
    m_text = re.sub(r'.+\n.+\n-{6}\n', "", m_text)  # 去除引用
    m_text = re.sub(r'@\S+\b', "", m_text)  # 去除@
    m_text = re.sub(r'，|,|。|\.|、|!|！|？|\?|;|；|=|\s|\'\"\‘\“', "", m_text)  # 去除符号
    m_text = re.sub(r'\d+', "", m_text)#去除数字
    m_text = re.sub(r'\[[^\[\]]{1,4}\]', "", m_text)#去除表情
    return m_text

def filte(msg):
    # print(msg.speaker,msg.text)
    msgType = None
    sqlMsg = msg
    # r = Config.test_isHZstaff(msg.speaker)
    r = Config.isAllStaffById(msg.speakid)
    if r:  # 公司员工
        msgType = "STAFF"
        sqlMsg = Message.sqlMessage(msg, "应用研发部")
        sqlMsg.setSpeaker(Config.getAllStaffNameById(msg.speakid))
        sqlMsg.setType("message")
        sqlMsg.setStatus(0)
        sqlMsg.setPerson(None)
        Model, engineerName = init.getbean(str(msg.text))
        r = Config.isStaffById(msg.speakid)
        if r:  # 应用研发部
            if len(msg.atList) > 0:  # @回复
                if ("$_$" in msg.text):
                    sqlMsg.setType("problem")
                    sqlMsg.setEngineer(sqlMsg.speaker)  # 给自己
                    # Model, engineerName = init.getbean(str(msg.text))
                    sqlMsg.setModle(Model)
                    for at in msg.atList:
                        if Config.isStaffByName(at):  # 给别人
                            sqlMsg.setEngineer(at)
                            continue
                else:  # 未检测命令
                    if len(msg.atList) > 0:
                        for at in msg.atList:  # 检测到@部门的人
                            if Config.isStaffByName(at):
                                sqlMsg.setType("message")
                                sqlMsg.speakerType = "应用研发部"
                                sqlMsg.setModle(Model)
                                sqlMsg.setEngineer(at)
                                msgType = "TRANSFER"
            else:#无@回复
                if "$_$" in msg.text:
                    sqlMsg.setType("problem")
                    sqlMsg.setEngineer(sqlMsg.speaker)  # 给自己
                    # Model, engineerName = init.getbean(str(msg.text))
                    sqlMsg.setModle(Model)
        else:  # 销售
            if len(msg.atList) > 0:  # @回复
                for at in msg.atList:
                    if Config.isStaffByName(at):  # @应用研发部
                        sqlMsg.setType("message")
                        sqlMsg.speakerType = "非应用研发部"
                        sqlMsg.setModle(Model)
                        sqlMsg.setEngineer(at)
                        msgType = "HAVE_KEY"
                        break
            else:  # 响应消息
                pass
    # 客户
    else:
        if len(msg.atList) > 0:  # 分析@
            for at in msg.atList:
                if Config.isAllStaffById(at):
                    m_text = str(msg.text)
                    m_text = cleanMsg(m_text)
                    if not Config.isBoring(m_text):  # 有意义
                        sqlMsg = Message.sqlMessage(msg, "客户")
                        Model, engineerName = init.getbean(msg.text)
                        if not Model == "another":
                            # 识别到关键字的消息
                            sqlMsg.setStatus(0)
                            sqlMsg.setType("message")
                            sqlMsg.setModle(Model)
                            sqlMsg.setEngineer(engineerName)
                            msgType = "HAVE_KEY"
                        else:
                            # 未识别到关键字的消息
                            sqlMsg.setStatus(0)
                            sqlMsg.setType("message")
                            sqlMsg.setModle("another")
                            msgType = "NO_KEY"
                    break
            else:
                return None, sqlMsg  # 不处理
        else:  # 分析消息
            m_text = str(msg.text)
            m_text = cleanMsg(m_text)
            if not Config.isBoring(m_text):  # 有意义
                sqlMsg = Message.sqlMessage(msg, "客户")
                Model, engineerName = init.getbean(msg.text)
                if not Model == "another":
                    # 识别到关键字的消息
                    sqlMsg.setStatus(0)
                    sqlMsg.setType("message")
                    sqlMsg.setModle(Model)
                    sqlMsg.setEngineer(engineerName)
                    msgType = "HAVE_KEY"
                else:
                    # 未识别到关键字的消息
                    sqlMsg.setStatus(0)
                    sqlMsg.setType("message")
                    sqlMsg.setModle("another")
                    msgType = "NO_KEY"
    return msgType, sqlMsg

import time
from subprocess import call
from xml.dom.minidom import parseString
import emailsender
import cx_Oracle

# conn = cx_Oracle.connect("kingdee/kingdee@220.178.253.190:9527/easdb")
conn = cx_Oracle.connect("kingdee/kingdee@192.168.8.201:1521/easdb")
cursor = conn.cursor()
flag = True

while True:

    # 获取58 59 60版本的发货通知单
    # result = cursor.execute('select FPROCINSTID,FPROCDEFVER, from T_WFR_ProcInst where FPROCDEFNAME_L2 like \'ZH_发货通知单新带信控_在用\' and FPROCDEFVER >= 58 and FSTATE =\'open.not_running.suspended\'')

    result = cursor.execute("select FDATAVALUE from T_WFR_ProcInst a left join T_WFR_ProcInstData on a.FPROCINSTID=T_WFR_ProcInstData.FPROCINSTID where a.FPROCDEFNAME_L2 LIKE 'ZH_发货通知单新带信控_在用' AND a.FPROCDEFVER in（'58'，'59'，'60'） AND a.FSTATE='open.not_running.suspended'")
    all_data = cursor.fetchall()

    l=len(all_data)
    for data in all_data:
        for item in data:
            # print(item)
            # 字符串转换成xml.dom.minidom.Document对象 xml_data是xml格式字符串
            DOMTree = parseString(item.read())

            collection = DOMTree.documentElement
            # 集合你要的标签
            VariationChilds = collection.getElementsByTagName("DataField")
            # 进行遍历取值
            for VariationChild in VariationChilds:
                if VariationChild.getAttribute("Name") == 'FHid':
                    value=VariationChild.getElementsByTagName("Value")[0];
                    print(value.childNodes[0].data)
    # 显示记录数
    print(l)

    if l>39:
        cmdbeep = 'beep'
        cmd = 'display notification \"' + \
              "又来一单，赶紧更新吧！！" + '\" with title \"来活啦【'+l.__str__()+'】\"'
        # 消息通知
        call(["osascript", "-e", cmd])
        # 逼逼赖赖
        call(["osascript", "-e", cmdbeep])
        call(["osascript", "-e", cmdbeep])

        if flag:
            emailsender.send_email('来活啦！！！','来活啦！！！')
            flag=not flag


    time.sleep(5);
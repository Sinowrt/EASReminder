import time
import datetime
from xml.dom.minidom import parseString
import emailsender
import cx_Oracle
import csv
import update

# 初始化两个已修改与未修改list
modifiedlist=[]
listlen=0

record = csv.reader(open('222.csv','r'))
for i in record:
    modifiedlist.append(i[0])

listlen=len(modifiedlist)

conn = cx_Oracle.connect("kingdee/kingdee@220.178.253.190:9527/easdb")
# conn = cx_Oracle.connect("kingdee/kingdee@192.168.8.201:1521/easdb")
cursor = conn.cursor()
print('数据库连接成功！')
while True:

    # 获取58 59 60版本的发货通知单
    # result = cursor.execute('select FPROCINSTID,FPROCDEFVER, from T_WFR_ProcInst where FPROCDEFNAME_L2 like \'ZH_发货通知单新带信控_在用\' and FPROCDEFVER >= 58 and FSTATE =\'open.not_running.suspended\'')
    print('查询开始')
    result = cursor.execute("select FDATAVALUE from T_WFR_ProcInst a left join T_WFR_ProcInstData on a.FPROCINSTID=T_WFR_ProcInstData.FPROCINSTID where a.FPROCDEFNAME_L2 LIKE 'ZH_发货通知单新带信控_在用' AND a.FPROCDEFVER in（'58'，'59'，'60'） AND a.FSTATE='open.not_running.suspended'")
    print('查询结束')
    all_data = cursor.fetchall()
    unmodifiedlist = []
    if not len(all_data) == len(modifiedlist):
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
                        value=VariationChild.getElementsByTagName("Value")[0].childNodes[0].data;
                        if value not in modifiedlist:
                            unmodifiedlist.append(value)
                        break

        if len(unmodifiedlist)>0:
            # 显示新增的记录
            print(unmodifiedlist)
            changed=[]
            for item in unmodifiedlist:
                rowcount=update.update_cficket(conn,item)
                print(str(rowcount))
                if rowcount > 0:
                    changed.append(item)
                    modifiedlist.append(item)

            content=''
            for item in changed:
                content=content+str(item)+'\n'
            emailsender.send_email('本次修改列表',content)

        if not len(modifiedlist) == listlen:
            listlen = len(modifiedlist)

            f = open('222.csv','w')
            writer = csv.writer(f)
            for i in modifiedlist:
                writer.writerow([i])
            f.close()

    print(str(datetime.datetime.now())+'\t脚本正常运行中...'+'\t 已挂起【'+str(len(modifiedlist))+'】')
    time.sleep(5)
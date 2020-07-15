import cx_Oracle

# conn = cx_Oracle.connect("kingdee/kingdee@220.178.253.190:9527/easdb")
# conn = cx_Oracle.connect("kingdee/kingdee@192.168.8.201:1521/easdb")
fhid='dU1AoE77R8CkM7NslNVIm5yp0I8='
def update_cficket(conn,fhid):
    cursor = conn.cursor()
    cursor.execute("UPDATE T_IM_SaleIssuebill SET cfticket = 1 WHERE fid IN (SELECT FDestObjectID FROM T_BOT_Relation WHERE fdestentityid='CC3E933B' AND fsrcentityid   ='9CA9D08F' AND FsrcObjectID='"+fhid+"' UNION SELECT FDESTOBJECTID FROM T_BOT_Relation b WHERE fdestentityid='CC3E933B' AND fsrcentityid='CC3E933B' AND FsrcObjectID  IN (SELECT FDESTOBJECTID FROM T_BOT_Relation a WHERE fdestentityid='CC3E933B' AND fsrcentityid   ='9CA9D08F' AND FsrcObjectID='"+fhid+"'))")
    conn.commit()
    return cursor.rowcount

# update_cficket(conn,fhid)
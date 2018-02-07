#--encoding:utf-8--
import MySQLdb as mysql

print "请选择操作："
print "1--修改Master节点密码"
print "2--切换Master节点IP"
print "3--获取Master节点列表"


oprate = raw_input('> ')

conn = mysql.connect("172.207.22.14","root","123456","xenproxy")
cursor = conn.cursor()

try:
    
    if oprate == "1":
        host_ip = raw_input('请输入要修改的节点IP：')
        # 根据ip查询节点是否存在
        count = cursor.execute('select ip from host_info_tab where ip = "%s"' %host_ip)
        # 若不存在，进行错误提示，并退出
        if count == 0:
            print "该节点不存在！！！"
    
        # 若存在，则根据输入的密码进行更新
        elif count == 1:
            username = raw_input("请输入新的用户名：")
            password = raw_input('请输入新的密码：')
            cursor.execute('UPDATE host_info_tab SET username = "%s", password = "%s" WHERE ip = "%s"' %(username,password,host_ip))
            conn.commit()
            print "节点信息更新成功！"
    elif oprate == "2":
        src_master = raw_input("请输入原Master节点IP：")
        # 到cluster_info_tab中查询是否存在
        count = cursor.execute('select masterHost from cluster_info_tab where masterHost = "%s"' %src_master)
        # 若不存在，进行错误提示，并退出
        if count == 0:
            print "该Master节点不存在！！！"
        elif count == 1:
            new_master = raw_input("请输入新Master节点IP：")
            # 到host_info_tab中查询是否存在
            count = cursor.execute('select ip from host_info_tab where ip = "%s"' %new_master)
            # 若不存在，进行错误提示，并退出
            if count == 0:
                print "该节点不存在！！！"
            else:
                cursor.execute('UPDATE cluster_info_tab SET masterHost = "%s" WHERE masterHost = "%s"' %(new_master, src_master))
                conn.commit()
                print "Master节点信息更新成功！"
    elif oprate == "3":
        cursor.execute('select masterHost,clusterId from cluster_info_tab')
        results = cursor.fetchall()
        for row in results:
            print row[0],"---",row[1]
    else:
        print "输入有误!"
except:
    import traceback
    traceback.print_exc()
    # 发生错误时会滚
    conn.rollback()
finally:
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    conn.close()

import mysql.connector as mc
def count_table(h,u,pw,db,port):
  try:
      connection = mc.connect(host=h,user=u,password=pw,database=db, port=port)
      mouse = connection.cursor()
      mouse.execute("show tables")
      tabel = mouse.fetchall()
      tot_tab = len(tabel)
      print(f'Table Count:{tot_tab}')
      mouse.close()
      connection.close()

  except mc.Error as err:
        print(f"Error: {err}")

count_table(
    h="xxxxxxxx",
    u="jasonm",
    pw="xxxxxxxxxxx",
    db="xxxxxxxx",
    port=5501
)
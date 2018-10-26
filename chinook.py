import sqlite3

def webpage(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/html; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    #connect to db
    conn = sqlite3.connect("chinook.db")
    conn.text_factory = str
    cur = conn.cursor()

    cur.execute("SELECT * FROM albums")
    rows = cur.fetchall()
 
    content=('''<!DOCTYPE html>
<html>
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    margin: auto;
    table-layout:auto;
}
td, th {
    border: 1px solid #ccc;
    text-align: left;
    padding: 8px;
}
tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
</head>
<body>
<table>
<caption><h2>Music Albums</h2></caption>
  <tr>
    <th>ID</th>
    <th>Title</th>
    <th>Artist ID</th>
  </tr>''')
    
    for row in rows:
        rowout='''<tr><td> {} </td><td> {} </td><td> {} </td></tr>'''.format(row[0],row[1],row[2])
        content = content + rowout
    
    htmlclose=('''</table>
</body>
</html>''')
    
    content = content + htmlclose
    return[bytes(content, 'UTF-8')]

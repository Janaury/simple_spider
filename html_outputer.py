#coding:utf8
class HtmlOutputer:
    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
  
    def output_html(self):
        fout = open('output.html','w')
        fout.write("<head><meta charset='utf-8''></head>")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr><td>%s</td></tr>" % data['url'].encode('utf-8'))
            fout.write("<tr'><td>%s</td></tr>" % data['title'].encode('utf-8'))
            fout.write("<tr><td>%s</td></tr>" % data['summary'].encode('utf-8'))
            fout.write("<tr><td>-------------------------------------------</td></tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
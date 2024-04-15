import subprocess
import os

def genPDF(template_html='template.html',template_css='template.css',output="out.pdf",variables=dict()):
    html_template = open(template_html)
    html_content = html_template.read().format(**variables)
    open('/tmp/tmp.html','w').write(html_content)
    subprocess.Popen(["weasyprint","/tmp/tmp.html",output,"-s",template_css]).wait()
    os.remove("/tmp/tmp.html")
    
genPDF(variables={'nombre':'David','dependencia':'asjdjsdgsdgd'})
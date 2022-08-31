from urllib import response

from flask import Flask, request
from flask_cors import CORS

from scripts.cms_discovery import build_with
from scripts.host_discovery import port_scan
from scripts.banner_grabing import ashok
from scripts.firewall_detection import run_wafw00f

app = Flask(__name__)
CORS(app)

@app.route('/post', methods=['POST'])
def attack():
   report = {}
   if request.method == 'POST':
      data = request.get_json()
      print(data)
      report['nmap_scan'] = "None"

      report['ashok_scan'] = "None"
      report['waf00f_scan'] = "None"

      if data["useNmap"] == True:
         print("Running Scan...")
         report['nmap_scan'] =  port_scan(data['targetUrl'])

      if data["useAshok"] == True:
         print("Running Ashok...")
         report['ashok_scan'] = ashok(data['targetUrl'])

      if data["useWappalyzer"] == True:
         print("Running Wappalyzer...")
         report['wappalyzer_scan'] = build_with(data['targetUrl'])

      if data["useWaf00f"] == True:
         print("Running Firewall scan...")
         report['waf00f_scan'] = run_wafw00f(data['targetUrl'])

   print(report)
   return report

if __name__ == '__main__':
   app.run()
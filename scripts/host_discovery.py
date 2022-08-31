import json

import nmap
import socket


def port_scan(url):
    third_level_domain = url.split('/')[2].split('.')[0]
    first_level_domain = url.split('/')[2].split('.')[1]
    top_level_domain = url.split('/')[2].split('.')[2]

    url =third_level_domain + '.' + first_level_domain + '.' + top_level_domain

    host = socket.gethostbyname(url)
    nm = nmap.PortScanner()
    try:
        scan = nm.scan(host,  arguments='-O')

        report_list = {}
        report_list['ip'] = nm.all_hosts()
        report_list['os_name'] = nm[host]['osmatch'][0]['name']
        report_list['os_accuracy'] = nm[host]['osmatch'][0]['accuracy']
        port_list = []
        ports = nm[host]['tcp'].keys()
        for port in ports:
            report = {}
            state = nm[host]['tcp'][port]['state']
            service = nm[host]['tcp'][port]['name']
            product = nm[host]['tcp'][port]['product']
            report['port'] = port
            report['state'] = state
            report['service'] = service
            report['product'] = product
            if state == 'open':
                port_list.append(report)

        report_list['ports'] = port_list
        return json.dumps(report_list)
    except Exception as e:
        print(e)

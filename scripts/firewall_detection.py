from modules.wafw00f.main import WAFW00F, buildResultRecord


def run_wafw00f(url):
    try:
        results = {}
        firewall_list = []

        attacker = WAFW00F(url)
        waf = attacker.identwaf(findall=True)
        if len(waf) > 0:
            for i in waf:
                firewall_list.append(buildResultRecord(url, i))
            results['firewalls'] = firewall_list
        if len(waf) == 0:
            firewall_list.append('None')
            results['firewalls'] = firewall_list
        results['number_of_requests'] = attacker.requestnumber
    except:
        results['firewalls'] = "Something went wrong"
        results['number_of_requests'] = "Something went wrong"
    return results

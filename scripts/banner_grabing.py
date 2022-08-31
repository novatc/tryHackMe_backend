from modules.Ashok.core.bannergrab import banner
from modules.Ashok.core.subdomains import sub
from modules.Ashok.core.geoip import geo

from modules.Ashok.plugins.dnslookup import dnslookup
from modules.Ashok.plugins.httpheaders import httpheader



def ashok(url):
    ashok_result = {}
    protocol = url.split('/')[0]
    third_level_domain = url.split('/')[2].split('.')[0]
    first_level_domain = url.split('/')[2].split('.')[1]
    top_level_domain = url.split('/')[2].split('.')[2]

    url = protocol + '//' + third_level_domain + '.' + first_level_domain + '.' + top_level_domain

    domain = first_level_domain + '.' + top_level_domain

    # Extract Http Headers from single url
    result = httpheader(url)
    ashok_result['headers'] = result

    # Dns Lookup of single target domain
    result = dnslookup(domain)
    ashok_result['dns'] = result

    ip = ashok_result['dns']['A']

    # Subdomain Lookup of single target domain
    result = sub(domain)
    ashok_result['subdomain'] = result

    # Banner grabbing of target ip address
    result = banner(ip)
    ashok_result['banner'] = result

    # GeoIP lookup of target ip address
    result = geo(ip)
    ashok_result['geoip'] = result

    return ashok_result


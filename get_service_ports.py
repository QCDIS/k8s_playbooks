import json
import sys

if __name__ == '__main__':
    svc_ports_path = sys.argv[1]
    port_type = sys.argv[2]
    public_ip = sys.argv[3]

    f = open(svc_ports_path, )
    svc_ports = json.load(f)

    services_array = []
    urls = []
    for pp in svc_ports:
        spec_type = pp['spec']['type']
        if spec_type.lower() == port_type.lower():
            service = {'name': pp['metadata']['name']}
            port_infos = []
            for port in pp['spec']['ports']:
                port_type_lower_first = port_type[0].lower() + port_type[1:]
                url = 'https://' + public_ip + ':' + str(port[port_type_lower_first])
                url_entry = {'url':url}
                urls.append(url_entry)
                if 'name' in port:
                    port_name = port['name']
                else:
                    port_name = port_type_lower_first
                port_info = {'name': port_name, 'url': url, 'port':port[port_type_lower_first]}
                port_infos.append(port_info)
            service['info'] = port_infos

            services_array.append(service)
    services = {'services':services_array}
    print(json.dumps(services))

import dnacmodule
import os
import jinja2
from jinja2.environment import Environment
import subprocess

username = "devnetuser"
password = "Cisco123!"
hostname = "https://sandboxdnac2.cisco.com"

# login to dnac
token = dnacmodule.getToken(username, password, hostname)
# get all devices from dnac
devices = dnacmodule.getDevices(hostname, token)
# create dictionary with only hostname and managementIpAddress keys
mylist = [{k: v for k, v in device.items()
           if k.startswith('hostname') or k.startswith('managementIpAddress')}
          for device in devices]
# specify Jinja2 template file
template_name = 'session_template.j2'
# specify registry file to ouput
output_file = 'putty.reg'
# create Jinja2 environment object and refer to templates directory
env = Environment(loader=jinja2.FileSystemLoader('templates'))
# create Jinja2 template object
template = env.get_template(template_name)
# rendertemplate to file
with open(output_file, "w") as f:
    f.write(template.render(mylist=mylist))
# add sessions to registry
subprocess.call(['reg', 'import', output_file])
# print success message
print(f"\nSessions created successfully, open Putty to use")

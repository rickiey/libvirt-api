import libvirt
from xml.etree import ElementTree
vmname="vmname:  "
dev="device:  "
cap="  capacity:  "
allocation="  allocation:  "
physical="  physical:  "
conn = libvirt.open("qemu:///system")
for id in conn.listDomainsID():
    domain = conn.lookupByID(id)
    tree = ElementTree.fromstring(domain.XMLDesc())
    devices = tree.findall('devices/disk/target')
    for d in devices:
        device = d.get('dev')
        try:
            devinfo = domain.blockInfo(device)
        except libvirt.libvirtError:
            pass
        print vmname,domain.name()
	print dev,device
	print cap,devinfo[0]
	print allocation,devinfo[1]
	print physical,devinfo[2]
conn.close()

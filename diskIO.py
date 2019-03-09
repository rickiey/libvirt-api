import libvirt
from xml.etree import ElementTree
conn = libvirt.open("qemu:///system")
for id in conn.listDomainsID():
    domain = conn.lookupByID(id)
    tree = ElementTree.fromstring(domain.XMLDesc())
    devices = tree.findall('devices/disk/target')
    for d in devices:
        device = d.get('dev')
        try:
            devstats = domain.blockStats(device)
            print domain.name(),device,devstats
        except libvirt.libvirtError:
            pass
conn.close()

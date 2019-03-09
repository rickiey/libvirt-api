import libvirt
conn = libvirt.open("qemu:///system")
for id in conn.listDomainsID():
    domain = conn.lookupByID(id)
    print "name:  "
    print domain.name()
    print "UUID:  "  
    print domain.UUIDString()
    print "info:  "
    print domain.info()
conn.close()

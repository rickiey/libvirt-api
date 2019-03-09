import libvirt
conn = libvirt.open("qemu:///system")
for id in conn.listDomainsID():
    domain = conn.lookupByID(id)
    domain.setMemoryStatsPeriod(10)
    meminfo = domain.memoryStats()
    free_mem = float(meminfo['unused'])
    total_mem = float(meminfo['available'])
    util_mem = ((total_mem-free_mem) / total_mem)*100
    print (str(domain.name())+' Memory usage :' + str(util_mem))
conn.close()

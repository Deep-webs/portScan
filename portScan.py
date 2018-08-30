#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:pinocao
import nmap
from optparse import OptionParser
import sys
'''
扫描网段端口状态，IP和端口号通过参数的形式传递
'''
nm = nmap.PortScanner()



class Scaner:
    def single(self, hoststr , portstr):
        nm_scan = nm.scan(hosts=hoststr, ports=portstr)
        if 'error' in nm.scaninfo():
            print(nm.scaninfo()['error'])
            exit(2)
        allhosts = nm.all_hosts()
        for h in allhosts:
            allports = nm[h].all_tcp()
            print('\n', '-----', h, '-----')
            for p in allports:
                print(h, 'tcp/' + str(p), nm[h]['tcp'][p]['state'])

    def mutiple(self, hostlist, portstr):
        for hoststr in hostlist.split(','):
            self.single(hoststr=hoststr, portstr=portstr)


'''
主体函数
'''


def main():
    parser = OptionParser(usage="%prog [Options]", version="%prog 1.0")
    parser.add_option("-H", "--host", action="store", dest="scanHost", help="The hosts will be scan")
    parser.add_option("-p", "--port", action="store", dest="scanPort", help="The ports will be scan")
    (options, args) = parser.parse_args()
    (scanHost, scanPort) = (options.scanHost, str(options.scanPort))
    if len(sys.argv) <= 1:
        parser.print_help()
        exit(3)
    else:
        ScanerResult = Scaner()
        if len(scanHost.split(',')) > 1:
            ScanerResult.mutiple(scanHost, scanPort)
        else:
            ScanerResult.single(scanHost, scanPort)


if __name__ == '__main__':
    main()





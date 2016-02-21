#!/usr/bin/env python

from deplopy.deplopy import SSHTransporter # this is an absolute import 'cause is a script


if __name__ == '__main__':
    import sys
    import pssh.utils

    pssh.utils.enable_host_logger()

    if len(sys.argv) < 3: # at least one command and one hosts
        print 'usage: %s cmd host1 [host2 [ host3 ] ...' % sys.argv[0]
        sys.exit(1)

    cmd = sys.argv[1]
    hosts = sys.argv[2:]

    transporter = SSHTransporter(hosts=hosts)

    output = transporter.run(cmd)

    for host in output:
        for stdout in output[host]['stdout']:
            print stdout


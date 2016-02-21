#!/usr/bin/env python


from deplopy.deplopy import SSHTransporter


if __name__ == '__main__':
    # import pssh.utils
    # pssh.utils.enable_host_logger()
    import sys
    import os
    if len(sys.argv) < 3: # at least one command and one hosts
        print 'usage: %s cmd host1 [host2 [ host3 ] ...' % sys.argv[0]
        sys.exit(1)

    local_filepath = sys.argv[1]
    hosts = sys.argv[2:]

    transporter = SSHTransporter(hosts=hosts)

    transporter.cp(local_filepath, os.path.join('/tmp', local_filepath))

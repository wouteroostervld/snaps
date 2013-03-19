import boto.ec2
import what
import sys
import os.path

class Connection(object):
    def __init__(self):
        self.idata=what.InstanceData()
        self.region=self.idata.region()
        self.instance_id=self.idata.instance_id()
        self._conn=boto.ec2.connect_to_region(self.region)

    def get_attached_volumes(self):
        return self._conn.get_all_volumes(filters={'attachment.instance-id': self.instance_id})

def renew_snapshot(volume, description):
    for snapshot in volume.snapshots():
        if snapshot.description == description:
            snapshot.delete()
    volume.create_snapshot(description)

def usage(argv):
    return "Usage: " + os.path.basename(argv[0]) + " DESCRIPTION\n" 

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        description=argv[1]
    except IndexError:
        sys.stderr.write(usage(argv))
        return 1
    conn=Connection()
    for volume in conn.get_attached_volumes():
        renew_snapshot(volume, "SNAPS " + description)
    return 0


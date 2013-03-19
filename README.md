snaps
=====

snaps is Amazon WebServices EC2 snapshots for the braindead. 

Prerequisites
=============
 * Shellaccess to Amazon Linux/FreeBSD/...-instance
 * python 2.6+
 * pip
 * boto

Install using:
    pip install git+https://github.com/Woutertje/what.git
    pip install git+https://github.com/Woutertje/snaps.git

What does it do?
================

It creates snapshots of all attached volumes of the current instance. If a snapshot already exists with same description it deletes the old snapshot.

Usage
=====

snaps DESCRIPTION

Examples
========

To do an hourly rolling backup. Paste this in your crontab (tested on Debian):

    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/aws/ec2/bin
    AWS_ACCESS_KEY_ID=YOURACCESSKEY
    AWS_SECRET_ACCESS_KEY=YOURSECRET
    20 *    * * *   snaps `date +\%H`




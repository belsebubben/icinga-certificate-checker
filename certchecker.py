#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import sys
import time
import datetime

#import date, timedelta, datetime

timeformat = "%Y-%m-%d"

today = datetime.datetime.today()

def timeLeftChecker(args):
    enddate = datetime.datetime.strptime(args.enddate, timeformat)

    expiresin = enddate - today

    warntime = datetime.timedelta(days=int(args.warn))
    
    ctiticaltime =  datetime.timedelta(days=int(args.crit))

    if ( expiresin < ctiticaltime ):
        print "Certificate: %s expires in %s days!! (%s)" % (args.certname, expiresin.days, enddate.date())
        sys.exit(2)

    if ( expiresin < warntime ):
        print "Certificate: %s expires in %s days! (%s)" % (args.certname, expiresin.days, enddate.date())
        sys.exit(1)

    if ( expiresin > warntime ):
        print "Certificate: %s expires in %s days. (%s)" % (args.certname, expiresin.days, enddate.date() )
        sys.exit(0)

    print "Certificate check for %s with end date %s failed" % (args.certname, args.enddate)
    sys.exit(2)

def parseArgs():
    parser = argparse.ArgumentParser(argument_default="")
    parser.add_argument("--certname")
    parser.add_argument("--enddate", help="Enddate denotes when the cert expires, format %%Y-%%m-%%d")
    parser.add_argument("--warn", help="How many days before expiry to give a warning , format %%Y-%%m-%%d")
    parser.add_argument("--crit", help="How many days before expiry to give a warning , format %%Y-%%m-%%d")
    args = parser.parse_args()
    return args



if __name__ == '__main__':
    args = parseArgs()
    timeLeftChecker(args)

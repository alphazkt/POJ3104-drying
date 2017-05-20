# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:03:30 2017

@author: AlphaTao
dryingPOJ3104
"""
def check(t):
    now=0    
    for i in waterlist:
        if i>t:
            now +=(i-t-1)/(k-1)+1
            if now>t:
                return False
    return True

if __name__=='__main__':
    n=input()
    waterlist=[int(i) for i in raw_input().split()]
    k=input()
    l=0
    r=max(waterlist)
    if k==1:
        print 'time=',r
    else:
        while(l<=r):
            mid=(l+r)/2
            if check(mid):
                r=mid-1
            else:
                l=mid+1
        print l
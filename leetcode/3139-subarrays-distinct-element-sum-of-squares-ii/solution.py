class Solution:
    def sumCounts(self, nums):
        n, mod = len(nums), 10**9+7
        s, q, lazy = [0]*(4*n), [0]*(4*n), [0]*(4*n)

        def upd(p,l,r,a,b):
            if a<=l and r<=b:
                d=r-l+1
                q[p]=(q[p]+2*s[p]+d)%mod
                s[p]=(s[p]+d)%mod
                lazy[p]+=1
                return
            m=(l+r)//2
            if lazy[p]:
                v=lazy[p]
                for c,x,y in ((p*2,l,m),(p*2+1,m+1,r)):
                    d=y-x+1
                    q[c]=(q[c]+2*v*s[c]+v*v*d)%mod
                    s[c]=(s[c]+v*d)%mod
                    lazy[c]+=v
                lazy[p]=0
            if a<=m: upd(p*2,l,m,a,b)
            if b>m: upd(p*2+1,m+1,r,a,b)
            s[p]=(s[p*2]+s[p*2+1])%mod
            q[p]=(q[p*2]+q[p*2+1])%mod

        last, ans = {}, 0
        for i,x in enumerate(nums):
            j=last.get(x,-1)+1
            upd(1,0,n-1,j,i)
            last[x]=i
            ans=(ans+q[1])%mod
        return ans

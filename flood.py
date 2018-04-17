def flood(pas,chas):
    ans = []
    if pas > 2*chas:
        print('Target HF too low')
    elif chas > 3*pas:
        print('Target HF too high')
    else:
        return floo(pas,chas,ans)
        
def floo(pas,chas,ans):
    take = int(chas/5)
    print('p,c,a: ',pas,chas,ans)
    if pas + take <= 2*(chas - take):
        #taking another 20% is fine
        ans.append(take)
        print('take: ',take)
        return floo(pas+take,chas-take,ans)
    else:
        #time to flood to the limit
        aim = int((pas + chas)/3) + ((pas + chas) % 3 > 0)
        ans.append(chas-aim)
        print('aim: ',aim)
        ans.append(int(aim/5))
        try:
            ans.remove(0)
        except ValueError:
            pass  # do nothing!
        return ans

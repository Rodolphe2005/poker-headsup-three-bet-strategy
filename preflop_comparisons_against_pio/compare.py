import pandas as pd
import os

hm = pd.read_csv('hm.csv')
hm = hm[['Cards', 'Total Hands', 'VPIP', '3Bet']]
hm['VPIP'] = hm['VPIP'].str.replace(',', '.').astype(float)
hm['3Bet'] = hm['3Bet'].str.replace(',', '.').astype(float)
hm['CALL_real'] = hm['VPIP'] - hm['3Bet']


pio = pd.read_csv('pio.csv')
pio = pio[['Hand', 'CALL', 'RAISE 100']]
print(hm)

def remove_suits(hand):
    c1, s1, c2, s2 = hand
    if s1==s2:
        return c1+c2+'s'
    else:
        if c1!=c2:
            return c1+c2+'o'
        else:
            return c1+c2

pio['Hand2'] = pio.Hand.apply(remove_suits)
pio2 = pio.drop_duplicates(subset=['Hand2'])
df = hm.merge(pio2, how='outer', left_on='Cards', right_on='Hand2')
df['CALL_diff'] = df['CALL_real'] - df['CALL']
df['3Bet_diff'] = df['3Bet'] - df['RAISE 100']
df2 = df.sort_values('CALL_diff')
df2 = df2[['Cards', 'Total Hands', 'CALL_diff', 'CALL_real', 'CALL', '3Bet_diff', '3Bet', 'RAISE 100']]
df2.to_csv('t.csv')
print(df2)
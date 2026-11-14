import json,os;from urllib.request import*;from time import time as T
V=(0,100,320,330,500,900,0);Y=(0,0,1,1,2,4,0)
U=("::::FFFF@@AA=>??;<=>;;<<:;;;::::","578879:;9;=>:<>?:<>?9;==79:<5789","78888:::9;;<:<<=:<=::;<<9:;;789:",";<<==>>?:;<<:;<<:;<<:;<<9:;<89:;","89::9:;;:;;<:;<<:;<<:;;<9:;;89::","455656786789789:89:;9:;<:;<=<==<")
W="89:;9:<=:<>?;=?@;=?@:<>?9:<=89:;"
P=[0]*1664;D=[0]*1664
for q,r in enumerate(U,1):
 for s in range(128):
  if s&136:continue
  f=s&7;i=(7-(s>>4))*4+min(f,7-f);v=V[q]+(ord(r[i])-58)*5;P[(q+6)*128+s]=v;P[(6-q)*128+(s^112)]=-v
  if q==6:d=(ord(W[i])-ord(r[i]))*5;D[1536+s]=d;D[s^112]=-d
Z=[i*0x2545F4914F6CDD1D&2**64-1 for i in range(1,1690)]
N=(-33,-31,-18,-14,14,18,31,33);K=(-17,-16,-15,-1,1,15,16,17);G=(-17,-15,15,17);R=(-16,-1,1,16);GR=G+R
C=[13,15,15,15,12,15,15,14]+[15]*104+[7,15,15,15,3,15,15,11]
LW=((1,(1,2),(0,1,2),2,3,1),(2,(-3,-2,-1),(0,-1,-2),-2,-4,-1))
B=[0]*128;S=1;A=15;E=-1;M=0;J=0;H=24;X=0;O=[0,0];SK=[];I=[];F=[];CG=-1
TT={};KL=[[0,0]for _ in range(256)];HS=[0]*1664
ND=0;DL=0;SL=0;NL=100000;MT=100000;BI=1000000;T0=T()
class TO(Exception):pass
def ak(s,by):
 for o in(15,17):
  t=s-o*by
  if not t&136 and B[t]==by:return 1
 for o in N:
  t=s+o
  if not t&136 and B[t]==2*by:return 1
 for o in K:
  t=s+o
  if not t&136 and B[t]==6*by:return 1
 for o in GR:
  t=s+o
  while not t&136:
   q=B[t]
   if q:
    if q==5*by or q==(3+(o in R))*by:return 1
    break
   t+=o
 return 0
def ld(f):
 global B,S,A,E,M,J,H,Q,X,O,SK,I
 w=f.split();B=[0]*128;M=J=H=0;X=0;O=[0,0];SK=[];I=F[:]
 r=7;c=0
 for ch in w[0]:
  if ch=='/':r-=1;c=0
  elif ch.isdigit():c+=int(ch)
  else:
   p='pnbrqk'.index(ch.lower())+1;q=p*(ch.isupper()*2-1);s=r*16+c;B[s]=q;M+=P[(q+6)*128+s];X^=Z[(q+6)*128+s];H+=Y[p]
   if p==6:O[q<0]=s;J+=D[(q+6)*128+s]
   c+=1
 S=1 if w[1]=='w' else -1;A=0
 for i,ch in enumerate('KQkq'):
  if ch in w[2]:A|=1<<i
 E=ord(w[3][0])-97+(int(w[3][1])-1)*16 if w[3]!='-' else -1
 if S<0:X^=Z[1664]
 X^=Z[1665+A]
 if E>=0:X^=Z[1681+(E&7)]
def sy(g):
 global CG,HS
 if g['game']!=CG:CG=g['game'];F.clear();HS=[0]*1664
 ld(g['fen']);F.append(X)
def pu(m):
 global S,A,E,M,J,H,X
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;fl=(m>>17)&7
 p=B[f];us=S<0
 cs=t-16*S if fl==2 else t;cp=B[cs]
 SK.append((cp,cs,A,E,X,M,J,H));I.append(X)
 if E>=0:X^=Z[1681+(E&7)]
 X^=Z[1665+A]
 B[f]=0;X^=Z[(p+6)*128+f];M-=P[(p+6)*128+f]
 if p==6*S:J-=D[(p+6)*128+f]
 if cp:
  B[cs]=0;X^=Z[(cp+6)*128+cs];M-=P[(cp+6)*128+cs];a=abs(cp);H-=Y[a]
 q=pr*S if pr else p
 B[t]=q;X^=Z[(q+6)*128+t];M+=P[(q+6)*128+t]
 if pr:H+=Y[pr]
 if q==6*S:O[us]=t;J+=D[(q+6)*128+t]
 if fl>=3:
  r,w=(t+1,t-1)if fl==3 else(t-2,t+1);rp=B[r];B[w]=rp;B[r]=0
  X^=Z[(rp+6)*128+r]^Z[(rp+6)*128+w];M+=-P[(rp+6)*128+r]+P[(rp+6)*128+w]
 A&=C[f]&C[t];X^=Z[1665+A]
 E=t-16*S if fl==1 else -1
 if E>=0:X^=Z[1681+(E&7)]
 X^=Z[1664];S=-S
def po(m):
 global S,A,E,M,J,H,X
 cp,cs,A,E,X,M,J,H=SK.pop();I.pop();S=-S
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;fl=(m>>17)&7
 q=B[t];B[t]=0;B[f]=S if pr else q
 if cp:B[cs]=cp
 if B[f]==6*S:O[S<0]=f
 if fl>=3:
  a,b=(t-1,t+1)if fl==3 else(t+1,t-2);B[b]=B[a];B[a]=0
def gn(caps,ttm,k1,k2):
 ms=[];ap=ms.append;sd=S;d=16*sd;lr=7*(sd>0);sr=1+5*(sd<0)
 def em(f,t,pr,fl,sc):
  m=f|(t<<7)|(pr<<14)|(fl<<17)
  sc+=1<<22 if m==ttm else 1<<19 if m==k1 or m==k2 else 0
  ap(m|(sc<<20))
 if not caps:
  kf=4+112*(sd<0)
  for bt,es,tr,tg,rf,rt in LW:
   if A&(bt<<(2*(sd<0))) and B[kf+rf]==4*sd and all(not B[kf+x] for x in es) and all(not ak(kf+x,-sd) for x in tr):em(kf,kf+tg,0,3+(tg<0),0)
 for s in range(128):
  p=B[s]
  if p*sd<=0:continue
  a=abs(p)
  if a==1:
   t=s+d
   if not t&136 and not B[t]:
    if (t>>4)==lr:
     for pr in(5,4,3,2):em(s,t,pr,0,(1<<20)+(V[pr]<<4))
    elif not caps:
     em(s,t,0,0,HS[(p+6)*128+t])
     if (s>>4)==sr:
      u=t+d
      if not B[u]:em(s,u,0,1,HS[(p+6)*128+u])
   for dd in(d-1,d+1):
    t=s+dd
    if t&136:continue
    q=B[t]
    if q*sd<0:
     if (t>>4)==lr:
      for pr in(5,4,3,2):em(s,t,pr,0,(1<<20)+(V[abs(q)]<<4)+(V[pr]<<4))
     else:em(s,t,0,0,(1<<20)+(V[abs(q)]<<4)-100)
    elif t==E:em(s,t,0,2,(1<<20)+1500)
  elif a==2 or a==6:
   for dd in N if a==2 else K:
    t=s+dd
    if t&136:continue
    q=B[t]
    if not q:
     if not caps:em(s,t,0,0,HS[(p+6)*128+t])
    elif q*sd<0:em(s,t,0,0,(1<<20)+(V[abs(q)]<<4)-V[a])
  else:
   for dd in G if a==3 else R if a==4 else GR:
    t=s+dd
    while not t&136:
     q=B[t]
     if not q:
      if not caps:em(s,t,0,0,HS[(p+6)*128+t])
     else:
      if q*sd<0:em(s,t,0,0,(1<<20)+(V[abs(q)]<<4)-V[a])
      break
     t+=dd
 return sorted(ms,reverse=True)
def uc(m):
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;return chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)+('nbrq'[pr-2] if pr else '')
def ev():return (M+J*(24-H)//24)*S
def ck():
 global ND;ND+=1
 if ND>NL or ND&2047==0 and T()>DL:raise TO
def md(s,p):return s-p if s>MT-1000 else s+p if s<-MT+1000 else s
def qs(a,b,p):
 ck()
 if X in I:return 0
 if p>96:return ev()
 chk=ak(O[S<0],-S)
 if not chk:
  st=ev()
  if st>=b:return st
  if st>a:a=st
 lg=0
 for m in gn(0 if chk else 1,0,0,0):
  c=m&1048575;pu(c)
  if ak(O[S>0],S):po(c);continue
  lg+=1;s=-qs(-b,-a,p+1);po(c)
  if s>a:a=s
  if a>=b:break
 return -(MT-p) if chk and lg==0 else a
def ab(a,b,d,p):
 global S,E,X
 ck()
 if p and X in I:return 0
 if d<=0 or p>120:return qs(a,b,p)
 chk=ak(O[S<0],-S)
 e=TT.get(X);ttm=0
 if e:
  ed,es,ef,ttm=e
  if ed>=d:
   s=md(es,p)
   if ef==0 or ef==1 and s>=b or ef==2 and s<=a:return s
 if d>=3 and not chk and b<MT-1000 and H>0 and ev()>=b:
  oz=X;oe=E
  if E>=0:X^=Z[1681+(E&7)]
  E=-1;X^=Z[1664];S=-S;I.append(oz)
  s=-ab(-b,-b+1,d-1-(2+(d>=6)),p+1)
  S=-S;E=oe;X=oz;I.pop()
  if s>=b:return s if s<MT-1000 else b
 k1,k2=KL[p]
 ms=gn(0,ttm,k1,k2);best=-BI;bm=0;a0=a;n=0;ex=chk
 for m in ms:
  c=m&1048575;t=(c>>7)&127;pr=(c>>14)&7;fl=(c>>17)&7;tc=B[t] or pr or fl==2
  pu(c)
  if ak(O[S>0],S):po(c);continue
  if n==0:s=-ab(-b,-a,d-1+ex,p+1)
  else:
   rd=1+(d>=6 and n>=8)if d>=3 and n>=3 and not chk and not tc else 0
   s=-ab(-a-1,-a,d-1-rd+ex,p+1)
   if s>a:s=-ab(-b,-a,d-1+ex,p+1)
  po(c);n+=1
  if s>best:best=s;bm=c
  if s>a:a=s
  if a>=b:
   if not tc:
    q=B[c&127]
    HS[(q+6)*128+t]+=d*d
    if c!=k1:KL[p][1]=KL[p][0];KL[p][0]=c
   break
 if n==0:return -(MT-p) if chk else 0
 TT[X]=(d,md(best,-p),2 if best<=a0 else 1 if best>=b else 0,bm)
 return best
def th():
 global ND,DL,SL,NL
 if len(TT)>3e5:TT.clear()
 fb=None
 for m in gn(0,0,0,0):
  c=m&1048575;pu(c)
  if not ak(O[S>0],S):fb=c;po(c);break
  po(c)
 if fb is None:return None
 ND=0;st=T();el=st-T0
 k=el>900;NL=100000-40000*k;SL=st+4-1.5*k;DL=st+8.5-.5*k
 pv=fb
 for de in range(1,33):
  try:ab(-BI,BI,de,0)
  except TO:break
  e=TT.get(X)
  if e and e[3]:pv=e[3]
  if T()>SL:break
 return pv
URL=os.environ['MAKEFUN_ENV_URL']
def rq(p,d):
 q=Request(URL+p,json.dumps(d).encode())
 return json.loads(urlopen(q,timeout=20).read())
def rs(g):
 try:rq('/resign',{'game':g})
 except:pass
while(g:=rq('/game',{}))['status']!='done':
 while g['status']=='your_move':
  LM=g['legal_moves']
  try:
   sy(g);mv=th();u=uc(mv)if mv else ''
   if u not in LM:u=LM[0]
  except:u=LM[0] if LM else ''
  if not u:rs(g['game']);break
  try:g=rq('/move',{'game':g['game'],'move':u})
  except:
   try:g=rq('/move',{'game':g['game'],'move':LM[0]})
   except:rs(g['game']);break

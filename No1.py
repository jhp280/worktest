urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/haha.png",
"http://gliacloud.com/haha.png",
]
dirfile=list();
nlist={}
totn=list()
for s in urls:
    totsplit=len(s.split('/'))
    k=s.split('/')[totsplit-1]
    if k not in dirfile:
        dirfile.append(k)
        nlist[k.split('.')[0]+k.split('.')[1]]=1;
    else:
        nlist[k.split('.')[0]+k.split('.')[1]]=nlist[k.split('.')[0]+k.split('.')[1]]+1
for key in nlist:
    totn.append(nlist[key])
totn.sort(reverse=True);
for i in range(3):
    for key in nlist:
        if(totn[i]==nlist[key]):
            print(key+" "+str(nlist[key]))
            nlist.pop(key)
            break;
print(nlist)

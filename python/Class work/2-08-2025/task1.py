d1={'p':600,'q':300,'r':'400'}
d2={'p':300,'q':200}
ans={}
for i,j,in d1.item():
    for k,l in d2.item():
        if i==k:
            ans[i]=j+1
            print(ans) 

from string import maketrans

ori = 'Of zit kggd zitkt qkt ygxk ortfzoeqs wqlatzwqssl qfr zvg ortfzoeqs yggzwqssl. Fgv oy ngx vqfz zg hxz zitd of gft soft, piv dgfn lgsxzogfl qkt zitkt? Zohl: hstqlt eiqfut zit ygkd gy zit fxdwtk ngx utz. Zit Hkgukqddtkl!'

def ali_decode(letter):
    t=maketrans("qwertyuiopasdfghjklzxcvbnm","abcdefghijklmnopqrstuvwxyz")
    return letter.translate(t)

print(ali_decode(ori))
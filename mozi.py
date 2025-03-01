import sys

from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po

from lcd_font_mc import LCD_font as LCD_font_mc

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)

display2 = LCD_font_mc(mc)
display2.init_col(COLOR_ON=param.DIAMOND_BLOCK, COLOR_OFF=param.AIR)
display2.init_row(X_ORG=-35, Y_ORG=param.Y_SEA + 85, Z_ORG=-20, COL_INTV=6)

display3 = LCD_font_mc(mc)
display3.init_col(COLOR_ON=param.DIAMOND_BLOCK, COLOR_OFF=param.AIR)
display3.init_row(X_ORG=-35, Y_ORG=param.Y_SEA + 73, Z_ORG=-20, COL_INTV=6)

#12=!,13=?,14=A,15=B,16=C,17=D,18=E,19=F,20=G,21=H,22=I,23=J,24=K,25=L,26=M,27=N,28=O,29=P,30=Q,31=R,32=S,33=T,34=U,35=V,36=W,37=X,38=Y,39=Z
#40=a,41=b,42=c,43=d,44=e,45=f,46=g,47=h,48=i,49=j,50=k,51=l,52=m,53=n,54=o,55=p,56=q,57=r,58=s,59=t,60=u,61=v,62=w,63=x,64=y,65=z
display2.update_col(col=0, code=21)
display2.update_col(col=1, code=44)
display2.update_col(col=2, code=51)
display2.update_col(col=3, code=51)
display2.update_col(col=4, code=54)
display2.update_col(col=5, code=12)

display3.update_col(col=0, code=27)
display3.update_col(col=1, code=48)
display3.update_col(col=2, code=42)
display3.update_col(col=3, code=44)
display3.update_col(col=5, code=59)
display3.update_col(col=6, code=54)
display3.update_col(col=8, code=52)
display3.update_col(col=9, code=44)
display3.update_col(col=10, code=44)
display3.update_col(col=11, code=59)
display3.update_col(col=13, code=64)
display3.update_col(col=14, code=54)
display3.update_col(col=15, code=60)
display3.update_col(col=16, code=12)
#!/usr/bin/env python

import os,time
from scp_file_test import scp_file
#os.chdir("/workspace/share/kong-05/xli3/xiaozhan_integration/vxworks")
#os.system("./wrenv.sh -p helix")
#os.chdir("/workspace/share/kong-05/xli3/xiaozhan_integration/vxworks/F10020")
os.system("vxprj vsb create -S -lp64 -cpu CORE -smp -inet6 -profile DEVELOPMENT -bsp itl_generic vsb_itl_generic")
os.chdir("vsb_itl_generic")
os.system("vxprj vsb add RTNET")
os.system("make -j 22")

os.chdir("/workspace/share/kong-05/xli3/xiaozhan_integration/vxworks/F10020")
os.system("vxprj create -inet6 itl_generic -vsb vsb_itl_generic llvm vip_itl_generic")
os.chdir("vip_itl_generic")
os.system("vxprj component add INCLUDE_ROMFS INCLUDE_RTNET INCLUDE_SHELL INCLUDE_RTNET_MUX INCLUDE_RTNET_PING INCLUDE_RTNET_FIB_SHOW INCLUDE_RTNET_SOCK_SHOW INCLUDE_RTNET_IP_SHOW INCLUDE_RTNET_DEMO INCLUDE_GEI825XX_VXB_END INCLUDE_RTNET_IPV6_SUPPORT")
#os.system("cp /workspace/share/kong-05/xli3/fragping.c .")
#os.system("vxprj file add fragping.c")
os.system("mkdir romfs")
os.chdir("romfs")
os.system("cp /workspace/share/kong-05/xli3/gei_interface_anvl_trial.json .")
os.chdir("/workspace/share/kong-05/xli3/xiaozhan_integration/vxworks/F10020/vip_itl_generic")
cmd=r'vxprj parameter setstring RTNET_JSON_FILE "/romfs/gei_interface_anvl_trial.json"'
os.system(cmd)
os.system("vxprj build")
src="/workspace/share/kong-05/xli3/xiaozhan_integration/vxworks/F10020/vip_itl_generic/default/vxWorks"
dst="windriver@128.224.163.8:/home/windriver"
passwd="windriver"
scp_file(src,dst,passwd)



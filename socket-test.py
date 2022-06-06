import netifaces as ni
import psutil
import os
import socket
import streamlit as st

def get_ip() -> list:
    if os.name =='nt':
        return socket.gethostbyname_ex(socket.gethostname())[2]

    else:
        result = []
        address_list = psutil.net_if_addrs()
        for nic in address_list.keys():
            ni.ifaddresses(nic)
            try:
                ip = ni.ifaddresses(nic)[ni.AF_INET][0]['addr']
                if ip not in ["127.0.0.1"]:
                    result.append(ip)
            except KeyError as err:
                pass
        return result

st.title('Socket Test')

ip_address = get_ip()

st.write('The current PC s IP address is', ip_address[0])
st.markdown(f'''
# The current PC IP address is
## f'{ip_address[0]}'
''')
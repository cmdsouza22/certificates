from OpenSSL.SSL import Connection, Context, SSLv3_METHOD, TLSv1_2_METHOD
from datetime import datetime, time
import socket
import pandas as pd
hosts = ['www.apple.com', 'www.google.com', 'www.facebook.com', 'www.netflix.com', 'www.yahoo.com']
file_path = '/Users/cdsouza2/outputTest/cert_details.csv'

df = []

try:
    for host in hosts:
        try:
            ssl_connection_setting = Context(SSLv3_METHOD)
        except ValueError:
            ssl_connection_setting = Context(TLSv1_2_METHOD)
        ssl_connection_setting.set_timeout(5)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, 443))
            c = Connection(ssl_connection_setting, s)
            c.set_tlsext_host_name(str.encode(host))
            c.set_connect_state()
            c.do_handshake()
            cert = c.get_peer_certificate()
            issuer = cert.get_issuer()
            subject_list = cert.get_subject().get_components()
            cert_byte_arr_decoded = {}
            for item in subject_list:
                cert_byte_arr_decoded.update({item[0].decode('utf-8'): item[1].decode('utf-8')})
            if len(cert_byte_arr_decoded) > 0:
                subject = cert_byte_arr_decoded
            if cert_byte_arr_decoded["CN"]:
                common_name = cert_byte_arr_decoded["CN"]
            expiry = datetime.strptime(str(cert.get_notAfter().decode('utf-8')), "%Y%m%d%H%M%SZ")
            data = issuer, subject, expiry
            df.append(data)
            c.shutdown()
            s.close()
    c_df = pd.DataFrame(df, columns = ['Cert_Issuer', 'Subject', 'Cert_Validity'])
    c_df['Cert_Validity'] = pd.to_datetime(c_df.Cert_Validity)
    c_df.sort_values(by='Cert_Validity').to_csv(file_path)
except:
    print("Connection to {} failed.".format(host)) 

from scapy.all import *
import couchdb
import time

def db_setup():
    # If your CouchDB server is running elsewhere, set it up like this:
    couch = couchdb.Server('http://<ip-address>:5984/')
    # select database
    db = couch['test']
    return db
    
db = db_setup()

def PacketHandler(db):
	def send_to_db(pkt):
		if pkt.haslayer(RadioTap) and pkt.haslayer(Dot11):        
			if pkt.type == 0 and pkt.subtype == 4:
				try:
					ssid = pkt[Dot11ProbeReq].info
				except:
					ssid = " "
				
				print "%s : %s" %(pkt.addr2,ssid)
				doc = {'type': 'request', 'addr2': pkt.addr2, 'ssid': ssid, 'time': time.time()}
				db.save(doc)
				# if pkt.addr2 not in device_list:
				# 	device_list.append(pkt.addr2)
				# 	doc = {'type': 'request', 'addr2': pkt.addr2, 'ssid': ssid, 'time': time.time()}
				# 	db.save(doc)
			
# 			elif pkt.type == 0 and pkt.subtype == 5:
# 				ssid = pkt[Dot11Elt][0].info
# 				doc = {'type' : 'response', 'addr1': pkt.addr1, 'addr2': pkt.addr2, 'ssid': ssid, 'time': time.time()}
# 				db.save(doc)
			
	return send_to_db

sniff(iface="mon0", prn=PacketHandler(db))

	


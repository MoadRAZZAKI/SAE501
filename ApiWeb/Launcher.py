import json
from flask import Flask, jsonify, request
from data_manager import DBConnector

app = Flask(__name__)
db_connector = DBConnector()

# Route to get all packets
@app.route('/api/data', methods=['GET'])
def get_all_data():
    db = db_connector.connect()
    data = db.packet_DHCP.find()  
    result = [{"Type": item["Type"], "Ether": item["Ether"], "IP": item["IP"], "DHCP": item["DHCP"], "UDP": item["UDP"], "BOOTP": item["BOOTP"]} for item in data]
    return jsonify(result)

# Route to filter packets by type
@app.route('/api/data/<packet_type>', methods=['GET'])
def filter_data_by_type(packet_type):
    db = db_connector.connect()
    data = db.packet_DHCP.find({"Type": packet_type})  
    result = [{"Type": item["Type"], "Ether": item["Ether"], "IP": item["IP"], "DHCP": item["DHCP"], "UDP": item["UDP"], "BOOTP": item["BOOTP"]} for item in data]
    return jsonify(result)

# Route to get DHCP packets by source MAC address
@app.route('/api/data/dhcp/source_mac/<source_mac>', methods=['GET'])
def get_dhcp_packets_by_source_mac(source_mac):
    db = db_connector.connect()
    data = db.packet_DHCP.find({"Ether.src": source_mac})  
    result = [{"Type": item["Type"], "Ether": item["Ether"], "IP": item["IP"], "DHCP": item["DHCP"], "UDP": item["UDP"], "BOOTP": item["BOOTP"]} for item in data]
    return jsonify(result)

# Route to get DHCP packets by destination MAC address
@app.route('/api/data/dhcp/destination_mac/<destination_mac>', methods=['GET'])
def get_dhcp_packets_by_destination_mac(destination_mac):
    db = db_connector.connect()
    data = db.packet_DHCP.find({"Ether.dst": destination_mac})  
    result = [{"Type": item["Type"], "Ether": item["Ether"], "IP": item["IP"], "DHCP": item["DHCP"], "UDP": item["UDP"], "BOOTP": item["BOOTP"]} for item in data]
    return jsonify(result)

# Route to get DHCP packets by source IP address
@app.route('/api/data/dhcp/source_ip/<source_ip>', methods=['GET'])
def get_dhcp_packets_by_source_ip(source_ip):
    db = db_connector.connect()
    data = db.packet_DHCP.find({"IP.src": source_ip})  
    result = [{"Type": item["Type"], "Ether": item["Ether"], "IP": item["IP"], "DHCP": item["DHCP"], "UDP": item["UDP"], "BOOTP": item["BOOTP"]} for item in data]
    return jsonify(result)

# Route to get DHCP packets by destination IP address
@app.route('/api/data/dhcp/destination_ip/<destination_ip>', methods=['GET'])
def get_dhcp_packets_by_destination_ip(destination_ip):
    db = db_connector.connect()
    data = db.packet_DHCP.find({"IP.dst": destination_ip})  
    result = [{"Type": item["Type"], "Ether": item["Ether"], "IP": item["IP"], "DHCP": item["DHCP"], "UDP": item["UDP"], "BOOTP": item["BOOTP"]} for item in data]
    return jsonify(result)

# Route to get DHCP packets by DHCP requested address
@app.route('/api/data/dhcp/requested_address/<requested_address>', methods=['GET'])
def get_dhcp_packets_by_requested_address(requested_address):
    db = db_connector.connect()
    data = db.packet_DHCP.find({"DHCP.options": requested_address})  
    result = [{"Type": item["Type"], "Ether": item["Ether"], "IP": item["IP"], "DHCP": item["DHCP"], "UDP": item["UDP"], "BOOTP": item["BOOTP"]} for item in data]
    return jsonify(result)

# Route to get DHCP packets by source port
@app.route('/api/data/dhcp/source_port/<source_port>', methods=['GET'])
def get_dhcp_packets_by_source_port(source_port):
    db = db_connector.connect()
    data = db.packet_DHCP.find({"UDP.sport": int(source_port)})  
    result = [{"Type": item["Type"], "Ether": item["Ether"], "IP": item["IP"], "DHCP": item["DHCP"], "UDP": item["UDP"], "BOOTP": item["BOOTP"]} for item in data]
    return jsonify(result)

# Route to get DHCP packets by destination port
@app.route('/api/data/dhcp/destination_port/<destination_port>', methods=['GET'])
def get_dhcp_packets_by_destination_port(destination_port):
    db = db_connector.connect()
    data = db.packet_DHCP.find({"UDP.dport": int(destination_port)})  
    result = [{"Type": item["Type"], "Ether": item["Ether"], "IP": item["IP"], "DHCP": item["DHCP"], "UDP": item["UDP"], "BOOTP": item["BOOTP"]} for item in data]
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)


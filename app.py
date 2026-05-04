from flask import Flask, render_template, jsonify, request
import csv, io

app = Flask(__name__)
packets_db = []

COMMON_PORTS = {
    '80':'HTTP','443':'HTTPS','22':'SSH','53':'DNS',
    '21':'FTP','25':'SMTP','3389':'RDP','5353':'mDNS','1900':'SSDP'
}

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    global packets_db

    file = request.files.get("file")
    if not file:
        return jsonify({"error":"No file"}),400

    stream = io.StringIO(file.stream.read().decode("utf-8"))
    reader = csv.DictReader(stream)

    packets = []

    for r in reader:

        src_port = str(r.get("Src Port","")).strip()
        dst_port = str(r.get("Dst Port","")).strip()
        proto = r.get("Protocol","N/A").upper()

        service = (
            r.get("Service")
            or COMMON_PORTS.get(dst_port)
            or COMMON_PORTS.get(src_port)
        )

        if not service:
            service = "Control" if proto=="ICMP" else "Data"

        packets.append({
            "time": r.get("Time","0"),
            "src_ip": r.get("Source IP","0.0.0.0"),
            "src_port": src_port or "—",
            "dst_ip": r.get("Destination IP","0.0.0.0"),
            "dst_port": dst_port or "—",
            "protocol": proto,
            "service": service,
            "size": int(r.get("Size",0))
        })

    packets_db = packets
    return jsonify({"status":"success","count":len(packets_db)})


@app.route('/packets')
def packets():

    proto = request.args.get("protocol","ALL").upper()
    search = request.args.get("search","").lower()

    result = packets_db

    if proto!="ALL":
        result = [p for p in result if p["protocol"]==proto]

    if search:
        result = [
            p for p in result
            if search in p["src_ip"]
            or search in p["dst_ip"]
            or search in p["service"].lower()
        ]

    total = len(result)

    stats = {
        "total": total,
        "tcp": sum(p["protocol"]=="TCP" for p in result),
        "udp": sum(p["protocol"]=="UDP" for p in result),
        "icmp": sum(p["protocol"]=="ICMP" for p in result),
        "avg_size": round(sum(p["size"] for p in result)/total,1) if total else 0
    }

    return jsonify({"packets":result,"stats":stats})


@app.route('/clear', methods=['POST'])
def clear():
    global packets_db
    packets_db = []
    return jsonify({"status":"cleared"})


if __name__ == "__main__":
    app.run(debug=True)
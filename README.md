🛰️ NetWatch – Network Packet Analyzer

NetWatch is a web-based network packet analysis dashboard designed to help users easily inspect and understand network traffic data. In modern networks, large amounts of packet data are generated, which can be difficult to analyze manually. This tool simplifies that process by allowing users to upload a CSV file containing packet information and instantly view meaningful insights.

The system processes the uploaded data using a Flask backend and presents it through a clean and interactive web interface. Users can view key statistics such as TCP, UDP, and ICMP traffic, as well as explore individual packets in a structured table. To make analysis easier, NetWatch also provides filtering and search features so users can quickly locate specific network activity.

Overall, NetWatch is designed to make basic network traffic analysis simple, fast, and visually clear for learning and educational purposes.



🚀 Features

📁 CSV Upload Support – Load packet capture files easily

📊 Live Statistics Dashboard – TCP, UDP, and ICMP counts

🔍 Smart Search & Filter – Search by IP, protocol, or service

⚡ Optimized Performance – Handles large datasets smoothly

🎨 Modern UI – Clean dark-themed interface

🛠 Tech Stack

Backend

Python

Flask

Frontend

HTML

CSS (Inline Styling)

JavaScript 

📂 Project Structure

NetWatch/

│

├── app.py

├── templates/

│   └── index.html

└── README.md


⚙️ How It Works

User uploads a CSV file

Flask reads and processes packet data

Data is stored in memory

Frontend fetches data using API (/packets)

Dashboard updates stats + table dynamically

🚀 Getting Started

1️⃣ Clone the repository

git clone https://github.com/your-username/netwatch.git

cd netwatch

2️⃣ Install dependencies

pip install flask

3️⃣ Run the application

python app.py

4️⃣ Open in browser

http://127.0.0.1:5000

📁 Expected CSV Format

Your CSV file should contain:

Time, Source IP, Destination IP, Src Port, Dst Port, Protocol, Size, Service

📊 Dashboard Preview

<img width="468" alt="NetWatch Dashboard" src="https://github.com/user-attachments/assets/a7ff11fc-8aca-4f6d-9ef2-04b1afa2c8b1" />

🧠 Challenges Faced

⚡ Performance Optimization

Large CSV files slowed down the interface, so only 200 rows are rendered at a time.

🧹 Data Cleaning Issues

Some CSV files had missing or invalid values, which required default handling.

🔗 Backend–Frontend Integration

Connected Flask APIs with JavaScript Fetch to enable real-time updates without page reload.

🔮 Future Improvements

📡 Real-time packet capture (live sniffing)

📈 Graph-based traffic visualization

📄 Export filtered results (CSV/PDF)

🔍 Advanced protocol classification

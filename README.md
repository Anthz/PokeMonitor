# **Pokémon TCG Monitor**  

**A smart, user-friendly tool to track Pokémon TCG prices and combat scalping bots.**  

![GUI Screenshot](https://via.placeholder.com/800x400?text=Pokémon+TCG+Monitor+GUI)  

---

## **✨ Features**  

✅ **Real-Time Price Monitoring**  
- Tracks eBay UK and other retailers (extensible to more sites).  
- Alerts when prices drop below your target.  

✅ **Anti-Scalping Tools**  
- Proxy rotation to avoid IP bans.  
- Built-in bot detection countermeasures.  

✅ **User-Friendly GUI**  
- Add/edit products with intuitive hints.  
- Test proxies with one click.  
- Clean dashboard with color-coded pricing.  

✅ **Safety & Reliability**  
- Input validation to prevent errors.  
- Graceful error handling with fallback notifications.  
- SQLite database for price history.  

---

## **🚀 Quick Start**  

### **1. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **2. Configure Products & Proxies**  
- Edit `config/products.yaml` (or use the GUI).  
- Add proxies to `config/proxies.txt` (one per line).  

### **3. Run the Application**  
```bash
python src/main.py
```

---

## **🛠 Technical Details**  

### **Built With**  
- **Python 3.10+**  
- **PyQt5** (Modern GUI)  
- **aiohttp** (Async HTTP requests)  
- **SQLAlchemy** (Database)  
- **Pydantic** (Data validation)  

### **Project Structure**  
```text
/pokemon-tcg-monitor
├── config/            # Product/proxy configs
├── data/              # SQLite database
├── src/               # Source code
│   ├── gui/           # Graphical interface
│   ├── models/        # Data structures
│   ├── scraper/       # Web scrapers
│   └── utils/         # Utilities (logging, alerts)
└── README.md
```

---

## **💡 Why This Project?**  

Pokémon TCG scalping has made it nearly impossible for fans to buy products at fair prices. This tool:  

🔹 **Empowers users** by providing real-time price tracking.  
🔹 **Exposes scalping tactics** through transparent monitoring.  
🔹 **Pressures retailers** to implement better anti-bot measures.  

---

## **🛡️ Ethics & Fair Use**  

⚠ **This tool is for educational and fair-use purposes only.**  
- Do **not** use it to scalp products.  
- Respect retailers' terms of service.  

---

## **📈 Future Roadmap**  
- [ ] Add more retailers (Amazon, Pokémon Center).  
- [ ] Price trend visualization.  
- [ ] Mobile app notifications.  

---

## **🤝 Contribute**  
Found a bug? Want to improve the tool?  
1. Fork the repository.  
2. Submit a pull request!  

---

**Happy hunting, trainers!** 🎮⚡
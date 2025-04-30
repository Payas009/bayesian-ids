# bayesian-ids
# bayesian-ids
**Early-warning intrusion-detection using Bayesian Networks**

## 🧠 Overview
This project demonstrates a probabilistic intrusion detection model using Bayesian Networks to assess the likelihood of cyber breaches based on weak indicators, such as:
- Access during off-hours
- Short-duration flows
- Suspicious port access
- Low byte–high packet traffic

## 📊 Dataset
- **CICIDS-2017** from the Canadian Institute for Cybersecurity.
- Used `Friday-WorkingHours-Afternoon-DDoS.pcap_ISCX.csv`.

## 🛠️ Features Engineered
- `Is_Off_Hours`
- `Short_Duration`
- `Low_Byte_High_Packet`
- `Suspicious_Port`
- Target label: `BreachWithin24h`

## 🔧 Tech Stack
- Python
- pgmpy
- pandas
- networkx
- matplotlib (optional)

## 🧪 How to Run
```bash
cd src/
python train_bn.py

# SDN Packet Drop Simulator
**Student: Mohammed Shahid Javed Mokashi**
**SRN: PES1UG24AM378**

## Problem Statement
Simulate selective packet dropping using SDN 
flow rules via OpenFlow and POX controller in Mininet.

## Topology
h1 (10.0.0.1) ─┐
h2 (10.0.0.2) ──── s1 ──── POX Controller
h3 (10.0.0.3) ─┘

DROP RULE: h1 → h3 is BLOCKED

## Setup & Execution

### 1. Start POX controller:
cd ~/pox
python3 pox.py log.level --DEBUG openflow.of_01 drop_controller

### 2. Start Mininet topology:
cd ~/PES1UG24AM378
sudo python3 topology.py

### 3. Run tests inside Mininet:
h1 ping h2 -c 5   # Should succeed (0% loss)
h1 ping h3 -c 5   # Should be dropped (100% loss)

### 4. Check flow table:
sh ovs-ofctl dump-flows s1

### 5. Regression test:
sudo python3 regression_test.py

## Expected Output
- h1 → h2: 0% packet loss ✅
- h1 → h3: 100% packet loss ✅
- Flow table shows drop rule with priority=100 ✅
- iperf h1→h2: ~56 Mbits/sec ✅
- iperf h1→h3: Connection timeout ✅

## Tools Used
- Mininet
- POX Controller
- OpenFlow 1.0
- tcpdump
- iperf
  ScreenShots Proof:
  <img width="942" height="284" alt="Screenshot 2026-04-13 101259" src="https://github.com/user-attachments/assets/d3dc9a6b-6be8-41db-8bf9-b11f4049431c" />
  <img width="905" height="138" alt="Screenshot 2026-04-13 101357" src="https://github.com/user-attachments/assets/8e8409bd-2d39-40d0-833e-1b9ea496a59c" />
<img width="486" height="142" alt="Screenshot 2026-04-13 101452" src="https://github.com/user-attachments/assets/ad9144c9-5a2c-4b2e-a422-b36867e531cb" />
<img width="1802" height="187" alt="Screenshot 2026-04-13 101902" src="https://github.com/user-attachments/assets/b3d63418-4e4b-42f5-be93-6ee3d9967c2c" />
<img width="1155" height="341" alt="Screenshot 2026-04-13 105906" src="https://github.com/user-attachments/assets/6aaf47fa-66bd-443f-8924-af61f4ad47e8" />
<img width="1500" height="68" alt="Screenshot 2026-04-13 105951" src="https://github.com/user-attachments/assets/72ffecb8-4957-42c7-897e-b1b6b893db82" />
<img width="1708" height="584" alt="Screenshot 2026-04-13 110231" src="https://github.com/user-attachments/assets/e4c33ab0-8187-435f-88c4-4a63cc2d0b5d" />
<img width="835" height="142" alt="Screenshot 2026-04-13 110719" src="https://github.com/user-attachments/assets/be31ffd2-5864-4929-a2ed-5c343b1c3efd" />
<img width="985" height="136" alt="Screenshot 2026-04-13 110946" src="https://github.com/user-attachments/assets/1926903f-8ff0-4be3-8c32-89040fb9b080" />
<img width="1148" height="210" alt="Screenshot 2026-04-13 111051" src="https://github.com/user-attachments/assets/8fcfbc00-9739-4aca-abfa-c644d882f5a7" />
<img width="1165" height="436" alt="Screenshot 2026-04-13 111541" src="https://github.com/user-attachments/assets/5678c98a-2b71-41a2-b85e-e3bd6efdad97" />
<img width="277" height="48" alt="Screenshot 2026-04-13 111626" src="https://github.com/user-attachments/assets/a1f328c2-f906-4f1d-80f0-6bc131b1e0d0" />
<img width="941" height="154" alt="Screenshot 2026-04-13 111842" src="https://github.com/user-attachments/assets/d612d812-5d04-41ad-86e7-be37e86cb2c6" />


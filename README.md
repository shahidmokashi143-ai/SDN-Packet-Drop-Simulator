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

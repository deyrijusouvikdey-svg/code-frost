"""
AUTONOMOUS SECURITY THREAT INTELLIGENCE (ASTI)
Advanced Single-File Python Project
No external libraries required
Author: Souvik Dey
"""

import random
import time
import statistics
import json
from datetime import datetime

# =====================================================
# THREAT INTELLIGENCE ENGINE
# =====================================================

class ThreatIntelligenceEngine:
    def __init__(self):
        self.baseline_requests = []
        self.baseline_failures = []
        self.blocked_ips = set()
        self.logs = []

    # ---------------------------
    # BASELINE LEARNING (AI-LIKE)
    # ---------------------------
    def learn_baseline(self, iterations=50):
        for _ in range(iterations):
            self.baseline_requests.append(random.randint(20, 300))
            self.baseline_failures.append(random.randint(0, 5))

    # ---------------------------
    # THREAT SCORING (STATISTICS)
    # ---------------------------
    def calculate_risk(self, log):
        req_mean = statistics.mean(self.baseline_requests)
        fail_mean = statistics.mean(self.baseline_failures)

        req_std = statistics.stdev(self.baseline_requests)
        fail_std = statistics.stdev(self.baseline_failures)

        req_score = (log["requests"] - req_mean) / (req_std + 1)
        fail_score = (log["failed_logins"] - fail_mean) / (fail_std + 1)

        risk_score = abs(req_score * 35) + abs(fail_score * 65)
        return round(min(risk_score, 100), 2)

    # ---------------------------
    # THREAT CLASSIFICATION
    # ---------------------------
    def classify_threat(self, risk_score):
        if risk_score > 80:
            return "CRITICAL"
        elif risk_score > 60:
            return "HIGH"
        elif risk_score > 30:
            return "MEDIUM"
        return "LOW"

    # ---------------------------
    # AUTONOMOUS RESPONSE
    # ---------------------------
    def autonomous_action(self, ip, level):
        if level == "CRITICAL":
            self.blocked_ips.add(ip)
            return f"IP {ip} BLOCKED automatically"
        elif level == "HIGH":
            return f"IP {ip} flagged for monitoring"
        return "No action required"

    # ---------------------------
    # LOG STORAGE
    # ---------------------------
    def store_log(self, log, risk, level, action):
        self.logs.append({
            "timestamp": datetime.now().isoformat(),
            "log": log,
            "risk_score": risk,
            "threat_level": level,
            "action": action
        })


# =====================================================
# LOG GENERATION (SIMULATED DATA)
# =====================================================

def generate_log():
    return {
        "ip": f"192.168.1.{random.randint(1,255)}",
        "requests": random.randint(10, 1000),
        "failed_logins": random.randint(0, 80),
        "country": random.choice(["IN", "US", "CN", "RU", "BR"])
    }


# =====================================================
# ATTACK SIMULATION
# =====================================================

def simulate_attack():
    return {
        "ip": "10.0.0.99",
        "requests": 950,
        "failed_logins": 75,
        "country": "RU"
    }


# =====================================================
# SYSTEM RUNNER
# =====================================================

def run_system():
    engine = ThreatIntelligenceEngine()
    engine.learn_baseline()

    print("\n🔐 Autonomous Security Threat Intelligence System Started")
    print("-" * 60)

    for i in range(5):
        log = generate_log()
        risk = engine.calculate_risk(log)
        level = engine.classify_threat(risk)
        action = engine.autonomous_action(log["ip"], level)
        engine.store_log(log, risk, level, action)

        print(f"\nEvent {i+1}")
        print("IP:", log["ip"])
        print("Requests:", log["requests"])
        print("Failed Logins:", log["failed_logins"])
        print("Risk Score:", risk)
        print("Threat Level:", level)
        print("Action:", action)

        time.sleep(1)

    print("\n🚨 Simulating real attack...")
    attack = simulate_attack()
    risk = engine.calculate_risk(attack)
    level = engine.classify_threat(risk)
    action = engine.autonomous_action(attack["ip"], level)
    engine.store_log(attack, risk, level, action)

    print("\nATTACK DETECTED")
    print("IP:", attack["ip"])
    print("Risk Score:", risk)
    print("Threat Level:", level)
    print("Autonomous Action:", action)

    # Save logs
    with open("asti_logs.json", "w") as f:
        json.dump(engine.logs, f, indent=4)

    print("\n📁 Logs saved to asti_logs.json")
    print("✅ System execution completed successfully")


# =====================================================
# ENTRY POINT
# =====================================================

if __name__ == "__main__":
    run_system()
c

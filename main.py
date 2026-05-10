import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.email_sender import send_email
from src.logger import setup_logger
import os

# ----------------------------
# SETUP
# ----------------------------
logger = setup_logger()

sns.set_theme(style="darkgrid")  # ⭐ PROFESSIONAL LOOK

df = pd.read_csv("data/contacts.csv")

success = 0
failed = 0
status_list = []

os.makedirs("images", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# ----------------------------
# EMAIL PROCESSING
# ----------------------------
for _, row in df.iterrows():
    name = row["name"]
    email = row["email"]

    message = f"Hello {name}, automated reminder system notification."

    status = send_email(email, "Reminder Alert", message)
    status_list.append(status)

    if "SUCCESS" in status:
        success += 1
        logger.info(f"Sent: {email}")
    else:
        failed += 1
        logger.error(f"Failed: {email}")

print("EMAIL PROCESS COMPLETED")

# =====================================================
# 📊 1. KPI DASHBOARD (VERY IMPRESSIVE)
# =====================================================
plt.figure(figsize=(8,5))
plt.bar(["Total", "Success", "Failed"],
        [len(df), success, failed],
        color=["blue", "green", "red"])

plt.title("📊 Email Automation KPI Dashboard", fontsize=14)
plt.ylabel("Count")

plt.savefig("images/1_kpi_dashboard.png")
plt.close()

# =====================================================
# 📊 2. PIE CHART (BEAUTIFUL)
# =====================================================
plt.figure(figsize=(6,6))
plt.pie(
    [success, failed],
    labels=["Success", "Failed"],
    autopct="%1.1f%%",
    colors=["#2ecc71", "#e74c3c"],
    startangle=90
)

plt.title("📧 Email Success Ratio")
plt.savefig("images/2_email_pie.png")
plt.close()

# =====================================================
# 📊 3. CONTACT ACTIVITY (VISUAL GRID STYLE)
# =====================================================
plt.figure(figsize=(10,5))
sns.barplot(x=df["name"], y=[1]*len(df), palette="coolwarm")

plt.title("👥 Contact Activity Overview")
plt.xlabel("Contacts")
plt.ylabel("Activity")

plt.xticks(rotation=45)
plt.savefig("images/3_contact_activity.png")
plt.close()

# =====================================================
# 📊 4. EMAIL FLOW TIMELINE (PROFESSIONAL LOOK)
# =====================================================
plt.figure(figsize=(8,4))
sns.lineplot(x=range(len(status_list)), y=[1 if "SUCCESS" in s else 0 for s in status_list])

plt.title("📈 Email Execution Timeline")
plt.ylabel("Status (1=Success, 0=Fail)")
plt.xlabel("Execution Order")

plt.savefig("images/4_execution_timeline.png")
plt.close()

# =====================================================
# CSV REPORT
# =====================================================
df["status"] = status_list
df.to_csv("outputs/report.csv", index=False)

print("📸 4 HIGH-QUALITY IMAGES GENERATED in images/")
print("📄 REPORT GENERATED in outputs/")
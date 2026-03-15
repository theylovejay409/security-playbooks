# Architecture Overview

The **Cyber Threat Playbook** is structured to provide a clear, modular, and professional layout for cybersecurity research, lab simulations. The architecture is designed for educational, hands-on use while maintaining real-world workflow relevance.

## Repository Structure

```
cyber-threat-playbook/
├─ detection-rules/    # Sigma, YARA, Suricata rules for threat detection
├─ scenarios/          # MITRE ATT&CK-based attack simulations
├─ labs/               # PoC scripts and lab walkthroughs
├─ examples/           # Sample outputs, logs, and screenshots
├─ docs/               # Documentation and guides
└─ tools/              # Helper scripts and parsers
```

## Key Components

### 1. Detection Rules

- **Purpose:** Identify suspicious activities and simulate detection in lab environments.
- **Formats:** Sigma, YARA, and Suricata.
- **Use Case:** Threat hunting, SIEM integration, or educational analysis.

### 2. Scenarios

- **Purpose:** Provide realistic attack simulations based on MITRE ATT&CK.
- **Examples:** Phishing campaigns, malware propagation, lateral movement.
- **Use Case:** Red/Blue team exercises, understanding attacker tactics.

### 3. Labs

- **Purpose:** Hands-on exercises with scripts and walkthroughs.
- **Languages:** Python primarily, with optional Bash or PowerShell scripts.
- **Use Case:** Practice detection, incident response, or research in isolated environments.

### 4. Examples

- **Purpose:** Visualize outputs of detection rules and scenario executions.
- **Contents:** Screenshots, log extracts, and sample alerts.

### 5. Docs

- **Purpose:** Provide Quick Start guides, architecture overview, and usage instructions.
- **File Example:** [architecture.md](docs/architecture.md), [quick_start.md](docs/quick_start.md).

### 6. Tools

- **Purpose:** Helper scripts to parse, validate, or simulate scenarios (e.g., Sigma parser).

## Design Principles

1. **Modularity:** Each component is independent and reusable.  
2. **Educational Focus:** Scripts and scenarios are safe to run in isolated labs.  
3. **Realistic Simulations:** Scenarios mimic real-world attacks without targeting production systems.  
4. **Extensible:** Users can add new rules, scenarios, or labs easily.

## Recommended Usage

1. Start with [quick_start.md](docs/quick_start.md) to set up your lab environment.  
2. Explore detection rules in [detection-rules/](detection-rules/).  
3. Run scenarios in [scenarios/](scenarios/) with labs as guided exercises.  
4. Reference [examples/](examples/) to validate your results.  
5. Extend repository content with new scripts or detection rules as needed.

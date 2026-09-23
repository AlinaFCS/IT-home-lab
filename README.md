# IT-home-lab

Hands-on practice repository covering both IT support/systems administration and
blue-team security fundamentals — built while preparing for entry-level IT and security
roles. Everything here is a real lab I built and broke on purpose, not a tutorial I
copied.

## IT Support & Systems Administration

- **[active-directory-lab](active-directory-lab)** — Windows Server 2022 domain
  controller built from scratch in VirtualBox: AD DS setup, OUs, security groups, a
  Windows 11 client joined to the domain, and a first Group Policy.
- **[troubleshooting-tickets](troubleshooting-tickets)** — three help-desk style tickets
  worked from symptom to root cause on the lab above: an expired account, a broken DNS
  setting, and a GPO applying somewhere it shouldn't.
- **[powershell-automation](powershell-automation)** — bulk-creating AD users from a CSV
  with a PowerShell script instead of the ADUC wizard, including the debugging that came
  with it.
- **[python-network-check](python-network-check)** — a small Python script that pings a
  list of hosts and reports which are up, plus everything that went wrong getting Python
  and a working script onto the domain controller in the first place.
- **[google-workspace-helpdesk](google-workspace-helpdesk)** — a ticketing system built
  from Google Forms, Sheets and Drive: request intake, a status-tracked ticket queue, a
  live dashboard, and sharing permissions set by least privilege.

## Security / SOC

- **[phishing](phishing)** — phishing email analysis: headers, IOC extraction,
  verdicts.
- **[incident-reports](incident-reports)** — write-ups on investigating security
  events.
- **[snort](snort)** — intrusion detection basics.
- **[splunk](splunk)** — SIEM-style alert investigation.
- **[wireshark](wireshark)** — packet capture analysis.

## Tools & Technologies

Windows Server 2022, Active Directory, Group Policy, PowerShell, Python, VirtualBox, Google Workspace (Forms, Sheets, Drive) ·
CyberChef, VirusTotal, AbuseIPDB, Snort, Splunk, Wireshark, TryHackMe (Blue Team paths)

## Disclaimer

All data in this repository is either anonymized, publicly available, self-generated in
a lab environment, or synthetic test data created for practice. No real personal or
sensitive data is intentionally exposed.

## About

Working toward an entry-level IT/security role — right now focused on systems
administration fundamentals (Windows Server, AD, networking, scripting) alongside blue
team basics (phishing analysis, log investigation, SIEM tooling).

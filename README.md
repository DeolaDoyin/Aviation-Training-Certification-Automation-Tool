# Aviation Training & Certification Automation Tool

## Project Overview
Compliance with international aviation frameworks requires strict monitoring of personnel qualifications. Developed for the DAAS and HR divisions at the NCAA, this system automates the tracking of mandatory ICAO-compliant staff certification renewals, replacing manual cross-checking methods.

## Features
- **Relational Database Backend:** Built with SQLite3 to maintain structured records of personnel, certification types, and issuance dates.
- **Time-Delta Calculation Logic:** Uses Python's `datetime` and `timedelta` to automatically calculate the exact remaining days before a certificate expires.
- **Conditional Status Flags:** Programmed to apply color-coded visibility flags:
  - **Yellow:** Active certifications expiring within 30 days.
  - **Red:** Expired certifications requiring immediate renewal tracking.

## Tech Stack
- **Language:** Python 3.x
- **Database Engine:** SQLite3
- **Core Modules:** datetime

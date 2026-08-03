# M.I.W

> A lightweight, dedicated Slack bot designed for hardware engineers, makers, and robotics teams to eliminate context-switching during build sessions.

---

## M.I.W

**M.I.W** brings micro-controller specifications, quotes, and bot diagnostics directly inside your Slack workspace. Instead of opening multiple browser tabs to look up board details or double-check component specs while coding, team members can query technical data instantly using native Slack slash commands.

---

## Features & Slash Commands

| Command | Description | Example Usage |
| :--- | :--- | :--- |
| `/miw-wiki` | Queries the Wikipedia REST API to fetch hardware summaries and specs instantly in-chat. | `/miw-wiki ESP32` |
| `/miw-random` | Pulls a random tech thought or hardware-related insight to keep team morale high. | `/miw-random` |
| `/miw-status` | Performs a real-time system diagnostic check displaying runtime environment details. | `/miw-status` |

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.14.3
* **Framework:** `slack_bolt` (Slack Socket Mode)
* **API Integration:** REST / HTTP requests (`requests`, `aiohttp`)
* **Cloud Hosting:** Render (24/7 Web Service)
* **Version Control:** Git & GitHub

---

## 🚀 Local Setup & Installation

To run this project locally for development or testing:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/danielmcneto/MIWbot.git](https://github.com/danielmcneto/MIWbot.git)
   cd MIWbot

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   
3. **Configure Environment Variables:**
   Create a .env file in the root directory and add your Slack API credentials:
   ```bash
   SLACK_BOT_TOKEN=xoxb-your-bot-token
   SLACK_APP_TOKEN=xapp-your-app-token

4. **Launch the bot:**
   ```bash
   python slacker.py

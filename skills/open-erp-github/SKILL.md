---
name: open-erp-github
description: Start and open the user's local ERPNext Docker practice project when they say "打开erp", "打开 ERP", "启动erp", "打开ERPNext", or similar Chinese requests. Use this skill to check Docker, open Docker Desktop if needed, run Docker Compose in D:\erpnext-practice\frappe_docker, check ERPNext container status, and open http://localhost:8080.
---

# Open ERPNext Local

Use this skill when the user asks to open or start ERP/ERPNext.

## Workflow

1. Check Docker availability first:
   - Run a Docker status/version check such as `docker version` or `docker info`.
   - If Docker CLI is missing, tell the user Docker is not installed or not in PATH.
   - If Docker is installed but the engine is not running, open Docker Desktop and wait briefly for it to start.
2. Go to the ERPNext Docker project folder:
   - `D:\erpnext-practice\frappe_docker`
   - If the folder does not exist, tell the user clearly and stop.
3. Start ERPNext with Docker Compose:
   - Run `docker compose -f pwd.yml up -d` from `D:\erpnext-practice\frappe_docker`.
   - If this requires user permission or Docker Desktop confirmation, tell the user what to approve.
4. Check container status:
   - Run `docker compose -f pwd.yml ps` from the same folder.
   - Summarize which containers are running, starting, unhealthy, or exited.
5. Open ERPNext in the browser:
   - Open `http://localhost:8080`.
6. Tell the user the final state:
   - Whether Docker is running.
   - Whether Compose was started successfully.
   - Whether the ERPNext containers look healthy/running.
   - The URL opened: `http://localhost:8080`.

## Rules

- Do not delete containers, images, volumes, or project files.
- Do not run `docker compose down`, prune, reset, clean, remove, or delete commands unless the user explicitly asks and confirms.
- Do not modify ERPNext configuration files unless the user explicitly asks.
- Do not expose secrets, passwords, tokens, or database credentials if they appear in output.
- Prefer concise beginner-friendly explanations.
- If the browser page fails to load, explain that ERPNext may still be starting and suggest waiting 1-3 minutes before refreshing.

## Commands

Use these commands as the default sequence when appropriate:

```powershell
docker info
Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
Set-Location "D:\erpnext-practice\frappe_docker"
docker compose -f pwd.yml up -d
docker compose -f pwd.yml ps
Start-Process "http://localhost:8080"
```

Only run the Docker Desktop open command if Docker is not already running.
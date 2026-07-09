---
name: close-erpnext
description: Safely stop the user's local Docker ERPNext system and then close Docker Desktop background processes when they say "关闭 ERPNext", "关闭ERP系统", "停止 ERPNext", "停止本地ERP", or similar Chinese requests. Use this skill to check Docker, run `docker compose -f pwd.yml down` in D:\erpnext-practice\frappe_docker, verify container status, close Docker Desktop after ERPNext stops, and confirm data was not deleted.
---

# 关闭 ERPNext

Use this skill when the user asks to safely stop the local Docker version of ERPNext, close Docker Desktop background processes, and release computer memory without deleting ERPNext data.

## ERPNext Path

`D:\erpnext-practice\frappe_docker`

## Workflow

1. Check whether Docker Desktop / Docker Engine is running.
2. If Docker is not running, tell the user ERPNext may already be closed and stop the workflow.
3. If Docker is running, verify the ERPNext project directory exists:
   - `D:\erpnext-practice\frappe_docker`
4. Enter the ERPNext project directory.
5. Run this safe shutdown command only:
   - `docker compose -f pwd.yml down`
6. After shutdown, check container status:
   - `docker compose -f pwd.yml ps`
7. Close Docker Desktop background processes after ERPNext containers are stopped:
   - Prefer closing Docker Desktop gracefully if possible.
   - If needed, stop only Docker Desktop user processes such as `Docker Desktop` and `com.docker.backend`.
   - Do not stop Windows system services unless the user explicitly asks and confirms.
   - Do not run `wsl --shutdown` unless the user explicitly asks and confirms, because it may affect other WSL work.
8. Tell the user ERPNext has stopped, Docker Desktop background has been closed if possible, and data was not deleted.

## Safety Rules

- Do not delete ERPNext data.
- Never run `docker compose -f pwd.yml down -v`.
- Never delete Docker volumes.
- Never delete `D:\erpnext-practice\frappe_docker`.
- Do not run Docker prune, remove, reset, clean, or volume deletion commands.
- Do not stop Windows services automatically.
- Do not run `wsl --shutdown` automatically.
- Do not modify ERPNext configuration files.
- Do not expose secrets, passwords, tokens, or database credentials if they appear in output.
- Keep explanations beginner-friendly and concise.

## Approved PowerShell Flow

Use this exact flow as the model for execution:

```powershell
$erpPath = "D:\erpnext-practice\frappe_docker"

Write-Host "正在检查 Docker 是否运行..."

try {
    docker info | Out-Null
    Write-Host "Docker 正在运行。"
} catch {
    Write-Host "Docker 没有运行，ERPNext 可能已经关闭。"
    exit
}

if (!(Test-Path $erpPath)) {
    Write-Host "ERPNext 项目目录不存在：$erpPath"
    exit
}

Set-Location $erpPath

Write-Host "正在关闭 ERPNext..."
docker compose -f pwd.yml down

Write-Host "正在检查 ERPNext 容器状态..."
docker compose -f pwd.yml ps

Write-Host "正在关闭 Docker Desktop 后台..."
Get-Process -Name "Docker Desktop","com.docker.backend" -ErrorAction SilentlyContinue | Stop-Process -Force

Write-Host "ERPNext 已关闭。"
Write-Host "Docker Desktop 后台已尝试关闭。"
Write-Host "注意：本次只停止容器，没有删除数据。"
```

## Response

After completion, report:

- Whether Docker was running.
- Whether ERPNext was stopped successfully.
- The result of the container status check.
- Whether Docker Desktop background processes were closed.
- Confirm: "本次只停止容器，没有删除数据。"

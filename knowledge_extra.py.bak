"""knowledge_extra.py - more topics for CYBROETHICGRAM AI.
Networking, DNS, defensive/ethical cybersecurity, Linux, other languages,
and ready-to-run Python example programs.
main.py loads it with:  python_knowledge.KNOWLEDGE.extend(EXTRA)
"""
from textwrap import dedent

CREATOR = "Mohammad Hamza Aadi"


def E(keywords, text):
    return (keywords, dedent(text).strip("\n"))


EXTRA = [
    # ------------------------------------------------------------ GENERAL
    E(["hi", "hello", "hey", "hii"], r"""
        Hello! I'm CYBROETHICGRAM AI, your
        student assistant for programming
        and ethical cybersecurity.
        Type 'help' to see what to ask.
    """),

    E(["developer", "creator", "owner", "who made you", "who created you",
       "your developer", "made you", "built you"],
      "I was created by " + CREATOR + " as a student learning project: "
      "CYBROETHICGRAM AI - Learn. Build. Secure. Create."),

    E(["who are you", "what can you do", "your name"], r"""
        I'm CYBROETHICGRAM AI. I teach:
        - Python and other languages
        - Example programs (ask: programs)
        - Networking, DNS, ports, HTTP
        - Cybersecurity and ethical hacking
          (legal, defensive, authorized)
        - Linux and Termux basics
        Ask: what is dns / first code /
        ethical hacking / linux commands
    """),

    # --------------------------------------------------------- NETWORKING
    E(["networking", "network", "networks", "computer network"], r"""
        Networking is how devices connect and share data.
        Parts: devices, media (WiFi/cable), hardware (router, switch, modem) and rules called protocols (IP, TCP, HTTP, DNS).
        Types:
        - LAN: home/school network
        - WAN: large area; the Internet is the biggest WAN
        Ask me: ip address, dns, ports, osi model, tcp vs udp, http, firewall.
    """),

    E(["ip address", "ip", "ip addresses", "ipv4", "ipv6"], r"""
        An IP address identifies a device on a network.
        IPv4: four numbers 0-255, like 192.168.1.5
        IPv6: longer, like 2001:db8::1
        Private ranges (inside LANs): 10.x.x.x, 172.16-31.x.x, 192.168.x.x
        127.0.0.1 = localhost (your own device).
        See yours in Termux:
          pkg install net-tools
          ifconfig
    """),

    E(["dns", "domain name system", "domain name"], r"""
        DNS (Domain Name System) is the internet's phonebook. It turns names like google.com into IP addresses so computers can connect.
        How it works:
        1. You type a website name
        2. Your device asks a DNS resolver (ISP, or public like 8.8.8.8 or 1.1.1.1)
        3. The resolver asks root, then the TLD (.com), then the domain's nameserver
        4. The IP comes back and is cached for a while (TTL)
        Try in Python:
          import socket
          print(socket.gethostbyname('example.com'))
        Or in Termux:
          pkg install dnsutils
          nslookup example.com
    """),

    E(["dns record", "dns records", "record types", "mx record", "a record",
       "cname"], r"""
        Common DNS records:
        - A: name -> IPv4 address
        - AAAA: name -> IPv6 address
        - CNAME: alias to another name
        - MX: mail servers for the domain
        - NS: the domain's nameservers
        - TXT: free text (email security, verification)
        - PTR: IP -> name (reverse lookup)
        TTL = how long an answer may be cached.
        Check one:  dig example.com MX
    """),

    E(["dns security", "dns spoofing", "dns poisoning", "dnssec",
       "dns attack", "cache poisoning"], r"""
        DNS was designed without much security.
        Risks: spoofing / cache poisoning (fake answers send you to a wrong site), and hijacked DNS settings on routers.
        Defenses:
        - DNSSEC: signs DNS answers
        - DoH / DoT: encrypt DNS queries
        - Use trusted resolvers
        - Change default router passwords
        - Always check HTTPS and the padlock
    """),

    E(["dhcp"], r"""
        DHCP automatically gives devices an IP address, gateway and DNS server when they join a network. Your router usually runs it.
    """),

    E(["mac address", "mac"], r"""
        A MAC address is a hardware ID of a network card, like AA:BB:CC:11:22:33. It works inside the local network (layer 2), while IP addresses work across networks.
    """),

    E(["router", "switch", "modem", "hub", "gateway", "access point"], r"""
        - Modem: connects you to the ISP
        - Router: connects networks and forwards traffic between them (your home gateway)
        - Switch: connects devices inside a LAN using MAC addresses
        - Hub: old, repeats data to all ports
        - Access point: gives WiFi
    """),

    E(["osi model", "osi", "layers", "network layers"], r"""
        OSI model, 7 layers (top to bottom):
        7 Application (HTTP, DNS)
        6 Presentation (encryption, format)
        5 Session
        4 Transport (TCP, UDP)
        3 Network (IP, routers)
        2 Data Link (MAC, switches)
        1 Physical (cables, radio)
        Memory trick: All People Seem To Need Data Processing.
    """),

    E(["tcp ip", "tcp/ip", "tcp ip model"], r"""
        TCP/IP model has 4 layers: Application (HTTP, DNS), Transport (TCP, UDP), Internet (IP), Network Access (WiFi, Ethernet). It is the model the real Internet uses.
    """),

    E(["tcp", "udp", "tcp vs udp", "difference between tcp and udp"], r"""
        TCP: reliable, ordered, connection-based (3-way handshake). Used for web, email, file transfer.
        UDP: fast, no guarantees, no handshake. Used for video calls, games, DNS queries.
    """),

    E(["port", "ports", "port number", "port numbers"], r"""
        A port number picks the service on a device (0-65535).
        Common ports:
        20/21 FTP
        22 SSH
        23 Telnet (insecure)
        25 SMTP (mail)
        53 DNS
        80 HTTP
        110 POP3
        143 IMAP
        443 HTTPS
        3306 MySQL
        3389 RDP
        Close ports you don't use.
    """),

    E(["https", "tls", "ssl", "certificate", "padlock"], r"""
        HTTPS = HTTP + TLS encryption. TLS (successor of SSL) encrypts data and proves the site's identity with a certificate.
        The padlock means the connection is encrypted, not that the site is trustworthy. Phishing sites can have it too.
    """),

    E(["http", "web", "how the web works", "url"], r"""
        HTTP is the language browsers and servers use.
        Request methods: GET (read), POST (send), PUT (update), DELETE (remove).
        URL parts:
          https://example.com:443/page?x=1
        scheme://host:port/path?query
        Browser flow: DNS lookup -> connect (TCP/TLS) -> send request -> get response -> render page.
    """),

    E(["status code", "status codes", "http status", "404", "200", "500"], r"""
        HTTP status codes:
        2xx success (200 OK)
        3xx redirect (301 moved)
        4xx client error (403 forbidden, 404 not found)
        5xx server error (500 internal error)
    """),

    E(["subnet", "subnetting", "cidr", "subnet mask"], r"""
        A subnet splits a network into smaller parts. CIDR writes the mask as a number:
        /24 = 255.255.255.0 = 254 hosts
        /16 = 255.255.0.0 = 65534 hosts
        Python:
          import ipaddress
          n = ipaddress.ip_network('192.168.1.0/24')
          print(n.num_addresses)  # 256
    """),

    E(["nat", "network address translation"], r"""
        NAT lets many devices in a home network share one public IP. Your router rewrites addresses for outgoing and incoming traffic. It also hides private devices from the Internet by default.
    """),

    E(["vpn", "proxy", "tor"], r"""
        VPN: encrypts your traffic and sends it through another server. Useful on public WiFi. It does not make you anonymous or immune to malware.
        Proxy: a middleman server for web requests.
        Tor: routes traffic through several relays for privacy.
    """),

    E(["firewall"], r"""
        A firewall filters traffic using rules (allow/block by IP, port, protocol). It can be software (on your device) or hardware (on the network edge). It is a core defensive layer.
    """),

    E(["ping", "traceroute", "netstat", "nslookup", "dig", "curl",
       "network commands", "network tools"], r"""
        Handy network commands:
        - ping example.com: is a host reachable?
        - traceroute example.com: path of hops
        - nslookup / dig: DNS queries
        - curl https://example.com: fetch a page
        - ifconfig / ip addr: your IPs
        - netstat / ss: connections and ports
        Termux: pkg install dnsutils net-tools
    """),

    E(["nmap", "port scan", "port scanning", "scanner"], r"""
        Nmap is a network mapper: it finds devices and open ports so defenders can see what is exposed.
        Only scan your own devices/network or targets that gave you written permission. Scanning others can be illegal.
        Safe practice on yourself:
          nmap 127.0.0.1
    """),

    E(["wireshark", "packet", "packets", "sniffing"], r"""
        Wireshark is a packet analyzer. It shows the traffic on your own network so you can learn protocols and troubleshoot. Only capture traffic on networks you own or are authorized to test.
    """),

    E(["wifi", "wi-fi", "wpa2", "wpa3", "wifi security"], r"""
        Secure your WiFi:
        - Use WPA3 (or WPA2) with a long passphrase
        - Change the router's admin password
        - Disable WPS
        - Keep router firmware updated
        - Use a guest network for visitors
        Avoid WEP; it is broken.
    """),

    E(["localhost", "loopback", "127.0.0.1"], r"""
        localhost (127.0.0.1) always means "this same device". It is the safe place to practise networking code and run test servers.
    """),

    E(["bandwidth", "latency", "speed", "bitrate"], r"""
        Bandwidth = how much data per second can flow (Mbps).
        Latency = delay for data to travel (ms), measured with ping.
        Low latency matters for games and calls; high bandwidth for downloads.
    """),

    # ------------------------------------------------------ CYBERSECURITY
    E(["cybersecurity", "cyber security", "security", "cia triad"], r"""
        Cybersecurity protects systems, networks and data.
        CIA triad:
        - Confidentiality: only the right people see data
        - Integrity: data is not secretly changed
        - Availability: systems work when needed
        Defense in depth = many layers (updates, firewall, strong passwords, backups, training).
    """),

    E(["learn ethical hacking", "how to learn ethical hacking",
       "learn hacking", "learn cybersecurity", "learn cyber security",
       "start ethical hacking", "start hacking", "become ethical hacker",
       "become a hacker", "become an ethical hacker", "become hacker", "ethical hacking roadmap",
       "cybersecurity roadmap", "roadmap"], r"""
        How to learn ethical hacking (step by step):
        1. Computer basics: how OS, files and processes work
        2. Networking: IP, DNS, ports, TCP/UDP, HTTP (ask: networking)
        3. Linux and the terminal (ask: linux commands)
        4. Programming: Python first, then C basics
        5. Security basics: CIA triad, passwords, phishing, encryption
        6. Web security: OWASP Top 10 concepts
        7. Practise ONLY in legal labs (ask: legal labs)
        8. Certificates: Security+, eJPT (ask: certification)
        Rule: always get written permission before testing any system.
    """),

    E(["ethical hacking", "ethical hacker", "pentest", "penetration testing",
       "white hat", "hacking"], r"""
        Ethical hacking = testing systems with written permission to find weaknesses before criminals do.
        Types: white hat (authorized), black hat (criminal), grey hat (unauthorized but no bad intent, still illegal).
        Typical authorized phases:
        1. Scope and permission
        2. Information gathering
        3. Scanning/analysis
        4. Testing weaknesses
        5. Report and fix advice
        Never test systems without permission. It is illegal almost everywhere (for example India's IT Act and the US CFAA). Practise in legal labs.
    """),

    E(["legal labs", "practice labs", "labs", "ctf", "tryhackme",
       "hack the box", "dvwa", "juice shop", "where to practice"], r"""
        Legal places to practise:
        - TryHackMe (guided beginner rooms)
        - OverTheWire (Linux wargames)
        - picoCTF (student CTF)
        - OWASP Juice Shop (vulnerable web app you run yourself)
        - DVWA (vulnerable web app for your own lab)
        - Hack The Box
        - VirtualBox home lab with your own VMs
        Learn Linux, networking and Python first.
    """),

    E(["certification", "certifications", "ceh", "security+", "oscp",
       "ejpt", "career"], r"""
        Security career path:
        - Start: networking, Linux, Python
        - Entry certs: CompTIA Security+, Network+, eJPT
        - Later: CEH, OSCP, CISSP
        Roles: SOC analyst, penetration tester, security engineer, incident responder.
    """),

    E(["malware", "virus", "worm", "trojan", "ransomware", "spyware"], r"""
        Malware types (defender view):
        - Virus: attaches to files, spreads when run
        - Worm: spreads by itself over networks
        - Trojan: looks useful but is harmful
        - Ransomware: locks files and demands payment
        - Spyware: secretly collects information
        Defense: updates, antivirus, backups, no pirated or unknown apps, don't click unknown links.
    """),

    E(["phishing", "social engineering", "scam", "scams"], r"""
        Phishing tricks people into giving passwords or money, usually with fake emails, SMS or sites. Social engineering = manipulating people instead of machines.
        Spot it: urgency, odd sender address, mismatched links, requests for OTP/passwords.
        Defense: don't click, check the real address, use 2-factor authentication, report it.
    """),

    E(["password", "passwords", "2fa", "mfa", "two factor",
       "two-factor", "password manager"], r"""
        Good password habits:
        - Long (12+ chars) passphrases
        - Unique for every account
        - Use a password manager
        - Turn on 2FA/MFA (app or key beats SMS)
        - Never share OTPs
        Sites should store hashes with bcrypt/argon2, never plain text.
    """),

    E(["encryption", "encrypt", "decrypt", "cryptography", "aes", "rsa",
       "symmetric", "asymmetric"], r"""
        Encryption scrambles data so only key holders can read it.
        - Symmetric (AES): one shared key, fast
        - Asymmetric (RSA): public key encrypts, private key decrypts
        Python (pip install cryptography):
          from cryptography.fernet import Fernet
          key = Fernet.generate_key()
          f = Fernet(key)
          token = f.encrypt(b'secret')
          print(f.decrypt(token))
    """),

    E(["sql injection", "sqli", "injection"], r"""
        SQL injection happens when user input is glued into a database query so the input can change the query.
        Defense: parameterized queries, input validation, least-privilege database accounts.
        Safe Python (sqlite3):
          cur.execute(
            'SELECT * FROM users WHERE name = ?',
            (name,))
        Never build SQL with string joins.
    """),

    E(["xss", "csrf", "web security", "cross site scripting"], r"""
        XSS: a site shows untrusted input as code in other users' browsers. Defense: escape output, Content-Security-Policy.
        CSRF: tricks a logged-in user's browser into sending unwanted requests. Defense: CSRF tokens, SameSite cookies.
        Also: validate input, use HTTPS, set secure cookies, patch frameworks.
    """),

    E(["owasp", "owasp top 10", "top 10"], r"""
        OWASP Top 10 (2021 list):
        1 Broken Access Control
        2 Cryptographic Failures
        3 Injection
        4 Insecure Design
        5 Security Misconfiguration
        6 Vulnerable/Outdated Components
        7 Identification & Authentication Failures
        8 Software & Data Integrity Failures
        9 Logging & Monitoring Failures
        10 Server-Side Request Forgery
        Check owasp.org for the newest list.
    """),

    E(["dos", "ddos", "denial of service"], r"""
        A DoS attack tries to make a service unavailable by overwhelming it; DDoS uses many machines. Attacking others is a crime.
        Defense: rate limiting, CDN/scrubbing services, firewalls, autoscaling, monitoring.
    """),

    E(["vulnerability", "vulnerabilities", "cve", "exploit",
       "responsible disclosure", "bug bounty", "zero day"], r"""
        A vulnerability is a weakness. CVE is the public ID system for known ones (for example CVE-2021-44228).
        Responsible disclosure: report the issue privately to the owner, give time to fix, then share details.
        Bug bounties (HackerOne, Bugcrowd) pay for in-scope, authorized reports.
        Keep systems updated; most attacks use old known flaws.
    """),

    E(["authentication", "authorization", "authentication vs authorization"], r"""
        Authentication = proving who you are (password, OTP, fingerprint).
        Authorization = what you are allowed to do after login (admin vs user).
    """),

    E(["backup", "backups", "best practices", "security tips", "stay safe"], r"""
        Basic security habits:
        - Update OS and apps
        - Strong unique passwords + 2FA
        - Backups: 3 copies, 2 media types, 1 offsite (3-2-1)
        - Least privilege: give only needed access
        - Verify links and downloads
        - Encrypt your phone and laptop
    """),

    E(["kali", "kali linux", "metasploit", "burp suite", "burp", "tools",
       "hacking tools"], r"""
        Common security tools (use only with permission):
        - Kali Linux: distro with security tools
        - Nmap: network mapping
        - Wireshark: traffic analysis
        - Burp Suite: web app testing
        - Metasploit: testing framework
        Learn the basics first, then use them in lab environments you own.
    """),

    # --------------------------------------------------------------- LINUX
    E(["linux", "linux commands", "terminal", "command line", "commands",
       "shell"], r"""
        Essential Linux commands:
        pwd  show current folder
        ls  list files
        cd folder  change folder
        mkdir name  new folder
        touch f  new file
        cat f  show file
        nano f  edit file
        cp a b  copy
        mv a b  move/rename
        rm f  delete
        grep text f  search in file
        man cmd  manual
        clear  clean screen
    """),

    E(["permissions", "chmod", "chown", "file permissions"], r"""
        Linux permissions: r=read, w=write, x=execute for owner, group, others.
          chmod +x script.sh   make runnable
          chmod 644 file       rw- r-- r--
        Least privilege: give only what is needed.
    """),

    E(["termux", "pkg", "termux commands"], r"""
        Termux tips:
          pkg update && pkg upgrade
          pkg install python clang git
          termux-setup-storage  (access phone files)
          nano main.py
          python main.py
        Stop a running program with CTRL + C.
    """),

    E(["bash", "shell script", "bash script"], r"""
        A bash script is a file of commands.
          #!/bin/bash
          echo "Hello"
          for i in 1 2 3; do echo $i; done
        Run:  chmod +x s.sh && ./s.sh
    """),

    # ----------------------------------------------------------- LANGUAGES
    E(["c", "cpp", "c plus plus", "c language", "c programming"], r"""
        C is a fast, low-level language used for systems and embedded code. C++ adds classes and more.
        C program:
          #include <stdio.h>
          int main(void) {
              int age;
              printf("Age: ");
              scanf("%d", &age);
              printf("You are %d\n", age);
              return 0;
          }
        Compile and run in Termux:
          clang hello.c -o hello
          ./hello
        C++ prints with:  std::cout << "Hi";
    """),

    E(["java"], r"""
        Java is a popular language for apps, backends and Android.
          public class Hello {
              public static void main(String[] a) {
                  System.out.println("Hello");
              }
          }
        Run:  javac Hello.java && java Hello
        Termux: pkg install openjdk-17
    """),

    E(["javascript", "js", "node", "nodejs"], r"""
        JavaScript makes web pages interactive and also runs on servers (Node.js).
          let name = 'Sam';
          console.log('Hi ' + name);
          const add = (a, b) => a + b;
    """),

    E(["html", "css", "web design", "website"], r"""
        HTML is the structure of a page, CSS the style.
          <h1>Hello</h1>
          <p>My first page</p>
          <style>h1 { color: teal; }</style>
    """),

    E(["sql", "database", "databases", "sqlite", "mysql"], r"""
        SQL talks to databases.
          CREATE TABLE users(id INT, name TEXT);
          INSERT INTO users VALUES (1, 'Sam');
          SELECT * FROM users WHERE id = 1;
          UPDATE users SET name='Ana' WHERE id=1;
          DELETE FROM users WHERE id=1;
        Python includes sqlite3 for small projects.
    """),

    E(["git", "github", "version control"], r"""
        Git tracks changes to your code.
          git init
          git add .
          git commit -m "first commit"
          git push
        GitHub hosts your repositories online.
    """),

    E(["data structure", "data structures", "stack", "queue", "linked list"], r"""
        Data structures organise data:
        - Array/list: ordered items
        - Stack: last in, first out (undo)
        - Queue: first in, first out (lines)
        - Linked list: items point to the next
        - Hash table (dict): fast key lookup
        - Tree/graph: hierarchy and networks
        Python stack:
          s = []
          s.append(1)
          s.pop()
    """),

    E(["algorithm", "algorithms", "sorting", "bubble sort", "searching",
       "binary search", "big o"], r"""
        An algorithm is step-by-step instructions to solve a problem.
        Bubble sort:
          for i in range(len(a)):
              for j in range(len(a)-i-1):
                  if a[j] > a[j+1]:
                      a[j], a[j+1] = a[j+1], a[j]
        Binary search (sorted list): check the middle, discard half, repeat.
        Big O describes speed growth: O(1) fast, O(n) linear, O(n^2) slow.
        In Python just use sorted(a).
    """),

    # ------------------------------------------------- PYTHON PROGRAMS
    E(["programs", "all programs", "all code", "all codes", "codes",
       "example programs", "practice programs", "program list"], r"""
        Ask me for these Python programs:
        first code - hello world
        second code - ask the name
        third code - calculator
        fourth code - multiplication table
        fifth code - even or odd
        sixth code - guessing game
        seventh code - palindrome
        eighth code - fibonacci
        ninth code - password strength
        tenth code - to-do list
        Network programs:
        dns lookup program
        echo server
        http request program
        port checker
        40 more programs in Python AND C:
        python programs / c programs
        prime number in c
        Then type 'save' or 'save all'.
    """),

    E(["first code", "first program", "hello world"], r"""
        First code: Hello World
          print('Hello, world!')
        Save as hello.py and run:
          python hello.py
    """),

    E(["second code", "second program"], r"""
        Second code: ask the name
          name = input('Your name: ')
          print('Hello,', name)
    """),

    E(["third code", "third program", "calculator"], r"""
        Third code: calculator
          a = float(input('First: '))
          op = input('Operator + - * /: ')
          b = float(input('Second: '))
          if op == '+':
              print(a + b)
          elif op == '-':
              print(a - b)
          elif op == '*':
              print(a * b)
          elif op == '/':
              if b == 0:
                  print('Cannot divide by 0')
              else:
                  print(a / b)
          else:
              print('Unknown operator')
    """),

    E(["fourth code", "fourth program", "multiplication table", "table"], r"""
        Fourth code: multiplication table
          n = int(input('Table of: '))
          for i in range(1, 11):
              print(n, 'x', i, '=', n * i)
    """),

    E(["fifth code", "fifth program", "even or odd", "even odd"], r"""
        Fifth code: even or odd
          n = int(input('Number: '))
          if n % 2 == 0:
              print('Even')
          else:
              print('Odd')
    """),

    E(["sixth code", "sixth program", "guessing game", "guess game"], r"""
        Sixth code: guessing game
          import random
          secret = random.randint(1, 20)
          while True:
              g = int(input('Guess 1-20: '))
              if g < secret:
                  print('Higher')
              elif g > secret:
                  print('Lower')
              else:
                  print('Correct!')
                  break
    """),

    E(["seventh code", "seventh program", "palindrome"], r"""
        Seventh code: palindrome check
          w = input('Word: ').lower()
          if w == w[::-1]:
              print('Palindrome')
          else:
              print('Not a palindrome')
    """),

    E(["eighth code", "eighth program", "fibonacci"], r"""
        Eighth code: Fibonacci
          a, b = 0, 1
          for _ in range(10):
              print(a, end=' ')
              a, b = b, a + b
    """),

    E(["ninth code", "ninth program", "password strength",
       "password checker"], r"""
        Ninth code: password strength checker
          pw = input('Password: ')
          score = 0
          if len(pw) >= 12:
              score += 1
          if any(c.isdigit() for c in pw):
              score += 1
          if any(c.isupper() for c in pw):
              score += 1
          if any(c.islower() for c in pw):
              score += 1
          if any(not c.isalnum() for c in pw):
              score += 1
          print('Strength:', score, '/ 5')
    """),

    E(["tenth code", "tenth program", "todo", "to-do list", "todo list"], r"""
        Tenth code: to-do list saved to a file
          tasks = []
          while True:
              t = input('Task (q=quit): ')
              if t == 'q':
                  break
              tasks.append(t)
          with open('tasks.txt', 'w') as f:
              f.write('\n'.join(tasks))
    """),

    E(["dns lookup program", "dns program", "lookup program"], r"""
        DNS lookup program
          import socket
          site = input('Website: ')
          try:
              print(socket.gethostbyname(site))
          except socket.gaierror:
              print('Name not found')
    """),

    E(["echo server", "tcp server", "client server", "socket program",
       "socket programming"], r"""
        Echo server and client on localhost.
        server.py (run first):
          import socket
          s = socket.socket()
          s.bind(('127.0.0.1', 5000))
          s.listen(1)
          conn, addr = s.accept()
          data = conn.recv(1024)
          conn.sendall(data)
          conn.close()
        client.py (second terminal):
          import socket
          c = socket.socket()
          c.connect(('127.0.0.1', 5000))
          c.sendall(b'hello')
          print(c.recv(1024))
    """),

    E(["http request program", "urllib", "fetch website", "get request"], r"""
        HTTP request with no install:
          from urllib.request import urlopen
          r = urlopen('https://example.com')
          print(r.status)
          print(r.read()[:100])
    """),

    E(["port checker", "check port", "open port program"], r"""
        Check a port on YOUR OWN device only:
          import socket
          port = int(input('Port: '))
          s = socket.socket()
          s.settimeout(1)
          r = s.connect_ex(('127.0.0.1', port))
          print('open' if r == 0 else 'closed')
          s.close()
    """),
]

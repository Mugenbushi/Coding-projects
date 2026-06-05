# Coding Projects

A collection of Python projects focused on security tooling and CLI utilities, written while building up practical skills in networking, cryptography, and Python fundamentals. Each script is self-contained and runnable from the command line.

> ⚠️ The networking tools (port scanners, WHOIS, nmap wrapper) are for educational use and authorized testing only. Only scan hosts you own or have explicit permission to test (e.g., `scanme.nmap.org`).

---

## Projects

### `port_scan_test_2.py` — Multithreaded Port Scanner with Banner Grabbing
A concurrent TCP port scanner that checks a target across a list of common ports and attempts to identify the service running on each open port.

- Uses a `Queue` of ports and a pool of worker threads (default 10) for fast, parallel scanning.
- A `threading.Lock` keeps console output from interleaving across threads.
- `connect_ex()` is used to test each port (returns `0` when open).
- For open ports it grabs a service banner: it reads any data the service sends on connect, and for web ports (80, 443, 8080, 8000) it sends a minimal HTTP request to coax a response.
- Defaults to scanning `scanme.nmap.org` on ports `[21, 22, 25, 80, 443, 3306, 5432, 8080]`.

**Run:** `python port_scan_test_2.py`

### `portscanner.py` — Simple Full-Range Port Scanner
A single-threaded scanner that walks every port from 1–65534 on a user-supplied IP and reports which are open.

- Prompts for a target IP and prints a `pyfiglet` ASCII banner plus a timestamped header.
- Sets a 0.5s socket timeout and handles `KeyboardInterrupt` (clean exit) and `socket.error` (host unreachable).
- Good as a from-scratch baseline before the threaded version above.

**Dependencies:** `pyfiglet`
**Run:** `python portscanner.py`

### `file_encrypt.py` — Password-Based File Encryption/Decryption
A CLI tool that encrypts or decrypts a file using a password.

- Derives a 32-byte key from the password with **PBKDF2-HMAC-SHA256** (100,000 iterations), then encrypts with **Fernet** (symmetric authenticated encryption).
- Encrypting writes a new `.encrypted` file; decrypting strips that suffix to restore the original.
- Optionally deletes the source file after the operation.

**Dependencies:** `cryptography`
**Run:** `python file_encrypt.py`

> Note: the salt is currently hardcoded. A natural next improvement is generating a random salt per file and storing it alongside the ciphertext.

### `passwordpassmap.py` — Password Manager Prototype
A simple account create/login flow that stores credentials in memory.

- Hashes passwords with **SHA-256** before storing them in a dictionary (no plaintext storage).
- Uses `getpass` so passwords aren't echoed to the terminal.
- Menu loop for create account / login / exit.

**Run:** `python passwordpassmap.py`

> Note: storage is in-memory only (resets on exit) and SHA-256 alone is fast/unsalted. A future version could add persistence and a slow, salted hash (bcrypt/argon2).

### `passgen.py` — Random Password Generator
Generates a random password from letters, digits, and punctuation.

- Default length of 10, easily configurable via the function argument.

**Run:** `python passgen.py`

### `pythonwhois.py` — WHOIS Lookup
Performs a raw WHOIS query by opening a socket to `whois.iana.org` on port 43 and printing the response. Demonstrates talking to a TCP service directly without a library.

**Run:** `python pythonwhois.py`

### `to_do.py` — Command-Line To-Do List
A persistent to-do app using `argparse` subcommands, with tasks stored as JSON in `tlist.json`.

- `add "<task>"` — add a task
- `list` — list tasks with done/not-done status
- `done <index>` — mark a task complete
- `delete <index>` — remove a task

**Run:** `python to_do.py add "Write README"` then `python to_do.py list`

### `pythonnmap.py` — Nmap Wrapper (work in progress)
A scaffold for using the `python-nmap` library to run `-sV -sC` service/script scans and parse results by host, protocol, and port. Currently commented out as a reference template.

### `pythoncipher.py` — Caesar Cipher (work in progress)
A scaffold for Caesar cipher encrypt/decrypt using `str.maketrans` for character shifting. Currently commented out as a reference template.

---

## Getting Started

```bash
git clone https://github.com/Mugenbushi/Coding-projects.git
cd Coding-projects
pip install cryptography pyfiglet python-nmap
```

Each script runs independently with `python <script>.py`.

## Roadmap
- Audio file converter (TBA)
- Random per-file salts for `file_encrypt.py`
- Persistent storage + stronger hashing for the password manager
- Finish the nmap wrapper and Caesar cipher

## License
No license specified yet. Consider adding one (e.g., MIT) if you want others to reuse the code.

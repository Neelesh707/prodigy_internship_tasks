#!/bin/bash
# ─── Validation ───────────────────────────────────────────
if [ -z "$1" ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

domain=$1
RED="\033[1;31m"
GREEN="\033[1;32m"
RESET="\033[0m"

info_path="$domain/info"
subdomain_path="$domain/subdomains"
screenshot_path="$domain/screenshots"

# ─── Directory Setup ──────────────────────────────────────
for dir in "$domain" "$subdomain_path" "$info_path" "$screenshot_path"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
    fi
done

# ─── Tool dependency check ────────────────────────────────
for tool in whois subfinder assetfinder httprobe gowitness; do
    if ! command -v "$tool" &>/dev/null; then
        echo -e "${RED}[-] Missing tool: $tool — please install it.${RESET}"
        exit 1
    fi
done

# ─── Recon ────────────────────────────────────────────────
echo -e "${RED}[+] Checking whois...${RESET}"
whois "$domain" > "$info_path/whois.txt"

echo -e "${RED}[+] Launching subfinder...${RESET}"
subfinder -d "$domain" -silent > "$subdomain_path/found.txt"

echo -e "${RED}[+] Running assetfinder...${RESET}"
assetfinder --subs-only "$domain" | grep "\.$domain$" >> "$subdomain_path/found.txt"

# Deduplicate before probing
sort -u "$subdomain_path/found.txt" -o "$subdomain_path/found.txt"

echo -e "${RED}[+] Checking what's alive...${RESET}"
cat "$subdomain_path/found.txt" \
    | httprobe -prefer-https \
    | tee "$subdomain_path/alive_with_proto.txt" \
    | sed 's/https\?:\/\///' \
    | sort -u \
    | tee "$subdomain_path/alive.txt"

echo -e "${RED}[+] Taking screenshots...${RESET}"
gowitness scan file \
    -f "$subdomain_path/alive_with_proto.txt" \
    --write-screenshots \
    --screenshot-path "$screenshot_path/"

echo -e "${GREEN}[+] Done! Results saved to ./$domain/${RESET}"

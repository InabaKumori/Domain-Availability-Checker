import sys
import itertools
import string
import whois
from datetime import datetime, timedelta
from multiprocessing import Pool, Manager

def check_domain_availability(domain, grace_period, mode, available_domains, unavailable_domains):
    try:
        w = whois.whois(domain)
        if not w.domain_name:
            available_domains.append(domain)
            if mode == "debug" or mode == "error":
                print(f"{domain} is available for registration.")
            return
        if w.status:
            for status in w.status:
                if "available" in status.lower() or "free" in status.lower():
                    available_domains.append(domain)
                    if mode == "debug" or mode == "error":
                        print(f"{domain} is available for registration.")
                    return
        if w.expiration_date:
            if isinstance(w.expiration_date, list):
                expiration_date = w.expiration_date[0]
            else:
                expiration_date = w.expiration_date
            if expiration_date < datetime.now() - timedelta(days=grace_period):
                available_domains.append(domain)
                if mode == "debug" or mode == "error":
                    print(f"{domain} is available for registration.")
                return
        unavailable_domains.append(domain)
        if mode == "debug" or mode == "info":
            print(f"{domain} is not available for registration.")
    except (whois.parser.PywhoisError, ConnectionResetError, TimeoutError):
        pass

def generate_domains(tld, length):
    chars = string.ascii_lowercase + string.digits
    for combination in itertools.product(chars, repeat=length):
        domain = ''.join(combination) + tld
        yield domain

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python newscript.py <tld> <length> <processes> <mode> <grace_period>")
        print("Modes: debug, info, error")
        print("Grace Period: Number of days after expiration to consider a domain available (e.g., 0 for immediately available, 30 for available after 30 days)")
        sys.exit(1)

    tld = sys.argv[1]
    length = int(sys.argv[2])
    processes = int(sys.argv[3])
    mode = sys.argv[4]
    grace_period = int(sys.argv[5])

    manager = Manager()
    available_domains = manager.list()
    unavailable_domains = manager.list()

    pool = Pool(processes=processes)

    for domain in generate_domains(tld, length):
        pool.apply_async(check_domain_availability, args=(domain, grace_period, mode, available_domains, unavailable_domains))

    pool.close()
    pool.join()

    total_domains = len(available_domains) + len(unavailable_domains)
    if mode == "debug" or mode == "info":
        print(f"\nSummary:")
        print(f"Total domains checked: {total_domains}")
        print(f"Available domains: {len(available_domains)}")
        print(f"Unavailable domains: {len(unavailable_domains)}")

    if mode == "debug" or mode == "error":
        print("\nAvailable domains:")
        for domain in available_domains:
            print(domain)

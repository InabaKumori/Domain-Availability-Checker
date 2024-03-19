# Domain Availability Checker

This Python script efficiently checks the availability of domain names based on the specified top-level domain (TLD), length of the domain, and other criteria. It leverages the `whois` library to query domain registration details and determines if a domain is available, already registered, or soon to be available based on its expiration date.

## Features

- **Flexible Domain Generation**: Dynamically generates domain names based on specified length and TLD.
- **Concurrent Processing**: Utilizes multiprocessing to speed up the checking process across multiple domains.
- **Customizable Grace Period**: Allows specifying a grace period to consider recently expired domains as available.
- **Output Modes**: Supports different output modes (`debug`, `info`, `error`) to tailor the verbosity of the script's output.

## Requirements

- Python 3.x
- `whois` Python package

Before running the script, ensure you have Python 3.x installed on your system and install the `whois` package using pip:

```bash
pip install python-whois
```

## Installation

Clone the repository to get started with the Domain Availability Checker:

```bash
git clone https://github.com/inabakumori/domain-availability-checker.git
```

Navigate to the cloned directory:

```bash
cd domain-availability-checker
```

## Usage

Run the script from the command line, providing the required arguments:

```bash
python domain_checker.py <tld> <length> <processes> <mode> <grace_period>
```

- `<tld>`: The top-level domain (e.g., `.com`, `.net`) to check for availability.
- `<length>`: The length of the domain names to generate and check.
- `<processes>`: The number of concurrent processes to use for checking domain availability.
- `<mode>`: Output mode (`debug`, `info`, `error`).
- `<grace_period>`: Number of days after expiration to consider a domain available.

Example:

```bash
python domain_checker.py .com 3 10 debug 30
```

## Contributing

Your contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is open source and available under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Acknowledgments

- This tool was developed to assist web developers, researchers, and hobbyists in finding available domain names efficiently.

from Vulnerabilities import Vulnerabilities
from Policy import Policy

def print_detected_vulnerabilities(vulnerabilities, policy):
    detected_vulnerabilities = vulnerabilities.get_vulnerabilities()

    for vulnerability_name, multilabels in detected_vulnerabilities.items():
        print(f"Detected Vulnerability: {vulnerability_name}")

        for multilabel in multilabels:
            sources = multilabel.get_sources()
            sinks = policy.get_sinks_for_vulnerability(vulnerability_name)
            sanitizers = policy.get_sanitizers_for_vulnerability(vulnerability_name)

            print("\tSources:")
            for source in sources:
                print(f"\t\t{source}")

            print("\tSinks:")
            for sink in sinks:
                print(f"\t\t{sink}")

            print("\tPossible Sanitizers:")
            for sanitizer in sanitizers:
                print(f"\t\t{sanitizer}")

            print("\n")

print_detected_vulnerabilities(vulnerabilities, policy)
import re

# This module provides support for regular expressions in Python

def matchre(data, *args):
    # Function to search for multiple regex patterns in the data
    # Takes variable number of arguments (regex patterns) and searches them in the data
    # Prints matched content or "No <pattern> found" if not found
    for regstr in args:
        matchObj = re.search(regstr + '.*', data, re.M | re.I)
        if matchObj:
            print(matchObj.group(0).lstrip().rstrip())
        else:
            print("No ", regstr, "found")


def extract_message_id(data):
    # Extracts Message-ID from email headers
    # Uses positive lookbehind (?<=) to match content after "Message-ID: "
    message_id_pattern = r'(?<=Message-ID: ).*'
    message_id = re.search(message_id_pattern, data, re.I)
    if message_id:
        return message_id.group(0).lstrip().rstrip()
    else:
        return "No Message-ID found"

def extract_received_from(data):
    # Extracts the "Received from" information from email headers
    # Uses positive lookbehind and lookahead to get content between "Received: from" and ")"
    received_pattern = r'(?<=Received: from ).*?(?=\))'
    received_from = re.findall(received_pattern, data, re.I)
    if received_from:
        return received_from[-1].lstrip().rstrip()
    else:
        return "No Received from details found"

def extract_received_ip(data):
    # Extracts IP address from the received headers
    # Matches IP address pattern within square brackets [x.x.x.x]
    received_ip_pattern = r'\[([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\]'
    received_ip = re.findall(received_ip_pattern, data, re.I)
    if received_ip:
        return received_ip[-1].lstrip().rstrip()
    else:
        return "No Received IP found"

def extract_subject(data):
    # Extracts email subject
    # Uses positive lookbehind to match content after "Subject: "
    subject_pattern = r'(?<=Subject: ).*'
    subject = re.search(subject_pattern, data, re.I)
    if subject:
        return subject.group(0).lstrip().rstrip()
    else:
        return "No Subject found"

def extract_dkim_signature(data):
    # Extracts DKIM signature from email headers
    # Uses positive lookbehind to match content after "DKIM-Signature: "
    dkim_signature_pattern = r'(?<=DKIM-Signature: ).*'
    dkim_signature = re.search(dkim_signature_pattern, data, re.I)
    if dkim_signature:
        return dkim_signature.group(0).lstrip().rstrip()
    else:
        return "No DKIM Signature found"

def extract_content_transfer_encoding(data):
    # Extracts Content-Transfer-Encoding value
    # Uses positive lookbehind to match content after "Content-Transfer-Encoding: "
    cte_pattern = r'(?<=Content-Transfer-Encoding: ).*'
    cte = re.search(cte_pattern, data, re.I)
    if cte:
        return cte.group(0).lstrip().rstrip()
    else:
        return "No Content Transfer Encoding found"

def extract_date(data):
    # Extracts email date
    # Uses positive lookbehind to match content after "Date: "
    date_pattern = r'(?<=Date: ).*'
    date = re.search(date_pattern, data, re.I)
    if date:
        return date.group(0).lstrip().rstrip()
    else:
        return "No Date found"

def extract_mime_version(data):
    # Extracts MIME version
    # Uses positive lookbehind to match content after "MIME-Version: "
    mime_version_pattern = r'(?<=MIME-Version: ).*'
    mime_version = re.search(mime_version_pattern, data, re.I)
    if mime_version:
        return mime_version.group(0).lstrip().rstrip()
    else:
        return "No MIME Version found"

def extract_senders_and_receivers(data):
    # Extracts both senders and receivers from email headers
    # Returns two lists containing all "From: " and "To: " entries
    senders = re.findall(r'(?<=From: ).*', data, re.I)
    receivers = re.findall(r'(?<=To: ).*', data, re.I)
    return senders, receivers

def extract_dkim(data):
    # Extracts DKIM information
    # Uses positive lookbehind to match content after "DKIM-Signature: "
    dkim_pattern = r'(?<=DKIM-Signature: ).*'
    dkim = re.search(dkim_pattern, data, re.I)
    if dkim:
        return dkim.group(0).lstrip().rstrip()
    else:
        return "No DKIM found"

def extract_spf(data):
    # Extracts SPF (Sender Policy Framework) information
    # Uses positive lookbehind to match content after "Received-SPF: "
    spf_pattern = r'(?<=Received-SPF: ).*'
    spf = re.search(spf_pattern, data, re.I)
    if spf:
        return spf.group(0).lstrip().rstrip()
    else:
        return "No SPF found"

def display_analysis_results(data):
    # Function to display all extracted information in a formatted manner
    # Calls all extraction functions and prints their results
    print("\n**********************************************************************\n")
    print("\nAdditional Extracted Details:")
    print("\nMessage ID:")
    print(extract_message_id(data))
    print("\nReceived from:")
    print(extract_received_from(data))
    print("\nSubject:")
    print(extract_subject(data))
    print("\nReceived IP:")
    print(extract_received_ip(data))
    print("\nDKIM Signature:")
    print(extract_dkim_signature(data))
    print("\nContent Transfer Encoding:")
    print(extract_content_transfer_encoding(data))
    print("\nDate:")
    print(extract_date(data))
    print("\nMIME Version:")
    print(extract_mime_version(data))
    
    senders, receivers = extract_senders_and_receivers(data)
    print("\nSenders:")
    for sender in senders:
        print(sender)
    
    print("\nReceivers:")
    for receiver in receivers:
        print(receiver)
    
    print("\nDKIM:")
    print(extract_dkim(data))
    print("\nSPF:")
    print(extract_spf(data))
    print("\n**********************************************************************\n")


def main():


    # Main function to execute the program
    # Opens and reads the email header file
    # Calls functions to extract and display information
    filename = "D:\Sem 7\Practicals\CSDF\content\practical_1.txt"  # Hardcoded file path
    with open(filename, "r") as fo:
        data = fo.read()

    print("Extracted Details:")
    matchre(data, "MIME-version", "Date:", "Subject:", "Delivered-to:", "From:", "^To:")
    display_analysis_results(data)

if __name__ == "__main__":
    # Program entry point
    # Executes main() function when script is run directly
    main()


'''
$ python -u "d:\Sem 7\Practicals\CSDF\practical_1.py"
d:\Sem 7\Practicals\CSDF\practical_1.py:136: SyntaxWarning: invalid escape sequence '\S'
  filename = "D:\Sem 7\Practicals\CSDF\content\practical_1.txt"  # Hardcoded file path
Extracted Details:
MIME-Version: 1.0
Date: Mon, 23 Oct 2024 09:15:00 -0700
Subject: Testing email header analysis
No  Delivered-to: found
From: "Abhishek Paturkar" <paturkarabhishek03@gmail.com>
To: hariomvm21@gmail.com

**********************************************************************


Additional Extracted Details:

Message ID:
<1234567890@gmail.com>

Received from:
mail.gmail.com (mail.gmail.com. [74.125.200.108]

Subject:
Testing email header analysis

Received IP:
74.125.200.108

DKIM Signature:
v=1; a=rsa-sha256; c=relaxed/relaxed; d=gmail.com; s=2024;

Content Transfer Encoding:
7bit

Date:
Mon, 23 Oct 2024 09:15:00 -0700

MIME Version:
1.0

Senders:
"Abhishek Paturkar" <paturkarabhishek03@gmail.com>

Receivers:
hariomvm21@gmail.com


DKIM:
v=1; a=rsa-sha256; c=relaxed/relaxed; d=gmail.com; s=2024;
v=1; a=rsa-sha256; c=relaxed/relaxed; d=gmail.com; s=2024;

SPF:
pass (google.com: domain of paturkarabhishek03@gmail.com designates 74.125.200.108 as permitted sender) client-ip=74.125.200.108;

**********************************************************************
'''
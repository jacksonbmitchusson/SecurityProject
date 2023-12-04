import smtplib
import email
import subprocess
import time 

subject = 'Evil Twin Network Detected!'
app_pass = "lpum zhng bqln byov"
gmail = "csdetector@gmail.com"

def get_wifi_networks():
    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'networks']).decode('utf-8', errors="backslashreplace")
    networks_list = networks.split('\n')
    ssids = [line.split(':')[1].strip() for line in networks_list if 'SSID' in line]
    return ssids

#char_equiv = [(char1, [char, ..., char]), (char2, [char, ..., char]), ... ]
def replace_equiv_chars(s, char_equivs):
    out = []
    for i in range(len(s)):
        out_char = s[i]
        for pair in char_equivs:
            if s[i] in pair[1]:
                out_char = pair[0]
                break 
        out.append(out_char)
    return ''.join(out)

def varpadding(s, n, i, pad_char):
    return i*pad_char + s + (n - i)*pad_char

def hamming_dist(s1, s2):
    diff = len(s1) - len(s2)
    if(diff == 0):
        count = 0 
        for i in range(len(s1)):
            count += 1 if s1[i] != s2[i] else 0    
        return count
    
    min_dist = len(s1) + len(s2)
    for i in range(abs(diff) + 1):
        if(diff < 0): #s1 < s2 
            new_s1 = varpadding(s1, abs(diff), i, ' ')            
            min_dist = min(min_dist, hamming_dist(new_s1, s2))
        else:
            new_s2 = varpadding(s2, abs(diff), i, ' ')            
            min_dist = min(min_dist, hamming_dist(s1, new_s2))
    return min_dist

def generate_email_msg(gmail, recipient, subject, body): #NEED TO FIX
    msg = email.message.EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = gmail
    msg['To'] = recipient
    return msg
 
def send_email_alert(google_email, app_password, msg): #NEED TO FIX
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(google_email, app_password)
    print(msg)
    s.send_message(msg)
    s.quit()

def compare_networks(target, ssid, char_equivs):
    target_compare = replace_equiv_chars(target.lower(), char_equivs)
    ssid_compare = replace_equiv_chars(ssid.lower(), char_equivs)
    return hamming_dist(target_compare, ssid_compare)

def monitor_networks(target, recipient, hamming_dist_threshold=5, char_equivs=[], delaytime=1):
    detected_ssids = []
    print('Searching...')
    ssids = [ssid for ssid in get_wifi_networks() if ssid not in detected_ssids]

    #drop exactly one copy of target network, 
    # allows detecting exact copies
    for i in range(len(ssids)):
        if ssids[i] == target:
             del ssids[i]
             break

    for ssid in ssids:
        if compare_networks(target, ssid, char_equivs) < hamming_dist_threshold: #send email alert
            detected_ssids.append(ssid)
            body = f'An evil twin network has been detected! The SSID of the network is {ssid}\nNavigate to [url] to see further details and available actions.'
            print(f"Evil Twin detected!!!\nSSID: {ssid}\nSending alert email to {recipient} from {gmail}")

            if recipient != "": #if email is blank, user opted to not send email
                print(f"Gmail = {gmail} \n Password = {app_pass}")
                msg = generate_email_msg(gmail, recipient, subject, body)
                send_email_alert(gmail, app_pass, msg)
    
            return False #If returned false, reports an evil twin is found

    return True #If returned true, no evil twin is found

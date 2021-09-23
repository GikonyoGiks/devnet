import telnetlib, time
HOST="184.7.27.2"
tn=telnetlib.Telnet(HOST,"7030")
tn.set_debuglevel(5)
tn.write(b'\n')
while True:
    line = tn.read_until(b"\n")  # Read one line
    print(line)
    if b'3' or b'4' in line:  # last line, no more read
        tn.read_until(b"\n")
        tn.write(b"\r\n" + "en".encode('ascii') + b"\n")
        if tn.read_until(b"Password: ",timeout=10):
            tn.write("ISEisC00L".encode('ascii') + b"\n")
        tn.read_until(b"#")
        tn.write("copy flash:/SCRIPTS/ISESDA-DNA-Noc.cfg startup-config".encode('ascii') + b"\n")
        tn.write(b"\n")
        tn.write("reload".encode('ascii') + b"\n")
        tn.write(b"\n")
        time.sleep(600)
        tn.write(b"\r\n")
        tn.write(b"\n")
        print(tn.read_all().decode('ascii'))
        break

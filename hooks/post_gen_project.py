import subprocess

github_user = "{{ cookiecutter.github_user }}"
github_user_name = "{{ cookiecutter.project_author_name }}"
local_key = "{{ cookiecutter.local_key }}"

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")
# subprocess.call(['ssh-keygen', '-t', 'rsa', '-C', github_user])
# subprocess.call(['eval', '"$(ssh-agent -s)"'])
# subprocess.call(['ssh-add', f'~/.ssh/{local_key}'])
subprocess.call(['git', 'init'])
subprocess.call(['git', 'config', '--local', 'user.email', f'"{github_user}"'])
subprocess.call(['git', 'config', '--local', 'user.name', f'"{github_user_name}"'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")
import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-m", "--message", dest="new_message", help="Message to commit to github")

(options, arguments) = parser.parse_args()

subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', options.new_message])
subprocess.call(['git', 'push', 'origin', 'master'])
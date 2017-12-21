import os
import subprocess
cmd = ["docker-compose", "run", "--rm", "web", "config", "generate-secret-key"]
res = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
sk = res.split('\n')[-2]

filename = 'docker-compose.yml'
f = open(filename, 'r')
content = f.read()
nc = content.replace("# SENTRY_SECRET_KEY: ''", "SENTRY_SECRET_KEY: {}".format(sk))
f.close()

f = open(filename, 'w')
f.write(nc)
f.close()
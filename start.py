import subprocess

subprocess.call(["docker-compose", "build"])

cmd = ["docker-compose", "run", "--rm", "web", "config", "generate-secret-key"]
res = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
sk = res.strip()[-50:]

filename = 'docker-compose.yml'
f = open(filename, 'r')
content = f.read()
nc = content.replace("# SENTRY_SECRET_KEY: ''", "SENTRY_SECRET_KEY: {}".format(sk))
f.close()

f = open(filename, 'w')
f.write(nc)
f.close()
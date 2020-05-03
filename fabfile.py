from fabric import Connection

c = Connection('sfo', user='dimitri', port=22)
result = c.run('uname -s')
result.stdout.strip() == 'Linux'
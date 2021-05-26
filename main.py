import pysftp
import os
import build


if __name__ == '__main__':
    with pysftp.Connection(build.hostname, username=build.username, private_key_pass=build.private_key_pass) as sftp:
        os.chdir(build.drop)
        sftp.chdir('production/sa-payment')
        print(sftp.listdir('.'))
        sftp.get_d(remotedir='.', localdir='.', preserve_mtime=True)
        for filename in os.listdir():
            if filename.startswith("lcu_"):
                if sftp.exists(filename):
                    sftp.remove(filename)
                print(filename)


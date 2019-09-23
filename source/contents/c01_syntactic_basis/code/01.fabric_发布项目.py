from fabric import Connection


def main():
    conn = Connection('name:host', connect_kwargs={'password': 'password'})
    with conn.cd("cd /data"):
        c.run('ls')


if __name__ == "__main__":
    main()

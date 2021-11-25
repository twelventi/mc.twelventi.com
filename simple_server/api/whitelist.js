const fs = require('fs');
const PATH_TO_WHITELIST = `${__dirname}/whitelist.txt`
const PATH_TO_TOKENS = `${__dirname}/tokens.txt`

fs.appendFileSync(PATH_TO_WHITELIST, '');
fs.appendFileSync(PATH_TO_TOKENS, '');

exports.getTokens = () => {
    return fs.readFileSync(PATH_TO_TOKENS).toString().split('\n')
}

exports.createToken = () => {
    let token = "";
    for (let i = 0; i < 16; i++) {
        token += `${Math.floor(Math.random() * 10)}`
    }
    fs.appendFileSync(PATH_TO_TOKENS, `${token}\n`)
}

exports.addUserToWhitelist = (user) => {
    fs.writeFileSync('/tmp/minecraft.stdin', `whitelist add ${user}\n`)
}

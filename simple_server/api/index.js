var serve = require("koa-static");
var router = require("koa-router");
var mount = require('koa-mount')
var koa = require('koa');
var app = new koa();
var body = require('koa-body');
var { getTokens, addUserToWhitelist } = require('./whitelist')

const api = new router();
api.get("/hi", async (ctx) => {
    ctx.body="hi"
})
api.post("/submission", async (ctx) => {
    ctx.body={"success" : ctx.request }
    const {name, code} = ctx.request.body;
    if (getTokens().includes(code)) {
        ctx.body = {status: "succes"}
        addUserToWhitelist(name);
    } else {
        ctx.body = {status: "error"}
    }
})

app.use(body())

app.use(mount('/', serve(`${__dirname}/../ui`)));
app.use(mount('/api',api.routes()));

app.listen(3000, () => {
    console.log("server listening on 3000");
})
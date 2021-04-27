// 参考：https://mp.weixin.qq.com/s/CYYSKWu5CEkwf-HJ2_P8oQ
const Koa = require('koa')
const app = new Koa()

app.use(async (ctx, next) => {
  console.log('Middleware 1 Start')
  await next()
  console.log('Middleware 1 End')
})

app.use(async (ctx, next) => {
  console.log('Middleware 2 Start')
  await next()
  console.log('Middleware 2 End')

  ctx.body = 'hello, koa'
})

app.listen(3000)
console.log("koa listening in: http://localhost:3000")

// output
// Middleware 1 Start
// Middleware 2 Start
// Middleware 2 End
// Middleware 1 End

const KoaMini = require('./koa-mini')
const app1 = new KoaMini()

app1.use(async (ctx, next) => {
  console.log('Middleware 1 Start')
  await next()
  console.log('Middleware 1 End')
})

app1.use(async (ctx, next) => {
  console.log('Middleware 2 Start')
  await next()
  console.log('Middleware 2 End')

  ctx.body = 'hello, koa-mini'
})

app1.listen(3001)
console.log("koa-mini listening in: http://localhost:3001")
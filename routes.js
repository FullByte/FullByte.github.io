import { Router } from '@layer0/core'

const ONE_MINUTE = 60
const FAR_FUTURE = 60 * 60 * 24 * 365 * 10

const router = new Router()

router.match('/:path*', ({ serveStatic, cache }) => {
  cache({
    browser: false,
    edge: {
      maxAgeSeconds: FAR_FUTURE,
    },
  })
  serveStatic('site/:path*')
})

export default router
## Setup

```bash
npm install
```

Ensure you have **Node.js v16** installed

## Developing

The ui uses [sveltekit](https://kit.svelte.dev/docs)

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

```bash
npm run build
```

Optionally, you can define the following env variables:

* `VITE_API_BASE_URL=https://app-backend.example.com` to define the base url to the api (python app)
* `BASE_PATH=/subdirectory` to define the base path where the ui is deployed 

You can preview the built app with `npm run preview`. This should _not_ be used to serve your app in production.

## Testing

```bash
npm run cypress:open
```

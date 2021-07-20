<p  align="center">
 <img src="https://i.ibb.co/BGVBmMK/opal.png" height=170 alt="opal" border="0" />
</p>
<h2 align="center">
OPAL Fetcher for Postgres
</h2>

[Check out OPAL main repo here.](https://github.com/authorizon/opal)

### What's in this repo?
An OPAL [custom fetch provider](https://github.com/authorizon/opal/blob/master/docs/HOWTO/write_your_own_fetch_provider.md) to bring authorization state from [Postgres](https://www.postgresql.org/).

This fetcher is both functional and can be used by OPAL, but is also serving as an example how to write custom fetch providers for OPAL and how to publish them as pip packages.

### How to use this fetcher
1) Build a custom opal-client `Dockerfile` based on the official docker image, that includes this fetcher's pip package. Your `Dockerfile` should look like this:
```
FROM authorizon/opal-client:latest
RUN pip install --no-cache-dir --user opal-fetcher-postgres
```

2) Build your custom opal-client container:
```
docker build -t yourcompany/opal-client --target client .
```

3) Pass the following environment variable to the OPAL client docker container:
```
OPAL_FETCH_PROVIDER_MODULES='["opal_common.fetcher.providers","opal_fetcher_postgres.providers"]'
```
Notice that OPAL receives a list from where to search for fetch providers.
The list in our case includes the built-in providers (`opal_common.fetcher.providers`) and our custom postgres provider.

4) You can test this fetcher with the example docker compose file in this repository root:
```
docker compose up
```

### About OPAL (Open Policy Administration Layer)
[OPAL](https://github.com/authorizon/opal) is an administration layer for Open Policy Agent (OPA), detecting changes to both policy and policy data in realtime and pushing live updates to your agents.

OPAL brings open-policy up to the speed needed by live applications. As your application state changes (whether it's via your APIs, DBs, git, S3 or 3rd-party SaaS services), OPAL will make sure your services are always in sync with the authorization data and policy they need (and only those they need).

Check out OPAL's main site at [OPAL.ac](https://opal.ac).

<img src="https://i.ibb.co/CvmX8rR/simplified-diagram-highlight.png" alt="simplified" border="0">

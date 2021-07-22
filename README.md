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

### How to use this fetcher in your OPAL Setup
1) Build a custom opal-client `Dockerfile` based on the official docker image, that includes this fetcher's pip package. Your `Dockerfile` should look like this:
```
FROM authorizon/opal-client:latest
RUN pip install --no-cache-dir --user opal-fetcher-postgres
```

2) Build your custom opal-client container:
```
docker build -t yourcompany/opal-client .
```

3) Pass the following environment variable to the OPAL client docker container (comma-separated provider modules):
```
OPAL_FETCH_PROVIDER_MODULES=opal_common.fetcher.providers,opal_fetcher_postgres.provider
```
Notice that OPAL receives a list from where to search for fetch providers.
The list in our case includes the built-in providers (`opal_common.fetcher.providers`) and our custom postgres provider.

4) Your DataSourceEntries (either in `OPAL_DATA_CONFIG_SOURCES` or in dynamic updates) can now include this fetcher.

Example value of `OPAL_DATA_CONFIG_SOURCES` (formatted nicely, but in env var you should pack this to one-line and no-spaces):
```json
{
    "config": {
        "entries": [
            {
                "url": "postgresql://postgres@example_db:5432/postgres",
                "config": {
                    "fetcher": "PostgresFetchProvider",
                    "query": "SELECT * from city;",
                    "connection_params": {
                        "password": "postgres"
                    }
                },
                "topics": [
                    "policy_data"
                ],
                "dst_path": "cities"
            }
        ]
    }
}
```

Values for this fetcher config:
* The `url` is actually a postgres dsn. You can set the postgres password in the dsn itself if you want.
* `connection_params` are optional, if you want to include certain overrides outside the dsn.
* Your `config` must include the `fetcher` key to indicate to OPAL that you use a custom fetcher.
* Your `config` must include the `query` key to indicate what query to run against postgres.

### Example docker compose configuration - run this custom fetcher in one command
4) You can test this fetcher with the example docker compose file in this repository root:
```
docker compose up
```
this docker compose configuration already correctly configures OPAL to load the Postgres Fetch Provider, and correctly configures `OPAL_DATA_CONFIG_SOURCES` to include an entry that uses this fetcher.

### About OPAL (Open Policy Administration Layer)
[OPAL](https://github.com/authorizon/opal) is an administration layer for Open Policy Agent (OPA), detecting changes to both policy and policy data in realtime and pushing live updates to your agents.

OPAL brings open-policy up to the speed needed by live applications. As your application state changes (whether it's via your APIs, DBs, git, S3 or 3rd-party SaaS services), OPAL will make sure your services are always in sync with the authorization data and policy they need (and only those they need).

Check out OPAL's main site at [OPAL.ac](https://opal.ac).

<img src="https://i.ibb.co/CvmX8rR/simplified-diagram-highlight.png" alt="simplified" border="0">

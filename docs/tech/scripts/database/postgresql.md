# PostgreSQL

PostgreSQL isn’t just a database—it’s a toolbox, a playground, and sometimes a magical black box of awesome. Whether you’re new to Postgres or a longtime enthusiast, here are some deeper, less-traveled paths worth exploring.

Certainly! Here’s your nerdy, in-depth PostgreSQL blog entry in markdown:

## Extensibility: Build Your Own Tools

Postgres is famously extensible. You can define your own:

* **Custom Data Types**
  ```sql
  CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy');
  ```
* **Custom Functions & Operators**
  * Write functions in SQL, PL/pgSQL, Python, Perl, or even C.
  * Define operators like `++`, `#`, or any symbol you fancy.
* **Extensions**
  * Just `CREATE EXTENSION`. Some must-try gems:
    * `pg_trgm` for super-fast fuzzy string matching.
    * `hstore` for schema-less key/value storage.
    * `postgis` for advanced GIS/spatial queries.

## Full-Text Search: Search Like Google

Postgres includes a search engine for your data.

* **`tsvector`** and **`tsquery`** types enable stemming, ranking, dictionaries, and more.
* GIN/GiST indexes speed up queries over massive text datasets.

  ```sql
  SELECT * FROM articles
  WHERE to_tsvector('english', content) @@ to_tsquery('python & database');
  ```

## JSONB: The Best of Both Worlds

* Store and efficiently query JSON data.
* GIN indexes make JSONB queries *blazingly* fast.

  ```sql
  SELECT * FROM users WHERE data->'address'->>'city' = 'New York';
  ```

## Window Functions & Analytics

Complex analytics, rolling totals, running ranks—Postgres makes it all simple:

```sql
SELECT
  user_id,
  score,
  RANK() OVER (ORDER BY score DESC) AS ranking,
  SUM(score) OVER (ORDER BY score) AS running_total
FROM leaderboard;
```

No subqueries or awkward workarounds needed!

## CTEs & Recursive Queries

Common Table Expressions (`WITH` queries) are powerful, but recursion takes it further.

```sql
WITH RECURSIVE family_tree AS (
  SELECT id, name, parent_id FROM people WHERE name = 'Alice'
  UNION ALL
  SELECT p.id, p.name, p.parent_id
  FROM people p
  JOIN family_tree f ON p.parent_id = f.id
)
SELECT * FROM family_tree;
```

Perfect for traversing trees, org charts, and graphs.

## Multi-Version Concurrency Control (MVCC)

* Readers never block writers; writers never block readers.
* Each transaction gets a consistent “snapshot” of the data.
* Old row versions are vacuumed away in the background.

## Foreign Data Wrappers: Query *Everything*

With FDWs, Postgres can treat anything as a table:

* Other Postgres servers
* MySQL databases
* Flat files, REST APIs—even Twitter!

```sql
CREATE EXTENSION postgres_fdw;
CREATE SERVER foreign_db ...;
CREATE USER MAPPING ...;
IMPORT FOREIGN SCHEMA ... FROM SERVER foreign_db;
```

Now you can `SELECT` across databases as if they were one.

## Lateral Joins: Top N Per Group, The Easy Way

`LATERAL` lets you use columns from the left table in a subquery on the right.

```sql
SELECT user_id, posts.*
FROM users
LEFT JOIN LATERAL (
  SELECT * FROM posts WHERE posts.user_id = users.user_id ORDER BY created_at DESC LIMIT 3
) posts ON true;
```

Handy for “latest 3 posts per user,” and much more.

## Table Inheritance

Tables can inherit from other tables—a rarely-used but sometimes handy feature.

```sql
CREATE TABLE vehicle (id serial, name text);
CREATE TABLE car (num_wheels int) INHERITS (vehicle);
```

Queries on `vehicle` can include rows from all child tables.

## Listen/Notify: Real-Time Pub/Sub

Make your database event-driven. Listen for events, trigger actions:

```sql
NOTIFY mychannel, 'payload info';
```

Applications can `LISTEN mychannel` and react instantly.

## Transactional DDL

Most RDBMSs won’t roll back a failed schema change. Postgres can.

```sql
BEGIN;
ALTER TABLE users ADD COLUMN mood mood;
ROLLBACK;
```

No trace left behind.

## Constraint Exclusion & Partitioning

Partition large tables, and Postgres will automatically ignore irrelevant partitions based on your queries. Makes big data feel small.

## Upsert with `ON CONFLICT`

A classic: insert or update in a single query.

```sql
INSERT INTO users(id, name)
VALUES (1, 'Alice')
ON CONFLICT (id)
DO UPDATE SET name = EXCLUDED.name;
```

## Rich Index Types

Beyond B-tree, try:

* **GIN**: great for arrays, JSONB, full-text
* **GiST**: for geometric/range data
* **BRIN**: for big, append-only tables
* **SP-GiST**, **hash**, and more

## Custom Aggregates

Define new aggregate functions (think `array_agg()`, `string_agg()`, or your own custom rollups).

## Temporal Tables & Time Travel

Use range types (`tsrange`, `int4range`, etc.) to store periods, or try system-versioned extensions to query your data “as of” any point in time.

## Row-Level Security (RLS)

Restrict access to specific rows per user or app role.
Control visibility at the row level, not just table level.

## Killer Query Tools

* `EXPLAIN ANALYZE` exposes query plans, timings, row counts—get nerdy with query tuning!
* `pg_stat_statements` helps identify and fix slow queries.
* Tons of metrics for those who love to optimize.

## Offline Installation of PostgreSQL 14 on RHEL 9.5

Sometimes, installing PostgreSQL on an **offline server** (such as RHEL 9.5 without internet access) can be tricky. With this approach, you can easily perform an offline installation of PostgreSQL 14 on RHEL 9.x. This method also works for other packages if you need to set up software on machines without internet access.

### Preparation on the Online System

First, run these commands on a system with internet access.

#### Add the PostgreSQL Repository

To ensure your system can find the latest PostgreSQL packages, add the official PostgreSQL repository:

```bash
dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```

#### Disable the Default PostgreSQL Module

RHEL’s default PostgreSQL module may only offer older versions. Disable it to avoid conflicts:

```bash
dnf -qy module disable postgresql
```

#### Install the DNF Download Plugin

This plugin will let you download packages (and dependencies) without installing them:

```bash
dnf install -y dnf-plugins-core
```

#### Download PostgreSQL 14 and All Dependencies

Now, download the desired RPMs and all their dependencies:

```bash
dnf download --resolve postgresql14 postgresql14-server
```

All the required RPM files will now be in your current directory.

#### Package All RPM Files into an Archive

To make transferring files to the offline server easier, compress them into a single archive:

```bash
tar czvf pg14_rpms.tar.gz *.rpm
```

### Installation on the Offline Server (RHEL 9.5)

**The next steps are performed on your target system, which has no internet access.**

#### Transfer and Extract the Archive

Copy `pg14_rpms.tar.gz` to your offline server (via USB stick, SCP, etc.).

Extract the archive in your preferred directory (e.g., `/tmp/pg14_rpms`):

```bash
mkdir -p /tmp/pg14_rpms
cp pg14_rpms.tar.gz /tmp/pg14_rpms/
cd /tmp/pg14_rpms
tar xzvf pg14_rpms.tar.gz
```

#### Install the RPM Packages

Now install all the RPMs:

```bash
sudo dnf install *.rpm
```

**Tip:** If you run into GPG signature issues or missing dependencies, try `dnf install --nogpgcheck *.rpm`.

#### Initialize and Start PostgreSQL

Initialize the PostgreSQL data directory:

```bash
sudo /usr/pgsql-14/bin/postgresql-14-setup initdb
```

Enable and start the PostgreSQL service:

```bash
sudo systemctl enable --now postgresql-14
```

#### Ensure PostgreSQL Starts Automatically

Make sure PostgreSQL will start automatically on system boot:

```bash
sudo systemctl enable postgresql-14
sudo systemctl start postgresql-14
```

Alternatively (depending on your system):

```bash
sudo postgresql-setup --initdb
sudo systemctl enable postgresql.service
sudo systemctl start postgresql.service
```

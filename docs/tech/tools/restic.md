# Restic

Restic is a fast and secure backup program that supports deduplication, encryption, and a variety of backends (like local storage, SFTP, and cloud providers). It uses [rclone](rclone.md) for cloud sync/copy jobs.

| What          | Where                                                           |
|---------------|-----------------------------------------------------------------|
| Official Page | <https://restic.net/>                                           |
| Source        | <https://github.com/restic/restic>                              |
| Install       | <https://restic.readthedocs.io/en/stable/020_installation.html> |

## Tips

- Regularly verify your backups using ```restic check```.
- Restic supports hooks (like ```--before``` and ```--after```) that can be used to execute commands before or after the backup, which can be useful for database dumps or stopping/starting services.

## Examples

### Basic Backup

Backup a directory to a local repository

```bash

#!/bin/bash
export RESTIC_REPOSITORY=/path/to/repo
export RESTIC_PASSWORD=YourPassword

restic backup /path/to/data
```

### Backup with Exclusions

Backup a directory but exclude certain patterns:

```bash
#!/bin/bash
export RESTIC_REPOSITORY=/path/to/repo
export RESTIC_PASSWORD=YourPassword

restic backup /path/to/data --exclude '*.log' --exclude '/path/to/data/temp/'
```

### Backup to S3

Backup a directory to an S3 bucket:

```bash
#!/bin/bash
export RESTIC_REPOSITORY=s3:s3.amazonaws.com/bucket_name
export RESTIC_PASSWORD=YourPassword
export AWS_ACCESS_KEY_ID=YourAccessKey
export AWS_SECRET_ACCESS_KEY=YourSecretKey

restic backup /path/to/data
```

### Automated Cleanup

Remove old backups based on certain criteria:

```bash

#!/bin/bash
export RESTIC_REPOSITORY=/path/to/repo
export RESTIC_PASSWORD=YourPassword

# Keep the last 7 daily backups, 4 weekly backups, and 6 monthly backups
restic forget --prune --keep-daily 7 --keep-weekly 4 --keep-monthly 6
```

### Mount a Repository

Mount your Restic repository to a local directory for browsing:

```bash
#!/bin/bash
export RESTIC_REPOSITORY=/path/to/repo
export RESTIC_PASSWORD=YourPassword

mkdir /mnt/restic
restic mount /mnt/restic
```

### Backup with Tags

Backup data with specific tags for easier management:

```bash
#!/bin/bash
export RESTIC_REPOSITORY=/path/to/repo
export RESTIC_PASSWORD=YourPassword

restic backup /path/to/data --tag monthly --tag critical
```

### List Snapshots with Tags

List only the snapshots with a specific tag:

```bash
#!/bin/bash
export RESTIC_REPOSITORY=/path/to/repo
export RESTIC_PASSWORD=YourPassword

restic snapshots --tag monthly
```

### Backup and Send Notification

Backup data and send a notification email if the backup fails:

```bash
#!/bin/bash
export RESTIC_REPOSITORY=/path/to/repo
export RESTIC_PASSWORD=YourPassword

if ! restic backup /path/to/data; then
    echo "Backup failed!" | mail -s "Restic Backup Failure" your@email.com
fi
```

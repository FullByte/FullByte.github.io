# Gotify

Info

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

## Using gotify with github actions

Example of how i update gotify whenever there is a github action that builds the docker container.
The sensible vars are stored in the github project secrets.

```yml
 - name: Update me on this event
    run: |
        curl "${{ secrets.GOTIFY_URL }}/message?token=${{ secrets.GOTIFY_TOKEN }}" -F "title=0xfab1.net updated" -F "message=${{ github.event.head_commit.message }}" -F "priority=5"
```
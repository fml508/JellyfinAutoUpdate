# Jellyfin Auto Docker Updater

This script automatically checks for updates to the Jellyfin Docker image and replaces the running container with the latest version.  
It is designed for users who self-host Jellyfin and want a simple way to keep their setup up-to-date.

---

## ⚙️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/fml508/JellyfinAutoUpdate.git
   cd JellyfinAutoUpdate
   ```

2. **Create your `.env` file**

   Copy the example file and customize it:

   ```bash
   cp .env.example .env
   ```

3. **Edit `.env` to match your system**

   Open `.env` and replace the placeholder values with your actual configuration:

   | Variable            | Description |
   |---------------------|-------------|
   | `DOCKER_VERSION`    | Command to get the current version of your running Jellyfin container |
   | `DOCKERHUB_VERSION` | Command to get the latest version from Docker Hub |
   | `DOCKER_PULL`       | Pulls the latest Jellyfin image |
   | `DOCKER_STOP`       | Stops the currently running Jellyfin container |
   | `DOCKER_REMOVE`     | Removes the stopped container |
   | `DOCKER_RUN`        | Starts a new container with your desired volumes, ports, and image |

   Example `DOCKER_RUN` template:

   ```env
   DOCKER_RUN=sudo docker run -d --name jellyfin \
   -v /home/youruser/jellyfin/config:/config \
   -v /media:/media \
   -v jellyfin_cache:/cache \
   -p 8096:8096 jellyfin/jellyfin:latest
   ```

---

## 🚀 Usage

Run the updater script manually:

```bash
sudo python3 dockerupdate.py
```

The script will:

- Compare the running version with the latest available
- Pull the new image if needed
- Stop and remove the old container
- Start Jellyfin with the updated image

All actions are logged to `update.log`.

---

## 🛡️ Safety Notes

- Your `.env` file is ignored by Git via `.gitignore` and should never be committed.
- Only `.env.example` is included in the repository for reference.
- Make sure your volume paths and container names are correct to avoid data loss.

---

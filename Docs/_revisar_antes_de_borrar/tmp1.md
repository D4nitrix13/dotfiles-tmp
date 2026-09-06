apt update
apt install -y docker.io docker-compose make
mkdir /app

<https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04>

docker compose --project-name contacts-application --project-directory . -f docker-compose.yaml down --remove-orphans --rmi local --timeout 5

# TodoList -> taskroot (<http://taskroot.duckdns.org:3000/>)

/bin/docker compose --project-directory . --project-name todolist --file docker-compose.yaml up --build --detach

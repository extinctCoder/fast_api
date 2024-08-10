all: win_docker build docker_up

build: git_version docker_build

up: docker_up

down: docker_down

win_docker:
	@echo Checking Docker installation...
	@cmd /c "where docker >nul 2>nul && (echo Docker is installed && docker --version) || (echo Docker is not installed)"

git_version:
	@git describe --tags --abbrev=0 > .version || echo "UNKNOWN" > .version

docker_build:
	@docker compose build --no-cache

docker_up:
	@docker compose up

docker_up_d:
	@docker compose up -d

docker_down:
	@docker compose down


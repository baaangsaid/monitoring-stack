version: '3.5'
services:
  postgres:
    image: postgres:15-alpine
    container_name: zabbix-postgres
    restart: always
    environment:
      POSTGRES_DB: zabbix
      POSTGRES_USER: zabbix
      POSTGRES_PASSWORD: zabbixpass
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - zabbix-network

  zabbix-server:
    image: zabbix/zabbix-server-pgsql:alpine-latest
    container_name: zabbix-server
    restart: always
    depends_on:
      - postgres
    environment:
      DB_SERVER_HOST: postgres
      POSTGRES_USER: zabbix
      POSTGRES_PASSWORD: zabbixpass
      POSTGRES_DB: zabbix
    ports:
      - "10051:10051"
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro
      - zbx-server-data:/var/lib/zabbix
    networks:
      - zabbix-network

  zabbix-web:
    image: zabbix/zabbix-web-nginx-pgsql:alpine-latest
    container_name: zabbix-web
    restart: always
    depends_on:
      - postgres
      - zabbix-server
    environment:
      DB_SERVER_HOST: postgres
      POSTGRES_USER: zabbix
      POSTGRES_PASSWORD: zabbixpass
      POSTGRES_DB: zabbix
      ZBX_SERVER_HOST: zabbix-server
      PHP_TZ: Asia/Jakarta
    ports:
      - "8080:8080"
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro
    networks:
      - zabbix-network

  zabbix-agent:
    image: zabbix/zabbix-agent:alpine-latest
    container_name: zabbix-agent
    restart: always
    privileged: true
    depends_on:
      - zabbix-server
    environment:
      ZBX_SERVER_HOST: zabbix-server
      ZBX_HOSTNAME: "Zabbix server"
    ports:
      - "10050:10050"
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro
    networks:
      - zabbix-network

networks:
  zabbix-network:
    driver: bridge

volumes:
  pgdata:
    driver: local
  zbx-server-data:
    driver: local

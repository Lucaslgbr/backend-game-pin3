# backend-game-pin3

Equipe: André Cristen e Lucas Levi Gonçalves

Para configurar o projeto, siga os passoas a seguir:

1. Na raiz do projeto, crie um arquivo chamado .env, e adapte-o baseado no modelo abaixo(é necessário criar um banco no postgres):

	DB_NAME=backend_game

    DB_USER=postgres

    DB_PASSWORD=senha

    DB_HOST=127.0.0.1

    DB_PORT=5432
	
    DEBUG=True

2. Deploy:

	2.1 Deploy windows:
		- No root do projeto você encontrará a pasta "docs", dentro dela estarão os arquivos Redis e memcached. 
		- Baixe e execute o msi do Redis e deixe que o mesmo rode na porta padrão (6379). 
		- Baixe e descompacte a pasta do memcached. Há a possibilidade de roda-lo como um serviço do windows, mas caso isso não aconteça, é necessário deixa-lo rodando.

	2.2 Deploy Ubuntu:
		- Configure o NGINX e o GUNICORN seguindo o passo a passo do link: https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-pt
		*Caso esteja com problemas com o .sock do gunicorn, o mesmo deve ser habilitado com 'sudo', caso contrário não aparecer
		- Adicione o seguinte bloco no arquivo do NGINX :
   			upstream channels-backend {
    		server 0.0.0.0:8005;
			}
   
			server {
    			...
			 location /ws {
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
                proxy_redirect off;
                proxy_pass http://127.0.0.1:8002;
            }
    			...
			}

		2.2.1 Configurando o Redis:
			- $sudo apt install redis-server
			- Altere no arquivo /etc/redis/redis.conf 'supervised no' por 'supervised systemd'
			$sudo systemctl restart redis.service
			$sudo systemctl enable redis-server
			$sudo systemctl status redis
		2.2.2 Configurando o daphne:
			- $apt install daphne
			- Crie um arquivo chamado daphne.service, e modifique de acardo com o secessário:
				[Unit]
				Description=WebSocket Daphne Service
				After=network.target

				[Service]
				Type=simple
				User=root
				WorkingDirectory=/caminho/ate/o/projeto/game/    # Ex:/var/www/django_apps/game/backend-game-pin3/
				ExecStart=/caminho/ate/a/virtuelenv/bin/python /caminho/ate/a/virtuelenv/bin/daphne -b 0.0.0.0 -p {qualquer porta em desuso (Ex:8000)} backend.game.routing:application
				Restart=on-failure

				[Install]
				WantedBy=multi-user.target
			- $sudo systemctl daemon-reload
			- $sudo systemctl start daphne.service
			- $sudo systemctl enable daphne.service
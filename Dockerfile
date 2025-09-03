FROM nginx:1.27-alpine

# Copia todos os arquivos estáticos do site (inclui Selo.png)
COPY ./ /usr/share/nginx/html/

# Copia a configuração de produção do Nginx
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

# Exponha a porta padrão do Nginx
EXPOSE 80

# Usa o comando padrão do Nginx (daemon off)
CMD ["nginx", "-g", "daemon off;"]



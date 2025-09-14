# Para criar o arquivo requirements.txt

```shell
# Instalar o plugin
poetry self add poetry-plugin-export

# Gerar arquivo
poetry export -f requirements.txt --without-hashes -o
```
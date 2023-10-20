# Projeto e-diaristas

## Instalando o projeto

#### Clonar o projeto
`git clone https://github.com/cxmdev/Projeto-Diarista`

#### Instalar as dependencias
`pip install -r requirements.txt`

#### Alterar configuracoes do Banco de dados no arquivo settings.py
`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}`
#### Migrar banco de dados
`python manage.py migrate`

#### iniciar o servidor
`python manage.py runserver`
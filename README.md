# Projeto-PEOO
bla bla
CLONANDO O REPOSITÓRIO
Inicialmente, escolha um local para colocar os arquivos do projeto. Ao escolher, clique com o botão direito do mouse e vá na opção: 'Git Bash Here'
Irá aparecer uma janelinha: o terminal do git.
Nele, digite 'git clone {url do repositório}
Os arquivos do repositório devem aparecer nesse momento
Agora é só trrabalhar nos arquivos

PARA OS PASSOS A SEGUIR DEVE SE CRIAR UM "PERFIL" LOCAL
Primeiro você cria um nome de usuário 'git config --global user.name "Fulano de Tal"' (não precisa ser o mesmo do seu perfil)
Depois coloca o email 'git config --global user.email fulanodetal@exemplo.br' 
Atente-se para o '--global'. Ele só é necessário na primeira vez, se quiser alterar alguma dessas informações, não precisa usar ele de novo.
Para ver se está tudo certo, você pode dar um 'git --config list'

ATUALIZANDO REPOSITÓRIO (VAI QUE MAIS DE UM TÁ MEXENDO NO MESMO TEMPO)
'git pull'

ADICIONANDO AS MUDANÇAS FEITAS(SEJAM DE INCLUSÃO OU REMOÇÃO DE ALGO)
'git add .'

'git commit -m "Mensagem especificando o que fez"'

'git push'

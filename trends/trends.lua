function Initialize()
    print("Inicializando o script Lua para executar Python...")
    ExecutePython()
    print("Script Python executado com sucesso.")
end

function Update()
    print("Inicializando o script Lua para executar Python...")
    ExecutePython()
    print("Script Python executado com sucesso.")

    print("Atualizando...")
    -- Leia o arquivo de texto
    local file = io.open("E:\\Projetos\\api-rainmetter-python\\trends\\trends.txt", "r")
    if file then
        local trends = file:read("*all")
        file:close()
        print("Tendencias lidas com sucesso.")
        return trends
    end
    print("Erro ao ler as tendencias.")
    return "Erro ao ler as tendencias"
end

function ExecutePython()
    local pythonExe = 'E:\\Projetos\\api-rainmetter-python\\env\\Scripts\\python.exe'
    local trendsScript = 'E:\\Projetos\\api-rainmetter-python\\trends\\trends.py'

    -- Construir o comando Python sem abrir janela de prompt
    local command = string.format('start /B "" "%s" "%s" > NUL 2>&1', pythonExe, trendsScript)

    -- local command = "@echo off E:\\Projetos\\api-rainmetter-python\\env\\Scripts\\python.exe E:\\Projetos\\api-rainmetter-python\\trends.py exit"
    os.execute(command)
end